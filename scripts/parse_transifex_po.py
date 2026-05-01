#!/usr/bin/env python3
"""
Parse KoboToolbox Transifex PO files and extract UI strings.

This script extracts UI-relevant strings from the form-builder-translations
repository and generates a markdown reference file for use in documentation
translation.

Usage:
    python scripts/parse_transifex_po.py \\
        --repo-path external/form-builder-translations

    python scripts/parse_transifex_po.py \\
        --repo-path external/form-builder-translations \\
        --output skills/kobo-translation/references/transifex-ui-strings.md

Requirements:
    - polib: pip install polib
    - form-builder-translations repository cloned locally
"""

import sys
import re
import polib
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime
from collections import defaultdict


# UI-relevant string patterns (to filter out technical strings)
UI_PATTERNS = [
    r'^[A-Z][a-z]+',  # Title case (likely buttons/labels)
    r'^[A-Z]+$',      # All caps (likely tabs/sections)
    r'\.\.\.$',       # Ends with ellipsis (menu items)
]

# Technical string patterns to EXCLUDE
EXCLUDE_PATTERNS = [
    r'^%\(',          # Python format strings
    r'^\{\w+\}',      # Template variables
    r'\$\{',          # JavaScript template literals
    r'^[a-z_]+$',     # Snake_case (likely variable names)
    r'^\/',           # Paths
    r'^https?://',    # URLs
    r'^\d+$',         # Pure numbers
    r'%[sd]',         # Format placeholders
    r'\{\d+\}',       # Numbered placeholders
]


def is_ui_string(msgid: str) -> bool:
    """
    Determine if a string is likely a user-facing UI element.
    
    Args:
        msgid: The English source string from PO file
        
    Returns:
        True if string appears to be a UI element
    """
    if not msgid or len(msgid) > 100:  # Too long for UI element
        return False
    
    # Exclude technical patterns
    for pattern in EXCLUDE_PATTERNS:
        if re.search(pattern, msgid):
            return False
    
    # Check for UI patterns
    for pattern in UI_PATTERNS:
        if re.search(pattern, msgid):
            return True
    
    # Additional heuristics: short phrases starting with capital
    if len(msgid.split()) <= 5 and msgid[0].isupper():
        return True
    
    return False


def categorize_ui_string(msgid: str, context: str = '') -> str:
    """
    Categorize a UI string by type.
    
    Args:
        msgid: The English source string
        context: Optional context from PO file comments
        
    Returns:
        Category name for grouping in markdown
    """
    msgid_lower = msgid.lower()
    
    # Navigation tabs (typically all caps)
    if msgid.isupper() and len(msgid) < 20:
        return 'Navigation Tabs'
    
    # Buttons and actions
    elif any(word in msgid_lower for word in [
        'click', 'button', 'submit', 'save', 'delete', 'add', 
        'remove', 'edit', 'cancel', 'close', 'upload', 'download',
        'export', 'import', 'refresh', 'deploy'
    ]):
        return 'Core UI Actions & Buttons'
    
    # Form builder specific
    elif any(word in msgid_lower for word in [
        'question', 'form', 'library', 'group', 'validation',
        'skip logic', 'hint', 'label', 'required'
    ]):
        return 'Form Builder UI Elements'
    
    # Data management
    elif any(word in msgid_lower for word in [
        'submission', 'data', 'table', 'view', 'report', 'validate'
    ]):
        return 'Data Management UI'
    
    # Dialogs and messages
    elif any(word in msgid_lower for word in [
        'dialog', 'message', 'confirm', 'warning', 'error', 
        'success', 'loading'
    ]):
        return 'Dialogs & Messages'
    
    # Settings and configuration
    elif any(word in msgid_lower for word in [
        'settings', 'preferences', 'configuration', 'server',
        'username', 'password'
    ]):
        return 'Settings & Configuration'
    
    # Mobile app (KoboCollect)
    elif any(word in msgid_lower for word in [
        'collect', 'send', 'draft', 'finalize', 'get selected'
    ]):
        return 'KoboCollect (Mobile App) UI'
    
    else:
        return 'General UI Elements'


def parse_po_file(po_path: Path) -> List[Tuple[str, str, str]]:
    """
    Parse a PO file and extract UI strings.
    
    Args:
        po_path: Path to the PO file
        
    Returns:
        List of (msgid, msgstr, context) tuples
    """
    try:
        po = polib.pofile(str(po_path))
    except Exception as e:
        print(f"Error parsing {po_path}: {e}")
        return []
    
    ui_strings = []
    
    for entry in po:
        # Skip obsolete entries and empty translations
        if entry.obsolete or not entry.msgid or not entry.msgstr:
            continue
        
        # Check if it's a UI string
        if is_ui_string(entry.msgid):
            context = entry.comment or ''
            ui_strings.append((entry.msgid, entry.msgstr, context))
    
    return ui_strings


def extract_all_languages(repo_path: Path) -> Dict[str, Dict[str, str]]:
    """
    Extract UI strings from all supported language PO files.
    
    Args:
        repo_path: Path to form-builder-translations repository
        
    Returns:
        Dict mapping language code to {msgid: msgstr}
    """
    # Only Spanish, French, and Arabic as specified
    languages = {
        'es': 'Spanish',
        'fr': 'French',
        'ar': 'Arabic'
    }
    
    all_translations = {}
    
    for lang_code, lang_name in languages.items():
        po_file = repo_path / lang_code / 'LC_MESSAGES' / 'djangojs.po'
        
        if not po_file.exists():
            print(f"⚠️  Warning: {po_file} not found, skipping {lang_name}")
            continue
        
        ui_strings = parse_po_file(po_file)
        all_translations[lang_code] = {
            msgid: msgstr for msgid, msgstr, _ in ui_strings
        }
        print(f"✅ Extracted {len(ui_strings)} UI strings from {lang_name}")
    
    return all_translations


def generate_markdown(
    translations: Dict[str, Dict[str, str]], 
    output_path: Path = None
) -> str:
    """
    Generate markdown reference file from translations.
    
    Args:
        translations: Dict mapping language code to {msgid: msgstr}
        output_path: Optional path to write the markdown file
        
    Returns:
        Generated markdown content
    """
    # Get all unique English strings across all languages
    all_msgids = set()
    for lang_translations in translations.values():
        all_msgids.update(lang_translations.keys())
    
    # Sort and categorize
    categorized = defaultdict(list)
    for msgid in sorted(all_msgids):
        category = categorize_ui_string(msgid)
        
        row = {
            'msgid': msgid,
            'es': translations.get('es', {}).get(msgid, '[Missing]'),
            'fr': translations.get('fr', {}).get(msgid, '[Missing]'),
            'ar': translations.get('ar', {}).get(msgid, '[Missing]'),
        }
        categorized[category].append(row)
    
    # Generate markdown
    markdown = f"""# Transifex UI Strings (AUTHORITATIVE)

**🚨 CRITICAL: These are the EXACT translations from Transifex.**

**Source:** KoboToolbox form-builder-translations repository  
**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}  
**Languages:** Spanish (es), French (fr), Arabic (ar)  
**Priority:** HIGHEST - Use these translations exactly as shown  

⚠️ **USAGE RULE:** When translating documentation that mentions ANY UI element 
(buttons, tabs, menus, dialogs, settings), you MUST use EXACTLY these translations.
Do NOT adapt, modify, or localize these strings - they must match the UI character-for-character.

## How to Use This File

1. **First**, check if the English UI term appears in the tables below
2. **If found**, use the EXACT translation provided (including capitalization)
3. **If NOT found**, check `ui-terminology.md` for supplementary terms
4. When in doubt about whether something is a UI element, assume it is and check here first

---

"""
    
    # Add each category section
    for category, strings in sorted(categorized.items()):
        markdown += f"\n## {category}\n\n"
        markdown += "| English UI String | Spanish (Transifex) | French (Transifex) | Arabic (Transifex) |\n"
        markdown += "|-------------------|---------------------|--------------------|--------------------|\\n"
        
        for row in strings:
            # Escape pipe characters in strings
            msgid = row['msgid'].replace('|', '\\|')
            es = row['es'].replace('|', '\\|')
            fr = row['fr'].replace('|', '\\|')
            ar = row['ar'].replace('|', '\\|')
            
            markdown += f"| {msgid} | {es} | {fr} | {ar} |\n"
    
    # Add footer
    markdown += "\n---\n\n"
    markdown += f"**Total UI strings extracted:** {len(all_msgids)}  \n"
    markdown += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}  \n"
    markdown += f"**Source repository:** https://github.com/kobotoolbox/form-builder-translations/  \n\n"
    
    markdown += """## Maintenance

This file should be regenerated whenever the form-builder-translations 
repository is updated (biweekly on 1st and 15th of each month).

To regenerate:

```bash
cd external/form-builder-translations
git pull origin main
cd ../..
python scripts/parse_transifex_po.py \\
    --repo-path external/form-builder-translations \\
    --output skills/kobo-translation/references/transifex-ui-strings.md
```
"""
    
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding='utf-8')
        print(f"\n✅ Generated {output_path}")
    
    return markdown


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Parse KoboToolbox Transifex PO files and extract UI strings',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate with default output path
  python scripts/parse_transifex_po.py -r external/form-builder-translations
  
  # Specify custom output path
  python scripts/parse_transifex_po.py \\
      -r external/form-builder-translations \\
      -o custom/path/transifex-ui-strings.md
"""
    )
    
    parser.add_argument(
        '--repo-path', '-r',
        type=Path,
        required=True,
        help='Path to form-builder-translations repository'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        default=Path('skills/kobo-translation/references/transifex-ui-strings.md'),
        help='Output markdown file path (default: skills/kobo-translation/references/transifex-ui-strings.md)'
    )
    
    args = parser.parse_args()
    
    # Validate repository path
    if not args.repo_path.exists():
        print(f"❌ Error: Repository path not found: {args.repo_path}")
        print("\nTo set up the submodule:")
        print("  git submodule add https://github.com/kobotoolbox/form-builder-translations.git external/form-builder-translations")
        print("  git submodule update --init --recursive")
        return 1
    
    print(f"📖 Parsing PO files from {args.repo_path}...\n")
    
    # Extract translations
    translations = extract_all_languages(args.repo_path)
    
    if not translations:
        print("❌ Error: No translations extracted. Check that PO files exist.")
        return 1
    
    print(f"\n📝 Generating markdown reference...")
    
    # Generate markdown file
    generate_markdown(translations, args.output)
    
    print(f"\n✨ Done! Review {args.output} and adjust categorization as needed.")
    print("\nNext steps:")
    print("  1. Review the generated file for accuracy")
    print("  2. Manually verify a sample of UI strings against the actual UI")
    print("  3. Run: python scripts/split_skill_by_language.py")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
