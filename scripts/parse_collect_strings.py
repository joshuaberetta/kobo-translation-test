#!/usr/bin/env python3
"""
Parse Android XML string files from kobotoolbox/collect repository.

This script fetches and parses XML string resources from the kobotoolbox/collect
repository for multiple languages (en, fr, es, ar) and creates a consolidated
JSON file containing all translations indexed by string key.

Usage:
    python scripts/parse_collect_strings.py --output skills/kobo-translation/references/collect-strings.json
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Optional
from xml.etree import ElementTree as ET

try:
    import requests
except ImportError:
    print("Error: requests library not found. Install with: pip install requests")
    sys.exit(1)


# GitHub raw content URLs for kobotoolbox/collect string files
COLLECT_STRING_URLS = {
    'en': 'https://raw.githubusercontent.com/kobotoolbox/collect/master/strings/src/main/res/values/strings.xml',
    'fr': 'https://raw.githubusercontent.com/kobotoolbox/collect/master/strings/src/main/res/values-fr/strings.xml',
    'es': 'https://raw.githubusercontent.com/kobotoolbox/collect/master/strings/src/main/res/values-es/strings.xml',
    'ar': 'https://raw.githubusercontent.com/kobotoolbox/collect/master/strings/src/main/res/values-ar/strings.xml',
}


def fetch_xml_content(url: str, language: str) -> Optional[str]:
    """Fetch XML content from GitHub URL."""
    try:
        print(f"Fetching {language} strings from {url}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Warning: Failed to fetch {language} strings: {e}")
        return None


def parse_xml_strings(xml_content: str, language: str) -> Dict[str, str]:
    """Parse Android XML string file and extract string resources.
    
    Only extracts simple <string> elements, ignoring:
    - <plurals> elements (complex plural forms)
    - <string-array> elements (arrays of strings)
    - Strings with tools:ignore attribute (usually system strings)
    """
    strings = {}
    
    try:
        # Parse XML
        root = ET.fromstring(xml_content)
        
        # Extract simple <string> elements
        for string_elem in root.findall('.//string'):
            # Get the name attribute (key)
            name = string_elem.get('name')
            if not name:
                continue
            
            # Skip strings with tools:ignore attribute (usually internal/deprecated)
            if string_elem.get('{http://schemas.android.com/tools}ignore'):
                continue
            
            # Get the text content
            text = string_elem.text or ''
            
            # Handle string elements with nested tags (like <b>, <i>, etc.)
            # Convert to plain text by joining all text
            if list(string_elem):
                text = ''.join(string_elem.itertext())
            
            # Clean up the text
            text = text.strip()
            
            if text:
                strings[name] = text
        
        print(f"  Parsed {len(strings)} strings for {language}")
        
    except ET.ParseError as e:
        print(f"Error: Failed to parse XML for {language}: {e}")
    
    return strings


def merge_translations(all_strings: Dict[str, Dict[str, str]]) -> Dict[str, Dict[str, str]]:
    """Merge all language translations into a single structure.
    
    Returns:
        Dictionary with keys as string names and values as language dictionaries.
        Example: {"enter_data": {"en": "Start new form", "fr": "Remplir un formulaire"}}
    """
    # Collect all unique keys across all languages
    all_keys = set()
    for lang_strings in all_strings.values():
        all_keys.update(lang_strings.keys())
    
    # Build merged structure
    merged = {}
    for key in sorted(all_keys):
        merged[key] = {}
        for lang in ['en', 'fr', 'es', 'ar']:  # Maintain consistent order
            if lang in all_strings and key in all_strings[lang]:
                merged[key][lang] = all_strings[lang][key]
    
    return merged


def generate_json_output(merged_strings: Dict[str, Dict[str, str]], output_path: Path) -> None:
    """Generate the consolidated JSON file."""
    # Prepare metadata
    output_data = {
        "_metadata": {
            "source": "kobotoolbox/collect Android string resources",
            "repository": "https://github.com/kobotoolbox/collect",
            "languages": ["en", "fr", "es", "ar"],
            "total_strings": len(merged_strings),
            "template_format": "{{collect:<key>}}",
            "description": "Android app UI strings for use in documentation templates"
        },
        "strings": merged_strings
    }
    
    # Create output directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write JSON file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nSuccessfully generated {output_path}")
    print(f"Total strings: {len(merged_strings)}")
    
    # Show language coverage statistics
    lang_counts = {}
    for lang in ['en', 'fr', 'es', 'ar']:
        count = sum(1 for strings in merged_strings.values() if lang in strings)
        lang_counts[lang] = count
        coverage = (count / len(merged_strings) * 100) if merged_strings else 0
        print(f"  {lang}: {count} strings ({coverage:.1f}% coverage)")


def main():
    parser = argparse.ArgumentParser(
        description='Parse Android XML strings from kobotoolbox/collect repository'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('skills/kobo-translation/references/collect-strings.json'),
        help='Output path for consolidated JSON file'
    )
    parser.add_argument(
        '--branch',
        type=str,
        default='master',
        help='Git branch to fetch from (default: master)'
    )
    
    args = parser.parse_args()
    
    # Update URLs if different branch specified
    if args.branch != 'master':
        for lang in COLLECT_STRING_URLS:
            COLLECT_STRING_URLS[lang] = COLLECT_STRING_URLS[lang].replace('/master/', f'/{args.branch}/')
    
    print("Fetching Android string resources from kobotoolbox/collect...")
    print(f"Branch: {args.branch}\n")
    
    # Fetch and parse all language files
    all_strings = {}
    for lang, url in COLLECT_STRING_URLS.items():
        xml_content = fetch_xml_content(url, lang)
        if xml_content:
            all_strings[lang] = parse_xml_strings(xml_content, lang)
    
    if not all_strings:
        print("\nError: Failed to fetch any string files.")
        sys.exit(1)
    
    # Merge translations
    print("\nMerging translations...")
    merged_strings = merge_translations(all_strings)
    
    # Generate output file
    generate_json_output(merged_strings, args.output)
    
    print("\n✓ Done!")


if __name__ == '__main__':
    main()
