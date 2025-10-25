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
    
    def translate_file(self, source_path: str, target_lang: str,
                      complexity: str = None) -> str:
        """
        Translate a markdown file using Claude with embedded skill
        
        Args:
            source_path: Path to source markdown file
            target_lang: Target language (es, fr, ar)
            complexity: Force complexity level, or auto-detect if None
        """
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

Now translate this document following ALL rules above.
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
    
    args = parser.parse_args()
    
    # Verify source file exists
    if not Path(args.file).exists():
        print(f"❌ Source file not found: {args.file}")
        sys.exit(1)
    
    print("🚀 KoboToolbox Translation Agent - Test Mode")
    print("=" * 60)
    print(f"📄 Source: {args.file}")
    print(f"🌐 Target language: {args.language.upper()}")
    print("=" * 60)
    
    try:
        # Initialize agent
        agent = TranslationAgent(test_mode=True)
        
        # Translate
        print(f"\n🔄 Translating to {args.language.upper()}...")
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
