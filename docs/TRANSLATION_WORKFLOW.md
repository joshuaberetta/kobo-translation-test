# Translation Workflow Guide

## KoboToolbox Translation Workflow

## How Auto-Translation Works

This repository uses AI-powered translation with **diff-based updates** to minimize translation noise and preserve manual improvements.

### Translation Modes

#### 1. New Files (Full Translation)
When a new English file is added to `docs/en/`:
- The entire file is translated to each language (ES, FR, AR)
- New translation files are created in `docs/{lang}/`
- A PR is created with the translations for review

#### 2. Updates (Diff-Based Translation)
When an existing English file is changed:
1. **Git detects the actual changes** (lines added/removed)
2. **Only the changed content** is extracted and sent to the translation agent
3. **LLM translates just the diff** (not the entire document)
4. **Translation is intelligently merged** back into existing translated files
5. Unchanged parts of translations are **preserved exactly**

**Why diff-based?** LLMs are non-deterministic - they produce slightly different output each time, even for identical input. By translating only actual changes, we:
- ✅ Preserve manual reviewer improvements
- ✅ Reduce translation noise in git diffs
- ✅ Lower API costs (translate only what changed)
- ✅ Keep translations synchronized with source

## Protecting Manual Edits

**Problem:** If a reviewer makes manual improvements to a translation, those edits will be overwritten the next time the English source file is updated.

**Solution:** Mark files that contain approved manual edits:

### Step 1: Add Protection Marker

After making and approving manual edits to a translation, add this comment **at the top of the file**:

```html
<!-- MANUAL_EDIT: DO NOT AUTO-TRANSLATE -->
```

**Example:**

```markdown
<!-- MANUAL_EDIT: DO NOT AUTO-TRANSLATE -->
# Título del documento

Contenido traducido manualmente...
```

### Step 2: File is Now Protected

- The automated workflow will **skip** files with this marker
- Manual edits are preserved
- You'll see "⏭️ SKIPPED (manual edits detected)" in the workflow logs

### Step 3: Updating Protected Files

When the English source is updated and you need to update the protected translation:

**Option A: Remove marker temporarily**
1. Remove the `<!-- MANUAL_EDIT -->` comment
2. Let auto-translation run
3. Review the new translation
4. Re-add marker if manual edits are made

**Option B: Update manually**
1. Keep the marker in place
2. Manually update the translation based on English changes
3. Commit directly or via PR

## Workflow Decision Tree

```
English file updated
├─ Translation exists?
│  ├─ No → Auto-translate (new file)
│  └─ Yes → Has MANUAL_EDIT marker?
│     ├─ Yes → SKIP auto-translation
│     └─ No → Auto-translate (may overwrite previous content)
└─ Create PR with results
```

## Best Practices

### ✅ DO:
- Add `MANUAL_EDIT` marker immediately after making manual improvements
- Review auto-translation PRs carefully before merging
- Check git diff to see what actually changed
- Use markers sparingly - only for files with significant manual work

### ❌ DON'T:
- Don't rely on auto-translation to preserve manual edits without the marker
- Don't add markers to all files "just in case" - it defeats automation
- Don't forget to document why manual edits were needed (comment in file or PR)

## Example Scenarios

### Scenario 1: Minor typo fix in English

**English change:** "Click the buton" → "Click the button"

**What happens:**
- All translations re-generated
- If no MANUAL_EDIT marker: Translations updated automatically
- If MANUAL_EDIT marker: File skipped, reviewer must fix typo manually

**Recommendation:** Don't use marker for files with only minor translations.

### Scenario 2: Reviewer improves awkward AI translation

**English:** "The users can access the dashboard"
**AI Spanish:** "Los usuarios pueden acceder al panel"
**Reviewer edits to:** "Los usuarios y las usuarias pueden acceder al panel de control"

**What to do:**
1. Approve and merge the manual improvement
2. **Immediately** add `<!-- MANUAL_EDIT -->` to top of that Spanish file
3. Commit and push the marker
4. File is now protected from auto-translation

### Scenario 3: Major English update to protected file

**Situation:** File has MANUAL_EDIT marker, but English source has major changes

**What to do:**
1. Review the English changes
2. Decide: Is the manual work still relevant, or can we re-translate?
   - **If manual work is still valuable:** Update manually, keep marker
   - **If can re-translate:** Remove marker, let workflow run, review and re-add marker if needed

## Monitoring and Maintenance

### Check Protected Files

List all files with manual edit markers:

```bash
grep -r "MANUAL_EDIT" docs/{es,fr,ar}/ --include="*.md"
```

### Review Protection Status

Periodically review protected files:
- Are they still needed?
- Has the English source diverged significantly?
- Should they be re-translated from scratch?

### Workflow Logs

Check workflow runs to see which files were skipped:
- Go to Actions tab
- View latest "Auto-Translate Documentation" run
- Look for "⏭️ SKIPPED" messages

## FAQ

**Q: Will the AI re-translate exactly the same way each time?**
A: Mostly yes, but small variations can occur. This is why the marker system exists.

**Q: Can I protect just one section of a file?**
A: No, protection is file-level only. Consider splitting large files if needed.

**Q: What if I forget to add the marker?**
A: Your manual edits will be overwritten. Check the PR diff carefully and restore from git history if needed.

**Q: How do I restore overwritten manual edits?**
A: Use `git log` to find the commit with your manual edits, then cherry-pick or manually copy them back.

**Q: Should I add markers preemptively?**
A: No - only add after actual manual improvements. Markers reduce automation benefits.

## Summary

- **Auto-translation is the default** - fast and consistent
- **Use MANUAL_EDIT marker** to protect approved human improvements  
- **Review PRs carefully** before merging
- **Balance automation vs. quality** - use markers strategically, not universally
