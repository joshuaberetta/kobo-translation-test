---
name: kobo-translation
description: "Translation and localization guidelines for KoboToolbox content in French, Spanish, and Arabic. Use when translating KoboToolbox materials including: (1) Academy courses and educational content, (2) User interface text and documentation, (3) Support articles, (4) Marketing materials, (5) Form building terminology, or (6) XLSForm technical terms. Covers tone, pronouns (tú/usted, tu/vous), gender-inclusive language, and official translations for brand terms and UI elements."
---

# KoboToolbox Translation & Localization

## Overview

Translate KoboToolbox content in French, Spanish, and Arabic with consistent terminology, appropriate tone, and cultural adaptation.

## 🚨 CRITICAL: Pre-Translation Checklist

**BEFORE starting translation, read these reference files:**

1. **[brand-terminology.md](references/brand-terminology.md)** - For server names, Question Library, Formbuilder, and ALL brand terms
2. **[ui-terminology.md](references/ui-terminology.md)** - For button names, tabs, and capitalization rules

**Common mistakes to avoid:**
- ❌ Translating server names incorrectly (missing articles or adding extra words)
- ❌ Not including English term on first reference for Formbuilder
- ❌ Missing capital article for "Question Library" / "La bibliothèque de questions" / "La biblioteca de preguntas"
- ❌ Not capitalizing UI terms like "Brouillon" / "Borrador"
- ❌ Using "de" article when it shouldn't be there in French data management terms

## Quick Reference

**Translation types:**
- **OFFICIAL** - Must use EXACT translation character-for-character (brand terms, UI elements, XLSForm terms)
- **Preferred** - Can adapt for context (general terminology, course content)

**Key principles:**
- **ALWAYS check brand-terminology.md FIRST** before translating any brand-related terms
- Prioritize localization over literal translation
- Use gender-inclusive language
- Maintain consistency with KoboToolbox UI
- Apply appropriate formality level (vous/tu, usted/tú)

## Common Translation Pitfalls

### ⚠️ Brand Terms - Most Frequent Errors

| ❌ WRONG | ✅ CORRECT | Notes |
|---------|-----------|-------|
| **Spanish:** Servidor Global de KoboToolbox | **Servidor Global** | Do NOT add "de KoboToolbox" |
| **Spanish:** Servidor de la Unión Europea | **Servidor con sede en la Unión Europea** | Use full official name |
| **French:** serveur KoboToolbox mondial | **Le serveur KoboToolbox mondial** | Must include definite article "Le" (capitalized) |
| **French:** serveur Union européenne | **Le serveur KoboToolbox Union européenne** | Include article AND "KoboToolbox" |
| **Spanish:** la biblioteca de preguntas | **La biblioteca de preguntas** | Capital "L" for brand feature |
| **French:** la bibliothèque de questions | **La bibliothèque de questions** | Capital "L" for brand feature |

### ⚠️ First Reference Rule - Frequently Missed

**Formbuilder MUST include English on first reference:**

| Language | First Reference | Subsequent Uses |
|----------|----------------|-----------------|
| Spanish | editor de formularios de KoboToolbox (Formbuilder) | editor de formularios |
| French | l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder) | interface de création de formulaires |

### ⚠️ UI Capitalization - Often Forgotten

| Term | ❌ Wrong | ✅ Correct |
|------|---------|-----------|
| Draft (FR) | formulaire brouillon | formulaire Brouillon |
| Draft (ES) | borrador | Borrador (when in UI context) |

### ⚠️ French Article Usage

| Concept | ❌ Wrong | ✅ Correct | Rule |
|---------|---------|-----------|------|
| Data management | gestion de données | gestion de données | NO article for general concept |
| Managing your data | gérer vos données | gérer vos données | ✓ Correct |
| Projects and data section title | Gestion de projets et de données | Gestion de projets et données | NO "de" before "données" in compound titles |

## Translation Workflow

### Step 0: MANDATORY First Step

**🔴 STOP! Before translating anything:**

1. Identify all brand terms in the source text (KoboToolbox, servers, Question Library, Formbuilder, etc.)
2. Open **brand-terminology.md** and verify EXACT translations
3. Check **ui-terminology.md** for any UI elements (buttons, tabs, page names)
4. Note any terms requiring "English + translation" on first reference

### Step 1: Identify Content Type

**Formal communications** (server announcements, formal emails):
- French: Use "vous", addressee "Cher utilisateur, Chère utilisatrice"
- Spanish: Use "usted", addressee "Estimado usuario/a"

**User Interface**:
- French: Use formal "vous" and "votre"
- Spanish: Use informal "tú"

**Courses and educational content** (INCLUDES SUPPORT ARTICLES):
- French: Use formal "vous" (even for individuals)
- Spanish: Use informal "tú", "ustedes" for plural
- Examples:
  - FR: "Les utilisatrices et utilisateurs débutant(e)s"
  - ES: "Se te dirigirá" (neutral, not "serás dirigido/a")

**Support articles**:
- French: Use formal "vous"
- Spanish: Use informal "tú"
- Apply gender-inclusive language throughout

**Informal communications** (social media, blogs):
- Context-dependent
- Generally use "vous"/"usted" for semi-formal
- May use "tu"/"tú" for very informal contexts

### Step 2: Check Terminology Category

**🚨 Brand and product terms** → See [brand-terminology.md](references/brand-terminology.md)
- **OFFICIAL translations must be used EXACTLY** (KoboToolbox, Academy, User Plans, servers, Question Library, etc.)
- **Pay special attention to:**
  - Server names (require articles in French, specific wording in both languages)
  - Question Library (requires capital article in both languages)
  - Formbuilder (requires English + translation on first reference)
  - KoboCollect app name format

**Form building and XLSForm** → See [form-building-terms.md](references/form-building-terms.md)
- Many terms must include English + translation in parentheses
- Video subtitles: English only (character limits)
- Examples: list_name (nom de la liste), cascading select (Sélection en cascade)

**Question types and appearances** → See [question-types.md](references/question-types.md)
- Question appearances in written content: English + translation
- Example: "vertical, picker (sélecteur), rating (notation)"

**UI terminology** → See [ui-terminology.md](references/ui-terminology.md)
- **OFFICIAL translations, capitalize per UI**
- Common UI terms: FORMULAIRE/FORMULARIO, DONNÉES/DATOS, Brouillon/Borrador
- Flag any needed corrections in tracker

**Data collection terms** → See [data-collection-terms.md](references/data-collection-terms.md)
- Preferred translations, adapt for context
- Special rules for management, submissions, data collection

**Course and learning platform** → See [course-terminology.md](references/course-terminology.md)
- Preferred translations
- Context-specific adaptations allowed

### Step 3: Apply Gender-Inclusive Language

**French:**
- Use parenthetical markers: "utilisateur(rice)s", "débutant(e)s"
- Use double forms: "Les utilisatrices et utilisateurs"
- Course subtitles: "Vous serez redirigé(e)"

**Spanish:**
- **Strongly prefer neutral constructions:** "Se te dirigirá" instead of "serás dirigido/a"
- **Use double forms for nouns:** "los/as usuarios/as", "las/os participantes"
- When no neutral option exists, use masculine: "los usuarios"
- **Apply throughout:** Every mention of users/people should be inclusive

**Arabic:**
[To be specified based on project needs]

### Step 4: Handle Technical Terms

**XLSForm and form building terms that must stay in English:**
- Written content: English followed by translation in parentheses on first use
- Video subtitles: English only
- Examples:
  - list_name (nom de la liste)
  - XML values (valeurs XML)
  - data column name (nom du champ)

**Cascading select components:**
Always include English + translation approach:
```
"Pour chaque liste d'options, remplissez la colonne list_name (nom de la liste)."
```

## Core Translation Principles

**Localization over literal translation:**
- Adapt idioms and expressions naturally
- Maintain technical accuracy
- Ensure clarity for new users

**Consistency:**
- Use same term for same concept throughout
- Align with KoboToolbox UI terminology
- Flag UI terminology corrections in tracker

**Formatting:**
- Maintain spacing, paragraphs, structure when possible
- Use concise sentences
- Follow target language punctuation conventions
- Avoid slang: "gonna" → "going to"

**Acronyms:**
- First use: Full translation followed by acronym in parentheses
- If no common translated acronym exists, use English acronym
- Example: "l'Agence des Nations Unies pour les réfugiés (HCNUR)"

**Plain language:**
- Technical content must be beginner-friendly
- Avoid unnecessary jargon
- Prioritize clarity

## Common Translation Patterns

### French-Specific Rules

**"Data collection":**
- Default: "collecte de données" (general concept)
- Specific project data: "collecte des données"
- Not: "collecte de données d'enquête"

**"Submission/Record/Response":**
Context-dependent, see [data-collection-terms.md](references/data-collection-terms.md) for full guide:
- Use "soumission" for data management contexts, UI, Data table
- Use "réponse" or "formulaire" when less technical, avoid confusion

**"Upload":**
- Primary: "importer"
- Context: "envoyer" (e.g., send a form)
- Not: "télécharger"

**"View" (UI):**
- "mode" (mode Tableau, mode Carte)
- Not: "affichage" or "aperçu" for UI elements

**Website terms:**
- "site web" not "site Internet"
- "web" lowercase: "formulaire web Enketo"

### Spanish-Specific Rules

**"Management":**
- Data/case management: "manejo" (manejo de datos, manejo de casos)
- Teams/projects: "gestión" (gestión de equipos, gestión de proyectos)

**"Collect" (data):**
- Use "recolectar" not "recopilar"

**Gender-neutral when possible:**
- Prefer "Se te dirigirá" over "serás dirigido/a"
- Use masculine when no neutral option: "los usuarios"

### Cross-Language Rules

**"Disaggregate":**
- FR: "désagréger" (not "ventiler")
- ES: "desagregar"

**"Press" (button):**
- FR: "appuyer sur" (not "presser")
- ES: "click en"

**"Case sensitive":**
- FR: "sensibles à l'utilisation de majuscules et de minuscules" (not "sensible à la casse")
- ES: "distingue entre mayúsculas y minúsculas"

## Terminology References

For detailed term-by-term translations, consult these reference files:

- **[brand-terminology.md](references/brand-terminology.md)** - Brand terms, product names, user plans (OFFICIAL) - **READ THIS FIRST**
- **[form-building-terms.md](references/form-building-terms.md)** - Form building, XLSForm, cascading selects (OFFICIAL)
- **[question-types.md](references/question-types.md)** - Question types and appearances (PREFERRED for types, special rules for appearances)
- **[ui-terminology.md](references/ui-terminology.md)** - Formbuilder and KoboCollect UI (OFFICIAL) - **READ THIS SECOND**
- **[data-collection-terms.md](references/data-collection-terms.md)** - Data collection concepts (PREFERRED)
- **[course-terminology.md](references/course-terminology.md)** - Learning platform and course content (PREFERRED)

## Translation Decision Tree

```
START: Do I see ANY of these terms in the source text?
├─ Server names (Global Server, EU Server)?
│  └─ 🚨 STOP → Open brand-terminology.md → Use EXACT translation with articles
│
├─ "Question Library"?
│  └─ 🚨 STOP → Must be "La bibliothèque de questions" / "La biblioteca de preguntas" (capital L)
│
├─ "Formbuilder"?
│  └─ 🚨 STOP → First reference must include English in parentheses
│     ES: "editor de formularios de KoboToolbox (Formbuilder)"
│     FR: "l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder)"
│
├─ UI element (button, tab, menu - like DEPLOY, NEW, FORM, DATA)?
│  └─ Check ui-terminology.md → Use OFFICIAL translation → Match UI capitalization
│
├─ Draft / Brouillon / Borrador?
│  └─ Capitalize in UI contexts: "Brouillon" / "Borrador"
│
├─ XLSForm technical term (list_name, cascading select)?
│  └─ Written: English + translation in parentheses
│     Subtitles: English only
│     See form-building-terms.md
│
├─ Question appearance (minimal, picker, rating)?
│  └─ Written: English + translation in parentheses
│     Subtitles: English only
│     See question-types.md
│
├─ Form building or data collection term?
│  └─ Check if OFFICIAL or PREFERRED
│     Apply OFFICIAL exactly; adapt PREFERRED for context
│     See relevant reference file
│
├─ Course or educational content?
│  └─ Use PREFERRED translations
│     Apply appropriate pronoun formality
│     See course-terminology.md
│
└─ Unsure about gender inclusivity?
   └─ Use gender-neutral language
      FR: vous + parenthetical markers (e)
      ES: neutral constructions or tú with "se te"
```

## Enhanced Quality Checklist

Before finalizing translation:

**🚨 CRITICAL - Brand & UI Terms:**
- [ ] All server names use EXACT translations from brand-terminology.md (with articles!)
- [ ] "Question Library" has capital article: "La bibliothèque" / "La biblioteca"
- [ ] Formbuilder includes English on first reference
- [ ] All UI elements (buttons, tabs) match ui-terminology.md exactly
- [ ] UI terms capitalized correctly (Brouillon, Borrador, etc.)

**Language & Style:**
- [ ] Correct formality level (vous/tu, usted/tú) for content type
- [ ] Gender-inclusive language throughout (especially Spanish double forms)
- [ ] XLSForm/technical terms follow English + translation pattern
- [ ] Consistent terminology (same term for same concept)
- [ ] Plain language, beginner-friendly
- [ ] Proper acronym handling (full term + acronym first use)
- [ ] Target language punctuation conventions
- [ ] No slang or colloquialisms

**French-Specific:**
- [ ] "collecte de données" (not "collecte des données" unless specific data)
- [ ] "importer" for upload (not "télécharger")
- [ ] Gender-inclusive forms used: "utilisatrices et utilisateurs"

**Spanish-Specific:**
- [ ] "recolectar" for collect (not "recopilar")
- [ ] "manejo" for data/case management, "gestión" for teams/projects
- [ ] Gender-inclusive: "los/as usuarios/as" throughout
- [ ] Neutral constructions preferred: "Se te dirigirá"

## Translation Error Examples

### Example 1: Server Names
**Source:** "Most users sign up for an account on our Global KoboToolbox Server."

**❌ WRONG Spanish:**
"La mayoría de los usuarios se registran en nuestro Servidor Global de KoboToolbox."

**✅ CORRECT Spanish:**
"La mayoría de los/as usuarios/as se registran en nuestro Servidor Global."

**Errors fixed:**
1. Removed "de KoboToolbox" (not in official name)
2. Added gender inclusivity: "los/as usuarios/as"

**❌ WRONG French:**
"La plupart des utilisateurs s'inscrivent sur notre serveur KoboToolbox mondial."

**✅ CORRECT French:**
"La plupart des utilisatrices et utilisateurs s'inscrivent sur notre Le serveur KoboToolbox mondial."

**Errors fixed:**
1. Added definite article "Le" (capitalized)
2. Added gender inclusivity: "utilisatrices et utilisateurs"

### Example 2: Question Library
**Source:** "Build a form using a template from the question library."

**❌ WRONG Spanish:**
"Elabora un formulario usando una plantilla de la biblioteca de preguntas."

**✅ CORRECT Spanish:**
"Elabora un formulario usando una plantilla de La biblioteca de preguntas."

**Error fixed:** Capitalized "L" in "La" (brand feature name)

### Example 3: Formbuilder First Reference
**Source:** "Create a new form using the KoboToolbox Formbuilder."

**❌ WRONG French:**
"Créez un nouveau formulaire en utilisant l'interface de création de formulaires KoboToolbox."

**✅ CORRECT French:**
"Créez un nouveau formulaire en utilisant l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder)."

**Error fixed:** Added English term in parentheses on first reference

## Notes

**Reporting issues:**
If UI terminology needs correction, flag in comment and record in appropriate tracker or communications channel.

**Working document:**
This is a living guideline. Feedback welcome. More languages and terms will be added.

**Reference documents:**
- KoboToolbox Academy Course Style Guide
- Essentials Translation Glossary (Master)
- Transifex UI translations
- UN Women Gender Inclusive Language (Spanish)
- Clear Global terminology documents
