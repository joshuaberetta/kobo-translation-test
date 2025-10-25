#!/usr/bin/env python3
"""
KoboToolbox Translation Agent - Simplified Test Version
Translates documentation using Claude API with embedded kobo-translation skill
"""

import os
import sys
import json
import hashlib
import argparse
from pathlib import Path
from typing import Dict, Tuple
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()  # This loads .env file automatically

try:
    import anthropic
    from github import Github
except ImportError:
    print("❌ Missing dependencies. Install with: pip install -r requirements.txt")
    sys.exit(1)


class TranslationAgent:
    """Simplified AI agent for testing automated documentation translation"""
    
    def __init__(self, test_mode: bool = False):
        """
        Initialize the translation agent
        
        Args:
            test_mode: If True, run locally without GitHub integration
        """
        self.test_mode = test_mode
        
        # Load API key
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")
        
        self.claude = anthropic.Anthropic(api_key=api_key)
        
        # GitHub integration (only if not in test mode)
        if not test_mode:
            github_token = os.getenv('GITHUB_TOKEN')
            if not github_token:
                raise ValueError("GITHUB_TOKEN environment variable not set")
            
            self.github = Github(github_token)
            repo_name = os.getenv('GITHUB_REPOSITORY')
            if repo_name:
                self.repo = self.github.get_repo(repo_name)
            else:
                self.repo = None
        
        # Target languages
        self.languages = ['es', 'fr', 'ar']
        
        # Load skill content
        print("📚 Loading kobo-translation skill...")
        self.skill_context = self._load_skill_context()
        print("✅ Skill loaded successfully")
    
    def _load_skill_context(self) -> Dict[str, str]:
        """Load skill files from repository into memory"""
        skill_base = Path('skills/kobo-translation')
        
        if not skill_base.exists():
            raise FileNotFoundError(
                f"Skill directory not found: {skill_base}\n"
                "Make sure you've copied the kobo-translation skill to skills/"
            )
        
        context = {}
        
        # Read main skill file
        main_skill = skill_base / 'SKILL.md'
        if main_skill.exists():
            context['main'] = main_skill.read_text(encoding='utf-8')
        else:
            raise FileNotFoundError(f"SKILL.md not found in {skill_base}")
        
        # Read reference files
        refs_dir = skill_base / 'references'
        if refs_dir.exists():
            ref_files = {
                'brand': 'brand-terminology.md',
                'ui': 'ui-terminology.md',
                'data': 'data-collection-terms.md',
                'forms': 'form-building-terms.md',
                'questions': 'question-types.md',
                'course': 'course-terminology.md',
            }
            
            for key, filename in ref_files.items():
                file_path = refs_dir / filename
                if file_path.exists():
                    context[key] = file_path.read_text(encoding='utf-8')
                else:
                    print(f"⚠️  Optional reference file not found: {filename}")
        
        # Create condensed version for efficiency
        context['condensed'] = self._create_condensed_rules()
        
        return context
    
    def _create_condensed_rules(self) -> str:
        """Create condensed version with only critical rules"""
        return """
🚨 CRITICAL TRANSLATION RULES

You are translating KoboToolbox documentation. Follow these rules EXACTLY.

1. BRAND TERMS (Use EXACTLY - DO NOT MODIFY):

   Server Names:
   ├─ Spanish: "Servidor Global" (NOT "Servidor Global de KoboToolbox")
   ├─ Spanish EU: "Servidor con sede en la Unión Europea"
   ├─ French: "Le serveur KoboToolbox mondial" (MUST include "Le")
   └─ French EU: "Le serveur KoboToolbox Union européenne"

   Question Library:
   ├─ Spanish: "La biblioteca de preguntas" (CAPITAL L)
   └─ French: "La bibliothèque de questions" (CAPITAL L)

   Formbuilder (FIRST reference ONLY):
   ├─ Spanish: "editor de formularios de KoboToolbox (Formbuilder)"
   ├─ French: "l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder)"
   └─ Subsequent uses: Use short form only

   Keep in English:
   ├─ KoboToolbox (brand name)
   ├─ XLSForm (technical term)
   └─ Product names: iPhone, Android, Google Drive, Dropbox

2. UI ELEMENTS:
   ├─ Capitalize: Draft → Brouillon(FR) / Borrador(ES)
   ├─ Tabs ALL CAPS: FORM → FORMULAIRE / FORMULARIO, DATA → DONNÉES / DATOS
   └─ Buttons: NEW → NOUVEAU / NUEVO, DEPLOY → DÉPLOYER / DESPLEGAR

3. LANGUAGE STYLE:
   Spanish:
   ├─ Use informal "tú"
   ├─ Gender-inclusive: "los/as usuarios/as" (NOT "los usuarios")
   ├─ Data collection: "recolectar" (NOT "recopilar")
   └─ Management: "manejo de datos" (NOT "gestión de datos")
   
   French:
   ├─ Use formal "vous"
   ├─ Gender-inclusive: "utilisatrices et utilisateurs"
   ├─ Upload: "importer" (NOT "télécharger")
   └─ Data collection: "collecte de données"
   
   Arabic:
   ├─ Use formal Modern Standard Arabic
   ├─ Keep brand names in English
   └─ Use natural Arabic phrasing

4. FORMATTING:
   ├─ Preserve all HTML/markdown structure
   ├─ Keep links functional
   ├─ Maintain document hierarchy
   └─ Preserve icons like <i class="k-icon-plus"></i>

⚠️ CHECK THESE BEFORE SUBMITTING TRANSLATION
"""
    
    def determine_complexity(self, file_path: str) -> str:
        """
        Determine translation complexity based on file content
        
        Returns: 'simple', 'standard', or 'complex'
        """
        content = Path(file_path).read_text(encoding='utf-8')
        
        # Count brand terms
        brand_terms = [
            'KoboToolbox', 'Formbuilder', 'Question Library',
            'Global Server', 'European Union', 'XLSForm'
        ]
        brand_count = sum(content.count(term) for term in brand_terms)
        
        # Count UI elements
        ui_elements = ['DEPLOY', 'NEW', 'FORM', 'DATA', 'Settings', 'Save']
        ui_count = sum(content.count(term) for term in ui_elements)
        
        length = len(content)
        
        # Simple: Short with no brand terms
        if length < 1000 and brand_count == 0:
            return 'simple'
        
        # Complex: Long or many brand/UI terms
        if length > 3000 or brand_count > 5 or ui_count > 5:
            return 'complex'
        
        # Standard: Most documents
        return 'standard'
    
    def translate_diff(self, diff_content: str, target_lang: str,
                      context: str = None) -> str:
        """
        Translate only a diff (changed content) using Claude
        
        Args:
            diff_content: Only the changed lines/paragraphs to translate
            target_lang: Target language (es, fr, ar)
            context: Optional surrounding context for better translation
        """
        print(f"  📊 Translation mode: DIFF-BASED (changes only)")
        
        # Use condensed skill + brand terminology for diffs
        skill_prompt = f"""
{self.skill_context['condensed']}

## BRAND TERMINOLOGY REFERENCE (Check for every brand term)
{self.skill_context.get('brand', '[Brand terminology not available]')}
"""
        
        # Build prompt with EXTREME emphasis on diff-only translation
        context_note = ""
        if context:
            context_note = f"""
SURROUNDING CONTEXT (for reference only - DO NOT translate):
```
{context}
```
"""
        
        prompt = f"""{skill_prompt}

TARGET LANGUAGE: {target_lang.upper()}

🚨🚨🚨 CRITICAL INSTRUCTION 🚨🚨🚨

You are translating ONLY A DIFF - NOT a full document.

RULES:
1. Translate ONLY the exact content between the markers below
2. Do NOT translate anything outside the markers
3. Do NOT translate any context provided for reference
4. Do NOT add any explanations, comments, or meta-text
5. Output ONLY the translated version of the diff content
6. Do NOT translate the markers themselves
7. Do NOT modify, add to, or expand the content
8. ONLY translate what is explicitly between the BEGIN and END markers

This is an UPDATE to an existing translation. The rest of the document is already translated correctly.
Your job is to translate ONLY this small change.

{context_note}

---BEGIN DIFF TO TRANSLATE---
{diff_content}
---END DIFF TO TRANSLATE---

Now provide ONLY the translated diff content (nothing else):"""

        print(f"  🤖 Calling Claude API...")
        
        try:
            # Call Claude API with system message to reinforce diff-only behavior
            response = self.claude.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=8000,
                temperature=0.3,  # Lower for consistency
                system="""You are a precise translation tool. When translating a DIFF (partial content), you MUST:
1. Translate ONLY the content between the BEGIN and END markers
2. Output ONLY the translated text with NO additional content
3. NOT translate anything outside the markers
4. NOT add explanations, comments, or metadata
This is critical - translate ONLY what is explicitly marked for translation.""",
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            # Extract translation
            translation = ""
            for block in response.content:
                if block.type == "text":
                    translation += block.text
            
            # Report token usage
            usage = response.usage
            print(f"  📊 Tokens used: {usage.input_tokens} input, {usage.output_tokens} output")
            cost = (usage.input_tokens / 1_000_000 * 3) + (usage.output_tokens / 1_000_000 * 15)
            print(f"  💰 Estimated cost: ${cost:.4f}")
            
            return translation
            
        except Exception as e:
            print(f"  ❌ Translation failed: {e}")
            raise
    
    def translate_file(self, source_path: str, target_lang: str,
                      complexity: str = None, is_update: bool = False,
                      diff_content: str = None) -> str:
        """
        Translate a markdown file using Claude with embedded skill
        
        Args:
            source_path: Path to source markdown file
            target_lang: Target language (es, fr, ar)
            complexity: Force complexity level, or auto-detect if None
            is_update: If True, expects diff_content to be provided
            diff_content: Only the changed content (for updates)
        """
        # Handle diff-based updates
        if is_update:
            if not diff_content:
                raise ValueError("diff_content must be provided when is_update=True")
            
            print(f"  🔄 UPDATE MODE: Translating diff only")
            print(f"  📏 Diff size: {len(diff_content)} characters")
            
            # Safety check - if diff is suspiciously large, warn user
            if len(diff_content) > 5000:
                print(f"  ⚠️  WARNING: Diff is very large ({len(diff_content)} chars)")
                print(f"  ⚠️  Are you sure this is just a diff and not the full file?")
                response = input("  Continue? (y/n): ")
                if response.lower() != 'y':
                    raise ValueError("Translation cancelled by user")
            
            return self.translate_diff(diff_content, target_lang)
        
        # Full file translation (NEW content)
        # Read source file
        source_content = Path(source_path).read_text(encoding='utf-8')
        
        # Determine complexity if not specified
        if complexity is None:
            complexity = self.determine_complexity(source_path)
        
        print(f"  📊 Complexity level: {complexity}")
        
        # Select skill context based on complexity
        if complexity == 'simple':
            skill_prompt = self.skill_context['condensed']
        elif complexity == 'complex':
            # Use full skill + brand + UI references
            skill_prompt = f"""
{self.skill_context['condensed']}

## COMPLETE BRAND TERMINOLOGY REFERENCE
{self.skill_context.get('brand', '[Brand terminology not available]')}

## COMPLETE UI TERMINOLOGY REFERENCE
{self.skill_context.get('ui', '[UI terminology not available]')}
"""
        else:  # standard
            # Condensed + brand terminology (most common)
            skill_prompt = f"""
{self.skill_context['condensed']}

## BRAND TERMINOLOGY REFERENCE (Check for every brand term)
{self.skill_context.get('brand', '[Brand terminology not available]')}
"""
        
        # Build final prompt
        prompt = f"""{skill_prompt}

TARGET LANGUAGE: {target_lang.upper()}

Now translate this COMPLETE NEW document following ALL rules above.
Provide ONLY the translated markdown. No explanations, comments, or meta-text.

---BEGIN SOURCE DOCUMENT---
{source_content}
---END SOURCE DOCUMENT---

Translation:"""

        print(f"  🤖 Calling Claude API...")
        
        try:
            # Call Claude API
            response = self.claude.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=16000,
                temperature=0.3,  # Lower for consistency
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            # Extract translation
            translation = ""
            for block in response.content:
                if block.type == "text":
                    translation += block.text
            
            # Report token usage
            usage = response.usage
            print(f"  📊 Tokens used: {usage.input_tokens} input, {usage.output_tokens} output")
            cost = (usage.input_tokens / 1_000_000 * 3) + (usage.output_tokens / 1_000_000 * 15)
            print(f"  💰 Estimated cost: ${cost:.4f}")
            
            return translation
            
        except Exception as e:
            print(f"  ❌ Translation failed: {e}")
            raise
    
    def apply_translated_diff(self, existing_translation: str, 
                             translated_diff: str,
                             line_number: int = None,
                             old_content: str = None) -> str:
        """
        Apply a translated diff to an existing translation
        
        Args:
            existing_translation: Current translated document
            translated_diff: The newly translated diff content
            line_number: Line number where to apply change (optional)
            old_content: Old content to replace (optional, for search-replace)
        
        Returns:
            Updated translation with diff applied
        """
        if old_content:
            # Search and replace mode
            if old_content not in existing_translation:
                raise ValueError("old_content not found in existing translation")
            return existing_translation.replace(old_content, translated_diff, 1)
        
        elif line_number is not None:
            # Line number mode
            lines = existing_translation.split('\n')
            diff_lines = translated_diff.split('\n')
            
            # Replace at specific line
            lines[line_number:line_number+len(diff_lines)] = diff_lines
            return '\n'.join(lines)
        
        else:
            raise ValueError("Either old_content or line_number must be provided")
    
    def validate_translation(self, source_path: str, translation: str,
                           target_lang: str) -> Dict:
        """
        Perform basic validation checks on translation
        
        Returns: Dictionary with validation results
        """
        source_content = Path(source_path).read_text(encoding='utf-8')
        
        checks = {
            'has_content': len(translation.strip()) > 0,
            'preserves_headers': translation.count('#') == source_content.count('#'),
            'preserves_links': translation.count('[') >= source_content.count('[') * 0.9,
            'has_brand_term': 'KoboToolbox' in translation,
            'no_english_artifacts': 'TODO' not in translation and 'FIXME' not in translation,
        }
        
        # Language-specific checks
        if target_lang == 'es':
            checks['uses_informal'] = 'tú' in translation.lower() or 'tu ' in translation.lower()
            checks['gender_inclusive'] = 'los/as' in translation or 'las/os' in translation
        elif target_lang == 'fr':
            checks['uses_formal'] = 'vous' in translation.lower()
            checks['gender_inclusive'] = 'utilisatrices' in translation or 'utilisateurs' in translation
        
        checks['passed'] = all(checks.values())
        
        return checks
    
    def save_translation(self, translation: str, source_path: str,
                        target_lang: str) -> Path:
        """
        Save translation to appropriate location
        
        Returns: Path where translation was saved
        """
        source = Path(source_path)
        target_dir = Path('docs') / target_lang
        target_dir.mkdir(parents=True, exist_ok=True)
        
        target_path = target_dir / source.name
        target_path.write_text(translation, encoding='utf-8')
        
        return target_path


def main():
    """Main entry point for testing"""
    parser = argparse.ArgumentParser(
        description='KoboToolbox Translation Agent - Test Version'
    )
    parser.add_argument(
        '--file',
        required=True,
        help='Path to source file to translate (e.g., docs/en/test_simple.md)'
    )
    parser.add_argument(
        '--language',
        choices=['es', 'fr', 'ar'],
        required=True,
        help='Target language'
    )
    parser.add_argument(
        '--complexity',
        choices=['simple', 'standard', 'complex'],
        help='Force complexity level (auto-detect if not specified)'
    )
    parser.add_argument(
        '--save',
        action='store_true',
        help='Save translation to file (default: just display)'
    )
    parser.add_argument(
        '--test',
        action='store_true',
        help='Test mode - run locally without GitHub'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed output'
    )
    parser.add_argument(
        '--diff',
        type=str,
        help='Diff content to translate (for update mode). Use with --update-mode'
    )
    parser.add_argument(
        '--update-mode',
        action='store_true',
        help='Update mode: translate only the diff and apply to existing translation'
    )
    parser.add_argument(
        '--old-content',
        type=str,
        help='Old content to replace (used with --update-mode to find where to apply diff)'
    )
    
    args = parser.parse_args()
    
    # Verify source file exists
    if not Path(args.file).exists():
        print(f"❌ Source file not found: {args.file}")
        sys.exit(1)
    
    # Validate update mode arguments
    if args.update_mode and not args.diff:
        print("❌ --update-mode requires --diff to be provided")
        sys.exit(1)
    
    print("🚀 KoboToolbox Translation Agent - Test Mode")
    print("=" * 60)
    print(f"📄 Source: {args.file}")
    print(f"🌐 Target language: {args.language.upper()}")
    if args.update_mode:
        print(f"⚡ Mode: UPDATE (diff-based translation)")
    else:
        print(f"📝 Mode: NEW (full file translation)")
    print("=" * 60)
    
    try:
        # Initialize agent
        agent = TranslationAgent(test_mode=True)
        
        # Translate
        if args.update_mode:
            print(f"\n🔄 Translating diff to {args.language.upper()}...")
            translated_diff = agent.translate_file(
                args.file,
                args.language,
                is_update=True,
                diff_content=args.diff
            )
            
            # Apply to existing translation if it exists
            target_dir = Path('docs') / args.language
            target_file = target_dir / Path(args.file).name
            
            if target_file.exists() and args.save:
                print(f"\n📝 Applying translated diff to existing translation...")
                existing = target_file.read_text(encoding='utf-8')
                
                if args.old_content:
                    updated = agent.apply_translated_diff(
                        existing,
                        translated_diff,
                        old_content=args.old_content
                    )
                else:
                    # If no old_content specified, append or manual application needed
                    print("⚠️  No --old-content specified. Showing diff for manual application.")
                    updated = None
                
                if updated:
                    target_file.write_text(updated, encoding='utf-8')
                    print(f"✅ Updated translation saved to: {target_file}")
                else:
                    print("\n" + "=" * 60)
                    print("TRANSLATED DIFF (apply manually):")
                    print("=" * 60)
                    print(translated_diff)
                    print("=" * 60)
            else:
                print("\n" + "=" * 60)
                print("TRANSLATED DIFF:")
                print("=" * 60)
                print(translated_diff)
                print("=" * 60)
                if not args.save:
                    print("\nℹ️  Use --save to apply to existing translation")
        else:
            # Full file translation
            print(f"\n🔄 Translating complete file to {args.language.upper()}...")
            translation = agent.translate_file(
                args.file,
                args.language,
                args.complexity
            )
            
            # Validate
            print(f"\n✓ Translation complete!")
            print(f"\n🔍 Validating translation...")
            validation = agent.validate_translation(args.file, translation, args.language)
            
            print("\nValidation Results:")
            for check, passed in validation.items():
                if check == 'passed':
                    continue
                status = "✅" if passed else "❌"
                print(f"  {status} {check}")
            
            if validation['passed']:
                print(f"\n✅ All validation checks passed!")
            else:
                print(f"\n⚠️  Some validation checks failed - review translation carefully")
            
            # Save or display
            if args.save:
                target_path = agent.save_translation(translation, args.file, args.language)
                print(f"\n💾 Translation saved to: {target_path}")
            else:
                print("\n" + "=" * 60)
                print("TRANSLATION OUTPUT:")
                print("=" * 60)
                print(translation)
                print("=" * 60)
                print("\nℹ️  Use --save to write translation to file")
        
        print("\n✨ Translation test complete!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
