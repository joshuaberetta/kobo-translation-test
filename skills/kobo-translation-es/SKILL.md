---
name: kobo-translation-es
description: "Translation and localization guidelines for KoboToolbox content from English to Spanish. Use when translating KoboToolbox materials including: (1) Academy courses and educational content, (2) User interface text and documentation, (3) Support articles, (4) Marketing materials, (5) Form building terminology, or (6) XLSForm technical terms. Covers tone, pronouns (tu/usted, tu/vous), gender-inclusive language, and official translations for brand terms and UI elements."
---

# KoboToolbox Translation & Localization

## Overview

Translate KoboToolbox content from English to Spanish with consistent terminology, appropriate tone, and cultural adaptation.

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

## Spanish Critical Rules

🚨 **ALL Spanish documentation, UI text, and support articles use informal tú. NEVER use usted.**

| ❌ Wrong (usted) |
| --- |
| haga clic |
| su cuenta |
| su formulario |
| puede |
| tiene |
| vaya a Configuraciones |

If you find yourself writing "su", "usted", "haga", "vaya a" — stop and rewrite in tú.

Also: use **"clic"** (not "click"): "haz clic en el botón".

## Spanish Formality

Use **tú** (informal) throughout all Spanish documentation and UI text.

| Spanish |
| --- |
| tú |
| tú, ustedes (plural) |
| usted |

## Spanish Gender-Inclusive Language

🚨 Every mention of users or people must use inclusive forms:
- "los/as usuarios/as" — NOT "los usuarios"
- "el/la usuario/a" — NOT "el usuario"
- "los/as participantes" — NOT "los participantes"

Scan the entire article before submitting: if you find any bare masculine plural ("los usuarios", "los participantes"), replace it. This applies everywhere: body text, bullet lists, tables, and `<p class="note">` callouts.

## Spanish Language Rules

- **ALWAYS tú — NEVER usted** (see critical rule above)
- "clic" not "click": "haz clic en"
- "recolectar" (not "recopilar")
- "manejo" for data/case management
- "gestión" for teams/projects

## Spanish XLSForm Worksheet Tab Labels

When the source has a bold worksheet label like `**survey worksheet**`, `**choices worksheet**`, or `**settings worksheet**`, translate it using the pattern `**hoja [name]**` — keep the sheet name in English, prefix with the translated word only:

| English | Spanish |
|---------|---------|
| `**survey worksheet**` | `**hoja survey**` |
| `**choices worksheet**` | `**hoja choices**` |
| `**settings worksheet**` | `**hoja settings**` |

🚨 Do NOT write `**hoja de trabajo survey**` — that is wrong. The sheet name stays in English.

## Spanish Quality Checklist

- [ ] tú throughout — no "su", "usted", "haga" anywhere
- [ ] "clic" not "click"
- [ ] gender-inclusive — "los/as usuarios/as" not "los usuarios" — every mention
- [ ] Worksheet labels use `**hoja survey**` not `**hoja de trabajo survey**`
- [ ] Article H1 matches article-titles.md Spanish entry exactly
- [ ] Cross-referenced article titles match article-titles.md Spanish entries exactly

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
