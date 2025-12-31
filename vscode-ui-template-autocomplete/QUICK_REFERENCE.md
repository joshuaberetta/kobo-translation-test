# Quick Reference - UI String Extraction System

## 📁 Key Files

```
scripts/extract_msgids.py                           # Extraction script
external/form-builder-translations/ui-strings.json  # Extracted UI strings (843)
vscode-ui-template-autocomplete/src/jsonLoader.ts   # JSON loader
```

## 🚀 Quick Commands

### Extract UI Strings
```bash
python3 scripts/extract_msgids.py
```

### Build Everything
```bash
./scripts/build_extension.sh
```

### Test Extension
Press `F5` (or `Fn+F5` on Mac) in VS Code

### Reload UI Strings
In VS Code: `Ctrl+Shift+P` → "Kobo: Reload UI Strings"

## 📊 Statistics

- **Total UI Strings**: 843
- **Source**: English PO file (`en/LC_MESSAGES/djangojs.po`)
- **Output**: JSON file (`ui-strings.json`)
- **Load Time**: 10-20ms (was 200-500ms)
- **Speed Improvement**: 20-50x faster

## 🎯 Usage in Markdown

### Basic Template
```markdown
{{ui:Deploy}}
```

### With Formatting
```markdown
{{ui:Deploy|bold}}           → **Deploy**
{{ui:Data|code}}             → `Data`
{{ui:Save|upper}}            → SAVE
{{ui:Form|upper,bold}}       → **FORM**
```

### Autocomplete Triggers
- Type `{{ui:` → Shows all UI strings
- Type `{{ui:dep` → Filters to "Deploy", "Deployed", etc.
- Type `{{ui:Deploy|` → Shows formatting options

## 🔄 Workflow

### When Transifex Updates

1. **Pull updates**
   ```bash
   cd external/form-builder-translations
   git pull
   ```

2. **Re-extract**
   ```bash
   cd ../..
   python3 scripts/extract_msgids.py
   ```

3. **Reload** (in VS Code)
   - Press `Ctrl+Shift+P`
   - Run "Kobo: Reload UI Strings"

### When Developing Extension

1. **Make changes** to TypeScript files

2. **Compile**
   ```bash
   cd vscode-ui-template-autocomplete
   npm run compile
   ```

3. **Reload** Extension Development Host
   - Press `Ctrl+Shift+P`
   - Run "Developer: Reload Window"

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "No UI strings loaded" | Run `python3 scripts/extract_msgids.py` |
| Autocomplete not working | Check file is `.md`, try `Ctrl+Space` |
| Wrong suggestions | Verify using `ui-strings.json` not Spanish PO |
| Extension not loading | Check Output panel for errors |
| Old strings showing | Reload UI Strings command |

## 📝 Configuration

In `.vscode/settings.json`:

```json
{
  "koboUITemplate.jsonFilePath": "external/form-builder-translations/ui-strings.json"
}
```

## ✅ Verification

### Check Extraction
```bash
# Count strings
cat external/form-builder-translations/ui-strings.json | grep -c '    "'

# View samples
head -30 external/form-builder-translations/ui-strings.json
```

### Check Extension
1. Open markdown file
2. Look for: "Loaded 843 UI strings" in status bar
3. Type `{{ui:` → autocomplete appears

## 📚 Documentation

- **[FIX_SUMMARY.md](FIX_SUMMARY.md)** - What was fixed and why
- **[EXTRACTION_DETAILS.md](EXTRACTION_DETAILS.md)** - Technical deep dive
- **[TESTING_CHECKLIST.md](TESTING_CHECKLIST.md)** - Comprehensive testing guide
- **[INSTALLATION.md](INSTALLATION.md)** - Installation instructions
- **[README.md](README.md)** - Main documentation

## 🎓 Common UI Strings

Quick reference for frequently used strings:

```
Deploy, Deployed, Deploying...
Data, DATA
Form, FORM
Save, Save Changes
Delete, Delete Project
Edit, Edit question
Settings
Projects, Library
Upload, Download
Export, Import
Share, Archive
Submit, Submission
Question, Group
Validation, Required
```

## 💡 Tips

1. **Use fuzzy search**: Type partial words (e.g., `dep` finds "Deploy")
2. **Start typing immediately**: No need to wait for full list
3. **Use formatting**: `|bold`, `|code`, `|upper` for styled text
4. **Check JSON file**: If unsure, search `ui-strings.json` directly
5. **Report issues**: If a string is missing, check the English PO file
