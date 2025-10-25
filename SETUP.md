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
# Create skills directory
mkdir -p skills

# Copy the kobo-translation skill you created earlier
# Copy all these files:
# - SKILL.md
# - references/brand-terminology.md
# - references/ui-terminology.md
# - references/data-collection-terms.md
# - references/form-building-terms.md
# - references/question-types.md
# - references/course-terminology.md

# Your structure should look like:
# skills/
# └── kobo-translation/
#     ├── SKILL.md
#     └── references/
#         ├── brand-terminology.md
#         ├── ui-terminology.md
#         └── ...
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
# SKILL.md  references/
# 
# skills/kobo-translation/references:
# brand-terminology.md  ui-terminology.md  ...

# If missing, copy them and push:
git add skills/
git commit -m "Add kobo-translation skill files"
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
