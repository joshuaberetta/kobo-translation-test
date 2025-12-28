# Quick Start: Transifex UI Template System

Get started with the hybrid UI template translation system in 5 minutes.

## Prerequisites

- Python 3.8+
- Git
- Anthropic API key (for translation agent)

## Step 1: Install Dependencies

```bash
pip install -r scripts/requirements.txt
```

This installs:
- `polib` - For parsing Transifex PO files
- `anthropic` - For Claude API
- `PyGithub` - For GitHub integration (optional)
- `python-dotenv` - For environment variables

## Step 2: Initialize Transifex Submodule

```bash
# Add the submodule
git submodule add https://github.com/kobotoolbox/form-builder-translations.git external/form-builder-translations

# Initialize and update
git submodule update --init --recursive

# Verify it's there
ls external/form-builder-translations/es/LC_MESSAGES/djangojs.po
```

## Step 3: Generate Transifex Reference File

```bash
python scripts/parse_transifex_po.py \
    --repo-path external/form-builder-translations \
    --output skills/kobo-translation/references/transifex-ui-strings.md
```

**Expected output:**
```
📖 Parsing PO files from external/form-builder-translations...

✅ Extracted 243 UI strings from Spanish
✅ Extracted 239 UI strings from French
✅ Extracted 201 UI strings from Arabic

📝 Generating markdown reference...

✅ Generated skills/kobo-translation/references/transifex-ui-strings.md
```

## Step 4: Test Template Resolution

Create a test document:

```bash
cat > test_templates.md << 'EOF'
# Test Document

1. Click the {{ui:Deploy|bold}} button to publish your form.
2. Navigate to the {{ui:FORM}} tab.
3. Click {{ui:Save}} to save your changes.
4. Go to the {{ui:DATA}} tab to view your submissions.
5. Use {{ui:Cancel transfer}} to abort the transfer.

This is regular text that doesn't need templates.
Note: Template keys support spaces, underscores, and hyphens.
EOF
```

Resolve templates for Spanish:

```bash
python scripts/resolve_ui_templates.py \
    --input test_templates.md \
    --language es \
    --po-repo external/form-builder-translations
```

**Expected output:**
```
✅ Loaded 2650 translations from djangojs.po
📄 Reading test_templates.md...
🔄 Found 5 templates, resolving...

✅ Resolved templates written to test_templates_resolved.md

✅ All templates resolved successfully
```

Check the result:

```bash
cat test_templates_resolved.md
```

**Should show:**
```markdown
# Test Document

1. Click the **DESPLEGAR** button to publish your form.
2. Navigate to the FORMULARIO tab.
3. Click GUARDAR to save your changes.
4. Go to the DATOS tab to view your submissions.
5. Use Cancelar transferencia to abort the transfer.

This is regular text that doesn't need templates.
Note: Template keys support spaces, underscores, and hyphens.
```
```

## Step 5: Test with Translation Agent

Translate the resolved document:

```bash
python scripts/translation_agent.py \
    --file test_templates_resolved.md \
    --language es \
    --test \
    --save
```

Or translate with template resolution built-in:

```bash
python scripts/translation_agent.py \
    --file test_templates.md \
    --language es \
    --use-templates \
    --po-repo external/form-builder-translations \
    --test \
    --save
```

**What happens:**
1. Templates are resolved first (Deploy → DESPLEGAR, etc.)
2. Resolved content is sent to LLM for translation
3. LLM translates narrative text naturally
4. Output combines exact UI terms with natural flow

## Common Usage Patterns

### Pattern 1: Translate with Templates

```bash
python scripts/translation_agent.py \
    --file docs/en/getting_started.md \
    --language es \
    --use-templates \
    --save
```

### Pattern 2: Resolve Templates Only (No Translation)

```bash
python scripts/resolve_ui_templates.py \
    -i docs/en/article.md \
    -l fr \
    -p external/form-builder-translations \
    -o docs/en/article_fr_resolved.md
```

### Pattern 3: Update Transifex Reference

```bash
# Pull latest translations
cd external/form-builder-translations
git pull origin main
cd ../..

# Regenerate reference
python scripts/parse_transifex_po.py \
    --repo-path external/form-builder-translations

# Commit updated submodule
git add external/form-builder-translations
git commit -m "Update Transifex translations"
```

### Pattern 4: Test Unresolved Templates

```bash
# Create test with bad template
echo 'Click {{ui:BadKey}} button' > test_bad.md

# Try to resolve
python scripts/resolve_ui_templates.py \
    -i test_bad.md -l es -p external/form-builder-translations
```

**Expected warning:**
```
⚠️  1 unresolved templates (left in output):
  - {{ui:BadKey}} (key: BadKey)

💡 To fix: Either add these strings to Transifex or fix template keys.
```

### Pattern 5: Strict Mode (Fail on Unresolved)

```bash
# Will exit with error code 1 if templates don't resolve
python scripts/resolve_ui_templates.py \
    -i docs/en/article.md \
    -l es \
    -p external/form-builder-translations \
    --strict
```

## Updating the System

### When Transifex Updates (Biweekly)

KoboToolbox updates translations on the 1st and 15th of each month:

```bash
# 1. Update submodule
cd external/form-builder-translations
git pull origin main
cd ../..

# 2. Regenerate reference
python scripts/parse_transifex_po.py \
    --repo-path external/form-builder-translations

# 3. Commit changes
git add external/form-builder-translations skills/kobo-translation/references/transifex-ui-strings.md
git commit -m "Update Transifex UI strings - $(date +%Y-%m-%d)"

# 4. Retranslate docs with new terms (optional)
python scripts/bulk_retranslate.py
```

## Troubleshooting

### Problem: "PO file not found"

**Error:**
```
❌ Error: PO repository not found: external/form-builder-translations
```

**Solution:**
```bash
git submodule update --init --recursive
```

### Problem: "polib module not found"

**Error:**
```
ModuleNotFoundError: No module named 'polib'
```

**Solution:**
```bash
pip install polib
# or
pip install -r scripts/requirements.txt
```

### Problem: Templates not resolving

**Symptom:**
```
⚠️  3 unresolved templates:
  - {{ui:Deploy}} (key: Deploy)
```

**Checks:**
1. Is submodule initialized? `ls external/form-builder-translations/`
2. Is PO file there? `ls external/form-builder-translations/es/LC_MESSAGES/djangojs.po`
3. Is key spelled correctly? Check `skills/kobo-translation/references/transifex-ui-strings.md`
4. Case-sensitive match: `Deploy` not `deploy`, `FORM` not `form`
5. Exact text match: Use the exact UI text including spaces, e.g., `Cancel transfer` not `Cancel_transfer`

### Problem: Reference file empty or missing

**Solution:**
```bash
# Regenerate
python scripts/parse_transifex_po.py \
    --repo-path external/form-builder-translations \
    --output skills/kobo-translation/references/transifex-ui-strings.md

# Verify
cat skills/kobo-translation/references/transifex-ui-strings.md | head -20
```

## Next Steps

1. **Read the writer guide:** [docs/guides/UI_TEMPLATE_GUIDE.md](docs/guides/UI_TEMPLATE_GUIDE.md)
2. **Review the reference:** [skills/kobo-translation/references/transifex-ui-strings.md](skills/kobo-translation/references/transifex-ui-strings.md)
3. **Add templates to docs:** Start with high-priority getting started guides
4. **Test translations:** Compare output with actual UI
5. **Set up monitoring:** Watch form-builder-translations repo on GitHub

## Help

- **Template Guide:** `docs/guides/UI_TEMPLATE_GUIDE.md`
- **Implementation Details:** `IMPLEMENTATION_SUMMARY.md`
- **Integration Plan:** `docs/guides/TRANSIFEX_INTEGRATION_PLAN.md`
- **Submodule README:** `external/README.md`
