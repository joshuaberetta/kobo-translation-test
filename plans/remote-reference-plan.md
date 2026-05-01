# Plan: Remote Google Sheet as Source of Truth

## Goal

Replace the manually-maintained `sources/glossary.xlsx` with a live pull from the published Google Sheet. The local file becomes a cached copy that must be refreshed before regenerating the skill. A new `Article titles` tab introduces authoritative multilingual article titles that Claude must use verbatim when cross-referencing articles.

**Google Sheet URL (xlsx export):**
```
https://docs.google.com/spreadsheets/d/e/2PACX-1vTn5JHMRlVqh8z5DTflmRJgDmhyRmFDogzRol7ESs2nY67ROZVbHiFfEmTptcP4seGxZ_WQ72ui-5R_/pub?output=xlsx
```

---

## Sheet Structure

### Existing tabs (unchanged handling)
| Tab name | Output file |
|---|---|
| Proper & Kobo specific | `references/brand-terminology.md` |
| Academy | `references/course-terminology.md` |
| Documentation | `references/documentation-terminology.md` |
| Data collection | `references/data-collection-terms.md` |
| Form building | `references/form-building-terms.md` |
| Data management | `references/data-management-terms.md` |
| Formbuilder question types | `references/question-types.md` |
| Appearances | `references/question-types.md` (appended) |
| Formbuilder UI | `references/ui-terminology.md` |
| KoboCollect | `references/ui-terminology.md` (appended) |
| XLSForm | `references/form-building-terms.md` (appended) |

### New tab: `Article titles`
| Column | Notes |
|---|---|
| File name | Slug/filename of the article (used as key) |
| English | Official English title |
| French | Official French title |
| Spanish | Official Spanish title |
| Arabic | Official Arabic title |
| Notes | Optional translator notes |

This tab generates a new file: `references/article-titles.md`

---

## Changes Required

### 1. New script: `scripts/fetch_glossary.py`

Fetches the remote xlsx and writes it to `sources/glossary.xlsx`.

```
python scripts/fetch_glossary.py
```

- Downloads from the hardcoded Google Sheet URL using `urllib` (stdlib only, no extra deps)
- Writes to `sources/glossary.xlsx`, overwriting the previous cached copy
- Prints the sheet names found so the user can confirm the download succeeded
- Exits non-zero on network failure (does not silently leave a stale file)
- Stores the URL in a constant at the top of the file so it's easy to update

### 2. Update `regenerate_skill.py`: handle `Article titles` tab

In `generate_reference_files()`:
- Add `"Article titles"` to the routing map → `"article-titles.md"`
- Add a new `generate_article_titles_file(df)` function that:
  - Emits a header marking these titles as **OFFICIAL — must be used verbatim**
  - Renders a table: `File name | English | French | Spanish | Arabic | Notes`
  - Adds an instruction block explaining the cross-reference consistency rule

In `generate_skill_content()` / the static SKILL.md template:
- Add `article-titles.md` to the **Terminology References** section as OFFICIAL priority
- Add a pre-translation checklist item: "Check `article-titles.md` for any article titles referenced in the source"
- Add a note in the Quality Checklist: article title spellings match `article-titles.md` exactly

### 3. Update `validate_sources.py`

- Add `"Article titles"` to `EXPECTED_SHEETS`
- Validate that the `Article titles` sheet has columns: `File name`, `English`, `French`, `Spanish`, `Arabic`
- Keep `glossary.xlsx` as a required file (it is the cached copy that must exist before validation runs)

### 4. Update `sync_and_update.py`

- Add an optional `--fetch` flag (or make fetching the first step by default)
- When `--fetch` is passed (or by default), call `fetch_glossary.py` before validation/regeneration
- This replaces the manual "copy xlsx from Downloads" workflow for the glossary

### 5. Update `SKILL.md` template (in `regenerate_skill.py`)

Add to the **Pre-Translation Checklist** section:
```
4. **[article-titles.md](references/article-titles.md)** - Official article titles in all languages (OFFICIAL — verbatim)
```

Add a new subsection after Formatting Rules:
```markdown
## Article Title Consistency

When translating any article that references another article by title:
1. Look up the target article's filename in `references/article-titles.md`
2. Use the **exact title** listed for the target language — never translate it yourself
3. If a title is missing from the file, flag it rather than guessing
```

Add to Quality Checklist:
```
- [ ] Cross-referenced article titles match article-titles.md exactly
```

### 6. Update `sources/` README / SKILL.md "Updating This Skill" section

Change the update instructions to:
```
Run: python scripts/fetch_glossary.py   # pull latest from Google Sheet
     python scripts/regenerate_skill.py  # regenerate from cached copy
# or combined:
     python scripts/sync_and_update.py --fetch
```

---

## File Inventory

| File | Action |
|---|---|
| `scripts/fetch_glossary.py` | **NEW** — remote fetch script |
| `scripts/regenerate_skill.py` | **MODIFY** — handle `Article titles` tab, update SKILL.md template |
| `scripts/validate_sources.py` | **MODIFY** — expect `Article titles` sheet and its columns |
| `scripts/sync_and_update.py` | **MODIFY** — add `--fetch` flag / default fetch step |
| `references/article-titles.md` | **NEW** (generated) — official article title lookup |
| `SKILL.md` | **MODIFY** (generated) — article-titles reference + checklist items |
| `sources/glossary.xlsx` | **UNCHANGED role** — local cache; now populated by `fetch_glossary.py` |

---

## Non-Goals

- No automatic scheduled refresh (user runs fetch manually before regenerating)
- No diff/merge of remote vs. local — fetch always overwrites
- The `.xlsx` file stays committed as a fallback for offline use; fetch updates it
- No changes to the `.md` source files (`style-guide.md`, `workflow-rules.md`, `language-rules.md`)

---

## Resolved Decisions

1. **`fetch_glossary.py` is a pure download step** — it does not chain into regeneration. Run `regenerate_skill.py` separately after fetching.
2. **`glossary.xlsx` stays committed** as an offline fallback. Run `fetch_glossary.py` to refresh it before regenerating.
