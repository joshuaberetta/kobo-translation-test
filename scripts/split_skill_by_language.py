#!/usr/bin/env python3
"""
Split the multi-language SKILL.md and reference files into language-specific versions.
This reduces context window size by only including relevant language information.
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple, Set

# Language patterns for flexible column matching
LANG_PATTERNS = {
    'es': ['spanish', 'español', 'es', 'spanish (es)'],
    'fr': ['french', 'français', 'fr', 'french (fr)'],
    'ar': ['arabic', 'العربية', 'ar', 'arabic (ar)']
}

def is_target_lang_column(column_name: str, target_lang: str) -> bool:
    """Check if a column name matches the target language (handles variants)"""
    column_lower = column_name.lower().strip()
    patterns = LANG_PATTERNS.get(target_lang, [])
    # Use word boundaries to avoid false positives (e.g., 'es' in 'notes')
    return any(re.search(rf'\b{re.escape(pattern)}\b', column_lower) for pattern in patterns)

def is_other_lang_column(column_name: str, target_lang: str) -> bool:
    """Check if a column is for a different language than target"""
    column_lower = column_name.lower().strip()
    
    # Check all languages except target
    # Use word boundaries to avoid false positives (e.g., 'es' in 'notes', 'ar' in 'toolbar')
    for lang, patterns in LANG_PATTERNS.items():
        if lang != target_lang:
            if any(re.search(rf'\b{re.escape(pattern)}\b', column_lower) for pattern in patterns):
                return True
    return False

def is_metadata_column(column_name: str, target_lang: str) -> bool:
    """Check if column is metadata that should be kept (context-aware)"""
    column_lower = column_name.lower().strip()
    
    # Always keep these technical columns
    technical_keywords = ['xlsform', 'question type', 'appearance']
    if any(keyword in column_lower for keyword in technical_keywords):
        return True
    
    # Keep general metadata columns
    metadata_keywords = ['notes', 'note', 'example', 'context']
    has_metadata = any(keyword in column_lower for keyword in metadata_keywords)
    
    # But exclude error columns for other languages
    if '❌' in column_name or 'error' in column_lower or 'common error' in column_lower:
        # Only keep if no other language mentioned, or if target language mentioned
        if is_target_lang_column(column_name, target_lang):
            return True
        if is_other_lang_column(column_name, target_lang):
            return False
        # Generic error column with no language specified - keep it
        return True
    
    # Check for language-specific recommended updates
    if 'recommended' in column_lower or 'update' in column_lower:
        # Only keep if it's for the target language or language-agnostic
        if is_other_lang_column(column_name, target_lang):
            return False
        return True
    
    return has_metadata

def extract_table_columns(table_text: str, target_lang: str) -> str:
    """Extract only specified language columns from markdown tables"""
    lines = table_text.strip().split('\n')
    if len(lines) < 3:  # Need header, separator, and at least one data row
        return table_text
    
    header = lines[0]
    separator = lines[1]
    
    # Parse header to find column positions
    header_parts = [p.strip() for p in header.split('|')]
    header_parts = [p for p in header_parts if p]  # Remove empty
    
    if not header_parts:
        return table_text
    
    num_columns = len(header_parts)
    
    # Find which columns to keep
    keep_indices = []
    for i, col in enumerate(header_parts):
        col_lower = col.lower().strip()
        
        # Always keep English (source language)
        if 'english' in col_lower:
            keep_indices.append(i)
            continue
        
        # Keep target language column
        if is_target_lang_column(col, target_lang):
            keep_indices.append(i)
            continue
        
        # Skip other language columns
        if is_other_lang_column(col, target_lang):
            continue
        
        # Keep metadata columns (context-aware)
        if is_metadata_column(col, target_lang):
            keep_indices.append(i)
            continue
    
    # If we're keeping all columns or couldn't determine structure, return as-is
    if not keep_indices or len(keep_indices) == len(header_parts):
        return table_text
    
    # Rebuild table with only kept columns
    new_header_parts = [header_parts[i] for i in keep_indices]
    new_header = '| ' + ' | '.join(new_header_parts) + ' |'
    
    # Rebuild separator
    separator_parts = [p.strip() for p in separator.split('|')]
    separator_parts = [p for p in separator_parts if p]
    new_separator_parts = [separator_parts[i] if i < len(separator_parts) else '---' for i in keep_indices]
    new_separator = '| ' + ' | '.join(new_separator_parts) + ' |'
    
    # Process data rows - handle multi-line cells
    data_rows = lines[2:]
    new_data_rows = []
    
    for row in data_rows:
        # Count pipes to determine if this is a complete row
        pipe_count = row.count('|')
        
        # A proper markdown table row has num_columns + 1 pipes (one at start, one at end, rest between)
        # But cells can contain content without being properly formatted
        # We'll be lenient and just parse what we can
        
        # Split by pipe but be careful
        row_parts = row.split('|')
        # Remove leading/trailing empty parts from pipe delimiters
        if row_parts and row_parts[0].strip() == '':
            row_parts = row_parts[1:]
        if row_parts and row_parts[-1].strip() == '':
            row_parts = row_parts[:-1]
        
        # Only process rows that have the expected number of columns
        if len(row_parts) != num_columns:
            # This is likely a continuation line from a multi-line cell
            # Keep it as-is to preserve content even if table formatting is imperfect
            new_data_rows.append(row)
            continue
        
        # Strip whitespace but preserve empty cells and newlines within cells
        row_parts = [p.strip() for p in row_parts]
        
        # Build new row with only kept columns
        new_row_parts = [row_parts[i] if i < len(row_parts) else '' for i in keep_indices]
        new_data_rows.append('| ' + ' | '.join(new_row_parts) + ' |')
    
    return '\n'.join([new_header, new_separator] + new_data_rows)


def filter_prose_sections(content: str, target_lang: str) -> str:
    """
    Filter out language-specific prose sections for non-target languages.
    Handles usage guides, example blocks, and guideline sections.
    """
    lang_map = {
        'es': {'name': 'Spanish', 'code': 'ES', 'others': ['French', 'Arabic', 'FR', 'AR']},
        'fr': {'name': 'French', 'code': 'FR', 'others': ['Spanish', 'Arabic', 'ES', 'AR']},
        'ar': {'name': 'Arabic', 'code': 'AR', 'others': ['French', 'Spanish', 'FR', 'ES']}
    }
    
    if target_lang not in lang_map:
        return content
    
    target_name = lang_map[target_lang]['name']
    target_code = lang_map[target_lang]['code']
    other_langs = lang_map[target_lang]['others']
    
    lines = content.split('\n')
    filtered_lines = []
    in_excluded_section = False
    section_depth = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for language-specific section headers (### French-Specific Rules, ### Spanish Usage, etc.)
        # Pattern: ### Language "something" or ### Language-Specific or **Language:**
        if re.match(r'^#{2,}\s+(' + '|'.join(other_langs) + r')(-Specific|\s+)', line, re.IGNORECASE):
            in_excluded_section = True
            section_depth = len(re.match(r'^(#{2,})', line).group(1))
            i += 1
            continue
        
        # Check for bold language-specific headers (**French:** or **Spanish "..." Usage**)
        if line.startswith('**') and any(f'**{lang}' in line for lang in other_langs):
            # Skip this line and continue until we find a new section or blank line
            in_excluded_section = True
            section_depth = 0  # Bold sections end at next major section or blank line followed by new section
            i += 1
            continue
        
        # Check for example blocks (✅ CORRECT Spanish:, ❌ WRONG French:)
        if re.search(r'[✅❌]\s*(CORRECT|WRONG)\s+(' + '|'.join(other_langs) + r')', line, re.IGNORECASE):
            in_excluded_section = True
            section_depth = 0  # Example blocks end at next example or major section
            i += 1
            continue
        
        # Check if we're exiting an excluded section
        if in_excluded_section:
            # Exit on new heading at same or higher level
            if section_depth > 0 and re.match(r'^#{1,' + str(section_depth) + r'}\s+', line):
                in_excluded_section = False
                filtered_lines.append(line)
                i += 1
                continue
            
            # Exit on new bold language section for target language
            if line.startswith('**') and (f'**{target_name}' in line or f'**{target_code}' in line):
                in_excluded_section = False
                filtered_lines.append(line)
                i += 1
                continue
            
            # Exit on new example block for target language or English
            if re.search(r'[✅❌]\s*(CORRECT|WRONG)\s+(English|' + target_name + r')', line, re.IGNORECASE):
                in_excluded_section = False
                filtered_lines.append(line)
                i += 1
                continue
            
            # Exit on blank line followed by non-language-specific content (for bold sections)
            if section_depth == 0 and line.strip() == '':
                # Peek ahead to see if next non-blank line is a new section
                j = i + 1
                while j < len(lines) and lines[j].strip() == '':
                    j += 1
                if j < len(lines):
                    next_line = lines[j]
                    # If next line is a heading or doesn't start with language marker, exit section
                    if (next_line.startswith('#') or 
                        (next_line.startswith('**') and not any(f'**{lang}' in next_line for lang in other_langs)) or
                        not any(lang.lower() in next_line.lower() for lang in other_langs)):
                        in_excluded_section = False
                        filtered_lines.append(line)
                        i += 1
                        continue
            
            # Still in excluded section, skip this line
            i += 1
            continue
        
        # Not in excluded section, keep the line
        filtered_lines.append(line)
        i += 1
    
    return '\n'.join(filtered_lines)


def process_tables_in_content(content: str, target_lang: str) -> str:
    """
    Find all markdown tables in content and apply column filtering to each.
    """
    # Pattern to match markdown tables (header | separator | rows)
    # This is a simple approach: find table blocks by looking for consecutive lines with |
    lines = content.split('\n')
    result_lines = []
    in_table = False
    table_lines = []
    
    for i, line in enumerate(lines):
        # Check if this line is part of a table (contains |)
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_lines = [line]
            else:
                table_lines.append(line)
        else:
            # Not a table line
            if in_table:
                # End of table - process accumulated table
                if len(table_lines) >= 3:  # Valid table needs at least header, separator, one row
                    table_text = '\n'.join(table_lines)
                    filtered_table = extract_table_columns(table_text, target_lang)
                    result_lines.append(filtered_table)
                else:
                    # Not enough lines for a valid table, keep as-is
                    result_lines.extend(table_lines)
                
                in_table = False
                table_lines = []
            
            # Add the non-table line
            result_lines.append(line)
    
    # Handle case where content ends with a table
    if in_table and len(table_lines) >= 3:
        table_text = '\n'.join(table_lines)
        filtered_table = extract_table_columns(table_text, target_lang)
        result_lines.append(filtered_table)
    elif in_table:
        result_lines.extend(table_lines)
    
    return '\n'.join(result_lines)


def filter_language_specific_content(content: str, target_lang: str) -> str:
    """
    Legacy function - now delegates to the more comprehensive filtering functions.
    Remove language-specific content for other languages.
    Keep English source examples and target language translations.
    """
    # First filter prose sections (usage guides, examples, guidelines)
    content = filter_prose_sections(content, target_lang)
    
    # Then filter table columns
    content = process_tables_in_content(content, target_lang)
    
    return content


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
    
    # Apply comprehensive language-specific filtering
    # This now handles both table columns and prose sections
    content = filter_language_specific_content(content, target_lang)
    
    target_path.write_text(content, encoding='utf-8')
    print(f"✅ Created {target_path}")


def main():
    """Main execution"""
    base_dir = Path(__file__).parent.parent
    source_skill_dir = base_dir / 'skills' / 'kobo-translation-v2'
    
    languages = ['es', 'fr', 'ar']
    
    for lang in languages:
        print(f"\n📝 Processing {lang.upper()} skill files...")
        
        target_skill_dir = base_dir / 'skills' / f'kobo-translation-v2-{lang}'
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
