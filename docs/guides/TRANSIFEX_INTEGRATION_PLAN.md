# Transifex UI Terminology Integration Plan

**Created:** 10 December 2025  
**Status:** Planning Phase  
**Goal:** Ensure documentation translations match actual Transifex UI strings exactly

---

## Problem Statement

KoboToolbox uses Transifex for UI translations, but the documentation translation system currently relies on manually maintained UI terminology in `ui-terminology.md`. This creates a risk of:

- ❌ Documentation using different button/menu names than the actual UI
- ❌ Manual synchronization overhead between Transifex and docs
- ❌ Inconsistencies that confuse users
- ❌ No automated validation of terminology accuracy

## KoboToolbox Transifex Context

**Transifex Project:** https://www.transifex.com/kobotoolbox/kobotoolbox/

**Repository:** https://github.com/kobotoolbox/form-builder-translations/

**Key Resources:**
- `django.po` - Backend Python file strings (KPI application)
- `djangojs.po` - Frontend JavaScript file strings (UI elements)

**Format:** PO (Portable Object) files in gettext format

**Update Frequency:** Automated GitHub Action runs on 1st and 15th of each month

**Workflow:**
1. Developers add translatable strings to KPI codebase
2. Extract strings to PO files (using `json2po` for frontend, `makemessages` for backend)
3. Push source files to Transifex using Transifex CLI (`tx push -s`)
4. Translators translate strings in Transifex web interface
5. Pull reviewed translations using Transifex CLI (`tx pull -a -f --mode reviewed`)
6. Commit translations to `form-builder-translations` repository

**Implications for Documentation:**
- UI strings are in PO file format, not CSV/JSON by default
- Translations marked as "reviewed" in Transifex are authoritative
- Biweekly automated sync means terminology can update twice monthly
- Need to parse PO files to extract UI strings for documentation reference

## Current System Architecture

```
Translation Workflow:
├── skills/kobo-translation/
│   ├── SKILL.md (main guidelines)
│   └── references/
│       ├── brand-terminology.md (OFFICIAL - brand terms)
│       ├── ui-terminology.md (OFFICIAL - manually maintained UI terms) ⚠️
│       ├── form-building-terms.md
│       ├── data-collection-terms.md
│       └── ...other references

Translation Process:
1. Claude reads skill + all reference files
2. Translates documentation following guidelines
3. Uses ui-terminology.md for button/tab names
4. No validation against actual Transifex strings
```

**Gap:** No connection between Transifex (source of truth) and translation skill.

---

## Solution Approaches

### Approach A: Template Variable System (Like `t()` in Code)

**Concept:** Similar to frontend `t("Delete")`, use placeholders in English docs that get replaced during translation.

**Example English Source:**
```markdown
1. Click the {{ui:Deploy}} button to publish your form.
2. Navigate to the {{ui:FORM}} tab.
3. Click {{ui:Save}} to save your changes.
```

**Translation Process:**
1. Parser identifies `{{ui:KEY}}` placeholders
2. Looks up KEY in Transifex PO files
3. Replaces with translated string for target language
4. Spanish output: "Haz clic en el botón **DESPLEGAR**"

**Pros:**
- ✅ **Guaranteed accuracy** - Direct lookup from Transifex
- ✅ **Zero manual work** - Fully automated substitution
- ✅ **Auto-updates** - When UI changes, docs update automatically
- ✅ **No LLM involvement** for UI terms - Simple string replacement
- ✅ **Consistent with KPI workflow** - Same pattern as frontend code

**Cons:**
- ❌ **English docs less readable** - Placeholders break reading flow
- ❌ **Requires preprocessing** - Build step before translation
- ❌ **Breaking change** - Need to convert all existing docs
- ❌ **Learning curve** - Writers must learn template syntax
- ❌ **Complex implementation** - Parser + integration with translation agent

**Implementation Complexity:** High (3-4 weeks)

---

### Approach B: Hybrid Approach (Recommended in Plan)

**Concept:** Provide Transifex terms as reference in translation skill, let LLM use them during translation.

**Example English Source:**
```markdown
1. Click the **Deploy** button to publish your form.
2. Navigate to the **FORM** tab.
3. Click **Save** to save your changes.
```

**Translation Process:**
1. LLM reads English doc + Transifex reference skill
2. Identifies "Deploy", "FORM", "Save" as UI elements
3. Looks up exact translations in transifex-ui-strings.md
4. Translates with correct Transifex terms

**Pros:**
- ✅ **Human-readable docs** - No special syntax needed
- ✅ **Works with current workflow** - Minimal changes
- ✅ **Flexible** - Can handle edge cases naturally
- ✅ **Easy to maintain** - Update reference file only
- ✅ **Low barrier** - Writers don't learn new syntax

**Cons:**
- ❌ **Depends on LLM accuracy** - Might miss UI terms or use wrong one
- ❌ **Requires validation** - Need checks to catch errors
- ❌ **Not guaranteed** - Small risk of inconsistency

**Implementation Complexity:** Low (1-2 weeks)

---

### Approach C: Hybrid with Auto-Replacement (Best of Both)

**Concept:** Combine template variables for critical UI terms with LLM translation for everything else.

**Example English Source:**
```markdown
1. Click the {{ui:Deploy}} button to publish your form.
2. Navigate to the {{ui:FORM}} tab.
3. Click {{ui:Save}} to save your changes.
4. This will help you manage your data collection workflow.
```

**Translation Process:**
1. **Pre-processing:** Replace `{{ui:KEY}}` with Transifex terms
2. **LLM translation:** Translate remaining text naturally
3. **Post-processing:** Verify all UI terms used correctly

**Spanish output:**
```markdown
1. Haz clic en el botón **DESPLEGAR** para publicar tu formulario.
2. Navega a la pestaña **FORMULARIO**.
3. Haz clic en **GUARDAR** para guardar los cambios.
4. Esto te ayudará a gestionar tu flujo de trabajo de recolección de datos.
```

**Pros:**
- ✅ **Guaranteed accuracy for critical terms** - Template ensures correctness
- ✅ **Natural translation for narrative** - LLM handles context
- ✅ **Optional templates** - Can gradually adopt or use selectively
- ✅ **Best of both worlds** - Precision + flexibility
- ✅ **Validation built-in** - Easy to check if templates resolved correctly

**Cons:**
- ❌ **Medium complexity** - Requires preprocessing step
- ❌ **Mixed approach** - Two systems to maintain
- ❌ **Partial learning curve** - Writers need to know when to use templates

**Implementation Complexity:** Medium (2-3 weeks)

---

## Recommended Solution: Approach C (Hybrid with Auto-Replacement)

### Why This is the Best Choice

1. **Solves the core problem:** UI terminology will match Transifex exactly
2. **Backward compatible:** Can adopt incrementally without rewriting all docs
3. **Writer-friendly:** Templates only for UI terms (10-20% of content)
4. **Developer-friendly:** Similar pattern to frontend `t()` function
5. **Automated where needed:** Critical UI terms have zero-error guarantee
6. **Flexible where needed:** Narrative text gets natural, context-aware translation

### When to Use Each Approach

**Use templates (`{{ui:KEY}}`):**
- Navigation tabs (FORM, DATA, SUMMARY)
- Action buttons (Deploy, Save, Submit, Delete)
- Menu items
- Dialog titles
- Settings names
- Any term that appears in actual UI

**Use natural text:**
- Explanatory paragraphs
- Instructions and guidance
- Examples and scenarios
- Conceptual descriptions
- Technical explanations

### Implementation Strategy

**Phase 0 (New):** Build template replacement system
**Phase 1:** Extract Transifex terms (as planned)
**Phase 2:** Update skills with both templates + reference (hybrid)
**Phase 3:** Build validation + automation (as planned)

---

## Recommended Solution: Approach C Implementation

**Core Components:**

1. **Template System** - Optional placeholders for guaranteed accuracy
2. **Transifex Reference** - Fallback for LLM when templates not used
3. **Preprocessing Pipeline** - Resolve templates before translation
4. **Validation** - Verify all templates resolved correctly
5. **Human-Readable Docs** - Templates optional, not required

**Why This Works:**

✅ **Guaranteed accuracy** for critical UI terms via templates  
✅ **Single source of truth** from Transifex for both templates and LLM  
✅ **Incremental adoption** - Can add templates gradually  
✅ **Natural translations** for narrative content via LLM  
✅ **Developer-familiar** pattern from frontend workflow  
✅ **Easy to validate** - Simple regex to check template resolution  

---

## Implementation Phases

### Phase 0: Build Template Replacement System (NEW)

**Action:** Create preprocessing system to resolve UI term templates

**Purpose:** Enable optional `{{ui:KEY}}` placeholders that guarantee Transifex accuracy

#### 0.1 Template Resolver Script

**File:** `scripts/resolve_ui_templates.py`

**Features:**
- Parse markdown files for `{{ui:KEY}}` patterns
- Look up KEY in Transifex PO files
- Replace with translated string for target language
- Maintain markdown formatting (bold, etc.)
- Report unresolved templates as errors

**Code:**

```python
#!/usr/bin/env python3
"""
Resolve UI term templates in documentation before translation.

Replaces {{ui:KEY}} placeholders with actual Transifex translations.

Usage:
    python scripts/resolve_ui_templates.py \
        --input docs/en/article.md \
        --output docs/en/article_resolved.md \
        --language es \
        --po-repo ../form-builder-translations

    # Or process in-place
    python scripts/resolve_ui_templates.py \
        --input docs/en/article.md \
        --language es \
        --po-repo ../form-builder-translations \
        --in-place
"""

import re
import sys
import polib
from pathlib import Path
from typing import Dict, Optional, List, Tuple

# Template pattern: {{ui:KEY}} or {{ui:KEY|formatting}}
TEMPLATE_PATTERN = r'\{\{ui:([a-zA-Z0-9_]+)(?:\|([^}]+))?\}\}'

class TemplateResolver:
    """Resolves UI term templates using Transifex PO files"""
    
    def __init__(self, po_repo_path: Path, language: str):
        self.po_repo_path = po_repo_path
        self.language = language
        self.translations = self._load_translations()
        self.unresolved = []
    
    def _load_translations(self) -> Dict[str, str]:
        """Load translations from djangojs.po"""
        po_file = self.po_repo_path / self.language / 'LC_MESSAGES' / 'djangojs.po'
        
        if not po_file.exists():
            raise FileNotFoundError(
                f"PO file not found: {po_file}\n"
                f"Make sure form-builder-translations is cloned and language is valid."
            )
        
        po = polib.pofile(str(po_file))
        translations = {}
        
        for entry in po:
            if entry.msgid and entry.msgstr and not entry.obsolete:
                # Create lookup by exact msgid and also normalized key
                translations[entry.msgid] = entry.msgstr
                # Also store with underscores (for template keys)
                key = entry.msgid.replace(' ', '_')
                translations[key] = entry.msgstr
        
        print(f"Loaded {len(translations)} translations from {po_file.name}")
        return translations
    
    def _apply_formatting(self, text: str, formatting: Optional[str]) -> str:
        """Apply markdown formatting to translated text"""
        if not formatting:
            return text
        
        if formatting == 'bold':
            return f"**{text}**"
        elif formatting == 'italic':
            return f"*{text}*"
        elif formatting == 'code':
            return f"`{text}`"
        elif formatting == 'upper':
            return text.upper()
        elif formatting == 'lower':
            return text.lower()
        else:
            # Unknown formatting, skip
            return text
    
    def resolve_template(self, match: re.Match) -> str:
        """Resolve a single template match"""
        key = match.group(1)
        formatting = match.group(2)
        
        # Try exact key lookup
        if key in self.translations:
            translated = self.translations[key]
            return self._apply_formatting(translated, formatting)
        
        # Try with spaces instead of underscores
        key_with_spaces = key.replace('_', ' ')
        if key_with_spaces in self.translations:
            translated = self.translations[key_with_spaces]
            return self._apply_formatting(translated, formatting)
        
        # Not found - record and keep template
        self.unresolved.append((key, match.group(0)))
        return match.group(0)  # Return original template
    
    def resolve_file(self, content: str) -> str:
        """Resolve all templates in file content"""
        self.unresolved = []  # Reset for new file
        resolved = re.sub(TEMPLATE_PATTERN, self.resolve_template, content)
        return resolved
    
    def get_template_report(self) -> str:
        """Generate report of template resolution"""
        if not self.unresolved:
            return "✅ All templates resolved successfully"
        
        report = f"⚠️  {len(self.unresolved)} unresolved templates:\n"
        for key, template in self.unresolved:
            report += f"  - {template} (key: {key})\n"
        
        report += "\nAdd these strings to Transifex or fix template keys."
        return report

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Resolve UI term templates using Transifex translations'
    )
    parser.add_argument(
        '--input', '-i',
        type=Path,
        required=True,
        help='Input markdown file with templates'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        help='Output file (defaults to input_resolved.md)'
    )
    parser.add_argument(
        '--language', '-l',
        required=True,
        choices=['es', 'fr', 'ar'],
        help='Target language'
    )
    parser.add_argument(
        '--po-repo', '-p',
        type=Path,
        required=True,
        help='Path to form-builder-translations repository'
    )
    parser.add_argument(
        '--in-place',
        action='store_true',
        help='Modify input file in place'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Exit with error if any templates unresolved'
    )
    
    args = parser.parse_args()
    
    # Validate input
    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}")
        return 1
    
    if not args.po_repo.exists():
        print(f"Error: PO repository not found: {args.po_repo}")
        print("Clone it with:")
        print("  git clone https://github.com/kobotoolbox/form-builder-translations.git")
        return 1
    
    # Determine output path
    if args.in_place:
        output_path = args.input
    elif args.output:
        output_path = args.output
    else:
        output_path = args.input.parent / f"{args.input.stem}_resolved{args.input.suffix}"
    
    # Load and resolve
    try:
        resolver = TemplateResolver(args.po_repo, args.language)
        content = args.input.read_text(encoding='utf-8')
        
        # Count templates before resolution
        template_count = len(re.findall(TEMPLATE_PATTERN, content))
        print(f"Found {template_count} templates in {args.input.name}")
        
        # Resolve templates
        resolved_content = resolver.resolve_file(content)
        
        # Write output
        output_path.write_text(resolved_content, encoding='utf-8')
        print(f"\n✅ Resolved templates written to {output_path}")
        
        # Report
        print(f"\n{resolver.get_template_report()}")
        
        # Exit code
        if args.strict and resolver.unresolved:
            return 1
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

**Template Syntax:**

```markdown
# Basic template
{{ui:Deploy}}                    → DESPLEGAR (Spanish)

# With formatting
{{ui:Deploy|bold}}               → **DESPLEGAR**
{{ui:FORM|code}}                 → `FORMULARIO`

# Common UI terms
{{ui:Save}}                      → GUARDAR
{{ui:Delete}}                    → BORRAR
{{ui:Submit}}                    → ENVIAR
{{ui:DATA}}                      → DATOS
{{ui:New}}                       → NUEVO

# Multi-word (use underscore)
{{ui:Save_Draft}}                → GUARDAR BORRADOR
{{ui:Start_new_form}}            → INICIAR NUEVO FORMULARIO
```

**Usage Examples:**

```bash
# Resolve templates for Spanish translation
python scripts/resolve_ui_templates.py \
    --input docs/en/getting_started.md \
    --language es \
    --po-repo ../form-builder-translations

# Strict mode (fail on unresolved)
python scripts/resolve_ui_templates.py \
    --input docs/en/getting_started.md \
    --language es \
    --po-repo ../form-builder-translations \
    --strict

# In-place resolution (modifies original)
python scripts/resolve_ui_templates.py \
    --input docs/en/getting_started.md \
    --language es \
    --po-repo ../form-builder-translations \
    --in-place
```

**Time Estimate:** 3-4 hours development + testing

---

#### 0.2 Integration with Translation Agent

**File:** `scripts/translation_agent.py`

**Modification:** Add preprocessing step to resolve templates before translation

**Changes:**

```python
def translate_document(self, source_path: str, target_lang: str) -> str:
    """Translate document with template resolution"""
    
    # NEW: Resolve UI templates first
    if self.use_templates:
        print("🔄 Resolving UI templates...")
        resolver = TemplateResolver(
            po_repo_path=Path(self.po_repo),
            language=target_lang
        )
        content = Path(source_path).read_text()
        content = resolver.resolve_file(content)
        
        if resolver.unresolved:
            print(f"⚠️  {len(resolver.unresolved)} unresolved templates")
            for key, template in resolver.unresolved:
                print(f"  - {template}")
        
        # Use resolved content for translation
        source_text = content
    else:
        source_text = Path(source_path).read_text()
    
    # Continue with normal translation...
    return self.translate(source_text, target_lang)
```

**Configuration:**

Add to `.env` or command line:
```bash
# Enable template resolution
USE_UI_TEMPLATES=true
PO_REPO_PATH=../form-builder-translations

# Or via command line
python scripts/translation_agent.py \
    --file docs/en/article.md \
    --language es \
    --use-templates \
    --po-repo ../form-builder-translations
```

**Time Estimate:** 2-3 hours integration + testing

---

#### 0.3 Template Writing Guidelines

**File:** `docs/guides/UI_TEMPLATE_GUIDE.md`

**Content:** Documentation for writers on when and how to use templates

**Key Points:**

**When to Use Templates:**
- ✅ Navigation tabs (FORM, DATA, SUMMARY, etc.)
- ✅ Action buttons (Deploy, Save, Submit, Delete, etc.)
- ✅ Menu items that appear in UI
- ✅ Dialog titles
- ✅ Settings names
- ✅ Any term you want to guarantee matches UI exactly

**When NOT to Use Templates:**
- ❌ General concepts (even if related to UI features)
- ❌ Explanatory text
- ❌ Examples and scenarios
- ❌ Descriptive paragraphs
- ❌ Technical terms not in UI

**Example:**

```markdown
# Good: Mix of templates and natural text

To publish your form, click the {{ui:Deploy|bold}} button on the 
{{ui:FORM}} tab. This will make your form available for data collection.

Navigate to the {{ui:DATA}} tab to view your submissions. You can filter,
edit, and export the data from this interface.
```

```markdown
# Bad: Too many templates

{{ui:To}} {{ui:publish}} {{ui:your}} {{ui:form}}, {{ui:click}}...
```

**Template Key Naming:**
- Use exact UI string when possible: `{{ui:Deploy}}`
- Use underscores for multi-word: `{{ui:Save_Draft}}`
- Match PO file msgid exactly
- Case-sensitive

**Time Estimate:** 1-2 hours documentation

---

**Phase 0 Total Time Estimate:** 6-9 hours

**Deliverables:**
- ✅ Template resolver script
- ✅ Integration with translation agent
- ✅ Writer guidelines
- ✅ Example templates for common UI terms

---

### Phase 1: Create Transifex Reference File

**Action:** Create new reference file with actual Transifex translations

**File:** `skills/kobo-translation/references/transifex-ui-strings.md`

**Structure:**

```markdown
# Transifex UI Strings (AUTHORITATIVE)

**🚨 CRITICAL: These are the EXACT translations from Transifex.**

**Source:** Direct export from Transifex  
**Last Updated:** [DATE]  
**Priority:** HIGHEST - Use these translations exactly as shown  

⚠️ **USAGE RULE:** When translating documentation that mentions ANY UI element 
(buttons, tabs, menus, dialogs, settings), you MUST use EXACTLY these translations.
Do NOT adapt, modify, or localize these strings - they must match the UI character-for-character.

## How to Use This File

1. **First**, check if the English UI term appears in the tables below
2. **If found**, use the EXACT translation provided (including capitalization)
3. **If NOT found**, check `ui-terminology.md` for supplementary terms
4. When in doubt about whether something is a UI element, assume it is and check here first

## Core UI Actions & Buttons

| English UI String | French (Transifex) | Spanish (Transifex) | Arabic (Transifex) | Context |
|-------------------|-------------------|---------------------|-------------------|----------|
| Deploy | DÉPLOYER | DESPLEGAR | [Arabic] | Button to publish/deploy form |
| Save | SAUVEGARDER | GUARDAR | [Arabic] | Save button (general) |
| Save Draft | SAUVEGARDER LE BROUILLON | GUARDAR BORRADOR | [Arabic] | Save draft specifically |
| Submit | SOUMETTRE | ENVIAR | [Arabic] | Submit form data |
| New | NOUVEAU | NUEVO | [Arabic] | Create new project/form |
| Download | TÉLÉCHARGER | DESCARGAR | [Arabic] | Download button |
| Delete | SUPPRIMER | BORRAR | [Arabic] | Delete action |
| Edit | MODIFIER | EDITAR | [Arabic] | Edit action |
| Cancel | ANNULER | CANCELAR | [Arabic] | Cancel action |
| Close | FERMER | CERRAR | [Arabic] | Close dialog/window |
| Add | AJOUTER | AGREGAR | [Arabic] | Add item button |
| Remove | RETIRER | ELIMINAR | [Arabic] | Remove item |
| Upload | IMPORTER | SUBIR | [Arabic] | Upload file |
| Export | EXPORTER | EXPORTAR | [Arabic] | Export data |
| Import | IMPORTER | IMPORTAR | [Arabic] | Import data |
| Refresh | ACTUALISER | ACTUALIZAR | [Arabic] | Refresh/reload |
| Search | RECHERCHER | BUSCAR | [Arabic] | Search function |
| Filter | FILTRER | FILTRAR | [Arabic] | Filter data |
| Sort | TRIER | ORDENAR | [Arabic] | Sort function |
| Share | PARTAGER | COMPARTIR | [Arabic] | Share button |
| Preview | APERÇU | VISTA PREVIA | [Arabic] | Preview function |
| Settings | PARAMÈTRES | CONFIGURACIÓN | [Arabic] | Settings menu |
| Help | AIDE | AYUDA | [Arabic] | Help menu/button |

## Navigation Tabs (Main Interface)

**Note:** Main navigation tabs are typically ALL CAPS in the UI.

| English UI String | French (Transifex) | Spanish (Transifex) | Arabic (Transifex) | Context |
|-------------------|-------------------|---------------------|-------------------|----------|
| FORM | FORMULAIRE | FORMULARIO | [Arabic] | Form tab (all caps) |
| DATA | DONNÉES | DATOS | [Arabic] | Data tab (all caps) |
| SUMMARY | SOMMAIRE | RESUMEN | [Arabic] | Summary tab (all caps) |
| DOWNLOADS | TÉLÉCHARGEMENTS | DESCARGAS | [Arabic] | Downloads tab |
| GALLERY | GALERIE PHOTO | GALERÍA | [Arabic] | Gallery tab |
| MAP | CARTE | MAPA | [Arabic] | Map tab |
| TABLE | TABLEAU | TABLA | [Arabic] | Table tab |
| REPORTS | RAPPORTS | INFORMES | [Arabic] | Reports tab |
| SETTINGS | PARAMÈTRES | CONFIGURACIÓN | [Arabic] | Settings tab |

## Form Builder UI Elements

| English UI String | French (Transifex) | Spanish (Transifex) | Arabic (Transifex) | Context |
|-------------------|-------------------|---------------------|-------------------|----------|
| Build from scratch | CRÉATION DE FORMULAIRES | CREAR DESDE UN BORRADOR | [Arabic] | Create new form option |
| Draft | BROUILLON | BORRADOR | [Arabic] | Draft status (capitalize) |
| Question Library | LA BIBLIOTHÈQUE DE QUESTIONS | LA BIBLIOTECA DE PREGUNTAS | [Arabic] | Question Library feature |
| Add Question | AJOUTER UNE QUESTION | AGREGAR PREGUNTA | [Arabic] | Add question button |
| Add Group | AJOUTER UN GROUPE | AGREGAR GRUPO | [Arabic] | Add group button |
| Question Type | TYPE DE QUESTION | TIPO DE PREGUNTA | [Arabic] | Question type selector |
| Question Label | LIBELLÉ DE LA QUESTION | ETIQUETA DE PREGUNTA | [Arabic] | Question label field |
| Hint | INDICE | SUGERENCIA | [Arabic] | Hint/help text field |
| Required | OBLIGATOIRE | OBLIGATORIO | [Arabic] | Required field setting |
| Skip Logic | LOGIQUE DE SAUT | LÓGICA DE SALTO | [Arabic] | Skip logic feature |
| Validation | VALIDATION | VALIDACIÓN | [Arabic] | Validation feature |

## Data Management UI

| English UI String | French (Transifex) | Spanish (Transifex) | Arabic (Transifex) | Context |
|-------------------|-------------------|---------------------|-------------------|----------|
| Submissions | SOUMISSIONS | ENVÍOS | [Arabic] | Submitted data records |
| View | MODE | VISTA | [Arabic] | View/display mode |
| Table View | MODE TABLEAU | VISTA DE TABLA | [Arabic] | Table display mode |
| Map View | MODE CARTE | VISTA DE MAPA | [Arabic] | Map display mode |
| Report View | MODE RAPPORTS | VISTA DE INFORMES | [Arabic] | Report display mode |
| Edit Submission | MODIFIER LA SOUMISSION | EDITAR ENVÍO | [Arabic] | Edit submission action |
| Delete Submission | SUPPRIMER LA SOUMISSION | BORRAR ENVÍO | [Arabic] | Delete submission |
| Validate | VALIDER | VALIDAR | [Arabic] | Validate action |

## KoboCollect (Mobile App) UI

| English UI String | French (Transifex) | Spanish (Transifex) | Arabic (Transifex) | Context |
|-------------------|-------------------|---------------------|-------------------|----------|
| Start new form | REMPLIR UN FORMULAIRE | INICIAR NUEVO FORMULARIO | [Arabic] | Start new form entry |
| Drafts | ÉBAUCHES | BORRADORES | [Arabic] | Drafts menu (mobile) |
| Ready to send | PRÊT À ENVOYER | LISTO PARA ENVIAR | [Arabic] | Ready status |
| Sent | ENVOYÉ | ENVIADO | [Arabic] | Sent status |
| Download form | TÉLÉCHARGER FORMULAIRE | DESCARGAR FORMULARIO | [Arabic] | Download form menu |
| Delete form | SUPPRIMER FORMULAIRE | BORRAR FORMULARIO | [Arabic] | Delete form option |
| Select all | TOUT SÉLECTIONNER | SELECCIONAR TODO | [Arabic] | Select all checkbox |
| Get Selected | TÉLÉCHARGER LA SÉLECTION | OBTENER LOS SELECCIONADOS | [Arabic] | Download selected |
| Finalize | FINALISER | FINALIZAR | [Arabic] | Finalize form |
| NEXT | SUIVANT | SIG. | [Arabic] | Next button (navigation) |

## Dialogs & Messages

| English UI String | French (Transifex) | Spanish (Transifex) | Arabic (Transifex) | Context |
|-------------------|-------------------|---------------------|-------------------|----------|
| Success | SUCCÈS | ÉXITO | [Arabic] | Success message |
| Error | ERREUR | ERROR | [Arabic] | Error message |
| Warning | AVERTISSEMENT | ADVERTENCIA | [Arabic] | Warning message |
| Confirm | CONFIRMER | CONFIRMAR | [Arabic] | Confirmation dialog |
| Are you sure? | ÊTES-VOUS SÛR? | ¿ESTÁ SEGURO? | [Arabic] | Confirmation prompt |
| Loading... | CHARGEMENT... | CARGANDO... | [Arabic] | Loading indicator |

## Settings & Configuration

| English UI String | French (Transifex) | Spanish (Transifex) | Arabic (Transifex) | Context |
|-------------------|-------------------|---------------------|-------------------|----------|
| Server | SERVEUR | SERVIDOR | [Arabic] | Server settings |
| Username | NOM D'UTILISATEUR | NOMBRE DE USUARIO | [Arabic] | Username field |
| Password | MOT DE PASSE | CONTRASEÑA | [Arabic] | Password field |
| General Settings | PARAMÈTRES GÉNÉRAUX | CONFIGURACIÓN GENERAL | [Arabic] | General settings |
| User Interface | INTERFACE UTILISATEUR | INTERFAZ DE USUARIO | [Arabic] | UI settings |
| Form Management | GESTION DES FORMULAIRES | GESTIÓN DE FORMULARIOS | [Arabic] | Form management |

## Export & Download Options

| English UI String | French (Transifex) | Spanish (Transifex) | Arabic (Transifex) | Context |
|-------------------|-------------------|---------------------|-------------------|----------|
| New Export | NOUVEL EXPORT | NUEVO EXPORTABLE | [Arabic] | Create new export |
| Export Type | TYPE D'EXPORT | TIPO DE EXPORTACIÓN | [Arabic] | Export format selector |
| Include Media | INCLURE LES MÉDIAS | INCLUIR MEDIOS | [Arabic] | Include media option |
| Download | TÉLÉCHARGER | DESCARGAR | [Arabic] | Download button |

---

## How to Populate This File

### Step 1: Clone Transifex Translations Repository

```bash
# Clone the KoboToolbox translations repository
git clone https://github.com/kobotoolbox/form-builder-translations.git
cd form-builder-translations
```

This repository contains the latest reviewed translations from Transifex in PO file format.

### Step 2: Extract UI Strings from PO Files

**Option A: Manual Extraction (Quick Start)**

1. Open the relevant PO files:
   - `es/LC_MESSAGES/djangojs.po` - Spanish frontend UI strings
   - `fr/LC_MESSAGES/djangojs.po` - French frontend UI strings
   - `ar/LC_MESSAGES/djangojs.po` - Arabic frontend UI strings

2. PO file format:
   ```po
   #: location/in/code.js:123
   msgid "Deploy"
   msgstr "DESPLEGAR"
   
   #: another/location.js:456
   msgid "Save"
   msgstr "GUARDAR"
   ```

3. Extract UI-relevant strings:
   - Focus on `msgid` (English source) and `msgstr` (translation)
   - Look for button labels, menu items, tab names
   - Skip developer comments and technical strings

**Option B: Automated Extraction (Recommended)**

Use the PO file parser script (see Phase 3.3 below) to automatically extract and format UI strings.

### Step 3: Identify UI-Relevant Strings

Focus on these categories from `djangojs.po`:
- Button labels (Deploy, Save, Submit, Delete, etc.)
- Navigation tabs (FORM, DATA, SUMMARY, etc.)
- Menu items
- Dialog titles and messages
- Form builder UI elements
- Data management actions
- Settings and configuration options

**Note:** The `django.po` file contains backend strings which are less likely to be visible UI elements. Prioritize `djangojs.po` for user-facing interface terminology.

### Step 4: Populate the Tables

For each English UI string:
1. Find the corresponding `msgid`/`msgstr` pairs in PO files
2. Add to the appropriate table above
3. Include context notes from PO file comments (`#:` lines)
4. Verify capitalization matches the actual UI
5. Prioritize strings from `djangojs.po` (frontend UI)

### Step 5: Validate Against Live UI

1. Open your KoboToolbox instance in each language
2. Manually verify a sample of critical UI elements
3. Update any discrepancies
4. Add date stamp to "Last Updated" field
5. Cross-reference with https://app.transifex.com/kobotoolbox/kobotoolbox/

### Step 6: Maintain

**Sync Frequency:**
- KoboToolbox has automated sync on 1st and 15th of each month
- After each sync, review form-builder-translations repository for updates
- Update `transifex-ui-strings.md` if new UI strings added or changed

**Maintenance Tasks:**
- **Biweekly:** Check form-builder-translations repo for updates after automated sync
- **Monthly:** Review and update reference file with any new UI strings
- **Quarterly:** Full validation against live UI in all languages
- **As needed:** When new features added or UI redesigned

**Automation Option:** See Phase 3.3 for PO file parser script
```

**Deliverable:** Completed `transifex-ui-strings.md` file with actual Transifex translations

**Time Estimate:** 4-6 hours (manual) or 2-3 hours with automation

---

### Phase 2: Update Skill Priority Hierarchy

**Action:** Modify `SKILL.md` to establish Transifex precedence

**File:** `skills/kobo-translation/SKILL.md`

**Changes Required:**

#### 2.1 Update Pre-Translation Checklist

**Location:** Line ~31 (🚨 CRITICAL: Pre-Translation Checklist section)

**Change from:**
```markdown
**BEFORE starting translation, read these reference files:**

1. **[brand-terminology.md](references/brand-terminology.md)** - For server names, Question Library, Formbuilder, and ALL brand terms
2. **[ui-terminology.md](references/ui-terminology.md)** - For button names, tabs, and capitalization rules
```

**Change to:**
```markdown
**BEFORE starting translation, read these reference files:**

1. **[brand-terminology.md](references/brand-terminology.md)** - For server names, Question Library, Formbuilder, and ALL brand terms
2. **[transifex-ui-strings.md](references/transifex-ui-strings.md)** - For ALL UI elements (buttons, tabs, menus) - HIGHEST PRIORITY
3. **[ui-terminology.md](references/ui-terminology.md)** - For supplementary UI terms not in Transifex
```

#### 2.2 Update Translation Workflow Section

**Location:** Line ~95 (Translation Workflow section)

**Add new subsection after "Step 0: MANDATORY First Step":**

```markdown
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
```

#### 2.3 Update Terminology References Section

**Location:** Line ~665 (Terminology References section)

**Change from:**
```markdown
## Terminology References

For detailed term-by-term translations, consult these reference files:

- **[brand-terminology.md](references/brand-terminology.md)** - Brand terms, product names, user plans (OFFICIAL) - **READ THIS FIRST**
- **[form-building-terms.md](references/form-building-terms.md)** - Form building, XLSForm, cascading selects (OFFICIAL)
- **[question-types.md](references/question-types.md)** - Question types and appearances (PREFERRED for types, special rules for appearances)
- **[ui-terminology.md](references/ui-terminology.md)** - Formbuilder and KoboCollect UI (OFFICIAL) - **READ THIS SECOND**
- **[data-collection-terms.md](references/data-collection-terms.md)** - Data collection concepts (PREFERRED)
- **[documentation-terminology.md](references/documentation-terminology.md)** - Documentation website and Help Center terms (PREFERRED)
- **[course-terminology.md](references/course-terminology.md)** - Learning platform and course content (PREFERRED)
```

**Change to:**
```markdown
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
```

#### 2.4 Update Translation Decision Tree

**Location:** Line ~675 (Translation Decision Tree section)

**Change the first few decision points from:**
```markdown
```
START: Do I see ANY of these terms in the source text?
├─ Server names (Global Server, EU Server)?
│  └─ 🚨 STOP → Open brand-terminology.md → Use EXACT translation with articles
│
├─ "Question Library"?
│  └─ 🚨 STOP → Must be "La bibliothèque de questions" / "La biblioteca de preguntas" (capital L)
```
```

**Change to:**
```markdown
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
├─ "Question Library"?
│  └─ 🚨 STOP → Must be "La bibliothèque de questions" / "La biblioteca de preguntas" (capital L)
```
```

**Deliverable:** Updated `SKILL.md` with clear Transifex priority

**Time Estimate:** 30 minutes

---

### Phase 3: Create Automation Scripts (OPTIONAL)

**Action:** Build tools to monitor and validate UI terminology

#### 3.1 UI Term Validation Script

**File:** `scripts/validate_ui_terms.py`

**Purpose:** Scan translated docs to find UI terms that don't match form-builder-translations reference

**Features:**
- Load official UI terms from transifex-ui-strings.md reference file
- Scan all translated markdown files
- Identify potential UI elements in source (English) docs
- Check if translations match the reference exactly
- Report mismatches with file locations

**Pseudocode:**
```python
#!/usr/bin/env python3
"""
Validate that translated documentation uses correct Transifex UI terminology.

Usage:
    python scripts/validate_ui_terms.py --language es
    python scripts/validate_ui_terms.py --language es fr ar
    python scripts/validate_ui_terms.py --help
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple

def load_transifex_terms(language: str) -> Dict[str, str]:
    """
    Load official UI terms from transifex-ui-strings.md
    Returns dict mapping English UI string to translated version
    """
    # Parse markdown tables in transifex-ui-strings.md
    # Extract language column
    # Return {english: translation}
    pass

def load_ui_patterns() -> List[str]:
    """
    Load common UI element patterns to search for
    Returns list of English UI terms to look for
    """
    # Get all English strings from transifex-ui-strings.md
    # Common patterns: "click X", "**X** button", "X tab", etc.
    pass

def scan_document(doc_path: Path, en_doc_path: Path, 
                  transifex_terms: Dict[str, str]) -> List[Dict]:
    """
    Scan a translated document for UI terminology issues
    
    Args:
        doc_path: Path to translated document
        en_doc_path: Path to English source document
        transifex_terms: Official translations from Transifex
    
    Returns:
        List of issues found: [{term, found, expected, line_num}]
    """
    # Read both documents
    # Find UI elements in English doc
    # Find corresponding location in translated doc
    # Check if translation matches Transifex
    # Return list of mismatches
    pass

def scan_language(language: str) -> Dict[str, List]:
    """
    Scan all documents for a language
    Returns dict of {file_path: [issues]}
    """
    transifex_terms = load_transifex_terms(language)
    ui_patterns = load_ui_patterns()
    
    docs_dir = Path(f'docs/{language}')
    en_docs_dir = Path('docs/en')
    
    issues = {}
    
    for doc_path in docs_dir.glob('*.md'):
        en_doc_path = en_docs_dir / doc_path.name
        if not en_doc_path.exists():
            continue
            
        doc_issues = scan_document(doc_path, en_doc_path, transifex_terms)
        if doc_issues:
            issues[str(doc_path)] = doc_issues
    
    return issues

def report_issues(all_issues: Dict[str, Dict[str, List]]):
    """
    Generate report of all issues found
    """
    total_issues = sum(
        len(issues) 
        for lang_issues in all_issues.values() 
        for issues in lang_issues.values()
    )
    
    print(f"\n{'='*80}")
    print(f"UI TERMINOLOGY VALIDATION REPORT")
    print(f"{'='*80}\n")
    print(f"Total issues found: {total_issues}\n")
    
    for language, lang_issues in all_issues.items():
        if not lang_issues:
            print(f"✅ {language.upper()}: All UI terms match Transifex")
            continue
            
        print(f"\n❌ {language.upper()}: {len(lang_issues)} files with issues\n")
        
        for file_path, issues in lang_issues.items():
            print(f"  📄 {file_path}")
            for issue in issues:
                print(f"     Line {issue['line_num']}: '{issue['found']}'")
                print(f"     Expected (Transifex): '{issue['expected']}'")
                print(f"     English term: '{issue['term']}'")
                print()

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Validate UI terminology against Transifex'
    )
    parser.add_argument(
        '--language', '-l',
        nargs='+',
        choices=['es', 'fr', 'ar'],
        required=True,
        help='Languages to validate'
    )
    
    args = parser.parse_args()
    
    all_issues = {}
    for language in args.language:
        print(f"Scanning {language.upper()} documentation...")
        all_issues[language] = scan_language(language)
    
    report_issues(all_issues)
    
    # Exit with error code if issues found
    has_issues = any(lang_issues for lang_issues in all_issues.values())
    sys.exit(1 if has_issues else 0)

if __name__ == "__main__":
    main()
```

**Usage:**
```bash
# Validate Spanish translations
python scripts/validate_ui_terms.py --language es

# Validate all languages
python scripts/validate_ui_terms.py --language es fr ar

# Use in CI/CD
python scripts/validate_ui_terms.py --language es || echo "UI term mismatches found"
```

**Time Estimate:** 3-5 hours development + testing

---

#### 3.3 PO File Parser Utility

**File:** `scripts/parse_transifex_po.py`

**Purpose:** Extract UI strings from KoboToolbox PO files and generate markdown reference

**Features:**
- Parse PO files from form-builder-translations repository
- Extract msgid/msgstr pairs
- Filter for UI-relevant strings (exclude technical/developer strings)
- Categorize by UI element type
- Generate markdown table format
- Include context from PO file comments

**Pseudocode:**
```python
#!/usr/bin/env python3
"""
Parse KoboToolbox Transifex PO files and extract UI strings.

Usage:
    python scripts/parse_transifex_po.py --repo-path /path/to/form-builder-translations
    python scripts/parse_transifex_po.py --repo-path ../form-builder-translations --output skills/kobo-translation/references/transifex-ui-strings.md
    python scripts/parse_transifex_po.py --help

Requirements:
    - polib: pip install polib
    - form-builder-translations repository cloned locally
"""

import polib
import re
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime

# UI-relevant string patterns (to filter out technical strings)
UI_PATTERNS = [
    r'^[A-Z][a-z]+',  # Title case (likely buttons/labels)
    r'^[A-Z]+$',      # All caps (likely tabs/sections)
    r'\.\.\.$',       # Ends with ellipsis (menu items)
]

# Technical string patterns to EXCLUDE
EXCLUDE_PATTERNS = [
    r'^%\(',          # Python format strings
    r'^\{\w+\}',      # Template variables
    r'\$\{',          # JavaScript template literals
    r'^[a-z_]+$',     # Snake_case (likely variable names)
    r'^\/',           # Paths
]

def is_ui_string(msgid: str) -> bool:
    """Determine if string is likely a UI element"""
    # Exclude technical patterns
    for pattern in EXCLUDE_PATTERNS:
        if re.search(pattern, msgid):
            return False
    
    # Check for UI patterns
    for pattern in UI_PATTERNS:
        if re.search(pattern, msgid):
            return True
    
    # Additional heuristics
    if len(msgid.split()) <= 5 and msgid[0].isupper():
        return True
    
    return False

def categorize_ui_string(msgid: str, context: str = '') -> str:
    """Categorize UI string by type"""
    msgid_lower = msgid.lower()
    
    if msgid.isupper() and len(msgid) < 20:
        return 'Navigation Tabs'
    elif any(word in msgid_lower for word in ['click', 'button', 'submit', 'save', 'delete']):
        return 'Buttons & Actions'
    elif any(word in msgid_lower for word in ['menu', 'option', 'select']):
        return 'Menus & Options'
    elif any(word in msgid_lower for word in ['dialog', 'message', 'confirm', 'warning', 'error']):
        return 'Dialogs & Messages'
    elif any(word in msgid_lower for word in ['settings', 'preferences', 'configuration']):
        return 'Settings'
    else:
        return 'General UI'

def parse_po_file(po_path: Path) -> List[Tuple[str, str, str]]:
    """
    Parse PO file and extract UI strings
    
    Returns:
        List of (msgid, msgstr, context) tuples
    """
    po = polib.pofile(str(po_path))
    ui_strings = []
    
    for entry in po:
        if entry.msgid and entry.msgstr and not entry.obsolete:
            # Check if it's a UI string
            if is_ui_string(entry.msgid):
                context = entry.comment or ''
                ui_strings.append((entry.msgid, entry.msgstr, context))
    
    return ui_strings

def extract_all_languages(repo_path: Path) -> Dict[str, Dict[str, str]]:
    """
    Extract UI strings from all language PO files
    
    Returns:
        Dict mapping language code to {msgid: msgstr}
    """
    languages = {'es': 'Spanish', 'fr': 'French', 'ar': 'Arabic'}
    all_translations = {}
    
    for lang_code in languages.keys():
        po_file = repo_path / lang_code / 'LC_MESSAGES' / 'djangojs.po'
        if not po_file.exists():
            print(f"Warning: {po_file} not found")
            continue
        
        ui_strings = parse_po_file(po_file)
        all_translations[lang_code] = {msgid: msgstr for msgid, msgstr, _ in ui_strings}
        print(f"Extracted {len(ui_strings)} UI strings from {lang_code}")
    
    return all_translations

def generate_markdown(translations: Dict[str, Dict[str, str]], 
                      output_path: Path = None) -> str:
    """
    Generate markdown reference file from translations
    """
    # Get all unique English strings across all languages
    all_msgids = set()
    for lang_translations in translations.values():
        all_msgids.update(lang_translations.keys())
    
    # Sort and categorize
    categorized = {}
    for msgid in sorted(all_msgids):
        category = categorize_ui_string(msgid)
        if category not in categorized:
            categorized[category] = []
        
        row = {
            'msgid': msgid,
            'es': translations.get('es', {}).get(msgid, '[Missing]'),
            'fr': translations.get('fr', {}).get(msgid, '[Missing]'),
            'ar': translations.get('ar', {}).get(msgid, '[Missing]'),
        }
        categorized[category].append(row)
    
    # Generate markdown
    markdown = f"""# Transifex UI Strings (AUTHORITATIVE)

**Source:** KoboToolbox form-builder-translations repository  
**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}  
**Sync Frequency:** Automated biweekly (1st and 15th of month)  
**Priority:** HIGHEST - Use these translations exactly as shown  

⚠️ **USAGE RULE:** When translating documentation that mentions ANY UI element,
you MUST use EXACTLY these translations character-for-character.

---

"""
    
    for category, strings in categorized.items():
        markdown += f"\n## {category}\n\n"
        markdown += "| English UI String | French (Transifex) | Spanish (Transifex) | Arabic (Transifex) |\n"
        markdown += "|-------------------|-------------------|---------------------|-------------------|\n"
        
        for row in strings:
            markdown += f"| {row['msgid']} | {row['fr']} | {row['es']} | {row['ar']} |\n"
    
    markdown += "\n---\n\n"
    markdown += f"**Total UI strings:** {len(all_msgids)}  \n"
    markdown += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}  \n"
    markdown += f"**Source repository:** https://github.com/kobotoolbox/form-builder-translations/  \n"
    
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding='utf-8')
        print(f"\n✅ Generated {output_path}")
    
    return markdown

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Parse KoboToolbox Transifex PO files and extract UI strings'
    )
    parser.add_argument(
        '--repo-path', '-r',
        type=Path,
        required=True,
        help='Path to form-builder-translations repository'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        default=Path('skills/kobo-translation/references/transifex-ui-strings.md'),
        help='Output markdown file path'
    )
    
    args = parser.parse_args()
    
    if not args.repo_path.exists():
        print(f"Error: Repository path not found: {args.repo_path}")
        print("\nClone it with:")
        print("  git clone https://github.com/kobotoolbox/form-builder-translations.git")
        return 1
    
    print(f"Parsing PO files from {args.repo_path}...\n")
    translations = extract_all_languages(args.repo_path)
    
    print(f"\nGenerating markdown reference...")
    generate_markdown(translations, args.output)
    
    print(f"\n✅ Done! Review {args.output} and adjust categorization as needed.")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
```

**Setup & Usage:**

```bash
# Install dependencies
pip install polib

# Clone KoboToolbox translations repository
cd ..
git clone https://github.com/kobotoolbox/form-builder-translations.git
cd kobo-translation-test

# Run parser
python scripts/parse_transifex_po.py \
    --repo-path ../form-builder-translations \
    --output skills/kobo-translation/references/transifex-ui-strings.md

# Review output
cat skills/kobo-translation/references/transifex-ui-strings.md

# Manually adjust categorization and context as needed
vim skills/kobo-translation/references/transifex-ui-strings.md
```

**Benefits:**
- ✅ Fully automated extraction from PO files
- ✅ Automatic categorization by UI element type
- ✅ Easy to re-run when translations update
- ✅ No manual copy-paste from Transifex web interface
- ✅ Consistent with KoboToolbox's actual translation workflow

**Time Estimate:** 4-6 hours development + testing

---

### Phase 4: Update Language-Specific Skills

**Action:** Regenerate language-specific skills with new Transifex reference

**Files:** `skills/kobo-translation-{es,fr,ar}/references/transifex-ui-strings.md`

**Process:**

1. Copy populated `transifex-ui-strings.md` to base skill:
   ```bash
   cp transifex-ui-strings.md skills/kobo-translation/references/
   ```

2. Filter for each language using existing `split_skill_by_language.py`:
   ```bash
   python scripts/split_skill_by_language.py
   ```

3. Verify output:
   ```bash
   # Spanish skill should only have Spanish column
   cat skills/kobo-translation-es/references/transifex-ui-strings.md
   
   # French skill should only have French column
   cat skills/kobo-translation-fr/references/transifex-ui-strings.md
   
   # Arabic skill should only have Arabic column
   cat skills/kobo-translation-ar/references/transifex-ui-strings.md
   ```

**Note:** The `split_skill_by_language.py` script already handles filtering markdown tables by language. You may need to update it slightly to handle the new file, but the core logic should work as-is.

**Time Estimate:** 30 minutes

---

### Phase 5: Testing & Validation

**Action:** Verify the integration works correctly

#### 5.1 Manual Testing

1. **Create test document** with UI elements:
   ```markdown
   # Test Document
   
   1. Click the **Deploy** button to publish your form.
   2. Navigate to the **FORM** tab.
   3. Click **Save** to save your changes.
   4. Go to the **DATA** tab to view submissions.
   ```

2. **Translate with updated skill**:
   ```bash
   python scripts/translation_agent.py \
       --file docs/en/test_ui_elements.md \
       --language es \
       --test
   ```

3. **Verify Transifex terms used**:
   - Check that "Deploy" → "DESPLEGAR"
   - Check that "FORM" → "FORMULARIO"
   - Check that "Save" → "GUARDAR"
   - Check that "DATA" → "DATOS"

4. **Compare with Transifex**:
   - Open KoboToolbox in Spanish
   - Verify button/tab names match exactly

#### 5.2 Automated Testing

Create test suite: `tests/test_transifex_integration.py`

```python
#!/usr/bin/env python3
"""
Test that Transifex integration is working correctly
"""

def test_transifex_file_exists():
    """Verify transifex-ui-strings.md exists"""
    pass

def test_transifex_file_has_content():
    """Verify file has actual translations"""
    pass

def test_skill_references_transifex():
    """Verify SKILL.md mentions transifex-ui-strings.md"""
    pass

def test_translation_uses_transifex_terms():
    """Verify translations use Transifex strings"""
    # Translate test doc with UI elements
    # Parse output
    # Verify Transifex terms were used
    pass

def test_language_specific_skills_filtered():
    """Verify language-specific skills only have one language"""
    # Check es skill only has Spanish column
    # Check fr skill only has French column
    # Check ar skill only has Arabic column
    pass
```

**Run tests:**
```bash
pytest tests/test_transifex_integration.py -v
```

**Time Estimate:** 2-3 hours

---

## Implementation Checklist

### Approach C: Hybrid with Templates (RECOMMENDED)

#### Phase 0: Template System (NEW)

- [ ] **0.1:** Create `resolve_ui_templates.py` script
- [ ] **0.2:** Integrate with `translation_agent.py`
- [ ] **0.3:** Write template usage guidelines
- [ ] **0.4:** Create template catalog for common UI terms
- [ ] **0.5:** Test with sample documents

**Estimated Time:** 6-9 hours

#### Phase 1: Transifex Reference (Fallback for LLM)

- [ ] **1.1:** Create `parse_transifex_po.py` script (PO file parser)
- [ ] **1.2:** Clone form-builder-translations repository
- [ ] **1.3:** Run parser to generate `transifex-ui-strings.md`
- [ ] **1.4:** Review and refine categorization
- [ ] **1.5:** Populate template catalog from extracted terms

**Estimated Time:** 4-6 hours

#### Phase 2: Update Translation Skills

- [ ] **2.1:** Update `SKILL.md` with template usage instructions
- [ ] **2.2:** Update `SKILL.md` with Transifex reference priority
- [ ] **2.3:** Add examples showing template + LLM mix
- [ ] **2.4:** Update decision tree with template-first logic
- [ ] **2.5:** Regenerate language-specific skills

**Estimated Time:** 2-3 hours

#### Phase 3: Automation & Validation

- [ ] **3.1:** Create validation script for unresolved templates
- [ ] **3.2:** Create validation script for UI term consistency
- [ ] **3.3:** Add template resolution to GitHub Actions
- [ ] **3.4:** Set up monitoring for form-builder-translations updates

**Estimated Time:** 6-8 hours

#### Phase 4: Documentation & Training

- [ ] **4.1:** Document template syntax and guidelines
- [ ] **4.2:** Create examples for common scenarios
- [ ] **4.3:** Add templates to existing critical docs
- [ ] **4.4:** Train writers on when to use templates

**Estimated Time:** 3-4 hours

#### Phase 5: Testing & Rollout

- [ ] **5.1:** Test with sample documents (templates + narrative)
- [ ] **5.2:** Verify against actual UI in all languages
- [ ] **5.3:** Compare with non-template translations
- [ ] **5.4:** Gradual rollout to existing documentation

**Estimated Time:** 4-6 hours

**Total Estimated Time (Approach C):** 25-36 hours

---

### Alternative: Approach B Only (Reference-Based, No Templates)

If you prefer to skip the template system and rely purely on LLM + reference:

- [ ] **Phase 1:** Create `transifex-ui-strings.md` (4-6 hours)
- [ ] **Phase 2:** Update `SKILL.md` with Transifex priority (2-3 hours)
- [ ] **Phase 3:** Create validation script (4-6 hours)
- [ ] **Phase 4:** Test with sample documents (2-3 hours)

**Total Estimated Time (Approach B):** 12-18 hours

**Trade-off:** Faster to implement, but less guaranteed accuracy for UI terms

---

## Maintenance Plan

### Weekly (During Active Development)

- Monitor translation quality for UI elements
- Check for new UI strings added to Transifex
- Validate critical documentation pages

### Monthly

- Check form-builder-translations repo for updates (or set up GitHub notifications)
- Re-run PO parser if updates detected
- Run validation script across all languages
- Review and fix any mismatches
- Update timestamp in reference file

### Quarterly

- Comprehensive review of Transifex reference file
- Manual verification against actual UI
- Update any deprecated or changed terms
- Clean up unused entries

### On-Demand

- **Before major releases:** Pull latest from form-builder-translations and validate
- **When UI changes:** Check form-builder-translations for updates (after biweekly sync)
- **When issues reported:** Spot-check specific terms against latest PO files

---

## Success Metrics

### Immediate Outcomes

✅ Transifex reference file created and populated  
✅ SKILL.md updated with clear priority hierarchy  
✅ Language-specific skills regenerated  
✅ Test translations use correct Transifex terms  

### Medium-Term Goals (1-3 months)

✅ Zero UI terminology mismatches in new translations  
✅ Reduced user confusion about button/menu names  
✅ Streamlined workflow for UI string updates  
✅ Documented process for Transifex integration  

### Long-Term Vision (3-6 months)

✅ Automated monitoring of form-builder-translations updates  
✅ Validation integrated into CI/CD pipeline  
✅ Historical documentation updated with correct terms  
✅ Single source of truth for all UI translations (form-builder-translations repo)  

---

## Risk Assessment & Mitigation

### Risk: form-builder-translations format changes

**Impact:** Low  
**Likelihood:** Very Low  
**Mitigation:**
- PO file format is stable standard (gettext)
- Version control the reference file
- Parser script handles standard PO format
- Repository structure unlikely to change

### Risk: UI strings not categorized correctly

**Impact:** Medium  
**Likelihood:** Medium  
**Mitigation:**
- Include context column in reference tables
- Regular review with UI team
- Cross-reference with actual UI
- Use validation script to catch errors

### Risk: Skill file becomes too large

**Impact:** Low  
**Likelihood:** Low  
**Mitigation:**
- Already using language-specific skills
- Tables are efficient format
- Can split by category if needed
- Monitor token usage with Claude API

### Risk: Manual process too time-consuming

**Impact:** Medium  
**Likelihood:** Medium  
**Mitigation:**
- Start with manual approach (validate concept)
- Implement automation in Phase 3
- Prioritize most common UI elements first
- Automate incrementally

---

## Alternative Approaches Considered

### ❌ Template Variable System

**Approach:** Use `{button.deploy}` in source docs, replace during translation

**Rejected because:**
- Source docs become less readable
- Requires preprocessing pipeline
- More complex to maintain
- Doesn't fit current workflow

### ❌ Separate Translation Memory

**Approach:** Use translation memory system parallel to skill

**Rejected because:**
- Adds complexity
- Claude works better with explicit instructions
- Skill-based approach already working well
- Would require significant refactoring

### ❌ Direct Transifex API Integration

**Approach:** Query Transifex API during translation

**Rejected because:**
- Adds API call overhead
- Network dependency during translation
- Rate limiting concerns
- form-builder-translations repo provides same data without API complexity
- Static reference file is faster and more reliable

### ✅ Hybrid Approach (Selected)

**Why it works:**
- Fits existing workflow
- No preprocessing needed
- Clear priority hierarchy
- Optional automation path
- Human-readable documentation

---

## Resources & References

### Transifex Documentation

- [Transifex CLI](https://developers.transifex.com/docs/cli) (used by KPI maintainers)
- [PO File Format](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html)
- [polib Documentation](https://polib.readthedocs.io/)

### KoboToolbox-Specific

- [form-builder-translations repo](https://github.com/kobotoolbox/form-builder-translations/)
- [KoboToolbox on Transifex](https://www.transifex.com/kobotoolbox/kobotoolbox/)
- [KPI Repository](https://github.com/kobotoolbox/kpi)

### Internal Documentation

- Current translation workflow: `docs/guides/SETUP.md`
- Skill splitting logic: `scripts/split_skill_by_language.py`
- Translation agent: `scripts/translation_agent.py`

### Related Issues

- UI terminology consistency
- Documentation accuracy
- Translation quality assurance

---

## Approach Comparison

### Quick Decision Matrix

| Factor | Approach A<br/>(Templates Only) | Approach B<br/>(Reference Only) | Approach C<br/>(Hybrid) |
|--------|-------------------------------|--------------------------------|------------------------|
| **UI Term Accuracy** | 100% guaranteed | ~95% with validation | 100% for critical terms |
| **Implementation Time** | 3-4 weeks | 1-2 weeks | 2-3 weeks |
| **Writer Impact** | High - all UI terms need templates | None - natural writing | Low - optional templates |
| **Maintenance** | Low - auto-updates | Medium - periodic validation | Low - auto for templates |
| **English Readability** | Poor - many placeholders | Perfect - no special syntax | Good - minimal placeholders |
| **Breaking Changes** | Yes - convert all docs | No - drop-in addition | No - gradual adoption |
| **Error Risk** | Zero (template fails = visible) | Low (LLM might miss term) | Zero for templated terms |
| **Developer Familiar** | ✅ Same as `t()` pattern | ❌ Different approach | ✅ Similar to `t()` |

### Recommendation by Use Case

**Choose Approach B (Reference Only) if:**
- ⚡ Need quick implementation (1-2 weeks)
- 📝 Writers prefer no new syntax
- 🎯 Acceptable to have ~95% accuracy with periodic validation
- 🔄 Comfortable with LLM-based translation

**Choose Approach C (Hybrid) if:**
- ✅ Want guaranteed accuracy for critical UI terms
- 🎨 Balance between automation and control
- 📚 Willing to train writers on selective template use
- 🔧 Appreciate similarity to frontend `t()` pattern
- ⏱️ Can invest 2-3 weeks implementation

**Choose Approach A (Templates Only) if:**
- 🎯 Require 100% guaranteed accuracy for ALL UI terms
- 🔒 Zero tolerance for UI terminology errors
- ⚡ Have resources for full doc conversion
- 📝 Writers are technical and comfortable with templates

### KoboToolbox Recommendation

**Start with Approach C (Hybrid):**

1. **Week 1-2:** Build template system + PO parser
2. **Week 2-3:** Add templates to highest-impact docs (getting started, tutorials)
3. **Month 2-3:** Evaluate results, expand template usage
4. **Month 3-6:** Gradually templatize critical docs, use reference for rest

**Benefits:**
- Best of both worlds: guaranteed accuracy where needed, natural text elsewhere
- Incremental adoption reduces risk
- Similar pattern to frontend development
- Can fall back to reference-only if templates prove problematic

---

## Questions & Decisions Needed

### Before Starting Implementation

1. ✅ **Which resource(s)** contain the UI strings we need?
   - Answer: `djangojs.po` for frontend UI, `django.po` for backend (in form-builder-translations repo)
2. ✅ **What format** is easiest to work with?
   - Answer: PO files from form-builder-translations repository
3. ✅ **How often** should we sync?
   - Answer: Monitor form-builder-translations repo for updates (automated biweekly on 1st and 15th)
4. **Who has access** to form-builder-translations repository?
5. **Which UI elements are highest priority** to include first?
   - Answer: Main navigation tabs, primary action buttons (Deploy, Save, Submit), Form builder UI

### During Implementation

1. Should we validate existing translated docs against reference?
2. How should we handle deprecated UI strings?
3. What's the threshold for auto-fixing vs. manual review?
4. Should validation be blocking or just warnings?
5. **What's the best way to monitor** form-builder-translations for updates?
   - GitHub watch/notifications vs. manual checks vs. automated script

### Post-Implementation

1. Who owns maintaining the reference file?
2. What's the process for adding new UI strings when form-builder-translations updates?
3. How do we communicate UI changes to doc team?
4. Should we automate retranslation when form-builder-translations updates?
5. How often should we pull latest from form-builder-translations?

---

## Next Steps

### Immediate Actions (This Week)

**Decision Point:** Choose between Approach B (reference-only) or Approach C (templates + reference)

**For Approach C (Recommended):**

1. **Clone form-builder-translations repository** from GitHub
2. **Install dependencies** (`pip install polib`)
3. **Create template resolver prototype** - Test with 5-10 common UI terms
4. **Test template resolution** on sample document
5. **Review with team** - Does template syntax work for writers?
6. **Decide on adoption strategy** - Gradual or immediate?

**For Approach B (Simpler):**

1. **Clone form-builder-translations repository** from GitHub
2. **Install PO file parser dependencies** (`pip install polib`)
3. **Create PO parser script** or manually extract 10-20 common UI strings
4. **Create `transifex-ui-strings.md`** with extracted strings
5. **Update SKILL.md** with Transifex priority
6. **Test translation** with sample document

### Short-Term (Next 2 Weeks)

1. **Complete PO parser script** (Phase 3.3)
2. **Run parser on full djangojs.po files** for all languages
3. **Review and refine auto-generated reference file**
4. **Update SKILL.md** with priority hierarchy
5. **Regenerate language-specific skills**
6. **Test on real documentation**

### Medium-Term (Next Month)

1. **Implement validation script** (optional)
2. **Set up monitoring for form-builder-translations updates** (GitHub watch/notifications)
3. **Create workflow for pulling updates** when form-builder-translations changes
4. **Document workflow** for team
5. **Train team members** on new process

### Long-Term (Next Quarter)

1. **Implement automation scripts** (optional)
2. **Integrate into CI/CD**
3. **Audit existing translations**
4. **Measure impact on quality**

---

## Appendix

### Sample PO File Structure

Example from `djangojs.po`:

```po
# KoboToolbox Frontend UI Strings
msgid ""
msgstr ""
"Content-Type: text/plain; charset=UTF-8\n"

#: jsapp/js/components/formBuilder.js:123
msgid "Deploy"
msgstr "DESPLEGAR"  # Spanish
# msgstr "DÉPLOYER"  # French
# msgstr "[Arabic]"  # Arabic

#: jsapp/js/components/formBuilder.js:456
msgid "Save"
msgstr "GUARDAR"  # Spanish

#: jsapp/js/components/header.js:78
msgid "FORM"
msgstr "FORMULARIO"  # Spanish

#: jsapp/js/components/header.js:89
msgid "DATA"
msgstr "DATOS"  # Spanish
```

**Note:** Each language has its own PO file:
- `es/LC_MESSAGES/djangojs.po` - Spanish translations
- `fr/LC_MESSAGES/djangojs.po` - French translations  
- `ar/LC_MESSAGES/djangojs.po` - Arabic translations

### Sample UI Element Categories

Suggested groupings for reference file:

1. **Core Actions** - Deploy, Save, Submit, Cancel, Delete
2. **Navigation** - Tabs, menus, breadcrumbs
3. **Form Builder** - Question types, settings, validations
4. **Data Management** - Submissions, exports, reports
5. **Settings** - User preferences, project settings
6. **Mobile App** - KoboCollect specific UI
7. **Dialogs & Messages** - Confirmations, errors, warnings

### Integration with Existing Scripts

The `split_skill_by_language.py` script should handle the new file automatically:

```python
# Current logic in split_skill_by_language.py already handles:
ref_files = {
    'brand': 'brand-terminology.md',
    'ui': 'ui-terminology.md',
    'data': 'data-collection-terms.md',
    # ... other files
}

# Simply add:
ref_files = {
    'transifex': 'transifex-ui-strings.md',  # New!
    'brand': 'brand-terminology.md',
    'ui': 'ui-terminology.md',
    # ... rest
}
```

No changes needed to `translation_agent.py` - it loads all reference files automatically.

---

---

## Real-World Example: Hybrid Approach in Action

### English Source Document (with Templates)

```markdown
# Getting Started with KoboToolbox

To create your first form, click the {{ui:NEW|bold}} button on your project list.

## Creating a Form

1. Select {{ui:Build_from_scratch}} to start with a blank form
2. Add questions using the question panel on the left
3. Click {{ui:Save|bold}} frequently to save your work
4. When ready, navigate to the {{ui:FORM}} tab

## Publishing Your Form

Once your form is complete, click the {{ui:Deploy|bold}} button. This will 
make your form available for data collection through:

- Web forms (Enketo)
- Mobile app (KoboCollect)
- API integration

## Viewing Data

After collecting responses, go to the {{ui:DATA}} tab to:
- View submissions in table or map format
- Edit or delete individual responses
- Export data for analysis
```

### What Happens During Translation (Spanish)

**Step 1: Template Resolution**
```markdown
# Getting Started with KoboToolbox

To create your first form, click the **NUEVO** button on your project list.

## Creating a Form

1. Select CREAR DESDE UN BORRADOR to start with a blank form
2. Add questions using the question panel on the left
3. Click **GUARDAR** frequently to save your work
4. When ready, navigate to the FORMULARIO tab

## Publishing Your Form

Once your form is complete, click the **DESPLEGAR** button. This will 
make your form available for data collection through:

- Web forms (Enketo)
- Mobile app (KoboCollect)
- API integration

## Viewing Data

After collecting responses, go to the DATOS tab to:
- View submissions in table or map format
- Edit or delete individual responses
- Export data for analysis
```

**Step 2: LLM Translation** (of remaining text)
```markdown
# Primeros pasos con KoboToolbox

Para crear tu primer formulario, haz clic en el botón **NUEVO** en tu lista de proyectos.

## Creando un formulario

1. Selecciona CREAR DESDE UN BORRADOR para comenzar con un formulario en blanco
2. Agrega preguntas usando el panel de preguntas a la izquierda
3. Haz clic en **GUARDAR** frecuentemente para guardar tu trabajo
4. Cuando esté listo, navega a la pestaña FORMULARIO

## Publicando tu formulario

Una vez que tu formulario esté completo, haz clic en el botón **DESPLEGAR**. 
Esto hará que tu formulario esté disponible para la recolección de datos a través de:

- Formularios web (Enketo)
- Aplicación móvil (KoboCollect)
- Integración API

## Visualizando datos

Después de recolectar respuestas, ve a la pestaña DATOS para:
- Ver envíos en formato de tabla o mapa
- Editar o eliminar respuestas individuales
- Exportar datos para análisis
```

### Key Observations

✅ **Templates resolved correctly:**
- `{{ui:NEW|bold}}` → `**NUEVO**`
- `{{ui:Deploy|bold}}` → `**DESPLEGAR**`
- `{{ui:FORM}}` → `FORMULARIO`
- `{{ui:DATA}}` → `DATOS`

✅ **Natural translation for narrative:**
- "To create your first form" → "Para crear tu primer formulario"
- "Add questions using the panel" → "Agrega preguntas usando el panel"
- Context-aware phrasing maintained

✅ **Zero ambiguity for UI terms:**
- LLM cannot mistranslate button names
- Guaranteed to match actual KoboToolbox interface
- Writers can verify templates against UI before publishing

✅ **Minimal impact on source readability:**
- Only ~8 templates in entire article
- Bulk of content is natural English
- Easy to read and understand

---

**Document Version:** 1.0  
**Last Updated:** 10 December 2025  
**Author:** GitHub Copilot  
**Status:** Ready for Implementation
