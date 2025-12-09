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

| Context | Spanish | ❌ Common Error |
| --------- | --------- | ----------------- |
| UI element / Form status | **Borrador** | ❌ Using lowercase in UI contexts |
| Main navigation | **Ventana FORMULARIO** | ❌ Not all caps |
| Main navigation | **Ventana DATOS** | ❌ Not all caps |

**⚠️ RULE:** When referring to UI elements (buttons, tabs, statuses), use the EXACT capitalization from the UI.

## Formbuilder UI Terminology

### API and Core Elements

| English | Spanish | Notes |
| --------- | --------- | ------- |
| The application programming interface (API) / KoboToolbox API | interfaz de programación de aplicaciones (API) |  |
| Toolbar | barra de herramientas |  |
| Build from scratch | Crear desde un borrador |  |
| **Draft** | **Borrador** | 🚨 FR: not "ébauche" / Capitalize in UI contexts |
| Save Draft (Enketo) | Guardar borrador |  |

### Tabs and Views

| English | Spanish | Notes |
| --------- | --------- | ------- |
| FORM tab | **Ventana FORMULARIO** | 🚨 ALL CAPS for tab name |
| Form view / Form page | visualizar el formulario / página del formulario |  |
| DATA tab | **Ventana DATOS** | 🚨 ALL CAPS for tab name |
| SUMMARY tab | **Ventana RESUMEN** | 🚨 ALL CAPS for tab name |
| View | Vista | FR: Can be "affichage" or "aperçu" in other contexts, but not for UI elements |
| Table view | vista de Tabla |  |
| Map view | vista de Mapa |  |
| Report view | vista de Informes |  |

### Pages and Features

| English | Spanish |
| --------- | --------- |
| Downloads page | página de Descargas |
| Gallery page | página de Galería |
| New Export | Nuevo exportable |
| Save image as | Guardar la imágen como |
| Embeddable Web Form Code | Código de formulario web integrable |
| Hook / webhook | Hook / webhook |

## KoboCollect UI Terminology

### Main Menu

| English | Spanish | Recommended Update | Notes |
| --------- | --------- | ------------------- | ------- |
| Start new form | Iniciar nuevo formulario |  |  |
| Drafts | Borradores |  |  |
| Ready to send | Listo para enviar |  |  |
| Sent | Enviado |  |  |
| Download form | Descargar formulario |  |  |
| Delete form | Borrar formulario |  |  |

### Download Form Screen

| English | Spanish |
| --------- | --------- |
| Select all | Seleccionar todo |
| Refresh | Actualizar |
| Get Selected | Obtener los Seleccionados |

### Settings

| English | Spanish |
| --------- | --------- |
| Manually enter project details | Entrar los detalles del proyecto manualmente |
| Settings | Ajustes |
| Server | Servidor |

### GPS Questions

| English | Spanish | Recommended Update (ES) |
| --------- | --------- | ------------------------ |
| Start GeoPoint | Buscar Ubicación | Iniciar Geopunto |
| Start GeoTrace | Iniciar GeoLínea |  |
| Placement by tapping | Ubicación con toque |  |
| Manual location recording | Registro de localización manual |  |
| Record a point | Registrando un punto | Registrar un punto |
| Automatic location recording | Registro de localización automática | Registro de localización automático |
| Start | Iniciar |  |
| Recording interval | Intervalo de grabación |  |
| Accuracy requirement | Requisito de precisión |  |
| View of Change GeoTrace | Ver o cambiar GeoLínea |  |
| Start GeoShape | Iniciar GeoArea |  |

### Background Audio

| English | Spanish |
| --------- | --------- |
| Record audio | Grabar sonido de fondo |
| Disable recording | Desactivar la grabación |

### Repeat Groups

| English | Spanish |
| --------- | --------- |
| Add | Agregar |
| Do not add | No agregar |

### Form Navigation

| English | Spanish | Recommended Update |
| --------- | --------- | ------------------- |
| NEXT | SIG. | SIGUIENTE (ES) |
| Save as draft | Guardar como borrador | Sauvegarder le brouillon (FR) |
| Finalize | Finalizar |  |

### Sending Forms

| English | Spanish |
| --------- | --------- |
| Send Selected | Enviar seleccionado |

## Button Names - Capitalization Quick Reference

When translating button or tab names in documentation, match the UI capitalization:

| Example | Spanish |
| --------- | --------- |
| DATA | **DATOS** |
| FORM | **FORMULARIO** |
| DEPLOY | **DESPLEGAR** |
| NEW | **NUEVO** |
| Draft | **Borrador** |

**⚠️ IMPORTANT:** When writing support documentation, wrap UI element names in bold to indicate they are UI elements: **DÉPLOYER**, **Brouillon**, **onglet FORMULAIRE**

## Translation Examples

### Example 1: Draft Status

**Source:** "To start collecting data, click DEPLOY in the FORM page to deploy your draft form."



**Error:** Lowercase "brouillon" - should be capitalized "Brouillon" when referring to the UI status.

### Example 2: Tab Names

**Source:** "You can view your data in the DATA tab."

**✅ CORRECT Spanish:**
"Puedes visualizar tus datos en la ventana **DATOS**."

**❌ WRONG Spanish:**
"Puedes visualizar tus datos en la ventana **Datos**."

**Error:** Not all caps - should be "**DATOS**" to match UI.
