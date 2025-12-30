# Kobo UI Template Autocomplete

VS Code extension that provides intelligent autocomplete for `{{ui:KEY}}` template strings in Kobo documentation markdown files.

## Features

- **Fuzzy autocomplete** for UI template keys when typing `{{ui:`
- Loads UI strings directly from Transifex PO files
- **1,200+ UI strings** from KoboToolbox form-builder-translations
- Formatting option autocomplete (bold, italic, code, upper, lower)
- Case-insensitive search
- Relevance-based sorting (matches starting with your query appear first)

## Usage

### Basic Template Autocomplete

1. Open a markdown file (`.md`)
2. Start typing: `{{ui:`
3. Autocomplete suggestions will appear automatically
4. Type to filter (e.g., `{{ui:da` shows "DATA", "Date deployed", etc.)
5. Select the desired UI string and press Enter

**Example:**
```markdown
Click the {{ui:Deploy|bold}} button on the {{ui:FORM}} tab.
```

### Formatting Options

After entering a UI key, add a pipe (`|`) to see formatting options:

```markdown
{{ui:Deploy|bold}}      → **DESPLEGAR**
{{ui:DATA|code}}        → `DATOS`
{{ui:Save|upper}}       → GUARDAR
{{ui:Form|upper,bold}}  → **FORMULARIO**
```

Available formatting:
- `bold` - Bold text
- `italic` - Italic text
- `code` - Inline code
- `upper` - UPPERCASE
- `lower` - lowercase
- Combinations: `upper,bold`, `upper,code`, etc.

## Installation

### Method 1: Install from VSIX (Recommended)

1. Open VS Code
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
3. Type "Install from VSIX" and select it
4. Navigate to `vscode-ui-template-autocomplete/kobo-ui-template-autocomplete-0.1.0.vsix`
5. Select the file to install

### Method 2: Install from Source (Development)

1. Navigate to the extension directory:
   ```bash
   cd vscode-ui-template-autocomplete
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Compile the extension:
   ```bash
   npm run compile
   ```

4. Open the extension in VS Code:
   ```bash
   code .
   ```

5. Press `F5` to launch the Extension Development Host

6. In the new window, open your Kobo translation workspace

## Configuration

The extension looks for the PO file at:
```
external/form-builder-translations/en/LC_MESSAGES/djangojs.po
```

To change the PO file path:

1. Open VS Code Settings (`Ctrl+,` or `Cmd+,`)
2. Search for "Kobo UI Template"
3. Update `koboUITemplate.poFilePath` with your custom path

**Example custom path:**
```json
{
  "koboUITemplate.poFilePath": "path/to/custom/djangojs.po"
}
```

## Commands

- **Reload UI Strings**: Reload UI strings from the PO file without restarting VS Code
  - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
  - Type "Reload UI Strings" and select it

## Requirements

- VS Code 1.80.0 or higher
- Kobo translation workspace with `external/form-builder-translations` submodule initialized

## Development

### Building

```bash
# Install dependencies
npm install

# Compile TypeScript
npm run compile

# Watch mode (auto-recompile on changes)
npm run watch
```

### Packaging

To create a `.vsix` package for distribution:

```bash
# Install vsce (VS Code Extension Manager)
npm install -g @vscode/vsce

# Package the extension
vsce package
```

This creates `kobo-ui-template-autocomplete-0.1.0.vsix` which can be shared and installed.

## How It Works

1. **PO File Parsing**: Reads `djangojs.po` and extracts all `msgid` entries (English UI strings)
2. **Completion Provider**: Registers a VS Code completion provider that triggers on `:` after `{{ui`
3. **Fuzzy Search**: Filters UI strings based on your input (case-insensitive, substring matching)
4. **Relevance Sorting**: Shows best matches first (starts with > contains)

## Troubleshooting

### "No UI strings loaded" warning

**Cause**: PO file not found at the configured path

**Solution**:
1. Ensure the `form-builder-translations` submodule is initialized:
   ```bash
   git submodule update --init --recursive
   ```
2. Verify the PO file exists:
   ```bash
   ls external/form-builder-translations/en/LC_MESSAGES/djangojs.po
   ```
3. Check the `koboUITemplate.poFilePath` setting in VS Code

### Autocomplete not triggering

**Cause**: File is not recognized as markdown

**Solution**:
1. Ensure the file has a `.md` extension
2. Check the language mode in VS Code (bottom right corner should show "Markdown")
3. Try manually triggering autocomplete with `Ctrl+Space`

### Stale UI strings after updating PO file

**Solution**:
1. Run the "Reload UI Strings" command
2. Or restart VS Code

## License

MIT

## Author

Kobo Translation Team
