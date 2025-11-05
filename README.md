# KoboToolbox Translation Agent - Test Repository

This is a minimal test setup to validate the AI translation workflow before implementing in the full documentation repository.

**✨ NEW: SRT Subtitle Translation** - Now includes complete workflow for translating video subtitles with context-aware chunking to minimize hallucinations. See `SRT_WORKFLOW.md` for details.

## Repository Structure

```
kobo-translation-test/
├── .github/
│   └── workflows/
│       ├── translation-trigger.yml      # Detects changes to English docs
│       └── translation-agent.yml        # Runs translation agent
├── docs/
│   ├── en/                              # English source (source of truth)
│   │   ├── test_simple.md              # Simple test doc
│   │   └── test_complex.md             # Complex doc with brand terms
│   ├── es/                              # Spanish translations (auto-generated)
│   ├── fr/                              # French translations (auto-generated)
│   └── ar/                              # Arabic translations (auto-generated)
├── examples/
│   ├── sample_transcript_en.srt         # Sample video transcript
│   ├── test_webinar.srt                 # Real webinar content (tested ✅)
│   ├── test_srt_parser.py               # Parser verification test
│   └── TEST_RESULTS.md                  # Verification results
├── skills/
│   ├── kobo-translation/                # Main translation skill
│   │   ├── SKILL.md
│   │   └── references/
│   └── kobo-translation-srt/            # SRT subtitle extension skill
│       ├── SKILL.md
│       └── references/
│           └── subtitle-guidelines.md
├── scripts/
│   ├── translation_agent.py             # Main translation agent (docs)
│   ├── translate_srt.py                 # SRT translation agent (NEW)
│   ├── srt_helper.py                    # SRT parser & converter (NEW)
│   └── requirements.txt                 # Python dependencies
├── SRT_WORKFLOW.md                      # SRT translation guide (NEW)
├── SRT_IMPLEMENTATION.md                # Implementation details (NEW)
├── SETUP.md                             # Complete setup guide
├── QUICKSTART.md                        # Quick start checklist
└── README.md                            # This file
```

## 🆕 Meta Skill: Arabic Guide Generation

**NEW**: Use the existing French and Spanish guides to generate comprehensive Arabic translation guides!

The meta skill approach analyzes patterns from your well-developed French/Spanish guides and generates Arabic guides that follow the same structure, principles, and depth.

**Quick Start**:
```bash
# Generate complete Arabic guide
python scripts/generate_arabic_guide.py --all

# Generate specific reference file
python scripts/generate_arabic_guide.py --reference brand-terminology.md
```

See `ARABIC_GUIDE_GENERATION.md` for detailed instructions and `SOLUTION_SUMMARY.md` for the complete solution overview.

## Quick Start

### 1. Prerequisites

- GitHub account
- Anthropic API key ([get one here](https://console.anthropic.com/))
- Python 3.11+
- Git

### 2. Clone and Setup

```bash
# Clone this repository
git clone https://github.com/YOUR-ORG/kobo-translation-test.git
cd kobo-translation-test

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r scripts/requirements.txt
```

### 3. Configure Secrets

#### Local Testing (Optional)
```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your keys
nano .env
```

#### GitHub Secrets (Required for automation)
Go to: **Settings → Secrets and variables → Actions → New repository secret**

Add these secrets:
- `ANTHROPIC_API_KEY` - Your Claude API key
- `TRANSLATION_BOT_TOKEN` - GitHub Personal Access Token with repo permissions

### 4. Test Locally (Recommended First)

```bash
# Test translation of a single file
python scripts/translation_agent.py --test \
    --file docs/en/test_simple.md \
    --language es

# This will:
# - Load the kobo-translation skill
# - Translate to Spanish
# - Show the output (but not commit)
```

### 5. Test with GitHub Actions

#### Option A: Automatic (on push to main)
```bash
# Make a change to an English doc
echo "## New Section\n\nTest content" >> docs/en/test_simple.md

# Commit and push
git add docs/en/test_simple.md
git commit -m "Update test document"
git push

# Watch GitHub Actions run:
# https://github.com/YOUR-ORG/kobo-translation-test/actions
```

#### Option B: Manual Workflow Dispatch

You can manually trigger translations via GitHub's Actions tab:

**To translate specific files:**
1. Go to Actions → Auto-Translate Documentation
2. Click "Run workflow"
3. Enter files: `docs/en/test_simple.md,docs/en/test_complex.md`
4. Enter languages: `es,fr,ar`
5. Click "Run workflow"

**To translate ALL English source files:**
1. Go to Actions → Auto-Translate Documentation
2. Click "Run workflow"
3. Check ☑️ "Translate ALL English source files"
4. Enter languages: `es,fr,ar`
5. Click "Run workflow"

⚠️ **Warning**: Translating all files will:
- Process **100+ files** (based on your docs/en/ directory)
- Cost approximately **$15-30** depending on file sizes
- Take **30-60 minutes** to complete
- Create a large PR with many changes

This is useful for:
- Initial bulk translation setup
- Major skill/terminology updates that affect all files
- Periodic quality refresh of all translations

### 6. Review and Merge

1. GitHub Actions will create a PR with translations
2. Review the translations in the PR
3. Check the validation results
4. Merge if quality is good

## What Gets Tested

### Test Document 1: Simple (`test_simple.md`)
- Basic translation
- No brand terms
- Simple formatting
- **Purpose:** Verify basic translation works

### Test Document 2: Complex (`test_complex.md`)
- Contains brand terms (KoboToolbox, Formbuilder, servers)
- UI elements
- Links and formatting
- **Purpose:** Verify skill rules are followed

## Expected Workflow

```
1. Edit docs/en/test_simple.md
   ↓
2. Commit and push to main
   ↓
3. translation-trigger.yml detects change
   ↓
4. translation-agent.yml runs
   ↓
5. Agent translates to es, fr, ar
   ↓
6. Agent creates PR with translations
   ↓
7. You review PR
   ↓
8. Merge PR → translations live
```

## What to Check in PR

Look for these in the automated PR:

✅ **Brand Terms**
- [ ] Server names correct (check Spanish doesn't have "de KoboToolbox")
- [ ] Question Library has capital "L"
- [ ] Formbuilder includes English on first reference

✅ **UI Elements**
- [ ] Capitalization correct (Brouillon, Borrador)
- [ ] Button names match UI

✅ **Language Style**
- [ ] Spanish uses "tú" (informal)
- [ ] French uses "vous" (formal)
- [ ] Gender-inclusive language

✅ **Formatting**
- [ ] All links preserved
- [ ] Headings maintained
- [ ] Structure identical to source

## Troubleshooting

### "Workflow not triggering"
- Check `.github/workflows/` files are in correct location
- Verify GitHub Actions is enabled in repo settings
- Check file paths in trigger workflow match your changes

### "Translation agent fails"
- Check `ANTHROPIC_API_KEY` secret is set correctly
- Check `TRANSLATION_BOT_TOKEN` has correct permissions
- View full logs in GitHub Actions run

### "Translation quality poor"
- Review which skill level is being used (condensed/standard/full)
- Check skill files are in correct location
- Try using "full" skill mode for complex documents

### "Local test not working"
```bash
# Verify skill files exist
ls -R skills/kobo-translation/

# Check Python dependencies
pip list | grep anthropic

# Test with verbose output
python scripts/translation_agent.py --test --file docs/en/test_simple.md --language es --verbose
```

## Cost Estimate

For this test repo:
- 2 test documents × 3 languages = 6 translations
- ~$0.15 per document = **~$0.90 per test run**
- Testing 10 times = **~$9 total**

Very affordable for testing!

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

## Files Included

This repository includes:

- ✅ Minimal working translation agent
- ✅ GitHub Actions workflows
- ✅ Sample test documents
- ✅ Complete kobo-translation skill
- ✅ Validation scripts
- ✅ Documentation

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review GitHub Actions logs
3. Test locally first before debugging workflows

## License

[Your License Here]
