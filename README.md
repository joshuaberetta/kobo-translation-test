# KoboToolbox Translation Agent - Test Repository

This is a minimal test setup to validate the AI translation workflow before implementing in the full documentation repository.

## Features

✅ **Documentation Translation** - Automated translation of markdown docs with brand terminology preservation  
✅ **SRT Subtitle Translation** - Context-aware video subtitle translation with chunking to minimize hallucinations  
✅ **GitHub Actions Integration** - Automatic translation on commit or manual trigger  
✅ **Language-Specific Skills** - Optimized translation context for each language pair  
✅ **Prompt Caching** - 90% cost reduction on repeated translations

## Repository Structure

```
kobo-translation-test/
├── .github/workflows/           # GitHub Actions automation
├── docs/
│   ├── en/                      # English source (source of truth)
│   ├── es/fr/ar/                # Auto-generated translations
│   └── guides/                  # Detailed documentation
│       ├── SETUP.md             # Complete setup guide
│       ├── QUICKSTART.md        # Quick start checklist
│       ├── SRT_WORKFLOW.md      # SRT translation guide
│       ├── SRT_IMPLEMENTATION.md
│       ├── GITHUB_ACTIONS_SRT_GUIDE.md
│       ├── PROMPT_CACHING_IMPLEMENTATION.md
│       └── FUTURE_IMPROVEMENTS.md
├── examples/                    # Sample files and test results
├── skills/
│   ├── kobo-translation/        # ⚠️ EDIT HERE (source of truth)
│   ├── kobo-translation-{es,fr,ar}/  # Auto-generated
│   └── kobo-translation-srt/    # SRT extension skill
├── scripts/
│   ├── translation_agent.py     # Main doc translation
│   ├── translate_srt.py         # SRT translation
│   ├── srt_helper.py            # SRT utilities
│   ├── split_skill_by_language.py  # Skill generator
│   └── requirements.txt
├── tests/                       # Test scripts
└── transcripts/                 # Video subtitle files
```


## Quick Start

### Prerequisites
- GitHub account
- Anthropic API key ([get one here](https://console.anthropic.com/))
- Python 3.11+
- Git

### Setup (5 minutes)

1. **Clone and install dependencies:**
```bash
git clone https://github.com/YOUR-ORG/kobo-translation-test.git
cd kobo-translation-test
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r scripts/requirements.txt
```

2. **Configure GitHub Secrets:**
   - Go to: **Settings → Secrets → Actions**
   - Add `ANTHROPIC_API_KEY` - Your Claude API key
   - Add `TRANSLATION_BOT_TOKEN` - GitHub Personal Access Token

3. **Test locally (optional):**
```bash
# Test documentation translation
python scripts/translation_agent.py --test \
    --file docs/en/test_simple.md \
    --language es

# Test SRT subtitle translation
python scripts/translate_srt.py \
    examples/sample_transcript_en.srt \
    --language es
```

4. **Trigger automation:**
   - Edit any file in `docs/en/`
   - Commit and push
   - GitHub Actions will auto-translate to es, fr, ar
   - Review the PR created by the bot

📖 **Detailed guides:** See `docs/guides/` for complete setup instructions and advanced workflows.

## Common Workflows

### Translate Documentation

**Automatic (on push):**
```bash
echo "## New Section" >> docs/en/test_simple.md
git add docs/en/test_simple.md
git commit -m "Update docs"
git push
# Watch Actions tab for automated translation
```

**Manual trigger:**
1. Go to Actions → Auto-Translate Documentation
2. Click "Run workflow"
3. Enter files and languages
4. Review the PR

**Bulk retranslation (for testing skill updates):**

*Option 1: GitHub Actions (recommended for team use)*
1. Go to **Actions → Bulk Retranslate Documentation**
2. Click **"Run workflow"**
3. Select mode:
   - `test` - 2-3 test files only (safe)
   - `specific` - Specific files you list
   - `all` - ALL files (requires confirmation)
4. Enter target languages (e.g., `es,fr,ar`)
5. Review the PR created by the bot

*Option 2: Local execution (recommended for development)*
```bash
# Quick helper script
./scripts/retranslate.sh test-es        # Test with 2 files → Spanish
./scripts/retranslate.sh test-all       # Test with 2 files → all languages
./scripts/retranslate.sh all-es         # All docs → Spanish (with confirmation)
./scripts/retranslate.sh dry-run        # Preview what would be translated

# Direct Python usage (more options)
python scripts/bulk_retranslate.py --language es

# Retranslate all docs to all languages
python scripts/bulk_retranslate.py --language es fr ar

# Retranslate specific files
python scripts/bulk_retranslate.py --language es --files about_kobotoolbox.md quick_start.md

# Dry run to preview what would be translated
python scripts/bulk_retranslate.py --language es --dry-run

# See all options
python scripts/bulk_retranslate.py --help
```

📖 **Full guide:** See `docs/guides/BULK_RETRANSLATION.md` for detailed workflows and best practices.

### Translate Video Subtitles

**Local:**
```bash
python scripts/translate_srt.py your_video.srt --language es
```

**GitHub Actions:**
1. Upload `.srt` file to `transcripts/en/`
2. Go to Actions → Translate SRT Subtitles
3. Enter filename and languages
4. Download from Artifacts

📖 **SRT Guide:** See `docs/guides/SRT_WORKFLOW.md` for detailed subtitle translation workflow.

## Next Steps

Once testing is successful:

1. ✅ Verify translations match quality expectations
2. ✅ Confirm brand terms are handled correctly
3. ✅ Check PR review workflow works
4. ✅ Validate automation is reliable

Then:
- Migrate to full docs repository
- Add all English documentation files
- Train reviewers on PR process
- Set up monitoring and alerts

## Maintaining Translation Skills

### Single Source of Truth

All translation terminology and guidelines are maintained in **one place**:
```
skills/kobo-translation/
├── SKILL.md                    # ⚠️ Edit this file
└── references/                 # ⚠️ Edit these files
    ├── brand-terminology.md
    ├── course-terminology.md
    ├── data-collection-terms.md
    ├── form-building-terms.md
    ├── question-types.md
    └── ui-terminology.md
```

**⚠️ IMPORTANT:** These files contain translations for ALL languages (EN, ES, FR, AR) in table columns.

### Regenerating Language-Specific Skills

After editing any files in `skills/kobo-translation/`, run:

```bash
python3 scripts/split_skill_by_language.py
```

This automatically generates optimized, language-focused versions:
- `skills/kobo-translation-es/` - English → Spanish only
- `skills/kobo-translation-fr/` - English → French only
- `skills/kobo-translation-ar/` - English → Arabic only

**What the script does:**
- ✅ Filters table columns (keeps only English + target language)
- ✅ Removes prose sections for other languages
- ✅ Filters language-specific usage guides and examples
- ✅ Preserves technical metadata columns (XLSForm types, etc.)
- ✅ Reduces context window size for more efficient translations

### Workflow

```
1. Update terminology in skills/kobo-translation/references/*.md
   ↓
2. Run: python3 scripts/split_skill_by_language.py
   ↓
3. Commit all changes (source + generated skills)
   ↓
4. Translation agent uses optimized language-specific skills
```

### Testing Skill Updates with Bulk Retranslation

After updating skills, you can retranslate existing docs to compare quality:

```bash
# 1. Update skills
vim skills/kobo-translation/references/brand-terminology.md

# 2. Regenerate language-specific skills
python3 scripts/split_skill_by_language.py

# 3. Test on a few files first (dry run)
python scripts/bulk_retranslate.py --language es --files test_simple.md --dry-run

# 4. Retranslate test files
python scripts/bulk_retranslate.py --language es --files test_simple.md test_complex.md

# 5. Compare old vs new translations to evaluate skill improvements
git diff docs/es/test_simple.md

# 6. If satisfied, retranslate all docs (be aware of API costs!)
python scripts/bulk_retranslate.py --language es fr ar
```

**Cost estimation:** 
- Test files (2-3 docs): ~$0.50-$1.00
- All docs (~100 files): ~$15-$30 per run
- Use `--dry-run` first to preview scope

**🚫 DO NOT** manually edit files in:
- `skills/kobo-translation-es/`
- `skills/kobo-translation-fr/`
- `skills/kobo-translation-ar/`

These are **auto-generated** and will be overwritten when you run the script.

## Quality Checklist

When reviewing automated translation PRs, check:

✅ **Brand Terms**
- [ ] Server names correct (Spanish: no "de KoboToolbox")
- [ ] Question Library has capital "La"
- [ ] Formbuilder includes English on first reference

✅ **UI Elements**
- [ ] Capitalization matches UI
- [ ] Button names correct

✅ **Language Style**
- [ ] Spanish uses "tú" (informal)
- [ ] French uses "vous" (formal)
- [ ] Gender-inclusive language where appropriate

✅ **Formatting**
- [ ] All links preserved
- [ ] Headings maintained
- [ ] Structure identical to source

## Documentation

- **Setup Guide:** `docs/guides/SETUP.md` - Complete setup instructions
- **Quick Start:** `docs/guides/QUICKSTART.md` - Fast setup checklist
- **Bulk Retranslation:** `docs/guides/BULK_RETRANSLATION.md` - Regenerate translations when skills are updated
- **SRT Translation:** `docs/guides/SRT_WORKFLOW.md` - Video subtitle translation
- **GitHub Actions SRT:** `docs/guides/GITHUB_ACTIONS_SRT_GUIDE.md` - Automate SRT translation
- **Prompt Caching:** `docs/guides/PROMPT_CACHING_IMPLEMENTATION.md` - Cost optimization details
- **Future Plans:** `docs/guides/FUTURE_IMPROVEMENTS.md` - Planned enhancements

## Troubleshooting

**Workflow not triggering:**
- Verify GitHub Actions is enabled
- Check workflow file paths match your changes

**Translation agent fails:**
- Verify `ANTHROPIC_API_KEY` secret is set
- Check `TRANSLATION_BOT_TOKEN` has repo permissions
- Review logs in GitHub Actions

**Translation quality issues:**
- Ensure latest language-specific skills are generated
- Check skill files are in correct location
- Review terminology in `skills/kobo-translation/references/`

**Local test not working:**
```bash
# Verify dependencies
pip list | grep anthropic

# Test with verbose output
python scripts/translation_agent.py --test \
    --file docs/en/test_simple.md \
    --language es --verbose
```

## Cost Estimates

**Documentation:**
- Test docs: ~$0.90 per run (6 translations)
- Full docs (100+ files): ~$15-30 initial, ~$1-5 per update

**Subtitles:**
- 30-minute video: ~$2-5 per language (with caching)
- Prompt caching saves 90% on subsequent chunks

## Next Steps

Once testing is successful:

1. ✅ Verify translation quality meets expectations
2. ✅ Confirm brand terms are handled correctly
3. ✅ Validate automation workflow
4. ✅ Train team on PR review process
5. 🚀 Migrate to full documentation repository
