# Testing V2 Translation Skills

## Quick Start

### Option 1: GitHub Actions UI (Recommended)

1. Go to **Actions** tab in GitHub
2. Select **"Test V2 Translation Skills"** workflow
3. Click **"Run workflow"**
4. Configure:
   - **Languages:** `es` (or `es,fr,ar` for multiple)
   - **Test files:** Leave empty for defaults or specify custom files
   - **Skill version:** 
     - `v2` - Test only v2 skills
     - `v1` - Test only v1 skills  
     - `both` - Compare v1 vs v2
   - **Model:** Choose Claude model (default: sonnet)
5. Click **"Run workflow"**

### Option 2: Command Line

```bash
# Test v2 Spanish skill with default files
gh workflow run test-v2-skills.yml \
  -f languages=es \
  -f skill_version=v2

# Compare v1 vs v2 for multiple languages
gh workflow run test-v2-skills.yml \
  -f languages=es,fr \
  -f skill_version=both

# Test specific files
gh workflow run test-v2-skills.yml \
  -f languages=es \
  -f skill_version=v2 \
  -f test_files="about_kobotoolbox.md,creating_account.md"
```

## Default Test Files

The workflow uses these files by default (small → large complexity):
- `about_kobotoolbox.md` - Simple, brand-heavy content
- `creating_account.md` - Medium complexity with UI terms
- `formbuilder.md` - Large, technical content

## What Gets Tested

### V2 Skills Test (`skill_version=v2`)
- Uses `skills/kobo-translation-v2-{lang}/` 
- Tests improvements:
  - ✅ No multi-line table cell issues
  - ✅ Language-specific filtering
  - ✅ Word boundary matching
  - ✅ 46.9% smaller context

### Comparison Test (`skill_version=both`)
- Translates with V1 skills first
- Then translates with V2 skills
- Creates side-by-side comparison
- Generates comparison report

## Review Checklist

When reviewing the PR created by the workflow:

1. **Translation Quality**
   - [ ] Natural and accurate translations
   - [ ] Correct terminology from skill references
   - [ ] No untranslated content (except intentional)

2. **Formatting**
   - [ ] Tables render correctly
   - [ ] Links updated properly
   - [ ] Markdown formatting preserved

3. **V2 Improvements** (when comparing)
   - [ ] No French/Arabic content in Spanish translations
   - [ ] Clean table structure (no malformed rows)
   - [ ] Consistent terminology application

## Cost Estimation

Approximate costs per file per language:
- Small file (~1KB): $0.01-0.02
- Medium file (~5KB): $0.03-0.05  
- Large file (~15KB): $0.08-0.12

Default test (3 files × 1 language): ~$0.10-0.20

## Troubleshooting

### "V2 skill missing" error
Run the split script to generate v2 skills:
```bash
python scripts/split_skill_by_language.py
```

### Translation agent not finding skills
The workflow temporarily symlinks v2 skills to the expected location:
```
skills/kobo-translation-es → kobo-translation-v2-es
```

### Want to test locally first?

```bash
# Activate v2 skills
cd skills
ln -s kobo-translation-v2-es kobo-translation-es

# Run translation
cd ..
python scripts/bulk_retranslate.py --language es --files about_kobotoolbox.md --verbose

# Clean up
rm skills/kobo-translation-es
```

## Next Steps After Testing

1. ✅ Review translation quality in PR
2. ✅ Compare v1 vs v2 (if using both mode)
3. ✅ Merge if quality is acceptable
4. 🚀 Consider updating production skills to v2
5. 📊 Monitor cost/quality improvements

## See Also

- [BULK_RETRANSLATION_WORKFLOWS.md](../BULK_RETRANSLATION_WORKFLOWS.md) - General retranslation guide
- [skills/kobo-translation-v2/README.md](../skills/kobo-translation-v2/README.md) - V2 skill documentation
