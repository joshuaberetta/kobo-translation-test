# Translation Workflow and Quality Rules

## Pre-Translation Checklist

**🔴 BEFORE starting any translation, complete these steps:**

1. Identify all brand terms in the source text (KoboToolbox, servers, Question Library, Formbuilder, etc.)
2. Check the glossary for EXACT official translations
3. Check UI terminology for any UI elements (buttons, tabs, page names)
4. Note any terms requiring "English + translation" on first reference

---

## Translation Decision Tree

```
START: Do I see ANY of these terms in the source text?

├─ Server names (Global Server, EU Server)?
│  └─ 🚨 STOP → Check glossary → Use EXACT translation with articles
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
│  └─ Check glossary → Use OFFICIAL translation → Match UI capitalization
│
├─ Draft / Brouillon / Borrador?
│  └─ Capitalize in UI contexts: "Brouillon" / "Borrador"
│
├─ XLSForm technical term (list_name, cascading select)?
│  └─ Written: English + translation in parentheses
│     Subtitles: English only
│
├─ Question appearance (minimal, picker, rating)?
│  └─ Written: English + translation in parentheses
│     Subtitles: English only
│
├─ Form building or data collection term?
│  └─ Check if OFFICIAL or PREFERRED
│     Apply OFFICIAL exactly; adapt PREFERRED for context
│
├─ Course or educational content?
│  └─ Use PREFERRED translations
│     Apply appropriate pronoun formality
│
└─ Unsure about gender inclusivity?
   └─ Use gender-neutral language
      FR: vous + parenthetical markers (e)
      ES: neutral constructions or tú with "se te"
```

---

## Common Pitfalls to Avoid

### Brand Terms - Most Frequent Errors

| ❌ WRONG | ✅ CORRECT | Notes |
|---------|-----------|-------|
| **ES:** Servidor Global de KoboToolbox | **Servidor Global** | Do NOT add "de KoboToolbox" |
| **ES:** Servidor de la Unión Europea | **Servidor con sede en la Unión Europea** | Use full official name |
| **FR:** serveur KoboToolbox mondial | **Le serveur KoboToolbox mondial** | Must include article "Le" |
| **FR:** serveur Union européenne | **Le serveur KoboToolbox Union européenne** | Include article AND "KoboToolbox" |
| **ES:** la biblioteca de preguntas | **La biblioteca de preguntas** | Capital "L" for brand feature |
| **FR:** la bibliothèque de questions | **La bibliothèque de questions** | Capital "L" for brand feature |

### First Reference Rule - Frequently Missed

**Formbuilder MUST include English on first reference:**

| Language | First Reference | Subsequent Uses |
|----------|----------------|-----------------|
| Spanish | editor de formularios de KoboToolbox (Formbuilder) | editor de formularios |
| French | l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder) | interface de création de formulaires |

### UI Capitalization - Often Forgotten

| Term | ❌ Wrong | ✅ Correct |
|------|---------|-----------|
| Draft (FR) | formulaire brouillon | formulaire Brouillon |
| Draft (ES) | borrador | Borrador (in UI context) |
| FORM tab (FR) | onglet Formulaire | onglet FORMULAIRE |
| DATA tab (ES) | ventana Datos | ventana DATOS |

### French Article Usage

| Concept | ❌ Wrong | ✅ Correct | Rule |
|---------|---------|-----------|------|
| Data management | gestion des données | gestion de données | NO article for general concept |
| Compound titles | Gestion de projets et de données | Gestion de projets et données | NO extra "de" before "données" |

---

## Quality Checklist

### CRITICAL - Brand & UI Terms

- [ ] All server names use EXACT translations (with articles!)
- [ ] "Question Library" has capital article: "La bibliothèque" / "La biblioteca"
- [ ] Formbuilder includes English on first reference
- [ ] All UI elements match glossary exactly
- [ ] UI terms capitalized correctly (Brouillon, Borrador, FORMULAIRE, DATOS)

### Structure & Formatting

- [ ] HTML heading tags converted to markdown (## for h2, ### for h3)
- [ ] All other HTML tags preserved unchanged
- [ ] Internal documentation links kept as relative paths
- [ ] Cross-language reference links updated (../en/, ../es/, ../fr/, ../ar/)
- [ ] External links: translated text, unchanged URLs
- [ ] Image paths unchanged
- [ ] YouTube embed language parameters updated
- [ ] Arabic content wrapped in `<section dir="rtl">` tags
- [ ] Heading hierarchy maintained

### Language & Style

- [ ] Correct formality level (vous/tu, usted/tú) for content type
- [ ] Gender-inclusive language throughout
- [ ] XLSForm/technical terms follow English + translation pattern
- [ ] Consistent terminology throughout
- [ ] Plain language, beginner-friendly
- [ ] Proper acronym handling (full term + acronym first use)
- [ ] Target language punctuation conventions
- [ ] No slang or colloquialisms
- [ ] Natural word order (not forced English structure)

### French-Specific

- [ ] "collecte de données" (not "collecte des données" unless specific data)
- [ ] "importer" for upload (not "télécharger")
- [ ] Gender-inclusive forms: "utilisatrices et utilisateurs"
- [ ] Natural pronoun placement: "les rend" not forced English order
- [ ] "appuyer sur" for press (not "presser")
- [ ] Simplified "Let's go ahead" phrases

### Spanish-Specific

- [ ] "recolectar" for collect (not "recopilar")
- [ ] "manejo" for data/case management, "gestión" for teams/projects
- [ ] Gender-inclusive: "los/as usuarios/as" throughout
- [ ] Neutral constructions preferred: "Se te dirigirá"
- [ ] Natural sentence structure adapted from English

---

## Translation Examples

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
"La plupart des utilisatrices et utilisateurs s'inscrivent sur Le serveur KoboToolbox mondial."

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

### Example 4: HTML Headings to Markdown

**Source (with HTML):**
```html
<h3>Why KoboToolbox is unique</h3>
```

**✅ CORRECT (converted to markdown):**
```markdown
### Por qué KoboToolbox es único
```

**❌ WRONG (keeping HTML):**
```html
<h3>Por qué KoboToolbox es único</h3>
```

### Example 5: Cross-Language Links

**Source (English file in `docs/en/p_codes.md`):**
```markdown
[Lire en français](../fr/p_codes.md) | [Leer en español](../es/p_codes.md)

If using cascading lists, please [follow the instructions](cascading_select.md)
```

**✅ CORRECT Spanish (file in `docs/es/p_codes.md`):**
```markdown
[Read in English](../en/p_codes.md) | [Lire en français](../fr/p_codes.md)

Si utilizas listas en cascada, por favor [sigue las instrucciones](cascading_select.md)
```

**Key observations:**
- Internal doc link `cascading_select.md` stays as-is
- Cross-language links updated to use directory structure

### Example 6: Natural Language Flow

**Source:** "To support our nonprofit users, we provide our tools for free under the Community Plan."

**✅ CORRECT French:**
"Pour soutenir nos utilisateurs sans but lucratif, nous fournissons nos outils gratuitement dans le cadre du plan Community."

**✅ CORRECT Spanish:**
"Para apoyar a nuestros usuarios sin fines de lucro, proporcionamos nuestras herramientas de forma gratuita bajo el plan Community."

**Key observations:**
- French: "for free" → "gratuitement" (as adverb)
- French: "under the plan" → "dans le cadre du plan"
- Spanish: "for free" → "de forma gratuita"

---

## Reporting Issues

If UI terminology needs correction, flag in comment and record in appropriate tracker or communications channel.
