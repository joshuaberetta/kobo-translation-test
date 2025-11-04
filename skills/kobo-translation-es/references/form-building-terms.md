# Form Building Terminology (OFFICIAL)

All translations in this file are OFFICIAL and must be used exactly as specified.

**📝 FORMATTING NOTE:**
- **Convert HTML heading tags to markdown:** `<h2>` → `##`, `<h3>` → `###`, etc.
- **Keep internal doc links as-is:** Relative links like `[text](article.md)` automatically resolve to the correct language folder
- **Update cross-language links:** Use directory paths like `../en/article.md`, `../es/article.md`, `../fr/article.md`
- Keep all other HTML tags intact (iframe, section, etc.)

## CRITICAL: XLSForm Technical Terms

**These terms must be used in English in XLSForm standard and Formbuilder.**

**Translation approach:**
- **Written content**: Include English followed by translation in parentheses on first instance. Subsequent uses can be English only.
- **Video subtitles**: Use English only (due to character limits and video alignment).

Example: "Pour chaque liste d'options, remplissez la colonne list_name (nom de la liste)."

## Core Form Building Concepts

|---------|--------|---------|--------|-------|
| Form building | création de formulaire / construction de formulaires | elaboración de formularios | | |
| Form Style | style du formulaire | | | Refers to customization interface with themes. Also the XLSForm column name |
| Form themes | thèmes du formulaire | | | Different appearance options in style column |
| Form media | médias au sein du formulaire | datos multimedia del formulario | | |
| Question type | question de type [type name] | tipo de pregunta | | Example: "question de type texte" / "El tipo de pregunta texto" |

## Groups and Repeats

|---------|--------|---------|-------|
| Nested groups | sous-groupes | los subgrupos | |
| Roster | une série | grupo | Use only as specific example of groups, not equivalent to "group" |

## Range Question Components

|---------|--------|---------|
| start | départ / nombre de départ | inicio |
| end | arrivée / nombre d'arrivée | final |
| step | écart | intervalo |

## Question Elements

|---------|--------|---------|-------|
| Question appearances | | aspectos de las preguntas | |
| Question hint | indice de question | sugerencia de pregunta | |
| Guidance hint | instructions supplémentaires | sugerencia adicional | Include English on first reference (not yet in UI) |
| Regular hint | indication de base | sugerencias comunes | |

## XLSForm Technical Terms (English + Translation Approach)

|---------|--------|---------|-------|
| XML values | valeurs XML | valor XML | |
| XML headers | en-tête XML | encabezados XLM | |
| Value and header format | format pour les valeurs et l'en-tête | formato de los valores y encabezados | |
| Cascading select | Sélection en cascade | | In XLSForm called "choice filters" |

## Cascading Select Components

**MUST use English + translation in parentheses approach.**

|---------|--------|---------|---------|
| list_name | nom de la liste | nombre de la lista | "remplissez la colonne list_name (nom de la liste)" |
| label | libellé | etiqueta | Use "le libellé" for both questions and options |
| name | nom de l'élément | nombre | |
| Parent list | liste principale | lista principal | |
| Child list | liste secondaire | lista secundaria | |

## Variable and Column Names

|---------|--------|---------|-------|
| Variable name | nom de la variable | nombre de variable | |
| ${DataColumnName} | ${NomChamp} | ${Nombre} | |
| Data column prefix | préfixe du champ | prefijo de columna de datos | |
| Data column suffix | suffixe du champ | sufijo de columna de datos | |

### French "nom de champ" Usage

- **"Nom du champ"**: When referring to a specific question
- **"Nom de champ"**: When referring to the concept
- **"Noms des champs"**: When referring to specific fields (plural, specific data column names)
- **"Noms de champs"**: When referring to the concept in plural (information about data column names in general)

### Additional Technical Terms

|---------|--------|---------|-------|
| Question referencing format | format de référencement de questions | formato de pregunta de referencia | |

## Logic and Validation

|---------|--------|---------|-------|
| Single validation criteria | critère de validation simple | criterio simple de validación | |

## Form Actions

|---------|--------|---------|-------|
| Upload a form | envoyer un formulaire | enviar un formulario | |
| Form upload | envoi d'un formulaire | envío de un formulario | |
| Uploaded forms | formulaires envoyés | formularios enviados | |
| Load a form | ouvrir un formulaire | cargar un formulario | "When/once loaded" = "une fois le formulaire ouvert" |

## Survey Types

|---------|--------|---------|-------|
| Primary survey | Questionnaire principal | | Also called "parent" survey. Preferred terms are "primary/secondary" |
| Secondary survey | Questionnaire secondaire | | Also called "child" survey. Preferred terms are "primary/secondary" |
