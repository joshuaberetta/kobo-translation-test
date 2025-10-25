# Quick Start Checklist ✓

Use this checklist to set up your test repository in ~30 minutes.

## Prerequisites (5 min)
- [ ] GitHub account
- [ ] Python 3.11+ installed
- [ ] Git installed
- [ ] Text editor ready

## Setup Steps (15 min)

### 1. Get API Keys
- [ ] Get Anthropic API key from https://console.anthropic.com/
- [ ] Create GitHub Personal Access Token (Settings → Tokens)
  - [ ] Scope: "repo" checked
  - [ ] Save both keys securely

### 2. Create Repository
- [ ] Create new repo on GitHub: `kobo-translation-test`
- [ ] Keep it private for testing
- [ ] Do NOT initialize with README

### 3. Prepare Files Locally
- [ ] Extract the test-repo files
- [ ] Copy kobo-translation skill to `skills/kobo-translation/`
- [ ] Verify structure:
  ```
  kobo-translation-test/
  ├── .github/workflows/      ✓
  ├── docs/en/               ✓
  ├── skills/kobo-translation/ ✓
  └── scripts/               ✓
  ```

### 4. Configure Secrets
Go to GitHub repo: Settings → Secrets → Actions
- [ ] Add `ANTHROPIC_API_KEY` 
- [ ] Add `TRANSLATION_BOT_TOKEN`

### 5. Push to GitHub
```bash
cd kobo-translation-test
git init
git add .
git commit -m "Initial setup"
git remote add origin https://github.com/YOUR-USERNAME/kobo-translation-test.git
git push -u origin main
```
- [ ] All files pushed to GitHub
- [ ] Workflows visible in Actions tab

## Test Locally (5 min)

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install
pip install -r scripts/requirements.txt

# Create .env
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env

# Test
python scripts/translation_agent.py \
  --file docs/en/test_simple.md \
  --language es \
  --test
```

- [ ] Skill loads successfully
- [ ] Translation completes
- [ ] Cost shown (~$0.09)
- [ ] Translation looks good

## Test on GitHub (5 min)

```bash
# Make a change
echo "\n## Test\nContent" >> docs/en/test_simple.md
git add .
git commit -m "Test translation"
git push
```

Then check:
- [ ] Go to Actions tab
- [ ] "Translation Trigger" runs ✓
- [ ] "Translation Agent" runs ✓
- [ ] Download artifacts
- [ ] Review translations

## Success Criteria

You're ready to proceed if:
- [ ] Local translation works
- [ ] GitHub Actions runs without errors
- [ ] Brand terms translated correctly
- [ ] Cost per translation acceptable (~$0.09-0.15)
- [ ] Spanish has "Servidor Global" (not "de KoboToolbox")
- [ ] French has "Le serveur KoboToolbox mondial"
- [ ] Question Library has capital "L" in both languages

## If Something Fails

**Skill not found:**
```bash
ls -R skills/kobo-translation/
# Should show SKILL.md and references/
```

**API error:**
- Check API key is valid
- Try in browser: https://console.anthropic.com/

**GitHub workflow fails:**
- Check secrets are set correctly
- View workflow logs for specific error
- Try manual trigger first

## Cost Budget

Set aside for testing:
- 10 test runs × $0.15 = **$1.50**
- Full test suite (all languages) = **$5.00**
- **Total recommended: $10-20**

## Next Steps

Once everything works:
1. Test with complex document
2. Test all three languages
3. Review quality carefully
4. Plan production deployment

---

**Estimated Time:** 30 minutes  
**Estimated Cost:** $1-2 for testing  
**Difficulty:** Beginner-friendly
