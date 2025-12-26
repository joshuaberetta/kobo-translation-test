# UI Terminology (OFFICIAL)

All translations in this file are OFFICIAL and must be used exactly as specified.

**Capitalize according to UI appearance.** If modifications or corrections to UI terminology are needed, flag in comment and record in appropriate tracker or communications channel.

**📝 FORMATTING NOTE:**
- **Convert HTML heading tags to markdown:** `<h2>` → `##`, `<h3>` → `###`, etc.
- **Keep internal doc links as-is:** Relative links like `[text](article.md)` automatically resolve to the correct language folder
- **Update cross-language links:** Use directory paths like `../en/article.md`, `../es/article.md`, `../fr/article.md`
- Keep all other HTML tags intact (iframe, section, etc.)

## 🚨 CRITICAL: Capitalization Rules

**UI terms MUST match the exact capitalization shown in the actual KoboToolbox interface.**

### Most Commonly Missed Capitalizations

| Context | French | ❌ Common Error |
| --------- | -------- | ----------------- |
| UI element / Form status | **Brouillon** | ❌ Using lowercase in UI contexts |
| Main navigation | **onglet FORMULAIRE** | ❌ Not all caps |
| Main navigation | **onglet DONNÉES** | ❌ Not all caps |

**⚠️ RULE:** When referring to UI elements (buttons, tabs, statuses), use the EXACT capitalization from the UI.

## Formbuilder UI Terminology

### API and Core Elements

| English | French |
| --------- | -------- |
| The application programming interface (API) / KoboToolbox API | interface de programmation d'application (API) / API KoboToolbox |
| Toolbar | barre d'outils |
| Build from scratch | Création de formulaires (in UI) / Créer un formulaire à partir de zéro (in text) |
| **Draft** | **Brouillon** |
| Save Draft (Enketo) | Sauvegarder le brouillon |

### Tabs and Views

| English | French |
| --------- | -------- |
| FORM tab | **onglet FORMULAIRE** |
| Form view / Form page | mode formulaire / tableau de bord du formulaire |
| DATA tab | **onglet DONNÉES** |
| SUMMARY tab | **onglet SOMMAIRE** |
| View | mode |
| Table view | mode Tableau |
| Map view | mode Carte |
| Report view | mode Rapports |

### Pages and Features

| English | French |
| --------- | -------- |
| Downloads page | page Téléchargements |
| Gallery page | page Galerie Photo |
| New Export | Nouvel export |
| Save image as | Enregistrer l'image sous |
| Embeddable Web Form Code | Code de formulaire Web |
| Hook / webhook | Hook / webhook |

## KoboCollect UI Terminology

### Main Menu

| English | French | Recommended Update |
| --------- | -------- | ------------------- |
| Start new form | Remplir un formulaire |  |
| Drafts | Ébauches |  |
| Ready to send | Prêt à envoyer |  |
| Sent | Envoyé |  |
| Download form | Télécharger formulaire |  |
| Delete form | Supprimer formulaire |  |

### Download Form Screen

| English | French |
| --------- | -------- |
| Select all | Tout sélectionner |
| Refresh | Rafraîchir |
| Get Selected | Télécharger la sélection |

### Settings

| English | French |
| --------- | -------- |
| Manually enter project details | Saisir les détails du projet |
| Settings | Paramètres |
| Server | Serveur |

### GPS Questions

| English | French |
| --------- | -------- |
| Start GeoPoint | Démarrer le point |
| Start GeoTrace | Démarrer la ligne |
| Placement by tapping | Placement en tapotant |
| Manual location recording | Enregistrement manuel de la localisation |
| Record a point | Enregistrer un point |
| Automatic location recording | Enregistrement automatique de la localisation |
| Start | Démarrer |
| Recording interval | Intervalle d'enregistrement |
| Accuracy requirement | Exigence de précision |
| View of Change GeoTrace | Voir ou modifier la ligne |
| Start GeoShape | Démarrer le polygone |

### Background Audio

| English | French |
| --------- | -------- |
| Record audio | Enregistrement audio |
| Disable recording | Désactiver enregistrement |

### Repeat Groups

| English | French |
| --------- | -------- |
| Add | Ajouter |
| Do not add | Ne pas ajouter |

### Form Navigation

| English | French | Recommended Update |
| --------- | -------- | ------------------- |
| NEXT | SUIVANT | SIGUIENTE (ES) |
| Save as draft | Enregistrer comme ébauche | Sauvegarder le brouillon (FR) |
| Finalize | Finaliser |  |

### Sending Forms

| English | French |
| --------- | -------- |
| Send Selected | Envoyer éléments sélectionnés |

## Button Names - Capitalization Quick Reference

When translating button or tab names in documentation, match the UI capitalization:

| Example | French |
| --------- | -------- |
| DATA | **DONNÉES** |
| FORM | **FORMULAIRE** |
| DEPLOY | **DÉPLOYER** |
| NEW | **NOUVEAU** |
| Draft | **Brouillon** |

**⚠️ IMPORTANT:** When writing support documentation, wrap UI element names in bold to indicate they are UI elements: **DÉPLOYER**, **Brouillon**, **onglet FORMULAIRE**

## Translation Examples

### Example 1: Draft Status

**Source:** "To start collecting data, click DEPLOY in the FORM page to deploy your draft form."

**✅ CORRECT French:**
"Pour commencer à collecter des données, cliquez sur **DÉPLOYER** dans la page **FORMULAIRE** pour déployer votre formulaire **Brouillon**."

**❌ WRONG French:**
"Pour commencer à collecter des données, cliquez sur **DÉPLOYER** dans la page **FORMULAIRE** pour déployer votre formulaire **brouillon**."

**Error:** Lowercase "brouillon" - should be capitalized "Brouillon" when referring to the UI status.

### Example 2: Tab Names

**Source:** "You can view your data in the DATA tab."



**Error:** Not all caps - should be "**DATOS**" to match UI.
