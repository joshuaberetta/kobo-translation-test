---
name: kobo-translation-fr
description: "Translation and localization guidelines for KoboToolbox content from English to French. Use when translating KoboToolbox materials including: (1) Academy courses and educational content, (2) User interface text and documentation, (3) Support articles, (4) Marketing materials, (5) Form building terminology, or (6) XLSForm technical terms. Covers tone, pronouns (tu/usted, tu/vous), gender-inclusive language, and official translations for brand terms and UI elements."
---

# KoboToolbox Translation & Localization

## Overview

Translate KoboToolbox content from English to French with consistent terminology, appropriate tone, and cultural adaptation.

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

| French |
| -------- |
| vous |
| vous |
| vous |

## Gender-Inclusive Language

**French:** "utilisateur(rice)s", "Les utilisatrices et utilisateurs"

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
