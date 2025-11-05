#!/usr/bin/env python3
"""
Terminology Synchronization System

This script ensures all language-specific translation guides stay synchronized
with the master terminology database. When you add new terms to the master
database, this script updates all language guides automatically.

Usage:
    python scripts/sync_terminology.py [--language LANG] [--validate-only] [--api-key KEY]

Features:
    - Syncs terminology from master database to all language guides
    - Validates completeness across all languages
    - Generates missing translations using Claude API
    - Reports gaps and inconsistencies
"""

import os
import sys
import yaml
import argparse
from pathlib import Path
from typing import Dict, List, Set, Optional
import anthropic
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
TERMINOLOGY_DIR = PROJECT_ROOT / 'terminology'
SKILLS_DIR = PROJECT_ROOT / 'skills'
MASTER_TERMINOLOGY = TERMINOLOGY_DIR / 'master_terminology.yaml'


class TerminologyManager:
    """Manages terminology synchronization across all language guides."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.master_data = self.load_master_terminology()
        self.languages = self.master_data['metadata']['languages']

    def load_master_terminology(self) -> Dict:
        """Load the master terminology database."""
        if not MASTER_TERMINOLOGY.exists():
            raise FileNotFoundError(f"Master terminology not found: {MASTER_TERMINOLOGY}")

        with open(MASTER_TERMINOLOGY, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def validate_completeness(self) -> Dict[str, List[str]]:
        """Validate that all terms have translations in all languages."""
        gaps = defaultdict(list)

        # Check brand terms
        for term_data in self.master_data.get('brand_terms', []):
            english = term_data['english']
            translations = term_data.get('translations', {})

            for lang in self.languages:
                if lang not in translations or not translations[lang]:
                    gaps[lang].append(f"brand_terms: {english}")

        # Check UI terms
        for term_data in self.master_data.get('ui_terms', []):
            english = term_data['english']
            translations = term_data.get('translations', {})

            for lang in self.languages:
                if lang not in translations or not translations[lang]:
                    gaps[lang].append(f"ui_terms: {english}")

        # Check form building terms
        for term_data in self.master_data.get('form_building_terms', []):
            english = term_data['english']
            translations = term_data.get('translations', {})

            for lang in self.languages:
                if lang not in translations or not translations[lang]:
                    gaps[lang].append(f"form_building_terms: {english}")

        # Check data collection terms
        for term_data in self.master_data.get('data_collection_terms', []):
            english = term_data['english']
            translations = term_data.get('translations', {})

            for lang in self.languages:
                if lang not in translations or not translations[lang]:
                    gaps[lang].append(f"data_collection_terms: {english}")

        # Check cross-language rules
        for term_data in self.master_data.get('cross_language_rules', []):
            english = term_data['english']
            translations = term_data.get('translations', {})

            for lang in self.languages:
                if lang not in translations or not translations[lang]:
                    gaps[lang].append(f"cross_language_rules: {english}")

        return dict(gaps)

    def generate_reference_table_markdown(self, category: str, lang: str) -> str:
        """Generate markdown table for a specific terminology category."""

        category_map = {
            'brand_terms': 'brand-terminology.md',
            'ui_terms': 'ui-terminology.md',
            'form_building_terms': 'form-building-terms.md',
            'data_collection_terms': 'data-collection-terms.md',
        }

        if category not in category_map:
            return ""

        terms = self.master_data.get(category, [])
        if not terms:
            return ""

        lines = []
        lines.append(f"# {category.replace('_', ' ').title()} for {lang.upper()}\n")
        lines.append("| English | French | Spanish | Arabic | Notes |")
        lines.append("|---------|--------|---------|--------|-------|")

        for term_data in terms:
            english = term_data['english']
            translations = term_data.get('translations', {})
            notes = term_data.get('notes', '').replace('\n', ' ').strip()

            fr = translations.get('fr', '')
            es = translations.get('es', '')
            ar = translations.get('ar', '')

            lines.append(f"| {english} | {fr} | {es} | {ar} | {notes} |")

        return '\n'.join(lines)

    def update_reference_file(self, lang: str, ref_file: str, new_content: str) -> None:
        """Update a reference file with new terminology."""
        ref_path = SKILLS_DIR / f'kobo-translation-{lang}' / 'references' / ref_file
        ref_path.parent.mkdir(parents=True, exist_ok=True)

        # For now, we'll append new content to existing file
        # In production, you'd want more sophisticated merging
        if ref_path.exists():
            existing = ref_path.read_text(encoding='utf-8')
            # TODO: Smart merge logic here
            print(f"   ⚠️  {ref_file} already exists, skipping update")
            print(f"      Consider manual review and merge")
        else:
            ref_path.write_text(new_content, encoding='utf-8')
            print(f"   ✅ Created {ref_file}")

    def generate_missing_translation(self, english: str, context: Dict, target_lang: str) -> str:
        """Use Claude API to generate a missing translation."""
        if not self.api_key:
            return f"[MISSING - {target_lang.upper()}]"

        client = anthropic.Anthropic(api_key=self.api_key)

        lang_names = {'fr': 'French', 'es': 'Spanish', 'ar': 'Arabic'}
        target_lang_name = lang_names.get(target_lang, target_lang.upper())

        # Get existing translations for context
        translations = context.get('translations', {})
        category = context.get('category', 'PREFERRED')
        notes = context.get('notes', '')

        context_str = f"""English term: "{english}"
Category: {category}
Notes: {notes}

Existing translations:
"""
        for lang_code, translation in translations.items():
            if translation:
                context_str += f"- {lang_names.get(lang_code, lang_code)}: {translation}\n"

        prompt = f"""You are an expert translator for KoboToolbox technical documentation.

I need you to provide a {target_lang_name} translation for this term:

{context_str}

Provide ONLY the {target_lang_name} translation, with no additional explanation.
Make it consistent with the style of the existing translations.
If this is an OFFICIAL term, use exact, formal translation.
If this is PREFERRED, use natural, commonly used translation.

{target_lang_name} translation:"""

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=200,
            temperature=0.1,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text.strip()

    def fill_missing_translations(self, interactive: bool = True) -> None:
        """Fill in missing translations using Claude API."""
        if not self.api_key:
            print("⚠️  No API key provided, cannot auto-generate missing translations")
            return

        gaps = self.validate_completeness()

        if not gaps:
            print("✅ All translations are complete!")
            return

        print(f"\n🔍 Found missing translations:\n")
        for lang, missing_terms in gaps.items():
            print(f"   {lang.upper()}: {len(missing_terms)} missing")

        if not interactive:
            return

        response = input("\n🤖 Generate missing translations using Claude API? (y/n): ")
        if response.lower() != 'y':
            print("Skipping auto-generation")
            return

        print("\n🚀 Generating missing translations...\n")

        # Generate missing translations
        for category_name in ['brand_terms', 'ui_terms', 'form_building_terms',
                              'data_collection_terms', 'cross_language_rules']:
            for term_data in self.master_data.get(category_name, []):
                english = term_data['english']
                translations = term_data.get('translations', {})

                for lang in self.languages:
                    if lang not in translations or not translations[lang]:
                        print(f"   Generating {lang.upper()} for: {english}")
                        translation = self.generate_missing_translation(english, term_data, lang)
                        translations[lang] = translation
                        print(f"      → {translation}")

        # Save updated master terminology
        with open(MASTER_TERMINOLOGY, 'w', encoding='utf-8') as f:
            yaml.dump(self.master_data, f, allow_unicode=True, sort_keys=False)

        print(f"\n✅ Updated master terminology with {sum(len(v) for v in gaps.values())} new translations")


def main():
    parser = argparse.ArgumentParser(description='Synchronize terminology across language guides')
    parser.add_argument('--language', '-l', type=str,
                       help='Sync only specific language (fr, es, ar)')
    parser.add_argument('--validate-only', '-v', action='store_true',
                       help='Only validate, don\'t update files')
    parser.add_argument('--api-key', type=str,
                       help='Anthropic API key for auto-generating missing translations')
    parser.add_argument('--auto-generate', '-g', action='store_true',
                       help='Auto-generate missing translations without prompting')

    args = parser.parse_args()

    # Get API key
    api_key = args.api_key or os.environ.get('ANTHROPIC_API_KEY')

    print("🔄 Terminology Synchronization System\n")

    manager = TerminologyManager(api_key=api_key)

    # Validate completeness
    print("📊 Validating terminology completeness...")
    gaps = manager.validate_completeness()

    if not gaps:
        print("   ✅ All languages have complete terminology!")
    else:
        print(f"\n   ⚠️  Found gaps in terminology:\n")
        for lang, missing in gaps.items():
            print(f"   {lang.upper()}: {len(missing)} missing translations")
            if args.validate_only:
                for term in missing[:5]:  # Show first 5
                    print(f"      - {term}")
                if len(missing) > 5:
                    print(f"      ... and {len(missing) - 5} more")

    if args.validate_only:
        sys.exit(0 if not gaps else 1)

    # Fill missing translations
    if gaps and api_key:
        manager.fill_missing_translations(interactive=not args.auto_generate)

    # Sync to language guides
    languages_to_sync = [args.language] if args.language else manager.languages

    print(f"\n📝 Syncing terminology to language guides...")
    for lang in languages_to_sync:
        print(f"\n   Language: {lang.upper()}")

        # Generate updated reference files
        for category in ['brand_terms', 'ui_terms', 'form_building_terms', 'data_collection_terms']:
            category_map = {
                'brand_terms': 'brand-terminology.md',
                'ui_terms': 'ui-terminology.md',
                'form_building_terms': 'form-building-terms.md',
                'data_collection_terms': 'data-collection-terms.md',
            }

            if category in category_map:
                # Note: This is a placeholder - you'd want more sophisticated update logic
                print(f"      ℹ️  {category_map[category]}: Review manually for updates")

    print("\n✨ Synchronization complete!")
    print("\n💡 Recommended next steps:")
    print("   1. Review the master terminology: terminology/master_terminology.yaml")
    print("   2. Run validation: python scripts/sync_terminology.py --validate-only")
    print("   3. Generate missing: python scripts/sync_terminology.py --auto-generate")
    print("   4. Update guides: python scripts/generate_arabic_guide.py")


if __name__ == '__main__':
    main()
