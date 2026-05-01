# KoboToolbox Translation Style Guide

## Overview

This guide provides translation and localization guidelines for KoboToolbox content in French, Spanish, and Arabic. It applies to all KoboToolbox materials including Academy courses, documentation, UI text, support articles, and marketing content.

---

## 1. General Principles

### Localization Over Literal Translation

Prioritize natural-sounding translations over word-for-word translation. Adapt idioms, expressions, and sentence structure to target language conventions.

**Example:**
- EN: "KoboToolbox makes high quality data accessible to social impact organizations worldwide."
- FR: "KoboToolbox rend les données de haute qualité accessibles aux organisations à impact social dans le monde entier."
- ES: "KoboToolbox permite que los datos de alta calidad sean accesibles para organizaciones de impacto social a nivel mundial."

### Clarity and Plain Language

- Use plain language and concise sentences
- Technical content must be beginner-friendly
- Avoid unnecessary jargon
- Avoid slang or contractions ("gonna" → "going to")

### Terminology Consistency

- Use the same term for the same concept throughout
- Match KoboToolbox UI terminology exactly
- Flag UI terminology corrections in the appropriate tracker

---

## 2. Tone and Formality

### Content Type Matrix

| Content Type | French | Spanish |
|-------------|--------|---------|
| User Interface | vous (formal) | tú (informal) |
| Documentation/Support articles | vous (formal) | tú (informal) |
| Courses/Educational content | vous (formal) | tú (informal), ustedes (plural) |
| Formal communications | vous, "Cher utilisateur, Chère utilisatrice" | usted, "Estimado usuario/a" |
| Social media/Blogs | vous (semi-formal) | context-dependent |

### Tone Guidelines

- **Accessible**: Content should be easy to understand for new users
- **Factual**: Direct and informational, not promotional
- **Semi-formal**: Professional but not stiff

---

## 3. Gender-Inclusive Language

### French

- Use parenthetical markers: "utilisateur(rice)s", "débutant(e)s"
- Use double forms: "Les utilisatrices et utilisateurs"
- For courses/subtitles: "Vous serez redirigé(e)"
- Avoid overly complex constructions that harm readability

### Spanish

- **Strongly prefer neutral constructions**: "Se te dirigirá" instead of "serás dirigido/a"
- Use double forms for nouns: "los/as usuarios/as", "las/os participantes"
- When no neutral option exists, use masculine: "los usuarios"
- Apply gender inclusivity throughout - every mention of users/people should be inclusive

### Arabic

- [To be specified based on project needs]

---

## 4. Formatting Rules

### Punctuation

Follow target language conventions for punctuation.

### Spacing and Structure

- Maintain spacing, paragraphs, and structure from the original
- Apply same formatting for paragraphs as used in English

### Acronyms

- First use: Full translation followed by acronym in parentheses
- If no common translated acronym exists, use English acronym
- Example FR: "l'Agence des Nations Unies pour les réfugiés (HCNUR)"
- Example ES: "Agencia de las Naciones Unidas para los refugiados (ACNUR)"

---

## 5. XLSForm Technical Terms

### Never Translate

These elements must remain exactly as they appear in English:
- Worksheet names (survey, choices, settings)
- Column names (type, name, label, constraint, etc.)
- Question type values (select_one, text, integer, etc.)
- Appearance values (minimal, likert, autocomplete, etc.)
- Function names and operators (if, selected, and, or, etc.)
- Boolean operators

### Translation Approach

- **Written content**: Include English followed by translation in parentheses on first instance
- **Video subtitles**: Use English only (due to character limits)

**Example:**
"Pour chaque liste d'options, remplissez la colonne `list_name` (nom de la liste)."

### Code Formatting

- Terms formatted in code (`monospace`) should generally not be translated
- Exception: Placeholder text like `label::idioma` can show `label::language (code)`

---

## 6. Documentation Formatting

### HTML and Markdown

**HTML heading tags must be converted to markdown:**
- `<h1>` → `#`
- `<h2>` → `##`
- `<h3>` → `###`
- `<h4>` → `####`

**Keep all other HTML tags intact:**
- `<iframe>`, `<section>`, `<div>`, etc.
- Preserve attributes: `dir="rtl"`, `id`, `class`, `style`

### Links

**Internal documentation links:**
- Keep relative links as-is - they automatically resolve to the correct language folder
- Example: In `docs/es/article_a.md`, a link `[text](article_b.md)` correctly points to `docs/es/article_b.md`

**Cross-language reference links:**
- Update the path to point to the correct language directory
- From Spanish: `../en/filename.md`, `../fr/filename.md`, `../ar/filename.md`
- From French: `../en/filename.md`, `../es/filename.md`, `../ar/filename.md`

**Cross-language link text:**
- English: "Read in English"
- French: "Lire en français"
- Spanish: "Leer en español"
- Arabic: "اقرأ باللغة العربية"

**External links:**
- Translate the visible text but keep the URL unchanged
- Example: `[our mission](https://...)` → `[notre mission](https://...)`

### Images

- Keep image paths unchanged: `![image](images/about_kobotoolbox/usermap.png)`
- Do NOT translate image file names or paths

### YouTube Embeds

Update language parameters for target language:
- French: `cc_lang_pref=fr`, `hl=fr`
- Spanish: `cc_lang_pref=es`, `hl=es`
- Arabic: `cc_lang_pref=ar`, `hl=ar`

### Metadata

- Preserve "Last updated" lines with dates and GitHub links
- Keep "Last updated" text in English
- Keep GitHub URLs unchanged

---

## 7. Title and Heading Conventions

### Capitalization by Language

- **English**: Title case for main headings ("About KoboToolbox: Accessible Data Collection")
- **French**: Capitalize first word and proper nouns only ("À propos de KoboToolbox : Collecte de données accessible à toutes et tous")
- **Spanish**: Capitalize first word and proper nouns only ("Acerca de KoboToolbox: Recolección de datos accesibles para todas las personas")

### Article Titles and Headers

- Keep short and direct
- Prioritize idiomatic phrasing over literal translation
- Do not include parentheses in titles or headers - define terms in article text instead

**Example:**
- Wrong: "Comenzando con el editor de formularios de KoboToolbox (Formbuilder)"
- Correct: "Comenzando con el KoboToolbox Formbuilder"

### Inclusive Language in Titles

- French: "à toutes et tous" (to all, everyone)
- Spanish: "para todas las personas" (for all people)

---

## 8. Arabic-Specific Guidelines

### RTL Formatting

- Wrap Arabic content in `<section dir="rtl">` tags
- Keep heading IDs: `<h1 id="ar">`
- Cross-reference links stay OUTSIDE the RTL section
- Arabic titles are placed inside RTL section with proper heading markup

### Heading Levels

- Maintain heading hierarchy (h1, h2, h3)
- In Arabic translations, the h1 is inside the RTL section

---

## 9. Translation Types

### OFFICIAL Translations

Must use EXACT translation character-for-character. Includes:
- Brand terms (KoboToolbox, Academy, servers)
- UI elements (buttons, tabs, statuses)
- XLSForm terms

### PREFERRED Translations

Can adapt for context. Includes:
- General terminology
- Course content
- Data collection concepts

---

## 10. Video Subtitles (SRT Files)

For video subtitle translations, use the **kobo-translation-srt** skill extension which includes:
- All base rules PLUS subtitle-specific adaptations
- XLSForm terms: English only (no translations due to character limits)
- Character limits: 35-42 characters per line ideal, 50 max
- Natural spoken language (more conversational than written)
- Chunked translation approach to preserve context
- Same formality levels as educational content (vous/tú)

---

## 11. Diff-Based Translation Updates

### For New Files (Full Translation)
- Translate the complete source document
- Use consistent terminology for reliable, repeatable translations
- Follow all guidelines in this document

### For Updates (Diff-Based Translation)
- Translate ONLY the changed content provided between markers
- Do NOT translate anything outside the markers
- Do NOT add explanations or extra content
- Output ONLY the translated version of the diff content
- The system will automatically merge with the existing translated file

**Why diff-based?** LLMs are non-deterministic, so re-translating entire documents produces slightly different results each time, creating "translation noise" in git diffs. By translating only actual changes, we preserve manual reviewer improvements and reduce unnecessary churn.

---

## Reference Documents

- KoboToolbox Academy Course Style Guide
- Essentials Translation Glossary (Master)
- Transifex UI translations
- UN Women Gender Inclusive Language (Spanish)
- Clear Global terminology documents
