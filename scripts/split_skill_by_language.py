#!/usr/bin/env python3
"""
Split the multi-language SKILL.md and reference files into language-specific versions.
This reduces context window size by only including relevant language information.
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple

def extract_table_columns(table_text: str, keep_languages: List[str]) -> str:
    """Extract only specified language columns from markdown tables"""
    lines = table_text.strip().split('\n')
    if len(lines) < 3:  # Need header, separator, and at least one data row
        return table_text
    
    header = lines[0]
    separator = lines[1]
    data_rows = lines[2:]
    
    # Parse header to find column positions
    header_parts = [p.strip() for p in header.split('|')]
    header_parts = [p for p in header_parts if p]  # Remove empty
    
    # Find which columns to keep (English + keep_languages + Notes)
    keep_indices = []
    for i, col in enumerate(header_parts):
        col_lower = col.lower()
        if 'english' in col_lower or 'notes' in col_lower or 'note' in col_lower:
            keep_indices.append(i)
        else:
            for lang in keep_languages:
                if lang.lower() in col_lower:
                    keep_indices.append(i)
                    break
    
    if not keep_indices or len(keep_indices) == len(header_parts):
        # No filtering needed or couldn't determine structure
        return table_text
    
    # Rebuild table with only kept columns
    new_header_parts = [header_parts[i] for i in keep_indices]
    new_header = '| ' + ' | '.join(new_header_parts) + ' |'
    
    # Rebuild separator
    separator_parts = [p.strip() for p in separator.split('|')]
    separator_parts = [p for p in separator_parts if p]
    new_separator_parts = [separator_parts[i] if i < len(separator_parts) else '---' for i in keep_indices]
    new_separator = '| ' + ' | '.join(new_separator_parts) + ' |'
    
    # Rebuild data rows
    new_data_rows = []
    for row in data_rows:
        row_parts = [p.strip() for p in row.split('|')]
        row_parts = [p for p in row_parts if p or row_parts.index(p) > 0]  # Keep empty cells
        new_row_parts = [row_parts[i] if i < len(row_parts) else '' for i in keep_indices]
        new_data_rows.append('| ' + ' | '.join(new_row_parts) + ' |')
    
    return '\n'.join([new_header, new_separator] + new_data_rows)


def filter_language_specific_content(content: str, target_lang: str) -> str:
    """
    Remove language-specific content for other languages.
    Keep English source examples and target language translations.
    """
    lang_map = {
        'es': {'name': 'Spanish', 'others': ['French', 'Arabic', 'FR:', 'AR:']},
        'fr': {'name': 'French', 'others': ['Spanish', 'Arabic', 'ES:', 'AR:']},
        'ar': {'name': 'Arabic', 'others': ['French', 'Spanish', 'FR:', 'ES:']}
    }
    
    if target_lang not in lang_map:
        return content
    
    target_name = lang_map[target_lang]['name']
    other_langs = lang_map[target_lang]['others']
    
    lines = content.split('\n')
    filtered_lines = []
    skip_next = False
    in_excluded_section = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a language-specific section header to exclude
        if line.startswith('**') and any(other in line for other in other_langs):
            # Skip this section and its content until next section
            in_excluded_section = True
            i += 1
            continue
        
        # Check if we're entering our target language section
        if line.startswith('**') and target_name in line:
            in_excluded_section = False
        
        # Check for table rows with language indicators
        if '|' in line and any(f'**{other}**' in line or other in line for other in other_langs):
            # This is a table row for another language, skip it
            i += 1
            continue
        
        # If we're in an excluded section, skip
        if in_excluded_section:
            # Check if we've reached a new major section (reset)
            if line.startswith('#'):
                in_excluded_section = False
                filtered_lines.append(line)
            i += 1
            continue
        
        filtered_lines.append(line)
        i += 1
    
    return '\n'.join(filtered_lines)


def process_skill_file(source_path: Path, target_path: Path, target_lang: str):
    """Process main SKILL.md file for a specific language"""
    content = source_path.read_text(encoding='utf-8')
    
    # Update the header description
    lang_names = {'es': 'Spanish', 'fr': 'French', 'ar': 'Arabic'}
    lang_name = lang_names.get(target_lang, target_lang.upper())
    
    # Update front matter
    content = re.sub(
        r'description: "Translation and localization guidelines for KoboToolbox content in French, Spanish, and Arabic\.',
        f'description: "Translation and localization guidelines for KoboToolbox content from English to {lang_name}.',
        content
    )
    
    content = re.sub(
        r'name: kobo-translation',
        f'name: kobo-translation-{target_lang}',
        content
    )
    
    # Update overview
    content = re.sub(
        r'Translate KoboToolbox content in French, Spanish, and Arabic',
        f'Translate KoboToolbox content from English to {lang_name}',
        content
    )
    
    # Filter out other language content
    content = filter_language_specific_content(content, target_lang)
    
    # Update cross-language link examples
    if target_lang == 'es':
        content = content.replace('../en/', '../en/')  # Keep as is
        content = content.replace('../fr/', '../fr/')  # Keep for examples
        content = content.replace('../ar/', '../ar/')  # Keep for examples
    
    target_path.write_text(content, encoding='utf-8')
    print(f"✅ Created {target_path}")


def process_reference_file(source_path: Path, target_path: Path, target_lang: str):
    """Process a reference file for a specific language"""
    content = source_path.read_text(encoding='utf-8')
    
    # Keep only English and target language columns in tables
    lang_names = {'es': ['Spanish'], 'fr': ['French'], 'ar': ['Arabic']}
    keep_langs = ['English'] + lang_names.get(target_lang, [])
    
    # Filter content for target language
    content = filter_language_specific_content(content, target_lang)
    
    target_path.write_text(content, encoding='utf-8')
    print(f"✅ Created {target_path}")


def main():
    """Main execution"""
    base_dir = Path(__file__).parent.parent
    source_skill_dir = base_dir / 'skills' / 'kobo-translation'
    
    languages = ['es', 'fr', 'ar']
    
    for lang in languages:
        print(f"\n📝 Processing {lang.upper()} skill files...")
        
        target_skill_dir = base_dir / 'skills' / f'kobo-translation-{lang}'
        target_skill_dir.mkdir(parents=True, exist_ok=True)
        
        target_refs_dir = target_skill_dir / 'references'
        target_refs_dir.mkdir(parents=True, exist_ok=True)
        
        # Process main SKILL.md
        source_skill = source_skill_dir / 'SKILL.md'
        target_skill = target_skill_dir / 'SKILL.md'
        process_skill_file(source_skill, target_skill, lang)
        
        # Process reference files
        source_refs_dir = source_skill_dir / 'references'
        if source_refs_dir.exists():
            for ref_file in source_refs_dir.glob('*.md'):
                target_ref = target_refs_dir / ref_file.name
                process_reference_file(ref_file, target_ref, lang)
    
    print("\n✅ All language-specific skill files created successfully!")


if __name__ == '__main__':
    main()
