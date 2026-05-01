#!/usr/bin/env python3
"""
Validate kobo-translation source files.

Usage:
    python scripts/validate_sources.py

Checks:
    - All source files exist and are readable
    - Glossary has expected sheets and columns
    - Critical terms have translations
    - Markdown files have required sections
"""

import sys
from pathlib import Path
import pandas as pd

SKILL_ROOT = Path(__file__).parent.parent
SOURCES_DIR = SKILL_ROOT / "sources"

EXPECTED_SHEETS = [
    "Proper & Kobo specific",
    "Academy", 
    "Documentation",
    "Data collection",
    "Form building",
    "Data management",
    "Formbuilder question types",
    "Appearances",
    "Formbuilder UI ",
    "KoboCollect",
    "XLSForm",
]

REQUIRED_COLUMNS = ["English", "French", "Spanish"]

CRITICAL_TERMS = [
    "Global KoboToolbox Server",
    "European Union KoboToolbox Server",
    "Question Library",
    "KoboToolbox Academy",
    "Community Forum",
    "Help Center",
]

REQUIRED_SOURCE_FILES = [
    "glossary.xlsx",
    "style-guide.md",
    "workflow-rules.md",
    "language-rules.md",
]


def validate_glossary(filepath):
    errors = []
    
    if not filepath.exists():
        errors.append(f"Glossary not found: {filepath}")
        return errors
    
    try:
        xl = pd.ExcelFile(filepath)
    except Exception as e:
        errors.append(f"Cannot read glossary: {e}")
        return errors
    
    missing_sheets = set(EXPECTED_SHEETS) - set(xl.sheet_names)
    if missing_sheets:
        errors.append(f"Missing sheets: {', '.join(missing_sheets)}")
    
    brand_sheet = "Proper & Kobo specific"
    if brand_sheet in xl.sheet_names:
        df = pd.read_excel(xl, sheet_name=brand_sheet)
        
        missing_cols = set(REQUIRED_COLUMNS) - set(df.columns)
        if missing_cols:
            errors.append(f"Missing columns: {', '.join(missing_cols)}")
        
        if "English" in df.columns:
            english_terms = set(df["English"].dropna().tolist())
            missing_terms = set(CRITICAL_TERMS) - english_terms
            if missing_terms:
                errors.append(f"Missing critical terms: {', '.join(missing_terms)}")
    
    return errors


def validate_markdown_file(filepath, required_patterns):
    errors = []
    
    if not filepath.exists():
        errors.append(f"File not found: {filepath.name}")
        return errors
    
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        errors.append(f"Cannot read {filepath.name}: {e}")
        return errors
    
    if len(content) < 100:
        errors.append(f"{filepath.name} appears empty or too short")
    
    for pattern, error_msg in required_patterns:
        if pattern.lower() not in content.lower():
            errors.append(f"{filepath.name}: {error_msg}")
    
    return errors


def main():
    print("Validating kobo-translation source files...")
    print()
    
    all_errors = []
    
    # Check all required files exist
    print("Checking required files...")
    for filename in REQUIRED_SOURCE_FILES:
        filepath = SOURCES_DIR / filename
        if filepath.exists():
            print(f"  ✓ {filename}")
        else:
            print(f"  ✗ {filename} (MISSING)")
            all_errors.append(f"Missing required file: {filename}")
    print()
    
    # Validate glossary
    print("Validating glossary.xlsx...")
    glossary_errors = validate_glossary(SOURCES_DIR / "glossary.xlsx")
    if glossary_errors:
        all_errors.extend(glossary_errors)
        for err in glossary_errors:
            print(f"  ✗ {err}")
    else:
        print("  ✓ Glossary valid")
    
    # Validate style guide
    print("Validating style-guide.md...")
    style_errors = validate_markdown_file(
        SOURCES_DIR / "style-guide.md",
        [("formality", "Missing formality guidelines"),
         ("gender", "Missing gender-inclusive language section")]
    )
    if style_errors:
        all_errors.extend(style_errors)
        for err in style_errors:
            print(f"  ✗ {err}")
    else:
        print("  ✓ Style guide valid")
    
    # Validate workflow rules
    print("Validating workflow-rules.md...")
    workflow_errors = validate_markdown_file(
        SOURCES_DIR / "workflow-rules.md",
        [("checklist", "Missing quality checklist"),
         ("decision", "Missing decision tree or workflow")]
    )
    if workflow_errors:
        all_errors.extend(workflow_errors)
        for err in workflow_errors:
            print(f"  ✗ {err}")
    else:
        print("  ✓ Workflow rules valid")
    
    # Validate language rules
    print("Validating language-rules.md...")
    lang_errors = validate_markdown_file(
        SOURCES_DIR / "language-rules.md",
        [("french", "Missing French-specific rules"),
         ("spanish", "Missing Spanish-specific rules")]
    )
    if lang_errors:
        all_errors.extend(lang_errors)
        for err in lang_errors:
            print(f"  ✗ {err}")
    else:
        print("  ✓ Language rules valid")
    
    print()
    
    if all_errors:
        print(f"Validation failed with {len(all_errors)} error(s)")
        sys.exit(1)
    else:
        print("All validations passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()
