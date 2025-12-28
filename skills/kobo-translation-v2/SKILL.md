---
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

**BEFORE translating, check these reference files IN ORDER:**
1. **[brand-terminology.md](references/brand-terminology.md)** - Server names, Question Library, Formbuilder, and ALL brand terms
2. **[transifex-ui-strings.md](references/transifex-ui-strings.md)** - For ALL UI elements (buttons, tabs, menus) - **HIGHEST PRIORITY**
3. **[ui-terminology.md](references/ui-terminology.md)** - For supplementary UI terms not in Transifex

**Common mistakes:**
- Missing articles in French server names ("Le serveur...")
- Adding "de KoboToolbox" to Spanish server names
- Lowercase "La biblioteca" / "La bibliothèque" (must be capital L)
- Missing English term on first Formbuilder reference
- Incorrect UI capitalization (Brouillon, Borrador, DONNÉES, DATOS)
- Using UI translations that don't match Transifex exactly

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

## Translation Process

### Step 0: Pre-Translation Checks

**BEFORE translating anything:**

1. Identify all brand terms in the source text (KoboToolbox, servers, Question Library, Formbuilder)
2. Open **brand-terminology.md** and verify EXACT translations
3. Check **transifex-ui-strings.md** for any UI elements (buttons, tabs, menus, dialogs)
4. Check **ui-terminology.md** for supplementary UI terms not in Transifex
5. Note any terms requiring "English + translation" on first reference

### Step 0.5: UI Element Translation Priority

**When translating ANY UI element (buttons, tabs, menus, dialogs, status messages):**

1. **FIRST:** Check [transifex-ui-strings.md](references/transifex-ui-strings.md)
   - If found: Use EXACT translation (character-for-character match)
   - These are pulled directly from Transifex and MUST match the actual UI
   
2. **SECOND:** If not in Transifex file, check [ui-terminology.md](references/ui-terminology.md)
   - Supplementary UI terms and formatting guidance
   
3. **NEVER:** Adapt, localize, or modify Transifex UI strings
   - Even if it sounds better in the target language
   - Even if capitalization seems wrong
   - The UI uses these exact strings, documentation must match

**Example:**
- English doc: "Click the **Deploy** button"
- Find "Deploy" in transifex-ui-strings.md → Spanish: "DESPLEGAR"
- Translated doc: "Haz clic en el botón **DESPLEGAR**"

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

For detailed term-by-term translations, consult these reference files in priority order:

### HIGHEST PRIORITY - Transifex UI Strings
- **[transifex-ui-strings.md](references/transifex-ui-strings.md)** - Actual UI translations from Transifex (AUTHORITATIVE) - **CHECK FIRST FOR ANY UI ELEMENT**

### OFFICIAL - Must Use Exactly
- **[brand-terminology.md](references/brand-terminology.md)** - Brand terms, product names, user plans (OFFICIAL)
- **[ui-terminology.md](references/ui-terminology.md)** - Supplementary UI terms not in Transifex (OFFICIAL)
- **[form-building-terms.md](references/form-building-terms.md)** - Form building, XLSForm, cascading selects (OFFICIAL)

### PREFERRED - Can Adapt for Context
- **[question-types.md](references/question-types.md)** - Question types and appearances
- **[data-collection-terms.md](references/data-collection-terms.md)** - Data collection concepts
- **[documentation-terminology.md](references/documentation-terminology.md)** - Documentation website and Help Center terms
- **[course-terminology.md](references/course-terminology.md)** - Learning platform and course content

## Translation Decision Tree

```
START: Do I see ANY of these terms in the source text?
├─ UI element (button, tab, menu, dialog)?
│  └─ 🚨 STOP → Check transifex-ui-strings.md FIRST
│     ├─ Found? Use EXACT translation from Transifex (never modify)
│     └─ Not found? Check ui-terminology.md
│
├─ Server names (Global Server, EU Server)?
│  └─ 🚨 STOP → Open brand-terminology.md → Use EXACT translation with articles
│
├─ Question Library / Formbuilder / user plans?
│  └─ 🚨 STOP → Open brand-terminology.md → Use OFFICIAL translation
│
├─ XLSForm column / type / function name?
│  └─ 🚨 STOP → Keep in English + add translation in parentheses
│
└─ General terminology?
   └─ Check reference files → Adapt for context if needed
```

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
