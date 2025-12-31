# Testing Checklist - UI Template Autocomplete Fix

## ✅ Pre-Test Setup

- [x] Extract UI strings: `python3 scripts/extract_msgids.py`
- [x] Verify extraction: 843 strings in `ui-strings.json`
- [x] Compile extension: `npm run compile`
- [x] Check output files exist in `out/` directory

## 🧪 Test in Extension Development Host

### Launch Extension
1. Open `vscode-ui-template-autocomplete` in VS Code
2. Press `F5` (or `Fn+F5` on Mac)
3. New window opens with "[Extension Development Host]" in title

### Open Workspace
1. In Extension Development Host window: File → Open Folder
2. Select `kobo-translation-test` (repository root)
3. Wait for workspace to load

### Verify Loading
- [ ] Check status bar message: "Loaded 843 UI strings"
- [ ] No error messages in bottom right corner
- [ ] Output panel shows successful load (View → Output → "Kobo UI Template Autocomplete")

## 🎯 Functional Tests

### Test 1: Basic Autocomplete
Open `test-autocomplete.md` (or any `.md` file)

- [ ] Type `{{ui:` → Autocomplete appears automatically
- [ ] Shows a list of suggestions
- [ ] Suggestions are English UI strings (not Spanish)

### Test 2: Fuzzy Search
- [ ] Type `{{ui:dep` → Shows "Deployed", "Deploying...", "(deployed)", etc.
- [ ] Type `{{ui:data` → Shows "Data", data-related strings
- [ ] Type `{{ui:save` → Shows "Save", "Save Changes", etc.
- [ ] Type `{{ui:form` → Shows "Form", form-related strings

### Test 3: Relevance Sorting
- [ ] Type `{{ui:de` → "Delete" and "Deployed" appear near top (start with "De")
- [ ] Shorter matches appear before longer ones
- [ ] Exact start-matches appear before contains-matches

### Test 4: Formatting Options
- [ ] Type `{{ui:Deploy|` → Formatting suggestions appear (bold, italic, code, etc.)
- [ ] Can select formatting option
- [ ] Multiple formats: `{{ui:Deploy|upper,bold}`

### Test 5: Manual Trigger
- [ ] Type `{{ui:` and wait (no typing)
- [ ] Press `Ctrl+Space` (or `Cmd+Space` on Mac)
- [ ] Autocomplete appears

### Test 6: Selection and Insertion
- [ ] Type `{{ui:depl`
- [ ] Arrow down to "Deployed"
- [ ] Press Enter
- [ ] Result: `{{ui:Deployed}}`
- [ ] Cursor is after the key (ready for `|` or `}}`)

## 🐛 Edge Cases

### Empty Query
- [ ] Type just `{{ui:` (no additional text)
- [ ] Shows initial suggestions (top strings alphabetically)
- [ ] Can scroll through list

### Special Characters
- [ ] Search for strings with spaces: `{{ui:Save Ch` → "Save Changes"
- [ ] Search for strings with punctuation: `{{ui:don't` → strings with apostrophes
- [ ] Search for strings with symbols: `{{ui:##` → strings with ##

### Case Insensitivity
- [ ] Type `{{ui:DEPLOY` → Shows "Deployed", "Deploying..."
- [ ] Type `{{ui:deploy` → Same results
- [ ] Type `{{ui:DePlOy` → Same results

## 🔄 Reload Test

### Reload UI Strings Command
- [ ] Press `Ctrl+Shift+P` (or `Cmd+Shift+P`)
- [ ] Type "Kobo: Reload UI Strings"
- [ ] Run command
- [ ] Status message: "Reloaded 843 UI strings"
- [ ] Autocomplete still works

### After Code Changes
If you modify extension code:
- [ ] Save changes
- [ ] In Extension Development Host: `Ctrl+Shift+P` → "Developer: Reload Window"
- [ ] Extension reloads with changes

## 📊 Performance Check

### Load Time
- [ ] Extension loads in < 100ms (check Output panel timestamp)
- [ ] No noticeable delay when opening markdown files

### Autocomplete Response
- [ ] Suggestions appear instantly after typing `{{ui:`
- [ ] Filtering is instant as you type more characters
- [ ] No lag or stuttering

## ❌ Error Scenarios

### Missing JSON File
1. Temporarily rename `ui-strings.json`
2. Reload VS Code window
- [ ] Error message appears: "No UI strings loaded"
- [ ] Explains to check JSON file path

### Invalid JSON
1. Temporarily corrupt `ui-strings.json` (add invalid JSON)
2. Reload VS Code window
- [ ] Error message with details
- [ ] Extension doesn't crash

## ✨ Comparison with Old Behavior

### Before (PO Parser with Spanish file)
- ❌ Suggestions were Spanish translations (wrong)
- ❌ Slow loading (200-500ms)
- ❌ Inconsistent parsing
- ❌ Hard to debug

### After (JSON Loader with English keys)
- ✅ Suggestions are English UI keys (correct)
- ✅ Fast loading (10-20ms)
- ✅ Reliable, consistent
- ✅ Easy to debug and verify

## 📝 Final Verification

- [ ] All tests above pass
- [ ] No errors in Developer Console (Help → Toggle Developer Tools)
- [ ] No errors in Output panel
- [ ] Autocomplete works in multiple markdown files
- [ ] Extension doesn't slow down VS Code

## 🎉 Success Criteria

The fix is successful if:
1. ✅ Autocomplete shows **English UI strings** (not Spanish translations)
2. ✅ Loads **843 strings** consistently
3. ✅ Appears **instantly** after typing `{{ui:`
4. ✅ **Fuzzy search** works (finds "Deploy" when typing "dep")
5. ✅ **Formatting options** appear after `|`

---

## Next Steps After Testing

If all tests pass:
- [ ] Package extension: `vsce package`
- [ ] Install VSIX for daily use
- [ ] Document in main project README
- [ ] Update workflow documentation

If any tests fail:
- [ ] Note which test failed
- [ ] Check Developer Console for errors
- [ ] Check Output panel logs
- [ ] Review FIX_SUMMARY.md and EXTRACTION_DETAILS.md
