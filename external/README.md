# External Dependencies

This directory contains external repositories integrated as git submodules.

## form-builder-translations

**Repository:** https://github.com/kobotoolbox/form-builder-translations/

**Purpose:** Contains official Transifex UI translations for KoboToolbox in PO file format

**Languages:** Spanish (es), French (fr), Arabic (ar)

**Update Frequency:** Automated biweekly (1st and 15th of each month)

### Setup

To clone this repository with submodules:

```bash
git clone --recursive <this-repo-url>
```

If you already cloned without `--recursive`:

```bash
git submodule init
git submodule update
```

### Manual Update Workflow

When KoboToolbox updates UI translations (check after 1st and 15th of month):

```bash
# Navigate to submodule
cd external/form-builder-translations

# Pull latest translations
git pull origin main

# Return to parent repo
cd ../..

# Commit the updated submodule reference
git add external/form-builder-translations
git commit -m "Update Transifex translations to latest"

# Regenerate transifex-ui-strings.md reference
python scripts/parse_transifex_po.py \
    --repo-path external/form-builder-translations \
    --output skills/kobo-translation/references/transifex-ui-strings.md
```

### Troubleshooting

If the submodule directory is empty:

```bash
git submodule update --init --recursive
```

To check submodule status:

```bash
git submodule status
```
