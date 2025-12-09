# Bulk Retranslation Guide

This guide explains how to use the bulk retranslation feature to regenerate translations when skills are updated.

## Overview

The `bulk_retranslate.py` script allows you to:
- Retranslate all documentation files or a specific subset
- Test skill changes across your entire documentation corpus
- Compare old vs new translations to evaluate quality improvements
- Generate fresh translations for one or more target languages

## When to Use Bulk Retranslation

Use bulk retranslation when you:
- ✅ Update translation skills or terminology
- ✅ Want to test how skill changes affect translation quality
- ✅ Need to regenerate translations with updated brand terminology
- ✅ Want to compare translation quality before/after skill improvements
- ✅ Are migrating to a new translation model or approach

**⚠️ Cost Warning:** Bulk retranslation regenerates ALL translations from scratch, which can be expensive for large documentation sets. Always test on a small subset first.

## Installation

The script uses the same dependencies as the main translation agent:

```bash
cd kobo-translation-test
pip install -r scripts/requirements.txt
```

## Basic Usage

### GitHub Actions (Recommended for Teams)

The easiest way to bulk retranslate is through GitHub Actions:

1. Go to your repository on GitHub
2. Click **Actions** tab
3. Select **"Bulk Retranslate Documentation"** workflow
4. Click **"Run workflow"** button
5. Configure options:
   - **Languages:** Comma-separated list (e.g., `es,fr,ar`)
   - **Files:** Specific filenames or leave empty for mode-based selection
   - **Mode:**
     - `test` - Translate 2-3 test files only (safe for testing)
     - `specific` - Translate specific files you listed above
     - `all` - Translate ALL files (requires cost confirmation)
   - **Cost confirmation:** Check for `all` mode
6. Click **"Run workflow"**
7. Wait for completion (check Actions tab for progress)
8. Review and merge the automatically created PR

**Benefits of GitHub Actions:**
- ✅ No local setup required
- ✅ Team members can trigger without technical knowledge
- ✅ Automatic PR creation with detailed description
- ✅ Cost estimation and summary in PR
- ✅ Consistent environment (always uses latest skills)

### Local Command Line

For development and testing, use the local scripts:

#### Using Helper Script (Easiest)

```bash
# Test mode - 2 files to Spanish
./scripts/retranslate.sh test-es

# Test mode - 2 files to all languages
./scripts/retranslate.sh test-all

# All files to Spanish (with confirmation prompt)
./scripts/retranslate.sh all-es

# Preview without translating
./scripts/retranslate.sh dry-run
```

#### Using Python Script Directly (Most Flexible)

### Retranslate All Docs to One Language

```bash
python scripts/bulk_retranslate.py --language es
```

This will:
- Find all `.md` files in `docs/en/`
- Translate each to Spanish
- Save to `docs/es/`

### Retranslate All Docs to Multiple Languages

```bash
python scripts/bulk_retranslate.py --language es fr ar
```

### Retranslate Specific Files

```bash
python scripts/bulk_retranslate.py --language es --files about_kobotoolbox.md quick_start.md
```

### Dry Run (Preview Without Translating)

```bash
python scripts/bulk_retranslate.py --language es --dry-run
```

This shows what would be translated without actually calling the API.

## Advanced Options

### Custom Source Directory

```bash
python scripts/bulk_retranslate.py --language es --source-dir docs/en
```

### Adjust Delay Between Translations

```bash
# Increase delay to 2 seconds (default is 0.5s)
python scripts/bulk_retranslate.py --language es --delay 2

# Remove delay entirely (use with caution - may hit rate limits)
python scripts/bulk_retranslate.py --language es --no-delay
```

### Verbose Output

```bash
python scripts/bulk_retranslate.py --language es --verbose
```

Shows detailed progress and saves locations.

## Recommended Workflow

### Using GitHub Actions (Team Workflow)

#### 1. Update Skills

Edit your translation skills in the repository:
- Go to `skills/kobo-translation/references/`
- Edit terminology files (e.g., `brand-terminology.md`)
- Commit and push changes

#### 2. Regenerate Language-Specific Skills

```bash
python3 scripts/split_skill_by_language.py
git add skills/
git commit -m "Update translation skills"
git push
```

#### 3. Test on Sample Files

1. Go to **Actions → Bulk Retranslate Documentation**
2. Click **"Run workflow"**
3. Configure:
   - Mode: `test`
   - Languages: `es`
4. Review the created PR

#### 4. Compare Translations

In the PR:
- Click **"Files changed"** tab
- Review translated files
- Look for quality improvements from skill updates

#### 5. Retranslate All (if satisfied)

1. Go to **Actions → Bulk Retranslate Documentation**
2. Click **"Run workflow"**
3. Configure:
   - Mode: `all`
   - Languages: `es,fr,ar` (or specific languages)
   - Check cost confirmation ✅
4. Review and merge the PR

### Using Local Scripts (Development Workflow)

### 1. Update Skills

Edit your translation skills:

```bash
vim skills/kobo-translation/references/brand-terminology.md
```

### 2. Regenerate Language-Specific Skills

```bash
python3 scripts/split_skill_by_language.py
```

### 3. Test on Small Sample (Dry Run)

```bash
python scripts/bulk_retranslate.py --language es --files test_simple.md test_complex.md --dry-run
```

### 4. Retranslate Sample Files

```bash
python scripts/bulk_retranslate.py --language es --files test_simple.md test_complex.md
```

### 5. Compare Translations

```bash
git diff docs/es/test_simple.md
```

Review the changes to see if the skill updates improved quality.

### 6. Retranslate All (if satisfied)

```bash
# Option 1: One language at a time
python scripts/bulk_retranslate.py --language es

# Option 2: All languages (most expensive)
python scripts/bulk_retranslate.py --language es fr ar
```

### 7. Review and Commit

```bash
git add docs/es/ docs/fr/ docs/ar/
git commit -m "Regenerate translations with updated skills"
git push
```

## Cost Estimation

Approximate costs (using Claude Sonnet 4.5 with prompt caching):

| Scope | Translations | Est. Cost |
|-------|--------------|-----------|
| 2-3 test files (1 lang) | 3 | $0.50-$1.00 |
| 10 files (1 lang) | 10 | $2-$5 |
| All docs ~100 files (1 lang) | 100 | $15-$30 |
| All docs (3 langs) | 300 | $45-$90 |

**💡 Tips to reduce costs:**
- Use `--dry-run` first to confirm scope
- Test on 2-3 files before bulk retranslating
- Retranslate one language at a time
- Only retranslate when skill changes are significant

## Output and Statistics

The script provides:
- Progress indicator for each file and language
- Success/failure status for each translation
- Summary statistics:
  - Total files processed
  - Total translations (files × languages)
  - Successful translations
  - Failed translations
  - Total duration
  - Estimated cost
  - Average time per translation
- List of failed translations (if any)

Example output:

```
======================================================================
🔄 BULK RETRANSLATION
======================================================================
Files: 100
Languages: es, fr, ar
Total translations: 300
======================================================================

[1/100] about_kobotoolbox.md
  → ES ✅
  → FR ✅
  → AR ✅

[2/100] acknowledge.md
  → ES ✅
  → FR ✅
  → AR ✅

...

======================================================================
📊 SUMMARY
======================================================================
Total files: 100
Total translations: 300
✅ Successful: 298
❌ Failed: 2
⏱️  Duration: 450.2 seconds (7.5 minutes)
💰 Estimated cost: $42.50
⚡ Avg time per translation: 1.5 seconds
======================================================================
```

## Troubleshooting

### Import Error

```
❌ Error: Could not import translation_agent.py
```

**Solution:** Make sure you're running from the repository root:

```bash
cd /path/to/kobo-translation-test
python scripts/bulk_retranslate.py --language es
```

### Missing Dependencies

```
❌ Missing dependencies. Install with: pip install -r requirements.txt
```

**Solution:**

```bash
pip install -r scripts/requirements.txt
```

### Rate Limit Errors

If you hit API rate limits, increase the delay:

```bash
python scripts/bulk_retranslate.py --language es --delay 2
```

Or process fewer files at a time:

```bash
# Split into batches
python scripts/bulk_retranslate.py --language es --files file1.md file2.md file3.md
# Wait a bit...
python scripts/bulk_retranslate.py --language es --files file4.md file5.md file6.md
```

### Out of Memory

For very large documentation sets, process in smaller batches:

```bash
# Get list of files
ls docs/en/*.md > files.txt

# Process in batches of 20
head -20 files.txt | xargs -I {} python scripts/bulk_retranslate.py --language es --files {}
```

## Integration with Git Workflow

### Compare Before Committing

```bash
# Retranslate
python scripts/bulk_retranslate.py --language es --files about_kobotoolbox.md

# Review changes
git diff docs/es/about_kobotoolbox.md

# Commit if satisfied
git add docs/es/about_kobotoolbox.md
git commit -m "Retranslate about_kobotoolbox with updated skills"
```

### Bulk Comparison

```bash
# Retranslate all
python scripts/bulk_retranslate.py --language es

# See summary of changes
git diff --stat docs/es/

# Review specific files with large changes
git diff docs/es/
```

## Best Practices

1. **Always test first:** Use `--dry-run` and test on 2-3 files before bulk operations
2. **One language at a time:** Easier to review and debug issues
3. **Version control:** Commit before retranslating so you can revert if needed
4. **Monitor costs:** Keep track of API usage, especially for large document sets
5. **Review samples:** Don't blindly accept all changes - spot check quality
6. **Document changes:** Note what skills were updated in your commit message

## See Also

- [Translation Agent Documentation](../../scripts/translation_agent.py)
- [Skill Maintenance Guide](../README.md#maintaining-translation-skills)
- [Prompt Caching Implementation](PROMPT_CACHING_IMPLEMENTATION.md)
