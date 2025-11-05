#!/usr/bin/env python3
"""
Extract Terminology from Existing Reference Files

This script parses the existing French and Spanish reference files and
extracts all terminology into the master terminology database.

Usage:
    python scripts/extract_terminology.py [--dry-run] [--output FILE]
"""

import os
import sys
import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
SKILLS_DIR = PROJECT_ROOT / 'skills'
TERMINOLOGY_DIR = PROJECT_ROOT / 'terminology'
MASTER_FILE = TERMINOLOGY_DIR / 'master_terminology.yaml'


class TerminologyExtractor:
    """Extracts terminology from existing reference markdown files."""

    def __init__(self):
        self.extracted_terms = defaultdict(list)
        self.languages = ['fr', 'es', 'ar']

    def extract_from_table(self, table_text: str, file_category: str) -> List[Dict]:
        """Extract terms from a markdown table."""
        terms = []
        lines = [l.strip() for l in table_text.strip().split('\n') if l.strip()]

        if len(lines) < 2:  # Need at least separator and one data row
            return terms

        # Find the separator row (contains dashes)
        separator_idx = None
        for i, line in enumerate(lines):
            if '---' in line:
                separator_idx = i
                break

        if separator_idx is None:
            return terms

        # Count columns from separator
        separator_cells = [c.strip() for c in lines[separator_idx].split('|')[1:-1]]
        num_columns = len(separator_cells)

        # Standard column order for KoboToolbox terminology files:
        # English | French | Spanish | Arabic (optional) | Notes (optional)
        english_idx = 0
        fr_idx = 1 if num_columns > 1 else None
        es_idx = 2 if num_columns > 2 else None

        # If 4 columns, it could be: English | French | Spanish | Notes
        # If 5 columns: English | French | Spanish | Arabic | Notes
        if num_columns == 3:
            ar_idx = None
            notes_idx = None
        elif num_columns == 4:
            # 4 columns is ambiguous - could be with Arabic or with Notes
            # Heuristic: if there's a header row before separator, check it
            # Otherwise, assume it's English | French | Spanish | Notes (most common)
            ar_idx = None
            notes_idx = 3
        elif num_columns >= 5:
            ar_idx = 3
            notes_idx = 4
        else:
            ar_idx = None
            notes_idx = None

        # Parse data rows (everything after separator)
        for line in lines[separator_idx + 1:]:
            if not line.strip() or '---' in line:
                continue

            cells = [c.strip() for c in line.split('|')[1:-1]]

            if len(cells) < 2:  # Need at least English and one translation
                continue

            english = cells[english_idx] if english_idx < len(cells) else ''

            # Skip if no English term or if it's a header row
            if not english or english in ['', 'English', 'Term']:
                continue

            fr = cells[fr_idx] if fr_idx is not None and fr_idx < len(cells) else ''
            es = cells[es_idx] if es_idx is not None and es_idx < len(cells) else ''
            ar = cells[ar_idx] if ar_idx is not None and ar_idx < len(cells) else ''
            notes = cells[notes_idx] if notes_idx is not None and notes_idx < len(cells) else ''

            # Clean up markdown formatting
            english = self.clean_text(english)
            fr = self.clean_text(fr)
            es = self.clean_text(es)
            ar = self.clean_text(ar)
            notes = self.clean_text(notes)

            # Skip if this looks like a header or empty row
            if not english or english.startswith('-'):
                continue

            # Determine category - check if file indicates OFFICIAL or PREFERRED
            category = 'OFFICIAL'  # Default for most terminology files
            if file_category in ['data_collection_terms', 'course_terms']:
                category = 'PREFERRED'

            # Create term entry
            term_entry = {
                'english': english,
                'category': category,
                'translations': {},
                'file_source': file_category
            }

            if fr:
                term_entry['translations']['fr'] = fr
            if es:
                term_entry['translations']['es'] = es
            if ar:
                term_entry['translations']['ar'] = ar
            if notes:
                term_entry['notes'] = notes

            # Only add if we have at least one translation
            if term_entry['translations']:
                terms.append(term_entry)

        return terms

    def clean_text(self, text: str) -> str:
        """Clean markdown formatting from text."""
        # Remove bold markers
        text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
        # Remove emoji/warning symbols
        text = re.sub(r'[🚨❌✅⚠️ℹ️]', '', text)
        # Clean up whitespace
        text = ' '.join(text.split())
        return text.strip()

    def extract_from_file(self, file_path: Path, category: str) -> List[Dict]:
        """Extract all terms from a reference file."""
        if not file_path.exists():
            return []

        content = file_path.read_text(encoding='utf-8')

        # Find all markdown tables - look for separator rows with dashes
        # Tables can start with or without a header row
        table_pattern = r'(?:^\|.+\|\n)*^\|[\-:| ]+\|[\-:| ]*\n(?:^\|.+\|\n)+'
        tables = re.finditer(table_pattern, content, re.MULTILINE)

        all_terms = []
        for match in tables:
            table_text = match.group(0)
            terms = self.extract_from_table(table_text, category)
            all_terms.extend(terms)

        return all_terms

    def extract_all(self) -> Dict:
        """Extract all terminology from all reference files."""

        print("📖 Extracting terminology from reference files...\n")

        categories = {
            'brand-terminology.md': 'brand_terms',
            'ui-terminology.md': 'ui_terms',
            'form-building-terms.md': 'form_building_terms',
            'question-types.md': 'question_types',
            'data-collection-terms.md': 'data_collection_terms',
            'course-terminology.md': 'course_terms',
        }

        # We'll use French as the primary source
        fr_dir = SKILLS_DIR / 'kobo-translation-fr' / 'references'

        for filename, category_name in categories.items():
            file_path = fr_dir / filename

            print(f"   Processing {filename}...")
            terms = self.extract_from_file(file_path, category_name)

            if terms:
                self.extracted_terms[category_name].extend(terms)
                print(f"      ✓ Extracted {len(terms)} terms")
            else:
                print(f"      ⚠️  No terms found")

        # Now cross-reference with Spanish to fill in any missing Spanish translations
        es_dir = SKILLS_DIR / 'kobo-translation-es' / 'references'

        print("\n   Cross-referencing with Spanish files...")
        for filename, category_name in categories.items():
            es_file = es_dir / filename
            if es_file.exists():
                es_terms = self.extract_from_file(es_file, category_name)
                self.merge_spanish_translations(category_name, es_terms)

        # Cross-reference with Arabic
        ar_dir = SKILLS_DIR / 'kobo-translation-ar' / 'references'

        print("   Cross-referencing with Arabic files...")
        for filename, category_name in categories.items():
            ar_file = ar_dir / filename
            if ar_file.exists():
                ar_terms = self.extract_from_file(ar_file, category_name)
                self.merge_arabic_translations(category_name, ar_terms)

        return dict(self.extracted_terms)

    def merge_spanish_translations(self, category: str, es_terms: List[Dict]) -> None:
        """Merge Spanish translations into extracted terms."""
        existing_terms = self.extracted_terms[category]

        # Create lookup by English term
        for es_term in es_terms:
            english = es_term['english']
            es_translation = es_term['translations'].get('es', '')

            if not es_translation:
                continue

            # Find matching term in existing
            for existing in existing_terms:
                if existing['english'] == english:
                    if 'es' not in existing['translations'] or not existing['translations']['es']:
                        existing['translations']['es'] = es_translation
                    break

    def merge_arabic_translations(self, category: str, ar_terms: List[Dict]) -> None:
        """Merge Arabic translations into extracted terms."""
        existing_terms = self.extracted_terms[category]

        for ar_term in ar_terms:
            english = ar_term['english']
            ar_translation = ar_term['translations'].get('ar', '')

            if not ar_translation:
                continue

            for existing in existing_terms:
                if existing['english'] == english:
                    if 'ar' not in existing['translations'] or not existing['translations']['ar']:
                        existing['translations']['ar'] = ar_translation
                    break

    def generate_yaml(self, extracted: Dict) -> str:
        """Generate YAML content from extracted terms."""

        # Load existing master file if it exists
        existing_data = {}
        if MASTER_FILE.exists():
            with open(MASTER_FILE, 'r', encoding='utf-8') as f:
                existing_data = yaml.safe_load(f)

        # Merge with extracted data
        output = {
            'metadata': {
                'version': '2.0',
                'last_updated': '2025-11-05',
                'generated_from': 'Extracted from existing FR/ES/AR reference files',
                'languages': ['fr', 'es', 'ar'],
                'categories': list(extracted.keys()),
            }
        }

        # Add all extracted terms
        for category, terms in extracted.items():
            output[category] = terms

        # Add language-specific patterns from existing if available
        if 'language_specific' in existing_data:
            output['language_specific'] = existing_data['language_specific']

        return yaml.dump(output, allow_unicode=True, sort_keys=False, default_flow_style=False)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Extract terminology from reference files')
    parser.add_argument('--dry-run', action='store_true',
                       help='Print extracted data without saving')
    parser.add_argument('--output', type=str,
                       help='Output file (default: terminology/master_terminology_extracted.yaml)')
    parser.add_argument('--merge', action='store_true',
                       help='Merge with existing master_terminology.yaml instead of replacing')

    args = parser.parse_args()

    extractor = TerminologyExtractor()
    extracted = extractor.extract_all()

    # Generate YAML
    yaml_content = extractor.generate_yaml(extracted)

    # Print summary
    print("\n" + "="*80)
    print("📊 EXTRACTION SUMMARY")
    print("="*80)
    total_terms = sum(len(terms) for terms in extracted.values())
    print(f"\nTotal terms extracted: {total_terms}")
    print("\nBreakdown by category:")
    for category, terms in extracted.items():
        print(f"   {category:30s}: {len(terms):3d} terms")

    # Calculate translation completeness
    print("\nTranslation completeness:")
    for lang in ['fr', 'es', 'ar']:
        count = 0
        total = 0
        for terms in extracted.values():
            for term in terms:
                total += 1
                if lang in term['translations'] and term['translations'][lang]:
                    count += 1
        percentage = (count / total * 100) if total > 0 else 0
        print(f"   {lang.upper()}: {count}/{total} ({percentage:.1f}%)")

    if args.dry_run:
        print("\n" + "="*80)
        print("DRY RUN - Sample of extracted YAML:")
        print("="*80)
        print(yaml_content[:3000])
        print("\n... (truncated) ...")
        print(f"\nTotal YAML length: {len(yaml_content)} characters")
        print("\n💡 Run without --dry-run to save to file")
        return

    # Determine output file
    if args.output:
        output_file = Path(args.output)
    else:
        if args.merge:
            output_file = MASTER_FILE
            # TODO: Implement smart merging
            print("\n⚠️  Merge mode not yet implemented")
            print("   Saving to master_terminology_extracted.yaml instead")
            output_file = TERMINOLOGY_DIR / 'master_terminology_extracted.yaml'
        else:
            output_file = TERMINOLOGY_DIR / 'master_terminology_extracted.yaml'

    # Save
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(yaml_content, encoding='utf-8')

    print(f"\n✅ Saved to: {output_file}")
    print(f"   File size: {len(yaml_content)} bytes")

    print("\n📋 Next steps:")
    print("   1. Review the extracted file carefully")
    print("   2. Compare with terminology/master_terminology.yaml")
    print("   3. Merge or replace as appropriate")
    print("   4. Run validation: python scripts/validate_guides.py")


if __name__ == '__main__':
    main()
