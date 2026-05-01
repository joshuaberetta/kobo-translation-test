# Bulk Retranslation - Quick Reference

## 🎯 Purpose
Retranslate documentation files in bulk when translation skills are updated, allowing you to test quality improvements across your entire documentation corpus.

## 🚀 Quick Commands

### GitHub Actions (Easiest - No Local Setup)

1. Go to **Actions → Bulk Retranslate Documentation**
2. Click **"Run workflow"**
3. Configure:
   - **Mode:** `test` / `specific` / `all`
   - **Languages:** `es,fr,ar`
   - **Files:** (for specific mode only)
4. Review PR automatically created

### Local Command Line

```bash
# Test on 2 files → Spanish
./scripts/retranslate.sh test-es

# Test on 2 files → all languages  
./scripts/retranslate.sh test-all

# Preview what would be translated
./scripts/retranslate.sh dry-run

# Retranslate all → Spanish (with confirmation)
./scripts/retranslate.sh all-es

# Retranslate all → all languages (with confirmation)
./scripts/retranslate.sh all-langs
```

## 📋 Common Workflows

### Test Skill Changes
```bash
# 1. Update skills
vim skills/kobo-translation-v2/sources/style-guide.md

# 2. Regenerate language-specific skills  
python3 scripts/split_skill_by_language.py

# 3. Test translation
./scripts/retranslate.sh test-es

# 4. Compare changes
git diff docs/es/test_simple.md
```

### Retranslate Specific Files
```bash
python scripts/bulk_retranslate.py \
  --language es \
  --files about_kobotoolbox.md quick_start.md
```

### All Files, All Languages
```bash
python scripts/bulk_retranslate.py --language es fr ar
```

## 💰 Cost Estimates

| Scope | Cost |
|-------|------|
| 2-3 test files (1 lang) | $0.50-$1 |
| All ~100 files (1 lang) | $15-$30 |
| All ~100 files (3 langs) | $45-$90 |

## 📖 Documentation

- Full guide: `docs/guides/BULK_RETRANSLATION.md`
- Script help: `python scripts/bulk_retranslate.py --help`

## ⚙️ Options

```bash
python scripts/bulk_retranslate.py \
  --language es fr ar              # Target language(s)
  --files file1.md file2.md        # Specific files (default: all)
  --source-dir docs/en             # Source directory
  --dry-run                        # Preview only
  --verbose                        # Detailed output
  --delay 2                        # Delay between translations (seconds)
  --no-delay                       # Remove delay (use with caution)
```

## ✅ Features

- ✅ Retranslate all files or specific subset
- ✅ Support multiple target languages
- ✅ Dry-run mode to preview
- ✅ Progress tracking
- ✅ Cost estimation
- ✅ Failure reporting
- ✅ Configurable delays to avoid rate limits
