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
3. **[article-titles.md](references/article-titles.md)** - Official article titles in all languages (OFFICIAL — verbatim)

## Translation Types

- **OFFICIAL** - Use EXACT translation (brand terms, UI elements, XLSForm)
- **PREFERRED** - Adapt for context (general terminology, courses)

## XLSForm Terms

- **Never translate**: worksheet names, column names, type values, appearances, functions
- **Written content**: English + translation in parentheses
- **Subtitles**: English only

Example: `` `list_name` (nom de la liste / nombre de la lista) ``

## French Critical Rules

🚨 The **first mention** of the Formbuilder in any French article must include the English name in parentheses:

> interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**

Subsequent mentions can use the short form "Formbuilder" or "l'interface de création de formulaires".

## French Formality

Use **vous** throughout all French documentation and UI text.

| French |
| --- |
| vous |
| vous |
| vous |

## French Gender-Inclusive Language

🚨 Every mention of users or people must use inclusive forms:
- "utilisateur(rice)s" — NOT "utilisateurs" or "utilisateur(s)"
- "Les utilisatrices et utilisateurs" for formal constructions

Scan the entire article before submitting: if you find any bare "utilisateur(s)" or "les utilisateurs", replace it. This applies everywhere: body text, bullet lists, tables, and `<p class="note">` callouts.

## French Language Rules

- "collecte de données" (not "des données" unless specific)
- "importer" for upload (not "télécharger")
- "appuyer sur" for press (not "presser")
- "Introduction à..." for "Getting started" (not "Débuter avec")
- First Formbuilder mention: `interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**`

## French XLSForm Worksheet Tab Labels

When the source has a bold worksheet label like `**survey worksheet**`, `**choices worksheet**`, or `**settings worksheet**`, translate it using the pattern `**onglet [name]**` — keep the sheet name in English, prefix with the translated word only:

| English | French |
|---------|--------|
| `**survey worksheet**` | `**onglet survey**` |
| `**choices worksheet**` | `**onglet choices**` |
| `**settings worksheet**` | `**onglet settings**` |

🚨 Do NOT write `**hoja survey**` or `**hoja settings**` in French — those are Spanish forms. French always uses `**onglet**`.

## French Quality Checklist

- [ ] vous throughout
- [ ] First Formbuilder mention includes `(KoboToolbox Formbuilder)` parenthetical
- [ ] gender-inclusive — "utilisateur(rice)s" not "utilisateurs" — every mention including notes/callouts
- [ ] Worksheet labels use `**onglet survey**` not `**hoja survey**`
- [ ] Article H1 matches article-titles.md French entry exactly
- [ ] Cross-referenced article titles match article-titles.md French entries exactly

## Formatting Rules

- Convert HTML headings to markdown: `<h1>` → `#`, `<h2>` → `##`, `<h3>` → `###`
- **Malformed hierarchy fix:** If the source has `<h3>` directly under `<h1>` with no `<h2>` in between, render it as `##` — not `###`. Example: source is `# Title` then `<h3>Section</h3>` → output must be `# Title` then `## Section`. Do NOT output `### Section` in this case.
- Keep other HTML tags intact
- Internal links: keep as-is (auto-resolve)
- Cross-language links: use `../en/`, `../fr/`, `../es/`, `../ar/`
- Images/URLs: don't translate paths
- YouTube embeds: update `cc_lang_pref` and `hl` parameters

## 🚨 CRITICAL: Article H1 Heading

The article's own `# H1` must be a **faithful translation** of the English H1 — do not invent a shorter or restructured variant.

The `article-titles.md` file lists the official titles for each article. The H1 of the article being translated must **match its entry in article-titles.md exactly**. If no entry exists, translate faithfully and flag it.

## Article Title Consistency

When translating any article that references another article by title:
1. Look up the target article's filename in **[article-titles.md](references/article-titles.md)**
2. Use the **exact title** listed for the target language — never translate it yourself
3. If a title is missing from the file, flag it rather than guessing

This is critical: articles cross-reference each other, and titles must be identical across all languages.

## Terminology References

### OFFICIAL — Must Use Verbatim
- **[article-titles.md](references/article-titles.md)** - Article titles for all languages (OFFICIAL — verbatim for cross-references)
- **[brand-terminology.md](references/brand-terminology.md)** - Brand terms (OFFICIAL)
- **[ui-terminology.md](references/ui-terminology.md)** - UI elements (OFFICIAL)
- **[form-building-terms.md](references/form-building-terms.md)** - XLSForm terms (OFFICIAL)

### PREFERRED — Can Adapt for Context
- **[question-types.md](references/question-types.md)** - Question types/appearances
- **[data-collection-terms.md](references/data-collection-terms.md)** - Data collection
- **[course-terminology.md](references/course-terminology.md)** - Academy/courses
- **[documentation-terminology.md](references/documentation-terminology.md)** - Help Center
- **[sentence-structures.md](references/sentence-structures.md)** - Recurring sentence patterns (e.g. "Set to", "Both … support")

## Quality Checklist

**Brand & UI:**
- [ ] Server names with correct articles
- [ ] Capital L on Question Library (see brand-terminology.md)
- [ ] UI terms match exact capitalization

**Formatting:**
- [ ] HTML headings → markdown (h3 under h1 with no h2 → rendered as ##)
- [ ] Cross-language links updated
- [ ] Image paths unchanged
- [ ] YouTube language parameters set

**Language:**
- [ ] Gender-inclusive language throughout — every mention
- [ ] XLSForm terms in English + translation
- [ ] Natural word order

**Article titles:**
- [ ] Article H1 matches the article-titles.md entry exactly
- [ ] Cross-referenced article titles match article-titles.md exactly

## Updating This Skill

Source files in `sources/`:
- `glossary.xlsx` - Cached copy of the Google Sheet (offline fallback)
- `style-guide.md` - Style guidelines
- `workflow-rules.md` - Workflow/checklists
- `language-rules.md` - Language-specific rules

To refresh from the live Google Sheet:
```
python scripts/fetch_glossary.py    # pull latest xlsx from Google Sheets
python scripts/regenerate_skill.py  # rebuild skill from cached copy
```

Or combined:
```
python scripts/sync_and_update.py --fetch
```
