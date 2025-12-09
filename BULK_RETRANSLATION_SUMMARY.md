# Bulk Retranslation Feature - Summary

## What Was Added

This update adds bulk retranslation capabilities to test translation skill updates across your entire documentation corpus.

### New Files

1. **`scripts/bulk_retranslate.py`** - Main bulk retranslation script
   - Retranslate all docs or specific files to one or more target languages
   - Dry-run mode to preview without translating
   - Progress tracking and cost estimation
   - Configurable delay between translations to avoid rate limits

2. **`scripts/retranslate.sh`** - Helper script for common use cases
   - Quick commands: `test-es`, `test-all`, `all-es`, `all-langs`, `dry-run`
   - Safety confirmations for bulk operations
   - Colored output for better UX

3. **`.github/workflows/bulk-retranslate.yml`** - GitHub Actions workflow
   - Manual trigger from GitHub UI
   - Three modes: test, specific, all
   - Safety confirmation for expensive operations
   - Automatic PR creation
   - Detailed summary and cost estimation

4. **`docs/guides/BULK_RETRANSLATION.md`** - Complete guide
   - Usage examples for both GitHub Actions and local scripts
   - Recommended workflows
   - Cost estimation
   - Troubleshooting
   - Best practices

### Updated Files

- **`README.md`** - Added bulk retranslation documentation
  - New section in "Common Workflows"
  - Enhanced "Testing Skill Updates" section with workflow
  - Link to bulk retranslation guide

## Use Cases

### When to Use Bulk Retranslation

✅ **After updating translation skills/terminology**
   - Test how changes affect translation quality
   - Regenerate translations with updated brand terms

✅ **Quality comparison**
   - Compare old vs new translations
   - Evaluate skill improvements

✅ **Major skill refactoring**
   - Regenerate all translations when making significant skill changes
   - Test across entire documentation corpus

## Quick Start

### GitHub Actions (No Setup Required)

1. Go to **Actions → Bulk Retranslate Documentation**
2. Click **"Run workflow"**
3. Select mode: `test` (safe), `specific`, or `all`
4. Enter languages: `es` or `es,fr,ar`
5. Review the created PR

### Local Command Line

### Test on Sample Files
```bash
# Using helper script (easiest)
./scripts/retranslate.sh test-es

# Or direct Python
python scripts/bulk_retranslate.py --language es --files test_simple.md test_complex.md
```

### Preview Without Translating
```bash
./scripts/retranslate.sh dry-run
```

### Retranslate All Docs
```bash
# One language
./scripts/retranslate.sh all-es

# All languages (expensive!)
./scripts/retranslate.sh all-langs
```

## Recommended Workflow

When you update translation skills:

```bash
# 1. Update skills
vim skills/kobo-translation/references/brand-terminology.md

# 2. Regenerate language-specific skills
python3 scripts/split_skill_by_language.py

# 3. Test on sample files
./scripts/retranslate.sh test-es

# 4. Compare translations
git diff docs/es/test_simple.md

# 5. If satisfied, retranslate all
./scripts/retranslate.sh all-es  # or all-langs for all languages

# 6. Review and commit
git add docs/es/
git commit -m "Regenerate Spanish translations with updated skills"
```

## Cost Estimates

| Operation | Files | Languages | Est. Cost |
|-----------|-------|-----------|-----------|
| Test files | 2-3 | 1 | $0.50-$1 |
| Test files | 2-3 | 3 | $1.50-$3 |
| All docs | ~100 | 1 | $15-$30 |
| All docs | ~100 | 3 | $45-$90 |

**💡 Tip:** Always test on a few files first before bulk retranslating!

## Features

### Bulk Retranslate Script (`bulk_retranslate.py`)

- ✅ Retranslate all files in a directory
- ✅ Retranslate specific list of files
- ✅ Support multiple target languages
- ✅ Dry-run mode (preview without translating)
- ✅ Progress tracking with file/language status
- ✅ Success/failure reporting
- ✅ Cost estimation
- ✅ Configurable delay between translations
- ✅ Verbose mode for detailed output
- ✅ Summary statistics (duration, costs, success rate)

### Helper Script (`retranslate.sh`)

- ✅ Quick commands for common scenarios
- ✅ Safety confirmations for expensive operations
- ✅ Colored output for better UX
- ✅ Simple wrapper around Python script

### Documentation

- ✅ Comprehensive guide in `docs/guides/BULK_RETRANSLATION.md`
- ✅ Usage examples in README
- ✅ Integration with existing workflow
- ✅ Cost transparency

## Examples

### Example 1: Test Skill Changes
```bash
# Update terminology
echo "| KoboToolbox | KoboToolbox | KoboToolbox | كوبو تولبوكس |" >> skills/kobo-translation/references/brand-terminology.md

# Regenerate skills
python3 scripts/split_skill_by_language.py

# Test on 2 files
./scripts/retranslate.sh test-es

# Compare
git diff docs/es/test_simple.md
```

### Example 2: Retranslate Specific Files
```bash
python scripts/bulk_retranslate.py \
  --language es fr \
  --files about_kobotoolbox.md quick_start.md welcome.md
```

### Example 3: Preview Scope
```bash
# See what would be translated without doing it
python scripts/bulk_retranslate.py --language es --dry-run
```

## Safety Features

1. **Dry-run mode** - Preview before translating
2. **Confirmation prompts** - Helper script asks before expensive operations
3. **Cost warnings** - Shows estimated costs
4. **Progress tracking** - See what's happening in real-time
5. **Failure reporting** - Lists failed translations for retry

## Integration with Existing Tools

The bulk retranslation script:
- ✅ Uses the same `TranslationAgent` class as normal translation
- ✅ Respects the same language-specific skills
- ✅ Saves to the same directory structure
- ✅ Benefits from prompt caching
- ✅ Compatible with existing workflows

## Next Steps

Users can now:
1. Update translation skills confidently
2. Test changes on sample files
3. Compare old vs new translations
4. Regenerate all translations when satisfied
5. Track quality improvements over time

## Documentation Links

- Main guide: `docs/guides/BULK_RETRANSLATION.md`
- README section: "Common Workflows" → "Bulk retranslation"
- Script help: `python scripts/bulk_retranslate.py --help`
- Helper commands: `./scripts/retranslate.sh`
