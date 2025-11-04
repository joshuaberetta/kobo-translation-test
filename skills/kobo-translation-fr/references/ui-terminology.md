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

|------|---------|--------|---------|-----------------|
| Draft | UI element / Form status | **Brouillon** | **Borrador** | ❌ Using lowercase in UI contexts |
| Form tab | Main navigation | **onglet FORMULAIRE** | **Ventana FORMULARIO** | ❌ Not all caps |
| Data tab | Main navigation | **onglet DONNÉES** | **Ventana DATOS** | ❌ Not all caps |

**⚠️ RULE:** When referring to UI elements (buttons, tabs, statuses), use the EXACT capitalization from the UI.

## Formbuilder UI Terminology

### API and Core Elements

|---------|--------|---------|-------|
| The application programming interface (API) / KoboToolbox API | interface de programmation d'application (API) / API KoboToolbox | interfaz de programación de aplicaciones (API) | |
| Toolbar | barre d'outils | barra de herramientas | |
| Build from scratch | Création de formulaires (in UI) / Créer un formulaire à partir de zéro (in text) | Crear desde un borrador | |
| **Draft** | **Brouillon** | **Borrador** | 🚨 FR: not "ébauche" / Capitalize in UI contexts |
| Save Draft (Enketo) | Sauvegarder le brouillon | Guardar borrador | |

### Tabs and Views

|---------|--------|---------|-------|
| FORM tab | **onglet FORMULAIRE** | **Ventana FORMULARIO** | 🚨 ALL CAPS for tab name |
| Form view / Form page | mode formulaire / tableau de bord du formulaire | visualizar el formulario / página del formulario | |
| DATA tab | **onglet DONNÉES** | **Ventana DATOS** | 🚨 ALL CAPS for tab name |
| SUMMARY tab | **onglet SOMMAIRE** | **Ventana RESUMEN** | 🚨 ALL CAPS for tab name |
| View | mode | Vista | FR: Can be "affichage" or "aperçu" in other contexts, but not for UI elements |
| Table view | mode Tableau | vista de Tabla | |
| Map view | mode Carte | vista de Mapa | |
| Report view | mode Rapports | vista de Informes | |

### Pages and Features

|---------|--------|---------|
| Downloads page | page Téléchargements | página de Descargas |
| Gallery page | page Galerie Photo | página de Galería |
| New Export | Nouvel export | Nuevo exportable |
| Save image as | Enregistrer l'image sous | Guardar la imágen como |
| Embeddable Web Form Code | Code de formulaire Web | Código de formulario web integrable |
| Hook / webhook | Hook / webhook | Hook / webhook |

## KoboCollect UI Terminology

### Main Menu

|---------|--------|---------|-------------------|-------|
| Start new form | Remplir un formulaire | Iniciar nuevo formulario | | |
| Drafts | Ébauches | Borradores | | |
| Ready to send | Prêt à envoyer | Listo para enviar | | |
| Sent | Envoyé | Enviado | | |
| Download form | Télécharger formulaire | Descargar formulario | | |
| Delete form | Supprimer formulaire | Borrar formulario | | |

### Download Form Screen

|---------|--------|---------|
| Select all | Tout sélectionner | Seleccionar todo |
| Refresh | Rafraîchir | Actualizar |
| Get Selected | Télécharger la sélection | Obtener los Seleccionados |

### Settings

|---------|--------|---------|
| Manually enter project details | Saisir les détails du projet | Entrar los detalles del proyecto manualmente |
| Settings | Paramètres | Ajustes |
| Server | Serveur | Servidor |

### GPS Questions

|---------|--------|---------|------------------------|
| Start GeoPoint | Démarrer le point | Buscar Ubicación | Iniciar Geopunto |
| Start GeoTrace | Démarrer la ligne | Iniciar GeoLínea | |
| Placement by tapping | Placement en tapotant | Ubicación con toque | |
| Manual location recording | Enregistrement manuel de la localisation | Registro de localización manual | |
| Record a point | Enregistrer un point | Registrando un punto | Registrar un punto |
| Automatic location recording | Enregistrement automatique de la localisation | Registro de localización automática | Registro de localización automático |
| Start | Démarrer | Iniciar | |
| Recording interval | Intervalle d'enregistrement | Intervalo de grabación | |
| Accuracy requirement | Exigence de précision | Requisito de precisión | |
| View of Change GeoTrace | Voir ou modifier la ligne | Ver o cambiar GeoLínea | |
| Start GeoShape | Démarrer le polygone | Iniciar GeoArea | |

### Background Audio

|---------|--------|---------|
| Record audio | Enregistrement audio | Grabar sonido de fondo |
| Disable recording | Désactiver enregistrement | Desactivar la grabación |

### Repeat Groups

|---------|--------|---------|
| Add | Ajouter | Agregar |
| Do not add | Ne pas ajouter | No agregar |

### Form Navigation

|---------|--------|---------|-------------------|
| NEXT | SUIVANT | SIG. | SIGUIENTE (ES) |
| Save as draft | Enregistrer comme ébauche | Guardar como borrador | Sauvegarder le brouillon (FR) |
| Finalize | Finaliser | Finalizar | |

### Sending Forms

|---------|--------|---------|
| Send Selected | Envoyer éléments sélectionnés | Enviar seleccionado |

## Button Names - Capitalization Quick Reference

When translating button or tab names in documentation, match the UI capitalization:

|----------------|---------|--------|---------|
| Tabs (all caps) | DATA | **DONNÉES** | **DATOS** |
| Tabs (all caps) | FORM | **FORMULAIRE** | **FORMULARIO** |
| Buttons | DEPLOY | **DÉPLOYER** | **DESPLEGAR** |
| Buttons | NEW | **NOUVEAU** | **NUEVO** |
| Status | Draft | **Brouillon** | **Borrador** |

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
