# KoboToolbox Translation Agent

AI-powered translation workflow for KoboToolbox documentation. Translates markdown docs and video subtitles with consistent brand terminology across Spanish, French, and Arabic.

## Features

- **Documentation Translation** — Automated translation with brand terminology preservation
- **SRT Subtitle Translation** — Context-aware video subtitle translation with chunking
- **GitHub Actions Integration** — Automatic translation on commit or manual trigger
- **Language-Specific Skills** — Optimized translation context for each language pair
- **UI Template System** — Pre-resolved `{{ui:key}}` and `{{collect:key}}` placeholders for exact UI string consistency
- **Prompt Caching** — ~90% cost reduction on repeated translations

## Repository Structure

```
kobo-translation-test/
├── .github/workflows/
│   ├── auto-translate.yml       # Triggers on push to docs/en/
│   ├── bulk-retranslate.yml     # Manual bulk retranslation
│   ├── translate-srt.yml        # SRT subtitle translation
│   └── test-skills.yml          # Test skill changes
├── docs/
│   ├── en/                      # English source (source of truth)
│   ├── es/ fr/ ar/              # Auto-generated translations
│   └── guides/                  # Detailed documentation
├── skills/
│   ├── kobo-translation/        # ⚠️ EDIT HERE (source of truth)
│   │   ├── sources/             # Human-maintained inputs
│   │   │   ├── glossary.xlsx    # Cached copy of Google Sheet (offline fallback)
│   │   │   ├── style-guide.md
│   │   │   ├── workflow-rules.md
│   │   │   └── language-rules.md
│   │   ├── references/          # Auto-generated — do not edit directly
│   │   │   ├── brand-terminology.md
│   │   │   ├── article-titles.md        # Official article titles (all languages)
│   │   │   ├── sentence-structures.md   # Recurring sentence patterns
│   │   │   ├── transifex-ui-strings.md  # Web UI strings
│   │   │   ├── collect-strings.json     # Android app strings
│   │   │   └── ... (terminology files)
│   │   └── scripts/             # Maintenance automation
│   ├── kobo-translation-{es,fr,ar}/  # Auto-generated language variants
│   └── kobo-translation-srt/    # SRT extension skill
├── scripts/
│   ├── translation_agent.py     # Main doc translation
│   ├── bulk_retranslate.py      # Bulk retranslation
│   ├── resolve_ui_templates.py  # UI/collect template resolver
│   ├── parse_transifex_po.py    # Transifex PO parser
│   ├── parse_collect_strings.py # Android XML parser
│   ├── split_skill_by_language.py  # Language skill generator
│   ├── translate_srt.py         # SRT translation
│   └── requirements.txt
├── external/
│   └── form-builder-translations/  # Transifex PO files (git submodule)
├── transcripts/                 # Video subtitle files
└── examples/                    # Sample files and test results
```

## Quick Start

### Prerequisites

- Python 3.11+
- Git
- Anthropic API key ([get one here](https://console.anthropic.com/))
- GitHub Personal Access Token (for automation)

### 1. Install dependencies

```bash
git clone --recursive https://github.com/YOUR-ORG/kobo-translation-test.git
cd kobo-translation-test
pip install -r scripts/requirements.txt
```

The `--recursive` flag initializes the `external/form-builder-translations` submodule needed for UI template resolution. If you already cloned without it:

```bash
git submodule update --init --recursive
```

### 2. Configure environment

```bash
cp .env.example .env
# Edit .env and set ANTHROPIC_API_KEY
```

### 3. Configure GitHub Secrets

Go to **Settings → Secrets → Actions** and add:
- `ANTHROPIC_API_KEY` — Your Claude API key
- `TRANSLATION_BOT_TOKEN` — GitHub Personal Access Token (repo scope)

### 4. Test locally

```bash
# Test documentation translation (lean context — most articles)
python scripts/translation_agent.py \
    --file docs/en/about_kobotoolbox.md \
    --language es \
    --test --verbose

# Add Transifex UI strings for articles heavy with button/menu/tab references
python scripts/translation_agent.py \
    --file docs/en/about_kobotoolbox.md \
    --language es \
    --test --include-transifex

# Add KoboCollect Android strings for KoboCollect-specific content
python scripts/translation_agent.py \
    --file docs/en/about_kobotoolbox.md \
    --language es \
    --test --include-collect

# Test SRT subtitle translation
python scripts/translate_srt.py \
    examples/sample_transcript_en.srt \
    --language es
```

### 5. Trigger automation

Edit any file in `docs/en/`, commit and push — GitHub Actions will auto-translate to es, fr, ar and open a PR for review.

## UI Template System

Authors can embed UI string placeholders in English docs so translations always use exact UI terminology.

### Syntax

**Web interface strings (from Transifex):**
```markdown
Click **{{ui:Deploy}}** to publish your form.
Navigate to the {{ui:Form|upper}} builder.
```

**Android app strings (from KoboCollect):**
```markdown
Tap **{{collect:enter_data}}** to start a new form.
Check {{collect:send_data|bold}} to see forms ready to send.
```

**Formatting modifiers** (combinable with commas):
- `bold` → `**text**`
- `italic` → `*text*`
- `code` → `` `text` ``
- `upper` → `TEXT`
- `lower` → `text`

Example: `{{collect:finalize|upper,bold}}` → `**FINALISER**`

### Workflow

1. Author writes English doc with `{{ui:Deploy}}` or `{{collect:enter_data}}` placeholders
2. Pre-translation: templates resolved to target-language strings
3. AI translates remaining narrative content
4. Result: exact UI terminology + natural prose translation

### Generating reference files

**Web UI strings** — update after Transifex syncs (1st and 15th of month):

```bash
cd external/form-builder-translations && git pull origin master && cd ../..
python scripts/parse_transifex_po.py --repo-path external/form-builder-translations
# Output: skills/kobo-translation/references/transifex-ui-strings.md
```

**Android app strings** — update after KoboCollect releases:

```bash
python3 scripts/parse_collect_strings.py
# Output: skills/kobo-translation/references/collect-strings.json
```

### Resolving templates manually

```bash
python scripts/resolve_ui_templates.py \
    --input docs/en/article.md \
    --language fr \
    --po-repo external/form-builder-translations

# In-place resolution
python scripts/resolve_ui_templates.py \
    --input docs/en/article.md --language es \
    --po-repo external/form-builder-translations --in-place

# Strict mode (exit with error if any templates unresolved)
python scripts/resolve_ui_templates.py \
    --input docs/en/article.md --language ar \
    --po-repo external/form-builder-translations --strict
```

To find the correct key for a UI string, check `skills/kobo-translation/references/transifex-ui-strings.md`.

## Translation Context Flags

The agent loads a lean set of reference files by default (~9 terminology files). Two large reference files are opt-in to avoid overloading the context window:

| Flag | File | Size | When to use |
|------|------|------|-------------|
| `--include-transifex` | `transifex-ui-strings.md` | ~150k chars | Article has many UI element references (buttons, tabs, menus, dialogs) |
| `--include-collect` | `collect-strings.json` | ~60–70k chars | Article is specifically about KoboCollect (the Android app) |

Both flags are off by default. Most articles translate well without them — the lean context keeps quality high by avoiding token pressure on the model.

```bash
# Default — lean context, suitable for most articles
python scripts/translation_agent.py --file docs/en/article.md --language fr

# UI-heavy article (lots of button/menu references)
python scripts/translation_agent.py --file docs/en/article.md --language fr --include-transifex

# KoboCollect-specific article
python scripts/translation_agent.py --file docs/en/article.md --language fr --include-collect

# Both (e.g. a KoboCollect article with many UI references)
python scripts/translation_agent.py --file docs/en/article.md --language fr --include-transifex --include-collect
```

## Common Workflows

### Auto-translate on push

Push any change to `docs/en/` and the workflow opens a PR with translations for all configured languages.

### Manual translation

1. Go to **Actions → Auto-Translate Documentation**
2. Click **Run workflow**, enter files and languages
3. Review and merge the PR

### Bulk retranslation

Use this after updating skills to regenerate existing translations:

```bash
# Test on a few files first
python scripts/bulk_retranslate.py --language es --files test_simple.md test_complex.md

# All docs, all languages
python scripts/bulk_retranslate.py --language es fr ar

# Dry run to preview scope
python scripts/bulk_retranslate.py --language es --dry-run
```

Or via GitHub Actions: **Actions → Bulk Retranslate Documentation**.

### SRT subtitle translation

```bash
# Local
python scripts/translate_srt.py your_video.srt --language es
```

Via GitHub Actions: upload `.srt` to `transcripts/en/`, then **Actions → Translate SRT Subtitles**.

## Maintaining Translation Skills

All terminology lives in `skills/kobo-translation/sources/`. The glossary comes from a published Google Sheet; `glossary.xlsx` is a committed offline fallback — run `fetch_glossary.py` to refresh it before regenerating.

### Update workflow

```
1. Fetch latest glossary from Google Sheets
   python3 skills/kobo-translation/scripts/fetch_glossary.py
   ↓
2. Regenerate skill references and SKILL.md
   python3 skills/kobo-translation/scripts/regenerate_skill.py
   ↓
   (or combine steps 1–2: python3 skills/kobo-translation/scripts/sync_and_update.py --fetch)
   ↓
3. python3 scripts/split_skill_by_language.py
   ↓
4. Commit all changes (sources + generated skills)
   ↓
5. Translation agent picks up updated skills automatically
```

To update only the `.md` source files (style guide, workflow rules, language rules) without fetching the glossary, edit them directly in `sources/` then run step 2 onward.

**Do not manually edit** `skills/kobo-translation-{es,fr,ar}/` — these are overwritten by `split_skill_by_language.py`.

### Testing skill updates

```bash
# 1. Fetch and regenerate
python3 skills/kobo-translation/scripts/sync_and_update.py --fetch
python3 scripts/split_skill_by_language.py

# 2. Test on sample files
python scripts/bulk_retranslate.py --language es --files test_simple.md test_complex.md

# 3. Review changes
git diff docs/es/test_simple.md

# 4. If satisfied, retranslate everything
python scripts/bulk_retranslate.py --language es fr ar
```

## Quality Checklist

When reviewing translation PRs:

**Brand Terms**
- [ ] Server names correct — Spanish: "Servidor Global" (not "de KoboToolbox")
- [ ] French server: "Le serveur KoboToolbox mondial" (with "Le")
- [ ] Question Library: capital "La" in both languages
- [ ] Formbuilder: English term in parentheses on first reference

**UI Elements**
- [ ] Capitalization matches UI (Brouillon, Borrador, DONNÉES, DATOS)
- [ ] Button names match Transifex translations

**Language Style**
- [ ] Spanish: informal "tú", gender-inclusive "los/as"
- [ ] French: formal "vous", "utilisatrices et utilisateurs"

**Formatting**
- [ ] All links preserved
- [ ] Headings and structure identical to source
- [ ] No untranslated English content

## Troubleshooting

**Workflow not triggering:**
- Verify GitHub Actions is enabled for the repository
- Check workflow file paths match the files you changed

**Translation agent fails:**
- Verify `ANTHROPIC_API_KEY` secret is set
- Check `TRANSLATION_BOT_TOKEN` has repo permissions
- Review logs in the GitHub Actions run

**Skill files not found:**
```bash
ls -R skills/kobo-translation/
# Should show SKILL.md, sources/, references/, scripts/

# Regenerate language-specific skills if missing:
python3 skills/kobo-translation/scripts/regenerate_skill.py
python3 scripts/split_skill_by_language.py
```

**Templates not resolving:**
```bash
# Is submodule initialized?
ls external/form-builder-translations/es/LC_MESSAGES/djangojs.po

# If empty:
git submodule update --init --recursive

# Check key spelling against reference:
cat skills/kobo-translation/references/transifex-ui-strings.md | grep -i "deploy"
```

**Translation quality issues:**
- Ensure language-specific skills are up to date (re-run `split_skill_by_language.py`)
- Review terminology in `skills/kobo-translation/sources/`
- Test locally with `--verbose` to see which skill files are loaded

## Cost Estimates

**Documentation:**
- Test run (2-3 files, 1 language): ~$0.05–0.15
- Full corpus (~100 files, 1 language): ~$15–30 initial, ~$1–5 per update

**Subtitles:**
- 30-minute video, 1 language: ~$2–5 (with prompt caching)
- Prompt caching saves ~90% on repeated/chunked translations

## Documentation

- [docs/guides/SETUP.md](docs/guides/SETUP.md) — Complete setup instructions
- [docs/guides/QUICKSTART.md](docs/guides/QUICKSTART.md) — Fast setup checklist
- [docs/guides/BULK_RETRANSLATION.md](docs/guides/BULK_RETRANSLATION.md) — Bulk retranslation guide
- [docs/guides/UI_TEMPLATE_GUIDE.md](docs/guides/UI_TEMPLATE_GUIDE.md) — Full UI template reference
- [docs/guides/SRT_WORKFLOW.md](docs/guides/SRT_WORKFLOW.md) — Video subtitle translation
- [docs/guides/PROMPT_CACHING_IMPLEMENTATION.md](docs/guides/PROMPT_CACHING_IMPLEMENTATION.md) — Cost optimization details
- [skills/kobo-translation/README.md](skills/kobo-translation/README.md) — Skill maintainer guide
