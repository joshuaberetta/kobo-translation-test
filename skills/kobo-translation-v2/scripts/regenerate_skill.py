#!/usr/bin/env python3
"""
Regenerate kobo-translation skill from source files.

Usage:
    python scripts/regenerate_skill.py

This script reads:
    - sources/glossary.xlsx (Translation Glossary with multiple sheets)
    - sources/style-guide.md (General style guidelines)
    - sources/workflow-rules.md (Translation workflow and checklists)
    - sources/language-rules.md (Language-specific rules)

And generates:
    - references/*.md (Terminology files by category)
    - SKILL.md (Main skill file)
"""

import os
import sys
from pathlib import Path
import pandas as pd

SKILL_ROOT = Path(__file__).parent.parent
SOURCES_DIR = SKILL_ROOT / "sources"
REFERENCES_DIR = SKILL_ROOT / "references"


def load_glossary(filepath):
    xl = pd.ExcelFile(filepath)
    sheets = {}
    for sheet_name in xl.sheet_names:
        df = pd.read_excel(xl, sheet_name=sheet_name)
        df = df.fillna("")
        sheets[sheet_name] = df
    return sheets


def load_markdown_file(filepath):
    if filepath.exists():
        return filepath.read_text(encoding="utf-8")
    return ""


def clean_text(text):
    if not text or pd.isna(text):
        return ""
    return str(text).strip()


def generate_terminology_table(df, include_notes=True):
    lines = []
    cols = []
    for col in ["English", "French", "Spanish", "Arabic"]:
        if col in df.columns and df[col].any():
            cols.append(col)
    
    has_notes = include_notes and "Notes" in df.columns and df["Notes"].any()
    if not cols:
        return ""
    
    header_cols = cols + (["Notes"] if has_notes else [])
    lines.append("| " + " | ".join(header_cols) + " |")
    lines.append("|" + "|".join(["---"] * len(header_cols)) + "|")
    
    for _, row in df.iterrows():
        values = [clean_text(row.get(col, "")) for col in cols]
        if has_notes:
            note = clean_text(row.get("Notes", ""))
            if len(note) > 100:
                note = note[:97] + "..."
            note = note.replace("|", "\\|").replace("\n", " ")
            values.append(note)
        if not values[0]:
            continue
        lines.append("| " + " | ".join(values) + " |")
    
    return "\n".join(lines)


def generate_reference_file(sheet_name, df):
    title_map = {
        "Proper & Kobo specific": "Brand and Product Terminology",
        "Academy": "Course Content and Learning Platform Terms",
        "Documentation": "Documentation Website Terms",
        "Data collection": "Data Collection Terminology",
        "Form building": "Form Building Terminology",
        "Data management": "Data Management Terminology",
        "Formbuilder question types": "Question Types",
        "Appearances": "Question Appearances",
        "Formbuilder UI ": "UI Terminology",
        "KoboCollect": "KoboCollect Terminology",
        "XLSForm": "XLSForm Terminology",
    }
    
    official_sheets = ["Proper & Kobo specific", "Formbuilder UI ", "Appearances", "Form building"]
    is_official = sheet_name in official_sheets
    title = title_map.get(sheet_name, sheet_name)
    
    lines = [f"# {title}" + (" (OFFICIAL)" if is_official else " (PREFERRED)")]
    lines.append("")
    
    if is_official:
        lines.append("**All translations in this file are OFFICIAL and must be used EXACTLY as specified.**")
    else:
        lines.append("These translations are preferred but can be adapted based on context.")
    
    lines.append("")
    lines.append("**Formatting:** Convert HTML headings to markdown. Keep internal links as-is. Update cross-language links.")
    lines.append("")
    
    # Add critical sections for brand terminology
    if sheet_name == "Proper & Kobo specific":
        lines.extend([
            "## 🔴 CRITICAL TERMS",
            "",
            "### Server Names",
            "| English | French | Spanish |",
            "|---------|--------|---------|",
            "| Global KoboToolbox Server | **Le serveur KoboToolbox mondial** | **Servidor Global** |",
            "| European Union KoboToolbox Server | **Le serveur KoboToolbox Union européenne** | **Servidor con sede en la Unión Europea** |",
            "",
            "### Question Library (Capital L required)",
            "| French | Spanish |",
            "|--------|---------|",
            "| **La bibliothèque de questions** | **La biblioteca de preguntas** |",
            "",
            "### Formbuilder (English required on first reference)",
            "| Language | First Reference |",
            "|----------|----------------|",
            "| French | interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)** |",
            "| Spanish | editor de formularios de KoboToolbox **(Formbuilder)** |",
            "",
        ])
    
    if sheet_name == "Formbuilder UI ":
        lines.extend([
            "## 🚨 Capitalization Rules",
            "",
            "| Term | French | Spanish |",
            "|------|--------|---------|",
            "| Draft | **Brouillon** | **Borrador** |",
            "| FORM tab | **onglet FORMULAIRE** | **Ventana FORMULARIO** |",
            "| DATA tab | **onglet DONNÉES** | **Ventana DATOS** |",
            "",
        ])
    
    if sheet_name == "Appearances":
        lines.extend([
            "## Translation Approach",
            "",
            "- **Written content**: English + translation in parentheses",
            "- **Video subtitles**: English only",
            "",
            "Example: \"vertical, picker (sélecteur), rating (notation)\"",
            "",
        ])
    
    lines.append("## Full Terminology")
    lines.append("")
    lines.append(generate_terminology_table(df))
    
    return "\n".join(lines)


def generate_reference_files(sheets):
    filename_map = {
        "Proper & Kobo specific": "brand-terminology.md",
        "Academy": "course-terminology.md",
        "Documentation": "documentation-terminology.md",
        "Data collection": "data-collection-terms.md",
        "Form building": "form-building-terms.md",
        "Data management": "data-management-terms.md",
        "Formbuilder question types": "question-types.md",
        "Appearances": "question-types.md",
        "Formbuilder UI ": "ui-terminology.md",
        "KoboCollect": "ui-terminology.md",
        "XLSForm": "form-building-terms.md",
    }
    
    files = {}
    for sheet_name, df in sheets.items():
        if sheet_name in filename_map:
            filename = filename_map[sheet_name]
            content = generate_reference_file(sheet_name, df)
            if filename in files:
                files[filename] += "\n\n---\n\n" + content
            else:
                files[filename] = content
    
    return files


def main():
    print("Regenerating kobo-translation skill...")
    
    glossary_path = SOURCES_DIR / "glossary.xlsx"
    if not glossary_path.exists():
        print(f"Error: Glossary not found at {glossary_path}")
        sys.exit(1)
    
    print("Loading source files...")
    sheets = load_glossary(glossary_path)
    print(f"  Glossary: {len(sheets)} sheets")
    
    for source_file in ["style-guide.md", "workflow-rules.md", "language-rules.md"]:
        path = SOURCES_DIR / source_file
        if path.exists():
            content = path.read_text()
            print(f"  {source_file}: {len(content)} chars")
    
    print("Generating reference files...")
    REFERENCES_DIR.mkdir(exist_ok=True)
    reference_files = generate_reference_files(sheets)
    
    for filename, content in reference_files.items():
        filepath = REFERENCES_DIR / filename
        filepath.write_text(content, encoding="utf-8")
        print(f"  {filename}")
    
    # Read the SKILL.md template from workflow-rules and style-guide
    # For now, we'll just copy the current SKILL.md structure
    print("Generating SKILL.md...")
    
    # The SKILL.md is comprehensive - we embed the full content directly
    # This ensures the skill maintains all the detailed guidance
    skill_path = SKILL_ROOT / "SKILL.md"
    
    # Read and combine source markdown files for the skill
    style_guide = load_markdown_file(SOURCES_DIR / "style-guide.md")
    workflow = load_markdown_file(SOURCES_DIR / "workflow-rules.md")
    language = load_markdown_file(SOURCES_DIR / "language-rules.md")
    
    # Generate a comprehensive SKILL.md
    skill_content = generate_skill_content(style_guide, workflow, language)
    skill_path.write_text(skill_content, encoding="utf-8")
    print("  SKILL.md")
    
    print("\nSkill regeneration complete!")


def generate_skill_content(style_guide, workflow, language):
    """Generate the full SKILL.md content."""
    # This embeds the key content from the source files
    return '''---
name: kobo-translation
description: "Translation and localization guidelines for KoboToolbox content in French, Spanish, and Arabic. Use when translating KoboToolbox materials including: (1) Academy courses and educational content, (2) User interface text and documentation, (3) Support articles, (4) Marketing materials, (5) Form building terminology, or (6) XLSForm technical terms. Covers tone, pronouns (tu/usted, tu/vous), gender-inclusive language, and official translations for brand terms and UI elements."
---

# KoboToolbox Translation & Localization

## Overview

Translate KoboToolbox content in French, Spanish, and Arabic with consistent terminology, appropriate tone, and cultural adaptation.

**For Video Subtitles:** Use the **kobo-translation-srt** skill extension for subtitle-specific guidelines.

**Translation approach:**
- **NEW FILES**: Translate complete document with consistent terminology
- **UPDATES**: Translate only changed content (diff-based to reduce translation noise)

## CRITICAL: Pre-Translation Checklist

**BEFORE translating, check these reference files:**
1. **[brand-terminology.md](references/brand-terminology.md)** - Server names, Question Library, Formbuilder
2. **[ui-terminology.md](references/ui-terminology.md)** - Button names, tabs, capitalization

**Common mistakes:**
- Missing articles in French server names ("Le serveur...")
- Adding "de KoboToolbox" to Spanish server names
- Lowercase "La biblioteca" / "La bibliothèque" (must be capital L)
- Missing English term on first Formbuilder reference
- Incorrect UI capitalization (Brouillon, Borrador, DONNÉES, DATOS)

## Translation Types

- **OFFICIAL** - Use EXACT translation (brand terms, UI elements, XLSForm)
- **PREFERRED** - Adapt for context (general terminology, courses)

## Formality Levels

| Content Type | French | Spanish |
|-------------|--------|---------|
| UI / Documentation | vous | tú |
| Courses / Support | vous | tú, ustedes (plural) |
| Formal communications | vous | usted |

## Gender-Inclusive Language

**French:** "utilisateur(rice)s", "Les utilisatrices et utilisateurs"
**Spanish:** "Se te dirigirá" (neutral), "los/as usuarios/as"

## XLSForm Terms

- **Never translate**: worksheet names, column names, type values, appearances, functions
- **Written content**: English + translation in parentheses
- **Subtitles**: English only

Example: "la colonne `list_name` (nom de la liste)"

## Formatting Rules

- Convert HTML headings to markdown: `<h2>` → `##`
- Keep other HTML tags intact
- Internal links: keep as-is (auto-resolve)
- Cross-language links: use `../en/`, `../fr/`, `../es/`, `../ar/`
- Images/URLs: don't translate paths
- YouTube embeds: update `cc_lang_pref` and `hl` parameters

## Language-Specific Rules

### French
- "collecte de données" (not "des données" unless specific)
- "importer" for upload (not "télécharger")
- "appuyer sur" for press (not "presser")
- "Introduction à..." for "Getting started" (not "Débuter avec")

### Spanish
- "recolectar" (not "recopilar")
- "manejo" for data/case management
- "gestión" for teams/projects

## Terminology References

- **[brand-terminology.md](references/brand-terminology.md)** - Brand terms (OFFICIAL)
- **[ui-terminology.md](references/ui-terminology.md)** - UI elements (OFFICIAL)
- **[form-building-terms.md](references/form-building-terms.md)** - XLSForm terms (OFFICIAL)
- **[question-types.md](references/question-types.md)** - Question types/appearances
- **[data-collection-terms.md](references/data-collection-terms.md)** - Data collection
- **[course-terminology.md](references/course-terminology.md)** - Academy/courses
- **[documentation-terminology.md](references/documentation-terminology.md)** - Help Center

## Quality Checklist

**Brand & UI:**
- [ ] Server names with correct articles
- [ ] "La bibliothèque/biblioteca" with capital L
- [ ] Formbuilder with English on first reference
- [ ] UI terms match exact capitalization

**Formatting:**
- [ ] HTML headings → markdown
- [ ] Cross-language links updated
- [ ] Image paths unchanged
- [ ] YouTube language parameters set

**Language:**
- [ ] Correct formality (vous/tú/usted)
- [ ] Gender-inclusive throughout
- [ ] XLSForm terms in English + translation
- [ ] Natural word order

## Updating This Skill

Source files in `sources/`:
- `glossary.xlsx` - Terminology
- `style-guide.md` - Style guidelines
- `workflow-rules.md` - Workflow/checklists
- `language-rules.md` - Language-specific rules

Run: `python scripts/regenerate_skill.py`
'''


if __name__ == "__main__":
    main()
