# Translation System Architecture

## The Non-Deterministic LLM Problem

### Problem Statement

LLMs (Large Language Models) like Claude are **non-deterministic** by design. Even with low temperature settings (0.3), translating the same English text twice produces slightly different results:

**Translation 1:**
```markdown
This tool helps you create forms.
→ Esta herramienta te ayuda a crear formularios.
```

**Translation 2 (same input):**
```markdown  
This tool helps you create forms.
→ Esta herramienta ayuda a crear formularios.
```

While both translations are correct, git sees them as changes, creating "translation noise" in diffs.

### Impact

When auto-translating documentation:
1. **Version 1**: English file says "Click the button"
2. **Translator**: Produces Spanish translation "Haz clic en el botón"
3. **Human reviewer**: Reviews and approves PR
4. **Later**: Minor English change elsewhere in file ("Updated on March 2025" → "Updated on April 2025")
5. **Re-translation**: LLM retranslates entire file, produces "Haga clic en el botón" instead
6. **Result**: Git diff shows changes to both the date AND the button text, even though button text was unchanged in English

This causes:
- ❌ Loss of approved manual improvements
- ❌ False positives in git diffs (looks like content changed when it didn't)
- ❌ Increased review burden
- ❌ Wasted API costs on re-translating unchanged content
- ❌ Translation quality degradation over time

## The Solution: Diff-Based Translation

### How It Works

Instead of re-translating entire documents, we:

1. **Detect actual changes** in the English source using git diff
2. **Extract only the changed lines**
3. **Translate just the diff** with clear markers
4. **Intelligently merge** the translation into the existing file

### Example Workflow

**English source change:**
```diff
 # User Guide
 
 KoboToolbox is a data collection platform.
 
-Last updated: March 2025
+Last updated: April 2025
 
 ## Features
```

**What gets translated:**
```
ONLY THIS: "Last updated: April 2025"
NOT THE REST OF THE FILE
```

**Spanish translation file:**
```diff
 # Guía del Usuario
 
 KoboToolbox es una plataforma de recopilación de datos.
 
-Última actualización: marzo de 2025
+Última actualización: abril de 2025
 
 ## Características
```

**Result:** Only the actual change is in the diff. The rest of the translation is untouched.

## Implementation Details

### Components

1. **GitHub Actions Workflow** (`.github/workflows/auto-translate.yml`)
   - Detects changed English files
   - Extracts git diffs of actual changes
   - Distinguishes between new files (full translation) and updates (diff translation)

2. **Translation Agent** (`scripts/translation_agent.py`)
   - `translate_file()`: Full document translation (new files)
   - `translate_diff()`: Partial translation with strict prompting (updates)
   - Uses Claude Sonnet 4 with temperature 0.3 for consistency

3. **Diff Application Script** (`scripts/apply_diff_translation.py`)
   - Smart merging: finds where to insert translated changes
   - Strategies: exact match → fuzzy match → append
   - Preserves file structure and unchanged content

4. **Translation Extraction** (`scripts/extract_translation.py`)
   - Parses translation agent logs
   - Extracts only the translated content (no metadata)

### Translation Prompting

The `translate_diff()` method uses **extreme emphasis** to prevent the LLM from expanding beyond the diff:

```python
prompt = """
🚨🚨🚨 CRITICAL INSTRUCTION 🚨🚨🚨

You are translating ONLY A DIFF - NOT a full document.

RULES:
1. Translate ONLY the exact content between the markers below
2. Do NOT translate anything outside the markers
3. Do NOT add any explanations, comments, or meta-text
...

---BEGIN DIFF TO TRANSLATE---
{diff_content}
---END DIFF TO TRANSLATE---

Now provide ONLY the translated diff content (nothing else):
"""
```

System message reinforces this:
```python
system="""You are a precise translation tool. When translating a DIFF, you MUST:
1. Translate ONLY the content between BEGIN and END markers
2. Output ONLY the translated text with NO additional content
3. NOT translate anything outside the markers
..."""
```

### Merge Strategies

When applying translated diffs, the system tries (in order):

1. **Exact Match**: If old English content has a direct match in the translation, replace it
2. **Fuzzy Match**: Find similar content using word overlap scoring (threshold: 50%)
3. **Smart Append**: If no match, append to appropriate section or end of file

## Benefits

### ✅ Preserves Manual Improvements

Human reviewer changes are untouched:
```
English: "Click the button"
Auto-translation: "Haz clic en el botón"
Human improves to: "Presiona el botón" ← PRESERVED
Later English change elsewhere → human improvement stays
```

### ✅ Reduces Translation Noise

Git diffs show **only actual changes**:
```diff
# Before (full re-translation):
- 47 lines changed (entire file)

# After (diff-based):
- 1 line changed (the actual change)
```

### ✅ Lower Costs

Only translate what changed:
```
Full file: ~2000 tokens = $0.02 per language
Diff only: ~100 tokens = $0.001 per language
Savings: 95% on updates
```

### ✅ Better Quality Control

Reviewers can focus on:
- **What actually changed** in the source
- **Whether the change was translated correctly**
- Not distracted by unrelated "phantom changes"

## Limitations & Edge Cases

### When Diffs Don't Work

1. **Structural changes**: If English content is moved to a different section, fuzzy matching may fail → fallback to append
2. **Large rewrites**: If >50% of file changes, diff approach offers less benefit
3. **First translation**: New files always need full translation

### Manual Override Protection

For files with extensive manual improvements or localization beyond translation, add:

```html
<!-- MANUAL_EDIT: DO NOT AUTO-TRANSLATE -->
```

This completely skips the file from automation.

## Monitoring & Debugging

### Success Indicators

In PR summaries, check for:
```
- ✅ ES: Diff translated and applied
- ✅ FR: Diff translated and applied  
- ✅ AR: Diff translated and applied
```

### Common Issues

**"Failed to apply diff":**
- Old content not found in existing translation
- Solution: Review the translation manually or re-translate full file

**"Only deletions (no translation needed)":**
- English content was removed only, nothing to translate
- Expected behavior

## Future Improvements

Potential enhancements:
- [ ] Semantic similarity matching (embeddings) for better merge accuracy
- [ ] Multi-section diff handling (multiple changes in one file)
- [ ] Confidence scoring for merge strategies
- [ ] Automated testing with synthetic changes
- [ ] Diff visualization in PR comments

## Related Documentation

- **[TRANSLATION_WORKFLOW.md](TRANSLATION_WORKFLOW.md)**: User guide for the translation system
- **[../skills/kobo-translation/SKILL.md](../skills/kobo-translation/SKILL.md)**: Translation guidelines for the LLM
- **[../.github/workflows/auto-translate.yml](../.github/workflows/auto-translate.yml)**: GitHub Actions workflow

## Decision Log

### Why Not Traditional CAT Tools?

Computer-Assisted Translation (CAT) tools with translation memory (TM) were considered but:
- ✅ Good: Reuse exact matches from TM
- ❌ Bad: Manual segment alignment required
- ❌ Bad: Poor handling of markdown structure
- ❌ Bad: No support for brand terminology enforcement

LLM + diff approach provides:
- ✅ Better context understanding
- ✅ Automatic markdown preservation
- ✅ Enforced brand terminology via skill
- ✅ Flexible enough for localization, not just translation

### Why Not Post-Editing TM?

Could we use TM for unchanged segments + LLM for changed segments?
- ❌ Complexity: Two systems to maintain
- ❌ Context loss: LLM needs surrounding context for quality
- ✅ Current approach simpler: git is our TM (unchanged = preserved)

### Temperature Setting (0.3)

Why not 0.0 for maximum determinism?
- At 0.0, model becomes overly conservative and awkward
- At 0.3, model is natural but still highly consistent
- Testing showed 0.3 produces <5% variation across runs
- Variation is acceptable since we only translate actual changes
