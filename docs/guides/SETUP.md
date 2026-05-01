# Setup Guide - KoboToolbox Translation Agent Test

## Step-by-Step Setup Instructions

### 1. Create GitHub Repository

```bash
# Option A: Create on GitHub.com
# 1. Go to https://github.com/new
# 2. Name: kobo-translation-test
# 3. Visibility: Private (recommended for testing)
# 4. Initialize: Do NOT initialize with README (we have files)
# 5. Click "Create repository"

# Option B: Using GitHub CLI
gh repo create kobo-translation-test --private
```

### 2. Prepare Local Files

```bash
# Download the test repository files you've created
# (They should be in /mnt/user-data/outputs/test-repo/)

# Navigate to your working directory
cd ~/Projects  # or wherever you want to work

# Copy or move the test-repo files here
cp -r /path/to/test-repo kobo-translation-test
cd kobo-translation-test
```

### 3. Add Kobo Translation Skill

```bash
# The skills are included in the repository.
# Your structure should look like:
# skills/
# └── kobo-translation/
#     ├── SKILL.md
#     ├── sources/           # Human-maintained inputs
#     │   ├── glossary.xlsx
#     │   ├── style-guide.md
#     │   └── language-rules.md
#     └── references/        # Auto-generated
#         ├── brand-terminology.md
#         ├── ui-terminology.md
#         └── ...
# └── kobo-translation-es/   # Auto-generated language variants
# └── kobo-translation-fr/
# └── kobo-translation-ar/
```

### 4. Get Anthropic API Key

```bash
# 1. Go to https://console.anthropic.com/
# 2. Sign in or create account
# 3. Go to API Keys section
# 4. Create new key
# 5. Copy the key (starts with "sk-ant-...")
# 6. Save it securely - you'll need it for step 6
```

### 5. Create GitHub Personal Access Token

```bash
# 1. Go to https://github.com/settings/tokens
# 2. Click "Generate new token" → "Generate new token (classic)"
# 3. Name: "Translation Bot"
# 4. Expiration: 90 days (or your preference)
# 5. Scopes: Check "repo" (Full control of private repositories)
# 6. Click "Generate token"
# 7. Copy the token (starts with "ghp_...")
# 8. Save it securely - you'll need it for step 6
```

### 6. Configure GitHub Secrets

```bash
# Go to your repository on GitHub:
# https://github.com/YOUR-USERNAME/kobo-translation-test

# Navigate to: Settings → Secrets and variables → Actions → New repository secret

# Add these two secrets:

# Secret 1:
Name: ANTHROPIC_API_KEY
Value: [paste your Anthropic API key from step 4]

# Secret 2:
Name: TRANSLATION_BOT_TOKEN
Value: [paste your GitHub token from step 5]

# Click "Add secret" for each
```

### 7. Initialize Git and Push

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial setup: Translation agent test repository"

# Add remote (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/kobo-translation-test.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 8. Verify Setup

Check that everything is in place:

```bash
# On GitHub, verify you have:
# ✅ All files pushed
# ✅ .github/workflows/ directory with 2 workflow files
# ✅ docs/en/ with test files
# ✅ skills/kobo-translation/ with skill files
# ✅ scripts/ with translation_agent.py
# ✅ Two secrets configured (Settings → Secrets)

# Check Actions is enabled:
# Go to: https://github.com/YOUR-USERNAME/kobo-translation-test/actions
# Should show "Get started with GitHub Actions" or existing workflows
```

### 9. Test Locally (Recommended Before Automation)

```bash
# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r scripts/requirements.txt

# Create .env file for local testing
cp .env.example .env

# Edit .env and add your keys
nano .env  # or use any text editor

# Add:
# ANTHROPIC_API_KEY=sk-ant-...
# (no need for GITHUB_TOKEN for local testing)

# Test translation
python scripts/translation_agent.py \
  --file docs/en/test_simple.md \
  --language es \
  --test

# This should:
# ✅ Load the skill
# ✅ Translate to Spanish
# ✅ Show the translation
# ✅ Display cost estimate

# If successful, try saving:
python scripts/translation_agent.py \
  --file docs/en/test_simple.md \
  --language es \
  --save \
  --test

# Check the output:
cat docs/es/test_simple.md
```

### 10. Test GitHub Automation

```bash
# Option A: Manual trigger (easier for testing)
# 1. Go to: https://github.com/YOUR-USERNAME/kobo-translation-test/actions
# 2. Click "Translation Agent" workflow
# 3. Click "Run workflow" button
# 4. Select branch: main
# 5. Leave defaults or specify test file
# 6. Click "Run workflow"
# 7. Watch the workflow run

# Option B: Automatic trigger (tests full workflow)
# Make a change to an English file
echo "\n## New Section\nTest content" >> docs/en/test_simple.md

# Commit and push
git add docs/en/test_simple.md
git commit -m "Test: Update test document"
git push

# This should:
# 1. Trigger "Translation Trigger" workflow
# 2. Which triggers "Translation Agent" workflow
# 3. Translation agent runs
# 4. Translations generated and saved as artifacts

# Check results:
# Go to: https://github.com/YOUR-USERNAME/kobo-translation-test/actions
# Click on the latest workflow run
# Scroll down to "Artifacts" section
# Download "translations" artifact to see results
```

### 11. Review Results

```bash
# After workflow runs:

# Check the Actions tab:
# - Did both workflows complete successfully? ✅
# - Any error messages? ❌
# - Token usage shown in logs? 📊
# - Cost estimate reasonable? 💰

# Download the artifacts:
# 1. Click on workflow run
# 2. Scroll to "Artifacts"
# 3. Download "translations.zip"
# 4. Extract and review translated files

# Verify translation quality:
# - Brand terms correct? (Servidor Global, La biblioteca, etc.)
# - UI elements capitalized? (Brouillon, FORMULAIRE, etc.)
# - Gender-inclusive language? (los/as usuarios/as, etc.)
# - Links preserved? ✅
# - Formatting maintained? ✅
```

## Troubleshooting

### "Workflow not found"
- Check `.github/workflows/` directory exists
- Verify YAML files are valid (proper indentation)
- Make sure you pushed the files to GitHub

### "Secret not found"
- Go to Settings → Secrets and variables → Actions
- Verify both secrets are there
- Check spelling exactly matches: `ANTHROPIC_API_KEY` and `TRANSLATION_BOT_TOKEN`

### "Skill files not found"
```bash
# Verify locally:
ls -R skills/kobo-translation/

# Should show:
# skills/kobo-translation/:
# SKILL.md  sources/  references/  scripts/
# 
# skills/kobo-translation/references:
# brand-terminology.md  ui-terminology.md  ...

# If language-specific skills are missing, regenerate them:
python3 skills/kobo-translation/scripts/regenerate_skill.py
python3 scripts/split_skill_by_language.py
git add skills/
git commit -m "Regenerate translation skills"
git push
```

### "Translation failed"
- Check API key is valid (try in local test first)
- Check logs in GitHub Actions for specific error
- Verify skill files are readable (proper encoding, no corruption)

### "Rate limit exceeded"
- Anthropic API has rate limits
- Wait a few minutes and try again
- Consider upgrading API tier if needed

### "Local test works but GitHub Actions fails"
- Check Python version (should be 3.11 in workflow)
- Verify all dependencies in requirements.txt
- Check file paths are correct (relative to repo root)

## Next Steps After Successful Test

Once everything works:

1. ✅ **Test with complex document**
   ```bash
   python scripts/translation_agent.py \
     --file docs/en/test_complex.md \
     --language es \
     --save \
     --test
   ```

2. ✅ **Test all three languages**
   ```bash
   for lang in es fr ar; do
     python scripts/translation_agent.py \
       --file docs/en/test_complex.md \
       --language $lang \
       --save \
       --test
   done
   ```

3. ✅ **Review translation quality**
   - Compare with manual translations
   - Check all critical brand terms
   - Verify consistency

4. ✅ **Calculate costs for full deployment**
   - Count how many docs you have
   - Multiply by average cost per doc (~$0.13)
   - Add 20% buffer

5. ✅ **Plan full implementation**
   - Add PR creation logic (currently placeholder)
   - Add metadata tracking
   - Add validation checks
   - Set up reviewer workflow

6. ✅ **Migrate to production repo**
   - Copy working setup to main docs repo
   - Update paths and configuration
   - Train reviewers
   - Roll out gradually

## SRT Subtitle Translation Workflow

### Overview

The SRT translation workflow is specifically designed for translating video subtitles with:
- **Chunked translation**: Processes 20-30 subtitles at a time with overlap for context
- **Character limits**: Ensures subtitles stay readable on screen (35-42 chars ideal, 50 max)
- **Context preservation**: Maintains narrative flow while minimizing hallucinations
- **Timing preservation**: Keeps all timestamps and subtitle numbering intact

### Setup for SRT Translation

```bash
# The SRT translation skill is already included in the repository
# Structure:
# skills/
# ├── kobo-translation/       # Base translation skill
# └── kobo-translation-srt/      # SRT extension skill
#     ├── SKILL.md
#     └── references/
#         └── subtitle-guidelines.md

# SRT helper scripts are in scripts/:
# - srt_helper.py        # Parse, validate, and convert SRT files
# - translate_srt.py     # Translate SRT files with chunking
```

### Testing SRT Translation

**1. Validate an SRT file:**

```bash
# Check if an SRT file is properly formatted
python scripts/srt_helper.py validate examples/sample_transcript_en.srt

# Output shows:
# ✅ Valid / ❌ Invalid
# Subtitle count
# Any issues found (overlaps, missing text, etc.)
```

**2. Convert SRT to JSON (optional):**

```bash
# Convert to JSON for inspection
python scripts/srt_helper.py parse examples/sample_transcript_en.srt \
  --output examples/sample_transcript_en.json

# View the structure
cat examples/sample_transcript_en.json
```

**3. Translate an SRT file:**

```bash
# Translate to Spanish
python scripts/translate_srt.py examples/sample_transcript_en.srt \
  --language es \
  --video-title "Creating Forms in KoboToolbox"

# This will:
# 1. Parse the SRT file (45 subtitles in the example)
# 2. Create chunks of 25 subtitles with 3-subtitle overlap
# 3. Translate each chunk with context awareness
# 4. Output: examples/sample_transcript_en_es.srt

# Check the output
head -n 20 examples/sample_transcript_en_es.srt
```

**4. Customize chunking parameters:**

```bash
# Adjust chunk size and overlap for different needs
python scripts/translate_srt.py examples/sample_transcript_en.srt \
  --language fr \
  --chunk-size 20 \     # Smaller chunks = more API calls but better accuracy
  --overlap 5 \          # More overlap = better context but more token usage
  --video-title "Tutorial Title"
```

### SRT Translation Best Practices

**Chunk Size Guidelines:**

| Video Length | Chunk Size | Overlap | Rationale |
|--------------|------------|---------|-----------|
| Short (<5 min) | 30-40 | 3 | Full context fits, fewer chunks |
| Medium (5-15 min) | 25 | 3-5 | **Default - balanced** |
| Long (15-30 min) | 20 | 5 | More overlap prevents drift |
| Very Long (>30 min) | 15-20 | 5-7 | Tighter chunking for consistency |

**Cost Estimates for SRT Translation:**

```bash
# Sample video: 2-minute tutorial (45 subtitles)
# Chunk size: 25, Overlap: 3
# Result: 2 chunks

# Per language costs (approximate):
Spanish:  $0.25 - $0.35
French:   $0.25 - $0.35  
Arabic:   $0.30 - $0.40 (RTL complexity)

# All three languages: ~$0.90 for a 2-minute video

# For longer videos:
# 10-minute video (~225 subtitles): ~$2.00-3.00 per language
# 30-minute video (~675 subtitles): ~$6.00-9.00 per language
# 60-minute video (~1350 subtitles): ~$12.00-18.00 per language
```

**Quality Assurance for Subtitles:**

```bash
# After translating, validate the output
python scripts/srt_helper.py validate examples/sample_transcript_en_es.srt

# Check for:
# ✅ All subtitles translated (count matches)
# ✅ No timing changes
# ✅ Sequential numbering maintained
# ✅ No overlaps introduced

# Manual review checklist:
# - Brand terms correct (Servidor Global, La biblioteca de preguntas)
# - Character limits respected (<50 chars per line)
# - Natural spoken language
# - Technical terms in English (list_name, cascading select)
# - Consistent terminology throughout
```

### SRT Workflow Integration

**Option 1: Local batch translation**

```bash
#!/bin/bash
# translate_video_subtitles.sh

SOURCE_SRT="$1"
VIDEO_TITLE="$2"

for lang in es fr ar; do
  echo "Translating to $lang..."
  python scripts/translate_srt.py "$SOURCE_SRT" \
    --language "$lang" \
    --video-title "$VIDEO_TITLE"
done

echo "All translations complete!"
```

Usage:
```bash
./translate_video_subtitles.sh \
  "video_tutorials/intro.srt" \
  "Introduction to KoboToolbox"
```

**Option 2: Manual workflow**

```bash
# 1. Create English subtitles (YouTube auto-generate or manual)
# 2. Export as SRT
# 3. Clean and validate
python scripts/srt_helper.py validate video.srt

# 4. Translate
python scripts/translate_srt.py video.srt --language es

# 5. Review translation (open in subtitle editor)
# 6. Upload to video platform

# 7. Repeat for other languages
```

**Option 3: GitHub Actions (future)**

```yaml
# .github/workflows/translate-subtitles.yml
# (Not included in current test repo, but could be added)

name: Translate Video Subtitles
on:
  workflow_dispatch:
    inputs:
      srt_file:
        description: 'Path to SRT file'
        required: true
      video_title:
        description: 'Video title for context'
        required: true

jobs:
  translate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r scripts/requirements.txt
      - name: Translate subtitles
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          for lang in es fr ar; do
            python scripts/translate_srt.py "${{ github.event.inputs.srt_file }}" \
              --language "$lang" \
              --video-title "${{ github.event.inputs.video_title }}"
          done
      - name: Upload translations
        uses: actions/upload-artifact@v2
        with:
          name: translated-subtitles
          path: '**/*_es.srt'
```

### Common SRT Translation Issues

**Issue: Subtitles too long after translation**
```bash
# Solution: The translator tries to compress naturally,
# but you can manually edit if needed
# Use a subtitle editor like:
# - Subtitle Edit (Windows/Linux)
# - Aegisub (cross-platform)
# - Subtitle Workshop

# Check character counts:
python -c "
import sys
with open(sys.argv[1]) as f:
    for line in f:
        if line.strip() and '-->' not in line and not line.strip().isdigit():
            if len(line.strip()) > 50:
                print(f'Long: {len(line.strip())} chars - {line.strip()[:60]}...')
" examples/sample_transcript_en_es.srt
```

**Issue: Technical terms translated incorrectly**
```bash
# The SRT skill keeps XLSForm terms in English
# But verify by searching:
grep -n "list_name\|cascading" examples/sample_transcript_en_es.srt

# Should show English terms preserved
```

**Issue: Brand terms incorrect**
```bash
# Check server names:
grep -n "Servidor" examples/sample_transcript_en_es.srt
# Should be "Servidor Global" NOT "Servidor Global de KoboToolbox"

# Check Question Library:
grep -n "biblioteca" examples/sample_transcript_en_es.srt  
# Should be "La biblioteca de preguntas" with capital L
```

**Issue: Context lost between chunks**
```bash
# Increase overlap:
python scripts/translate_srt.py video.srt \
  --language es \
  --overlap 7  # More context between chunks

# Or reduce chunk size:
python scripts/translate_srt.py video.srt \
  --language es \
  --chunk-size 15  # Smaller chunks, more frequent context
```

### SRT Testing Checklist

Before using SRT translations in production:

- [ ] Test with short video (2-5 minutes)
- [ ] Validate all brand terms are correct
- [ ] Check character limits (no lines >50 chars)
- [ ] Verify technical terms in English
- [ ] Test with subtitle editor (timing sync)
- [ ] Calculate actual costs vs estimates
- [ ] Review with native speaker
- [ ] Test on actual video player
- [ ] Check readability at normal playback speed
- [ ] Verify formality level (tú vs vous)

### Example: Complete SRT Workflow

```bash
# Starting with English subtitles from YouTube
# File: intro_to_kobo.srt (English)

# Step 1: Validate source
python scripts/srt_helper.py validate intro_to_kobo.srt
# ✅ Valid, 120 subtitles, 5.2 minutes

# Step 2: Translate to Spanish
python scripts/translate_srt.py intro_to_kobo.srt \
  --language es \
  --video-title "Introduction to KoboToolbox" \
  --chunk-size 25 \
  --overlap 3

# Output:
# 📦 Created 5 chunks
# 🤖 Translating chunk 1/5... ✓
# 🤖 Translating chunk 2/5... ✓
# 🤖 Translating chunk 3/5... ✓
# 🤖 Translating chunk 4/5... ✓
# 🤖 Translating chunk 5/5... ✓
# ✅ Translated 120 subtitles
# 💾 Saved to: intro_to_kobo_es.srt
# 💰 Estimated cost: $1.85

# Step 3: Validate translation
python scripts/srt_helper.py validate intro_to_kobo_es.srt
# ✅ Valid, 120 subtitles

# Step 4: Check key terms
grep "Servidor Global" intro_to_kobo_es.srt
grep "La biblioteca de preguntas" intro_to_kobo_es.srt
# ✅ All correct

# Step 5: Manual review in subtitle editor
# Open in Aegisub or Subtitle Edit
# Check timing, readability, and flow

# Step 6: Upload to YouTube
# Video → Subtitles → Upload file → intro_to_kobo_es.srt

# Step 7: Repeat for other languages
python scripts/translate_srt.py intro_to_kobo.srt --language fr
python scripts/translate_srt.py intro_to_kobo.srt --language ar

# Total cost: ~$5.50 for all three languages
```

### When to Use SRT vs Document Translation

**Use SRT translation (`translate_srt.py`) for:**
- ✅ Video subtitles and captions
- ✅ Webinar transcripts
- ✅ Tutorial voiceovers
- ✅ Live event captions
- ✅ Any time-coded transcripts

**Use document translation (`translation_agent.py`) for:**
- ✅ Documentation articles
- ✅ Support articles
- ✅ Blog posts
- ✅ Marketing materials
- ✅ Email templates

**Key differences:**

| Feature | SRT | Document |
|---------|-----|----------|
| Format | Time-coded subtitles | Markdown/HTML |
| Character limits | Yes (35-42 ideal, 50 max) | No limits |
| XLSForm terms | English only | English + translation |
| Processing | Chunked with overlap | Full or diff-based |
| Context | Sequential narrative | Section-based |
| Cost per 1000 words | Higher (chunking overhead) | Lower (bulk processing) |

## Cost Tracking

Keep track of your testing costs:

| Test | Files | Languages | Total Cost | Date |
|------|-------|-----------|------------|------|
| Initial | 1 simple | es | $0.09 | |
| Complex | 1 complex | es | $0.15 | |
| All langs | 1 complex | es,fr,ar | $0.45 | |
| Full test | 2 files | es,fr,ar | $0.90 | |

Total budget for testing: ~$10-20 should be plenty

## Support

If you get stuck:
1. Check the troubleshooting section above
2. Review GitHub Actions logs carefully
3. Test locally to isolate issues
4. Check that skill files are valid and complete

## Ready to Go?

If you've completed all steps and tests pass, you're ready to use this for real translations!

The next document explains how to add PR creation and full automation.
