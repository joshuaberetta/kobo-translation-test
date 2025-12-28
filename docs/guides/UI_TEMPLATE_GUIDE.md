# UI Template Guide

**Guide for Documentation Writers**  
**Last Updated:** 28 December 2025

## Overview

This guide explains how to use **UI term templates** in KoboToolbox documentation to ensure translated UI elements (buttons, tabs, menus) match the actual interface exactly.

## What are UI Templates?

UI templates are placeholders in English documentation that get replaced with exact Transifex translations during the translation process.

**Syntax:** `{{ui:KEY}}` or `{{ui:KEY|formatting}}`

**Example:**
```markdown
Click the {{ui:Deploy|bold}} button to publish your form.
```

**Spanish output:**
```markdown
Haz clic en el botón **DESPLEGAR** para publicar tu formulario.
```

---

## When to Use Templates

### ✅ USE templates for:

- **Navigation tabs** - FORM, DATA, SUMMARY, SETTINGS, etc.
- **Action buttons** - Deploy, Save, Submit, Delete, Edit, Cancel
- **Menu items** - New, Download, Export, Import, Share
- **Dialog titles** - Confirm, Success, Error, Warning
- **Settings names** - Server, Username, Password
- **Any term** you want to guarantee matches the UI exactly

### ❌ DON'T USE templates for:

- **General concepts** - Even if related to UI features
- **Explanatory text** - Instructions and guidance
- **Examples and scenarios** - Narrative content
- **Descriptive paragraphs** - Conceptual descriptions
- **Technical terms** - Unless they appear verbatim in UI

---

## Template Syntax

### Basic Template

```markdown
{{ui:Deploy}}
```

Replaces with the translated string for "Deploy" (e.g., "DESPLEGAR" in Spanish).

**Key characteristics:**
- **Case-insensitive:** `{{ui:Deploy}}`, `{{ui:deploy}}`, and `{{ui:DEPLOY}}` all work the same
- **Special characters supported:** Parentheses, slashes, periods, commas, etc. are all allowed
- **Examples:** `{{ui:Barcode / QR Code}}`, `{{ui:Online-Offline (multiple submission)}}`, `{{ui:Failed to get submission.}}`

### With Formatting

Add `|format` to apply markdown formatting. You can combine multiple formats with commas:

```markdown
{{ui:Deploy|bold}}         → **DESPLEGAR**
{{ui:FORM|code}}           → `FORMULARIO`
{{ui:Save|italic}}         → *GUARDAR*
{{ui:deploy|upper}}        → IMPLEMENTAR (case-insensitive + uppercase)
{{ui:data|upper,bold}}     → **DATOS** (uppercase then bold)
```

**Supported formats:**
- `bold` - Wrap in `**text**`
- `italic` - Wrap in `*text*`
- `code` - Wrap in `` `text` ``
- `upper` - Convert to UPPERCASE (applied first)
- `lower` - Convert to lowercase (applied first)

**Multiple formats:** Separate with commas. Case transformations (`upper`/`lower`) are applied before markdown wrapping (`bold`/`italic`/`code`).

**Example:** `{{ui:form|upper,bold}}` → first uppercase "FORMULARIO", then wrap in bold → `**FORMULARIO**`

### Multi-word Terms

Multi-word UI strings can use either spaces or underscores:

```markdown
{{ui:Save Draft}}          → GUARDAR BORRADOR (spaces work!)
{{ui:Save_Draft}}          → GUARDAR BORRADOR (underscores also work)
{{ui:save draft|upper}}    → GUARDAR BORRADOR (case-insensitive!)
{{ui:Start new form}}      → INICIAR NUEVO FORMULARIO
{{ui:Question Library}}    → LA BIBLIOTECA DE PREGUNTAS
{{ui:Cancel transfer}}     → Cancelar transferencia (Spanish)
```

**Best Practice:** Use the exact text as it appears in the KoboToolbox UI, including spaces. Check the [transifex-ui-strings.md](../skills/kobo-translation/references/transifex-ui-strings.md) reference to find the correct key.

### Variable Placeholders

Some Transifex strings contain variable placeholders like `##VAR##`. The system handles two types:

**1. UI Term Placeholders (ALL_CAPS) - Automatically Replaced:**
```markdown
{{ui:Export ##SELECT_MANY## questions as…}}
→ Spanish: "Exportar preguntas Seleccionar varias como..."
→ ##SELECT_MANY## is replaced with "Seleccionar varias"

{{ui:cloned ##ASSET_TYPE## created}}
→ Spanish: "Asset Type clonado creado"
→ ##ASSET_TYPE## is replaced (or made readable if no translation)
```

**2. Dynamic Value Placeholders (snake_case/lowercase) - Preserved:**
```markdown
{{ui:##field_label## (required)}}
→ Spanish: "##field_label## (obligatorio)"
→ ##field_label## is kept for runtime substitution

{{ui:##count## characters left}}
→ Spanish: "##count## caracteres disponibles"
→ ##count## is kept for runtime substitution
```

**How it works:**
- **ALL_CAPS** patterns (e.g., `##SELECT_MANY##`, `##ASSET_TYPE##`) are UI terms → replaced with translations
- **snake_case/lowercase** patterns (e.g., `##count##`, `##username##`, `##field_label##`) are dynamic values → preserved for runtime

**Common UI term placeholders:**
- `##SELECT_MANY##` → Select Many question type
- `##ASSET_TYPE##` → Asset type name
- `##QUESTION_TYPE##` → Question type

**Common dynamic placeholders (preserved):**
- `##count##`, `##number##` → Numeric values
- `##username##`, `##username_list##` → User information  
- `##field_label##`, `##fileName##` → Dynamic text
- `##date##`, `##timestamp##` → Time values

---

## Examples

### Good: Mix of Templates and Natural Text

```markdown
To publish your form, click the {{ui:Deploy|bold}} button on the 
{{ui:FORM}} tab. This will make your form available for data collection 
across all your devices.

Navigate to the {{ui:DATA}} tab to view your submissions. You can filter,
edit, and export the data from this interface.
```

**Why this works:**
- UI elements (Deploy, FORM, DATA) use templates → guaranteed accuracy
- Narrative text ("This will make your form available...") stays natural → better readability
- Balance between precision and clarity

### Bad: Too Many Templates

```markdown
{{ui:To}} {{ui:publish}} {{ui:your}} {{ui:form}}, {{ui:click}} 
{{ui:the}} {{ui:Deploy}} {{ui:button}}.
```

**Why this is wrong:**
- Common words aren't UI elements
- Makes source docs unreadable
- These words aren't in Transifex PO files
- Templates will be left unresolved (warnings)

### Bad: Missing Templates Where Needed

```markdown
Click the **Deploy** button on the FORM tab.
```

**Why this is risky:**
- "Deploy" and "FORM" are UI elements
- Without templates, LLM might translate differently than actual UI
- User confusion if docs say "Desplegar" but UI says "PUBLICAR"

**Should be:**
```markdown
Click the {{ui:Deploy|bold}} button on the {{ui:FORM}} tab.
```

---

## Common UI Terms

### Navigation Tabs (ALL CAPS)

```markdown
{{ui:FORM}}         → FORMULARIO
{{ui:DATA}}         → DATOS
{{ui:SUMMARY}}      → RESUMEN
{{ui:DOWNLOADS}}    → DESCARGAS
{{ui:SETTINGS}}     → CONFIGURACIÓN
{{ui:MAP}}          → MAPA
{{ui:TABLE}}        → TABLA
{{ui:REPORTS}}      → INFORMES
```

### Core Actions & Buttons

```markdown
{{ui:Deploy}}       → DESPLEGAR
{{ui:Save}}         → GUARDAR
{{ui:Submit}}       → ENVIAR
{{ui:Delete}}       → BORRAR
{{ui:Edit}}         → EDITAR
{{ui:Cancel}}       → CANCELAR
{{ui:Close}}        → CERRAR
{{ui:Add}}          → AGREGAR
{{ui:Remove}}       → ELIMINAR
{{ui:Download}}     → DESCARGAR
{{ui:Export}}       → EXPORTAR
{{ui:Import}}       → IMPORTAR
{{ui:Share}}        → COMPARTIR
{{ui:Preview}}      → VISTA PREVIA
```

### Form Builder

```markdown
{{ui:Question_Library}}     → LA BIBLIOTECA DE PREGUNTAS
{{ui:Add_Question}}         → AGREGAR PREGUNTA
{{ui:Add_Group}}            → AGREGAR GRUPO
{{ui:Question_Type}}        → TIPO DE PREGUNTA
{{ui:Required}}             → OBLIGATORIO
{{ui:Skip_Logic}}           → LÓGICA DE SALTO
{{ui:Validation}}           → VALIDACIÓN
```

### KoboCollect (Mobile App)

```markdown
{{ui:Start_new_form}}       → INICIAR NUEVO FORMULARIO
{{ui:Ready_to_send}}        → LISTO PARA ENVIAR
{{ui:Download_form}}        → DESCARGAR FORMULARIO
{{ui:Delete_form}}          → BORRAR FORMULARIO
{{ui:Finalize}}             → FINALIZAR
```

---

## Template Keys Reference

### How to Find the Correct Key

1. **Check the Transifex reference file:**
   - `skills/kobo-translation/references/transifex-ui-strings.md`
   - Look in the "English UI String" column
   - Use exact spelling and capitalization

2. **Multi-word terms:**
   - Replace spaces with underscores: "Save Draft" → `Save_Draft`
   - Keep exact capitalization: "Start new form" → `Start_new_form`

3. **Verify in PO files** (if needed):
   - Check `external/form-builder-translations/{lang}/LC_MESSAGES/djangojs.po`
   - Look for the `msgid` (English source string)
   - Use that exact string with spaces replaced by underscores

### What if a Key Doesn't Work?

If you use a template and it **doesn't resolve** (warning appears), the template is left in the translated output unchanged:

```markdown
Source:     Click the {{ui:UnknownKey}} button
Translated: Haz clic en el {{ui:UnknownKey}} botón
```

**Warning output:**
```
⚠️  1 unresolved templates (left in output):
  - {{ui:UnknownKey}} (key: UnknownKey)
```

**To fix:**
1. Check spelling and capitalization
2. Check transifex-ui-strings.md for correct key
3. If term isn't in Transifex, remove template and use natural text instead

---

## Workflow

### 1. Writing New Documentation

When writing English docs that mention UI elements:

```markdown
1. Identify UI elements (buttons, tabs, menus)
2. Wrap them in templates: {{ui:KEY|format}}
3. Use natural text for everything else
4. Preview to ensure readability
```

### 2. Translation Process

The translation system automatically:

```markdown
1. Detects templates in source markdown
2. Looks up translations in PO files
3. Replaces templates with exact Transifex strings
4. Sends resolved content to LLM for natural text translation
5. Reports any unresolved templates
```

### 3. Updating Existing Docs

When adding UI references to existing docs:

```markdown
1. Find the UI term in the text
2. Replace with template: "Deploy" → {{ui:Deploy|bold}}
3. Run translation to verify template resolves
4. Fix any unresolved templates
```

---

## Translation Command

### Without Templates (Current Method)

```bash
python scripts/translation_agent.py \\
    --file docs/en/article.md \\
    --language es \\
    --save
```

LLM translates everything, including UI terms (risk of mismatch).

### With Templates (New Method)

```bash
python scripts/translation_agent.py \\
    --file docs/en/article.md \\
    --language es \\
    --use-templates \\
    --po-repo external/form-builder-translations \\
    --save
```

1. Templates resolved first (guaranteed accuracy)
2. LLM translates remaining text (natural flow)
3. Best of both worlds

---

## Best Practices

### ✅ DO:

- Use templates for **all** UI elements that appear in the actual interface
- Apply formatting (bold/code) via templates: `{{ui:Deploy|bold}}`
- Check transifex-ui-strings.md when unsure about a key
- Test templates with `--use-templates` flag before committing
- Keep narrative text natural (no templates)

### ❌ DON'T:

- Template every word in a sentence
- Use templates for concepts or general terms
- Guess at template keys (verify in transifex-ui-strings.md)
- Mix template syntax (stick to `{{ui:KEY}}`)
- Template text that doesn't appear in UI

---

## Troubleshooting

### Problem: Template Not Resolving

**Symptom:**
```
⚠️  1 unresolved templates:
  - {{ui:MyButton}} (key: MyButton)
```

**Solutions:**
1. Check spelling: `MyButton` vs `My_Button` vs `Mybutton`
2. Verify in transifex-ui-strings.md
3. Check PO file: `external/form-builder-translations/es/LC_MESSAGES/djangojs.po`
4. If not in Transifex, remove template

### Problem: Wrong Translation

**Symptom:** Template resolves but output doesn't match UI

**Solutions:**
1. Verify you're using correct language (es/fr/ar)
2. Check transifex-ui-strings.md has correct translation
3. Update submodule: `cd external/form-builder-translations && git pull`
4. Regenerate reference: `python scripts/parse_transifex_po.py -r external/form-builder-translations`

### Problem: Too Many Warnings

**Symptom:** Many unresolved templates

**Possible causes:**
1. Using templates for non-UI text
2. Incorrect key format (spaces instead of underscores)
3. Outdated PO files (need submodule update)
4. Using terms not in Transifex (newer features)

---

## FAQ

**Q: Should I template "form" and "data"?**  
A: Only if referring to the **FORM** and **DATA** tabs. In narrative text like "your form data", no template needed.

**Q: What about brand terms like "KoboToolbox"?**  
A: Brand terms don't use templates. They're handled by brand-terminology.md reference.

**Q: Can I use templates in code blocks?**  
A: No. Code blocks are usually not translated, and templates won't resolve there.

**Q: What if a UI term isn't in Transifex yet?**  
A: Use natural text (no template) and add to ui-terminology.md as a fallback until it's in Transifex.

**Q: Do templates work for Arabic (RTL)?**  
A: Yes. The template system is language-agnostic; formatting is handled by markdown.

---

## Related Documentation

- **Transifex UI Strings Reference:** `skills/kobo-translation/references/transifex-ui-strings.md`
- **Translation Skill:** `skills/kobo-translation/SKILL.md`
- **PO Parser Script:** `scripts/parse_transifex_po.py`
- **Template Resolver:** `scripts/resolve_ui_templates.py`
- **Translation Agent:** `scripts/translation_agent.py`

---

## Need Help?

- Check transifex-ui-strings.md for available templates
- Test with `--use-templates --po-repo external/form-builder-translations`
- Look at resolved vs unresolved template warnings
- Consult actual UI in target language to verify
