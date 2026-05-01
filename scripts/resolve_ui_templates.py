#!/usr/bin/env python3
"""
Resolve UI term templates in documentation before translation.

This script replaces {{ui:KEY}} placeholders with actual Transifex translations
from PO files. Unresolved templates are left in place with warnings.

Usage:
    python scripts/resolve_ui_templates.py \\
        --input docs/en/article.md \\
        --language es \\
        --po-repo external/form-builder-translations

    # Process in-place
    python scripts/resolve_ui_templates.py \\
        --input docs/en/article.md \\
        --language es \\
        --po-repo external/form-builder-translations \\
        --in-place

    # Strict mode (fail on unresolved templates)
    python scripts/resolve_ui_templates.py \\
        --input docs/en/article.md \\
        --language es \\
        --po-repo external/form-builder-translations \\
        --strict

Requirements:
    - polib: pip install polib
    - form-builder-translations repository cloned locally
"""

import sys
import re
import json
import polib
from pathlib import Path
from typing import Dict, Optional, List, Tuple


# Template patterns
# UI template: {{ui:KEY}} or {{ui:KEY|formatting}}
# Collect template: {{collect:KEY}} or {{collect:KEY|formatting}}
# Allows any character except: } (template end) and | (format separator before it's parsed)
# This supports all msgid strings from Transifex including special chars like: ().,/!?'@#&*+$[]°×…→
UI_TEMPLATE_PATTERN = r'\{\{ui:([^|}]+?)(?:\|([^}]+))?\}\}'
COLLECT_TEMPLATE_PATTERN = r'\{\{collect:([^|}]+?)(?:\|([^}]+))?\}\}'
# Combined pattern for counting all templates
ALL_TEMPLATES_PATTERN = r'\{\{(?:ui|collect):([^|}]+?)(?:\|([^}]+))?\}\}'


class TemplateResolver:
    """Resolves UI term templates using Transifex PO files and Android collect strings"""
    
    def __init__(self, po_repo_path: Path, language: str, collect_json_path: Optional[Path] = None):
        """
        Initialize the template resolver.
        
        Args:
            po_repo_path: Path to form-builder-translations repository
            language: Target language code (es, fr, or ar)
            collect_json_path: Path to collect-strings.json file (optional)
        """
        self.po_repo_path = po_repo_path
        self.language = language
        self.translations = self._load_translations()
        self.collect_strings = self._load_collect_strings(collect_json_path) if collect_json_path else {}
        self.unresolved = []
    
    def _load_translations(self) -> Dict[str, str]:
        """
        Load translations from djangojs.po file.
        
        Returns:
            Dict mapping msgid to msgstr
        """
        po_file = self.po_repo_path / self.language / 'LC_MESSAGES' / 'djangojs.po'
        
        if not po_file.exists():
            raise FileNotFoundError(
                f"PO file not found: {po_file}\n"
                f"Make sure form-builder-translations is cloned and language is valid."
            )
        
        try:
            po = polib.pofile(str(po_file))
        except Exception as e:
            raise RuntimeError(f"Error parsing PO file: {e}")
        
        translations = {}
        
        for entry in po:
            if entry.msgid and entry.msgstr and not entry.obsolete:
                # Store with lowercase key for case-insensitive lookup
                # This allows {{ui:Deploy}}, {{ui:deploy}}, or {{ui:DEPLOY}} to all work
                translations[entry.msgid.lower()] = entry.msgstr
                
                # Also store with underscores for template keys
                # (e.g., "Save Draft" -> "save_draft")
                key = entry.msgid.replace(' ', '_').lower()
                translations[key] = entry.msgstr
        
        print(f"✅ Loaded {len(translations)} translations from {po_file.name}")
        return translations
    
    def _load_collect_strings(self, collect_json_path: Path) -> Dict[str, str]:
        """
        Load Android collect string translations from JSON file.
        
        Args:
            collect_json_path: Path to collect-strings.json
            
        Returns:
            Dict mapping string key to translated value for target language
        """
        if not collect_json_path or not collect_json_path.exists():
            print("ℹ️  Collect strings file not found, {{collect:}} templates will not be resolved")
            return {}
        
        try:
            with open(collect_json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Extract strings for target language
            strings = {}
            for key, translations in data.get('strings', {}).items():
                if self.language in translations:
                    # Store with original key (case-sensitive)
                    strings[key] = translations[self.language]
                    # Also store lowercase version for case-insensitive lookup
                    strings[key.lower()] = translations[self.language]
            
            print(f"✅ Loaded {len(strings) // 2} collect strings from {collect_json_path.name}")
            return strings
            
        except Exception as e:
            print(f"⚠️  Warning: Failed to load collect strings: {e}")
            return {}
    
    def _apply_formatting(self, text: str, formatting: Optional[str]) -> str:
        """
        Apply markdown formatting to translated text.
        Supports comma-separated format specifiers: {{ui:data|upper,bold}}
        
        Args:
            text: The translated text
            formatting: Format specifier(s) - can be comma-separated
                       (bold, italic, code, upper, lower)
            
        Returns:
            Formatted text
        """
        if not formatting:
            return text
        
        # Split by comma to support multiple formats
        formats = [f.strip() for f in formatting.split(',')]
        
        # Apply case transformations first (upper/lower)
        for fmt in formats:
            if fmt == 'upper':
                text = text.upper()
            elif fmt == 'lower':
                text = text.lower()
        
        # Then apply markdown wrapping (order matters: bold outside italic)
        for fmt in formats:
            if fmt == 'bold':
                text = f"**{text}**"
            elif fmt == 'italic':
                text = f"*{text}*"
            elif fmt == 'code':
                text = f"`{text}`"
            elif fmt not in ['upper', 'lower']:
                # Unknown formatting, warn but continue
                print(f"⚠️  Warning: Unknown formatting '{fmt}', ignoring")
        
        return text
    
    def _replace_placeholders(self, text: str) -> str:
        """
        Replace frontend UI term placeholders (##VAR##) with translated terms.
        
        Distinguishes between:
        - UI terms: ALL_CAPS placeholders (##SELECT_MANY##, ##ASSET_TYPE##) → replaced
        - Dynamic values: snake_case/lowercase (##count##, ##username##) → kept as-is
        
        Args:
            text: Translated text that may contain ##VAR## placeholders
            
        Returns:
            Text with UI term placeholders replaced, dynamic values preserved
        """
        import re
        
        # Match ALL placeholders first to analyze them
        placeholder_pattern = r'##([^#]+)##'
        
        def replace_placeholder(match):
            var_name = match.group(1)
            
            # Check if this is an ALL_CAPS placeholder (likely a UI term)
            # Examples: SELECT_MANY, ASSET_TYPE, QUESTION_TYPE
            if re.match(r'^[A-Z][A-Z_]*[A-Z]$', var_name):
                # Convert to lowercase with spaces for lookup
                lookup_key = var_name.replace('_', ' ').lower()
                
                # Try to find translation for the UI term
                if lookup_key in self.translations:
                    return self.translations[lookup_key]
                
                # If not found, convert to readable text
                # SELECT_MANY -> Select Many
                return var_name.replace('_', ' ').title()
            
            # For all other cases (snake_case, lowercase, mixed case):
            # Keep the placeholder as-is for runtime replacement
            # Examples: ##count##, ##username##, ##fileName##, ##organization name##
            return match.group(0)  # Return original ##VAR##
        
        return re.sub(placeholder_pattern, replace_placeholder, text)
    
    def resolve_ui_template(self, match: re.Match) -> str:
        """
        Resolve a single {{ui:}} template match with case-insensitive lookup.
        
        Args:
            match: Regex match object for UI template
            
        Returns:
            Resolved text or original template if not found
        """
        key = match.group(1)
        formatting = match.group(2)
        
        # Normalize key to lowercase for case-insensitive lookup
        key_lower = key.lower()
        
        # Try direct lowercase lookup
        if key_lower in self.translations:
            translated = self.translations[key_lower]
            # Replace frontend variable placeholders with actual UI terms
            translated = self._replace_placeholders(translated)
            return self._apply_formatting(translated, formatting)
        
        # Try with spaces instead of underscores
        key_with_spaces = key.replace('_', ' ').lower()
        if key_with_spaces in self.translations:
            translated = self.translations[key_with_spaces]
            # Replace frontend variable placeholders with actual UI terms
            translated = self._replace_placeholders(translated)
            return self._apply_formatting(translated, formatting)
        
        # Not found - record and keep template (as specified: leave unresolved)
        self.unresolved.append((key, match.group(0)))
        return match.group(0)  # Return original template unchanged
    
    def resolve_collect_template(self, match: re.Match) -> str:
        """
        Resolve a single {{collect:}} template match.
        
        Args:
            match: Regex match object for collect template
            
        Returns:
            Resolved text or original template if not found
        """
        key = match.group(1)
        formatting = match.group(2)
        
        # Try exact key match (case-sensitive)
        if key in self.collect_strings:
            translated = self.collect_strings[key]
            return self._apply_formatting(translated, formatting)
        
        # Try lowercase version (case-insensitive fallback)
        key_lower = key.lower()
        if key_lower in self.collect_strings:
            translated = self.collect_strings[key_lower]
            return self._apply_formatting(translated, formatting)
        
        # Not found - record and keep template
        self.unresolved.append((key, match.group(0)))
        return match.group(0)  # Return original template unchanged
    
    def resolve_file(self, content: str) -> str:
        """
        Resolve all templates in file content (both {{ui:}} and {{collect:}}).
        
        Args:
            content: File content with templates
            
        Returns:
            Content with resolved templates
        """
        self.unresolved = []  # Reset for new file
        
        # Resolve UI templates first
        resolved = re.sub(UI_TEMPLATE_PATTERN, self.resolve_ui_template, content)
        
        # Then resolve collect templates
        resolved = re.sub(COLLECT_TEMPLATE_PATTERN, self.resolve_collect_template, resolved)
        
        return resolved
    
    def get_template_report(self) -> str:
        """
        Generate report of template resolution.
        
        Returns:
            Human-readable report string
        """
        if not self.unresolved:
            return "✅ All templates resolved successfully"
        
        report = f"⚠️  {len(self.unresolved)} unresolved templates (left in output):\n"
        for key, template in self.unresolved:
            report += f"  - {template} (key: {key})\n"
        
        report += "\n💡 To fix: Either add these strings to Transifex or fix template keys."
        return report


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Resolve UI term templates using Transifex translations',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Template Syntax:
  UI templates (web interface):
    {{ui:Deploy}}              → DESPLEGAR (Spanish)
    {{ui:Deploy|bold}}         → **DESPLEGAR**
    {{ui:FORM|code}}           → `FORMULARIO`
    {{ui:Save_Draft}}          → GUARDAR BORRADOR
  
  Collect templates (Android app):
    {{collect:enter_data}}     → Remplir un formulaire (French)
    {{collect:send_data|bold}} → **Prêt à envoyer**
    {{collect:finalize|upper}} → FINALISER

Examples:
  # Basic usage
  python scripts/resolve_ui_templates.py \\
      -i docs/en/getting_started.md \\
      -l es \\
      -p external/form-builder-translations

  # In-place resolution
  python scripts/resolve_ui_templates.py \\
      -i docs/en/article.md -l fr -p external/form-builder-translations --in-place

  # Strict mode (exit with error if unresolved)
  python scripts/resolve_ui_templates.py \\
      -i docs/en/article.md -l ar -p external/form-builder-translations --strict
"""
    )
    
    parser.add_argument(
        '--input', '-i',
        type=Path,
        required=True,
        help='Input markdown file with templates'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        help='Output file (defaults to <input>_resolved.md)'
    )
    parser.add_argument(
        '--language', '-l',
        required=True,
        choices=['es', 'fr', 'ar'],
        help='Target language (Spanish, French, or Arabic)'
    )
    parser.add_argument(
        '--po-repo', '-p',
        type=Path,
        required=True,
        help='Path to form-builder-translations repository'
    )
    parser.add_argument(
        '--collect-strings', '-c',
        type=Path,
        default=Path('skills/kobo-translation-v2/references/collect-strings.json'),
        help='Path to collect-strings.json file (default: skills/kobo-translation-v2/references/collect-strings.json)'
    )
    parser.add_argument(
        '--in-place',
        action='store_true',
        help='Modify input file in place (overwrite)'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Exit with error code if any templates unresolved'
    )
    
    args = parser.parse_args()
    
    # Validate input file
    if not args.input.exists():
        print(f"❌ Error: Input file not found: {args.input}")
        return 1
    
    # Validate PO repository
    if not args.po_repo.exists():
        print(f"❌ Error: PO repository not found: {args.po_repo}")
        print("\nTo set up the submodule:")
        print("  git submodule add https://github.com/kobotoolbox/form-builder-translations.git external/form-builder-translations")
        print("  git submodule update --init --recursive")
        return 1
    
    # Determine output path
    if args.in_place:
        output_path = args.input
    elif args.output:
        output_path = args.output
    else:
        stem = args.input.stem
        suffix = args.input.suffix
        output_path = args.input.parent / f"{stem}_resolved{suffix}"
    
    # Load and resolve templates
    try:
        print(f"📖 Loading translations for {args.language}...")
        resolver = TemplateResolver(args.po_repo, args.language, args.collect_strings)
        
        print(f"📄 Reading {args.input.name}...")
        content = args.input.read_text(encoding='utf-8')
        
        # Count templates before resolution
        template_matches = re.findall(ALL_TEMPLATES_PATTERN, content)
        template_count = len(template_matches)
        
        if template_count == 0:
            print("ℹ️  No templates found in input file")
        else:
            print(f"🔄 Found {template_count} templates, resolving...")
        
        # Resolve templates
        resolved_content = resolver.resolve_file(content)
        
        # Write output
        output_path.write_text(resolved_content, encoding='utf-8')
        
        if args.in_place:
            print(f"✅ Resolved templates written to {output_path} (in-place)")
        else:
            print(f"✅ Resolved templates written to {output_path}")
        
        # Report unresolved templates
        print(f"\n{resolver.get_template_report()}")
        
        # Exit code based on strict mode
        if args.strict and resolver.unresolved:
            print("\n❌ Strict mode: Exiting with error due to unresolved templates")
            return 1
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
