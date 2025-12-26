# Language-Specific Translation Rules

This document contains detailed translation rules and patterns specific to each target language.

---

## French-Specific Rules

### Data Collection

**Default: "collecte de données"** (general concept)

**Exception: "collecte des données"** only when referring to specific data for a specific project

**Rule:** The default should always be "collecte de données"

**Examples:**
- "la collecte de données" (data collection as a concept)
- "la collecte des données de ce projet" (collecting this project's data)
- NOT: "la collecte de données d'enquête"

### Submission/Record/Response

These are context-dependent translations. Choose based on clarity.

**Use "soumission" when:**
- Content focuses specifically on survey records/entries in data management context
- In UI and Data table contexts
- In modules focusing on data and submission management
- When avoiding confusion with question responses or the survey questionnaire

**Use "réponse" or "formulaire" when:**
- Less important to identify as specific UI concept
- Referring to submissions/responses to a survey generally
- No possibility of confusion

**Examples:**
- "ouvrir, supprimer, et valider des soumissions" (data management context)
- "l'enquêteur envoie le formulaire" (enumerator uploads submission)
- "pour modifier les réponses d'un individu" (modifying one person's submission)

**Note:** "réponse" or "formulaire" are often more natural outside of data management/UI discussions.

### Upload

- **Primary:** "importer"
- **Context-dependent:** "envoyer" (e.g., send a form)
- **NOT:** "télécharger"

### View (UI)

- Use "mode" (mode Tableau, mode Carte)
- NOT: "affichage" or "aperçu" for UI elements

### Website Terms

- "site web" NOT "site Internet"
- "web" lowercase: "formulaire web Enketo"

### Verb Constructions

French naturally places pronouns before verbs: "les rend" (makes them)
Don't force English word order.

### "Getting Started With…" Pattern

**DO NOT translate as "Débuter avec"** - this is awkward in French.

**Instead, adapt for context:**
- "Découvrir…" (Discover…)
- "Introduction à…" (Introduction to…)
- "Pour commencer avec…" (To begin with…)

**Example:**
- EN: "Getting started with KoboToolbox"
- FR: "Introduction à KoboToolbox" OR "Découvrir KoboToolbox"
- NOT: "Débuter avec KoboToolbox"

### "Press" (Button)

- Use "appuyer sur" (NOT "presser")
- Example: "appuyer sur le bouton Soumettre"

### "Let's Go Ahead And…"

- Simplify and omit "Let's go ahead"
- Example: "Let's go ahead and add the question" → "ajoutons la question"
- NOT: "allons-y et ajoutons la question"

### Data Column Name Usage

- **"Nom du champ"**: When referring to a specific question
- **"Nom de champ"**: When referring to the concept
- **"Noms des champs"**: Plural, referring to specific data column names
- **"Noms de champs"**: Plural concept (information about data column names in general)

### Case Sensitive

- FR: "sensibles à l'utilisation de majuscules et de minuscules"
- NOT: "sensible à la casse"

### Disaggregate

- FR: "désagréger"
- NOT: "ventiler"

---

## Spanish-Specific Rules

### Management

**"manejo"** - Preferred for:
- Data management (manejo de datos)
- Case management (manejo de casos)
- Project management (manejo de proyectos)

**"gestión"** - Preferred for:
- Managing teams (gestión de equipos)
- Managing projects (gestión de proyectos)
- Managing surveys (gestión de encuestas)

Both are acceptable depending on context, but follow patterns above for consistency.

### Collect (Data)

- Use "recolectar" NOT "recopilar"

### Gender-Neutral Constructions

**Strongly prefer neutral constructions:**
- "Se te dirigirá" instead of "serás dirigido/a"

**Use double forms for nouns:**
- "los/as usuarios/as"
- "las/os participantes"

**When no neutral option exists:**
- Use masculine: "los usuarios"

### Natural Word Order

Spanish sentence structure may differ from English. Don't force English patterns.

**Example:**
- EN: "makes data accessible"
- ES: "permite que los datos sean accesibles" (permits that the data be accessible)
- NOT: literal translation

### Disaggregate

- ES: "desagregar"

### Case Sensitive

- ES: "distingue entre mayúsculas y minúsculas"

---

## Arabic-Specific Rules

### RTL Formatting

**Wrap Arabic content in RTL tags:**
```html
<section dir="rtl">
  <h1 id="ar">العنوان بالعربية</h1>
  <!-- Arabic content here -->
</section>
```

### Cross-Reference Links

Cross-reference links stay OUTSIDE the RTL section.

### Heading Structure

- Maintain heading hierarchy (h1, h2, h3)
- Arabic h1 is placed inside the RTL section
- Keep heading IDs: `<h1 id="ar">`

### Natural Restructuring

Arabic often restructures significantly from English for natural expression.

**Example:**
- EN: "Designed by data collection practitioners specifically for challenging settings"
- AR: "مُصممة من قبل مختصين في جمع البيانات للتعامل مع الظروف الصعبة بشكل خاص"
- (designed... for dealing with difficult circumstances especially)

---

## Cross-Language Rules

### Social Impact Organizations

- FR: "organisations à impact social"
- ES: "organizaciones de impacto social"

### Practitioners

- FR: "praticiens" (context: data collection practitioners)
- ES: "personas profesionales" (gender-inclusive alternative)
- AR: "مختصين في جمع البيانات"

### Challenging Settings

- FR: "environnements difficiles"
- ES: "entornos desafiantes"
- AR: "الظروف الصعبة"

### Adapting Metaphors and Expressions

Don't translate idioms literally. "Accessible to/for" may require restructuring:
- French: "rendre accessible" (make accessible) rather than "être accessible à"

### Natural Language Adaptations

**English:** "Designed by data collection practitioners specifically for challenging settings"

**French (adapted structure):**
"Conçu par des praticiens de la collecte de données spécifiquement pour des environnements difficiles"

**Spanish (adapted structure):**
"Fue diseñado por personas profesionales de la recolección de datos específicamente para entornos desafiantes"

**Key observations:**
- Spanish uses gender-inclusive "personas profesionales" instead of literal "practitioners"
- Spanish adds "Fue" (was) for natural past tense flow
- All prioritize natural expression over literal translation

---

## Form Building Term Patterns

### Range Question Components

| English | French | Spanish |
|---------|--------|---------|
| start | départ / nombre de départ | inicio |
| end | arrivée / nombre d'arrivée | final |
| step | écart | intervalo |

### Skip Logic

- FR: "branchement conditionnel"
- Also known as: "logique de saut", "logique de branchement"
- NOT: "critères de passage"

### Save

- FR: "Enregistrer" / "Sauvegarder"
- NOT: "sauver"
- ES: "guardar"

### Form Upload Actions

| English | French | Spanish |
|---------|--------|---------|
| Upload a form | envoyer un formulaire | enviar un formulario |
| Form upload | envoi d'un formulaire | envío de un formulario |
| Uploaded forms | formulaires envoyés | formularios enviados |
| Load a form | ouvrir un formulaire | cargar un formulario |

### Parent/Child Terminology

| English | French | Spanish |
|---------|--------|---------|
| Parent list | liste principale | lista principal |
| Child list | liste secondaire | lista secundaria |
| Primary survey | Questionnaire principal | (primary) |
| Secondary survey | Questionnaire secondaire | (secondary) |

### Repeat Groups

- FR: "groupes répétés" / "répétitions de questions"
- NOT: "occurrences"
- For each instance: "répétitions d'un groupe répété"

---

## Dashboard and Visualization Terms

| English | French | Spanish |
|---------|--------|---------|
| Dashboard (data viz) | tableau de bord / rapport interactif | informe interactivo / tablero de control |
| Invalid values | valeurs incohérentes | valores inválidos |

Note: For Spanish, "dashboard" is acceptable in informal/social media contexts.
