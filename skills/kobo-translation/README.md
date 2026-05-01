# KoboToolbox Translation Skill - Maintainer Guide

This skill is designed to be **human-maintained** and **AI-executed**. Humans update the source files, run a script, and the skill regenerates itself for AI agents to use.

---

## Quick Start

**To pull the latest terminology from Google Sheets and regenerate:**
```bash
python scripts/sync_and_update.py --fetch
```

**To regenerate from the local cached glossary (offline):**
```bash
python scripts/update_skill.py
```

**To update guidelines only:**
```bash
# 1. Edit the appropriate markdown file in sources/
# 2. Run validation and regeneration
python scripts/update_skill.py
```

---

## File Structure

```
kobo-translation/
├── SKILL.md                    # Main skill file (AI reads this)
├── README.md                   # This file (for human maintainers)
│
├── sources/                    # ✏️ HUMAN-EDITED SOURCE FILES
│   ├── glossary.xlsx           # Cached copy of Google Sheet (offline fallback)
│   ├── style-guide.md          # General translation guidelines
│   ├── workflow-rules.md       # Translation workflow & checklists
│   └── language-rules.md       # French/Spanish/Arabic specific rules
│
├── references/                 # 🤖 AUTO-GENERATED (do not edit directly)
│   ├── brand-terminology.md
│   ├── ui-terminology.md
│   ├── form-building-terms.md
│   ├── question-types.md
│   ├── data-collection-terms.md
│   ├── course-terminology.md
│   ├── documentation-terminology.md
│   ├── data-management-terms.md
│   ├── sentence-structures.md  # Recurring sentence patterns
│   └── article-titles.md       # Official article titles in all languages
│
└── scripts/                    # Automation scripts
    ├── fetch_glossary.py       # Download latest glossary from Google Sheets
    ├── update_skill.py         # Main update script (validate + regenerate)
    ├── validate_sources.py     # Check source file integrity
    ├── regenerate_skill.py     # Regenerate references from glossary
    └── sync_and_update.py      # Fetch + update in one step (--fetch flag)
```

---

## Source Files: What Each Does

### `glossary.xlsx` — Terminology Database

This is a **cached copy** of the published Google Sheet. Run `python scripts/fetch_glossary.py` to refresh it. The regeneration script reads this file and generates the `references/*.md` files.

**Sheets (do not rename):**
| Sheet Name | Generates | Contains |
|------------|-----------|----------|
| `Proper & Kobo specific` | `brand-terminology.md` | Brand terms, servers, plans |
| `Academy` | `course-terminology.md` | Course and learning platform terms |
| `Documentation` | `documentation-terminology.md` | Help Center and doc terms |
| `Data collection` | `data-collection-terms.md` | Data collection concepts |
| `Form building` | `form-building-terms.md` | XLSForm and form building |
| `Data management` | `data-management-terms.md` | Data management terms |
| `Formbuilder question types` | `question-types.md` | Question type translations |
| `Appearances` | `question-types.md` | Question appearance translations |
| `Formbuilder UI ` | `ui-terminology.md` | Formbuilder UI elements |
| `KoboCollect` | `ui-terminology.md` | KoboCollect UI elements |
| `XLSForm` | `form-building-terms.md` | XLSForm-specific terms |
| `Sentence structures` | `sentence-structures.md` | Recurring sentence patterns |
| `Article titles` | `article-titles.md` | Official article titles (all languages) |

The `Article titles` sheet has a different column structure: `File name`, `English`, `French`, `Spanish`, `Arabic`, `Notes`. Titles are marked OFFICIAL — the AI must use them verbatim when cross-referencing articles.

### `style-guide.md` — General Guidelines

Contains overarching translation principles:
- Localization vs. literal translation
- Tone and formality levels
- Gender-inclusive language rules
- Formatting rules (HTML, markdown, links)
- XLSForm handling

### `workflow-rules.md` — Process & Checklists

Contains operational guidance:
- Pre-translation checklist
- Decision tree for term lookup
- Common pitfalls and errors
- Quality checklist
- Translation examples

### `language-rules.md` — Language-Specific Rules

Contains detailed rules per language:
- French-specific patterns
- Spanish-specific patterns
- Arabic-specific patterns
- Cross-language rules

---

## Editing Guidelines

### ✅ Safe to Edit

| File | What You Can Change |
|------|---------------------|
| `glossary.xlsx` | Add/edit/remove terms in any cell |
| `glossary.xlsx` | Add notes in the Notes column |
| `glossary.xlsx` | Reorder rows within sheets |
| `style-guide.md` | Any content |
| `workflow-rules.md` | Any content |
| `language-rules.md` | Any content |
| `SKILL.md` | Any content (but see notes below) |

### ⚠️ Do Not Change

| Item | Why |
|------|-----|
| **Sheet names** in glossary.xlsx | Script uses exact names to map to output files |
| **Column names** in glossary.xlsx | Must be: `English`, `French`, `Spanish`, `Arabic`, `Notes` |
| **Files in `references/`** | These are auto-generated; your changes will be overwritten |
| **Script files** | Unless you understand Python |

### 🔄 What Happens When You Edit

| You Edit... | What Regenerates |
|-------------|------------------|
| `glossary.xlsx` | All `references/*.md` files |
| `style-guide.md` | Nothing auto-regenerates (reference only) |
| `workflow-rules.md` | Nothing auto-regenerates (reference only) |
| `language-rules.md` | Nothing auto-regenerates (reference only) |
| `SKILL.md` | Nothing (this IS the output) |

---

## Glossary Editing Rules

### Column Structure (Required)

Every sheet must have these columns in this order:
```
| English | French | Spanish | Arabic | Notes |
```

- **English**: Required. The source term.
- **French**: Translation (can be empty)
- **Spanish**: Translation (can be empty)
- **Arabic**: Translation (can be empty)
- **Notes**: Usage notes, context, warnings (can be empty)

### Adding New Terms

1. Find the appropriate sheet for your term
2. Add a new row at the end (or insert where logical)
3. Fill in at minimum: `English` and one translation
4. Add `Notes` if there are special rules

**Example: Adding a new brand term**
```
| English              | French                  | Spanish                | Arabic | Notes                          |
| New Feature Name     | Nouvelle fonctionnalité | Nueva funcionalidad    |        | Capitalize in UI contexts      |
```

### Notes Column Best Practices

Use the Notes column for:
- ⚠️ Common errors to avoid
- 🚨 Critical usage rules
- Context-specific guidance
- Cross-references to other terms

**Good notes examples:**
- `FR: not "télécharger". Use "importer"`
- `ES: Use "manejo" for data, "gestión" for teams`
- `Must include English in parentheses on first use`
- `🚨 Capital L required - brand feature`

### Multi-line Translations

If a term has multiple valid translations, separate with newlines or slashes:
```
| English    | French                                    |
| Upload     | importer / envoyer (context-dependent)    |
```

Or use the Notes column to explain when to use each.

---

## Markdown File Editing Rules

### General Guidelines

1. **Use standard Markdown** — Headers, lists, tables, code blocks
2. **Keep structure consistent** — Don't remove major sections
3. **Use clear examples** — Show right ✅ and wrong ❌
4. **Be concise** — AI context windows are limited

### Section Headers

Keep the main section headers consistent so the validation script can verify file integrity:

**style-guide.md must contain:**
- "Formality" (or "formality")
- "Gender" (or "gender")

**workflow-rules.md must contain:**
- "Checklist" (or "checklist")
- "Decision" (or "decision")

**language-rules.md must contain:**
- "French" (or "french")
- "Spanish" (or "spanish")

### Adding New Rules

When adding new translation rules:

1. **Find the right file:**
   - General guidelines → `style-guide.md`
   - Process/workflow → `workflow-rules.md`
   - Language-specific → `language-rules.md`

2. **Follow existing patterns:**
   - Use tables for term comparisons
   - Use ❌/✅ for right/wrong examples
   - Include context and reasoning

3. **Update SKILL.md if needed:**
   - Major new rules should also appear in SKILL.md
   - SKILL.md is what the AI agent reads directly

---

## Running Updates

### Fetch + Full Update (Recommended)

```bash
python scripts/sync_and_update.py --fetch
```

Fetches the latest glossary from Google Sheets, then validates and regenerates all reference files.

### Full Update from Local Cache

```bash
python scripts/update_skill.py
```

Use this when offline or when you only changed the `.md` source files.

### Validation Only

```bash
python scripts/validate_sources.py
```

Use this to check your changes before committing.

### Fetch Glossary Only

```bash
python scripts/fetch_glossary.py
```

Downloads the Google Sheet to `sources/glossary.xlsx` without regenerating.

### Sync from Local Files

If you have a locally exported copy of the glossary:

```bash
python scripts/sync_and_update.py path/to/glossary.xlsx path/to/style-guide.md
```

Or point to a directory containing the files:

```bash
python scripts/sync_and_update.py ~/Downloads/translation-updates/
```

---

## Troubleshooting

### "Missing sheets" Error

**Problem:** The glossary is missing expected sheets.

**Solution:** Check that all 13 sheets exist with exact names (including the trailing space on "Formbuilder UI ").

### "Missing columns" Error

**Problem:** A sheet is missing required columns.

**Solution:** Ensure every sheet has: `English`, `French`, `Spanish`, `Arabic`, `Notes`

### "Missing critical terms" Error

**Problem:** Key brand terms are missing from the glossary.

**Solution:** These terms must exist in "Proper & Kobo specific":
- Global KoboToolbox Server
- European Union KoboToolbox Server
- Question Library
- KoboToolbox Academy
- Community Forum
- Help Center

### Changes Not Appearing

**Problem:** You edited a file but changes aren't reflected.

**Check:**
1. Did you edit the right file? (`sources/` not `references/`)
2. Did you run `python scripts/update_skill.py`?
3. For markdown files: Did you also update SKILL.md if needed?

### Script Errors

**Problem:** Python script fails to run.

**Check:**
1. Python 3.8+ is installed
2. pandas is installed: `pip install pandas openpyxl`
3. You're running from the skill root directory

---

## Best Practices

### Before Making Changes

1. **Back up the current state** (or use git)
2. **Run validation** to ensure starting point is clean
3. **Plan your changes** — what files need updating?

### After Making Changes

1. **Run `update_skill.py`** to regenerate and validate
2. **Review generated files** in `references/`
3. **Test with a sample translation** if possible
4. **Commit changes** with a descriptive message

### Version Control Tips

If using git:
```bash
# Good commit messages
git commit -m "Add new question type: Audio Recording"
git commit -m "Fix French server name translation"
git commit -m "Add Spanish rules for 'management' context"

# What to track
# ✅ Track: sources/, scripts/, SKILL.md, README.md
# ⚠️ Optional: references/ (can be regenerated)
```

### Collaboration

- **One person edits glossary at a time** to avoid merge conflicts
- **Use clear Notes** so others understand term choices
- **Document significant changes** in commit messages

---

## Quick Reference Card

| Task | Command |
|------|---------|
| Fetch latest + update everything | `python scripts/sync_and_update.py --fetch` |
| Update from local cache | `python scripts/update_skill.py` |
| Fetch glossary only | `python scripts/fetch_glossary.py` |
| Validate only | `python scripts/validate_sources.py` |
| Import local files | `python scripts/sync_and_update.py <files>` |

| Edit This | For This Purpose |
|-----------|------------------|
| `sources/glossary.xlsx` | Add/change terminology |
| `sources/style-guide.md` | Change general guidelines |
| `sources/workflow-rules.md` | Change process/checklists |
| `sources/language-rules.md` | Change language-specific rules |
| `SKILL.md` | Change what AI reads directly |

| Never Edit | Why |
|------------|-----|
| `references/*.md` | Auto-generated, will be overwritten |
| Sheet/column names | Scripts depend on exact names |

---

## Getting Help

- **Script issues:** Check Python/pandas installation
- **Translation questions:** Refer to source markdown files
- **Terminology conflicts:** Check Notes column in glossary
- **Process questions:** See workflow-rules.md
