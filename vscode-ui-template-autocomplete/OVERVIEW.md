# VS Code UI Template Autocomplete Extension - Overview

## What This Extension Does

Provides **fuzzy autocomplete** for `{{ui:KEY}}` template strings in Kobo documentation markdown files, making it easy for non-technical writers to use the template string system.

## The Problem It Solves

When writing Kobo documentation, writers need to use template strings like `{{ui:Deploy}}` to ensure UI elements match the actual interface exactly. However:

- There are **1,200+ UI strings** available
- Writers need to remember exact keys
- Manual lookup in reference files is time-consuming
- Typos in template keys cause resolution failures

## The Solution

This extension provides **intelligent autocomplete** that:

1. **Triggers automatically** when you type `{{ui:`
2. **Shows filtered suggestions** as you type (e.g., `{{ui:da` → "DATA", "Date deployed")
3. **Uses fuzzy matching** - finds strings containing your query
4. **Sorts by relevance** - best matches appear first
5. **Reads directly from PO files** - always up-to-date with Transifex

## How It Works

```
User types:    {{ui:da
Extension:     Searches 1,200+ UI strings from PO file
Results:       - DATA
               - Date deployed
               - Dashboard
               - Data sharing
               ...
User selects:  DATA
Output:        {{ui:DATA}}
```

### Formatting Support

After selecting a UI string, add `|` to see formatting options:

```
{{ui:Deploy|bold}}       → **DESPLEGAR**
{{ui:DATA|code}}         → `DATOS`
{{ui:Form|upper,bold}}   → **FORMULARIO**
```

## Architecture

### Components

1. **PO Parser** (`src/poParser.ts`)
   - Reads `djangojs.po` from form-builder-translations
   - Extracts all `msgid` entries (English UI strings)
   - Handles multi-line strings and escape sequences
   - Provides fuzzy search functionality

2. **Completion Provider** (`src/completionProvider.ts`)
   - Registers VS Code completion provider
   - Triggers on `:` after `{{ui`
   - Filters UI strings based on user input
   - Sorts results by relevance

3. **Extension Entry Point** (`src/extension.ts`)
   - Loads UI strings on activation
   - Registers completion providers
   - Provides reload command
   - Handles configuration

### Data Flow

```
┌─────────────────────────────────────────────────┐
│  form-builder-translations/en/.../djangojs.po   │
│  (1,200+ msgid entries)                         │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  PO Parser                                      │
│  - Reads PO file                                │
│  - Extracts msgid values                        │
│  - Creates normalized keys                      │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  Completion Provider                            │
│  - Listens for {{ui: pattern                    │
│  - Fuzzy searches UI strings                    │
│  - Returns sorted matches                       │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  VS Code Autocomplete UI                        │
│  - Shows suggestions                            │
│  - Handles user selection                       │
│  - Inserts completion                           │
└─────────────────────────────────────────────────┘
```

## Technical Details

### Fuzzy Matching Algorithm

The extension uses a simple but effective fuzzy matching:

1. **Normalize**: Convert both query and UI strings to lowercase
2. **Filter**: Include strings that contain the query as a substring
3. **Sort by relevance**:
   - Priority 1: Strings starting with query (highest)
   - Priority 2: Shorter strings (easier to read)
4. **Limit**: Return top 50 matches

### Performance

- **Load time**: ~100ms to parse 1,200+ strings
- **Search time**: <5ms for fuzzy search
- **Memory**: ~200KB for all UI strings in memory
- **File size**: ~15KB compiled extension

### Configuration

Users can customize the PO file path:

```json
{
  "koboUITemplate.poFilePath": "path/to/djangojs.po"
}
```

Default: `external/form-builder-translations/en/LC_MESSAGES/djangojs.po`

## Future Enhancements

Potential improvements (not in MVP):

1. **Multi-language support**: Show translations in autocomplete preview
2. **Template validation**: Warn about unresolvable templates in real-time
3. **Snippet library**: Common template patterns (e.g., "Click the {{ui:Deploy|bold}} button")
4. **Context awareness**: Suggest UI strings based on surrounding text
5. **Transifex integration**: Pull strings directly from Transifex API
6. **Hover tooltips**: Show translations when hovering over `{{ui:KEY}}`

## Testing

To test the extension:

1. Open in VS Code: `code vscode-ui-template-autocomplete`
2. Press `F5` to launch Extension Development Host
3. Open workspace root (`kobo-translation-test`)
4. Open `test-example.md`
5. Type `{{ui:` and verify autocomplete appears

## Maintenance

### Updating UI Strings

When form-builder-translations is updated:

1. Pull latest submodule: `git submodule update --remote`
2. Reload extension: Command Palette → "Reload UI Strings"
3. Or restart VS Code

### Modifying Extension

1. Edit TypeScript files in `src/`
2. Compile: `npm run compile`
3. Reload window: `Ctrl+Shift+P` → "Developer: Reload Window"

Or use watch mode: `npm run watch`

## Distribution

### For Development

Use Extension Development Host (F5) or symlink to `~/.vscode/extensions/`

### For Production

Package as VSIX:
```bash
npm install -g @vscode/vsce
vsce package
```

Distribute `kobo-ui-template-autocomplete-0.1.0.vsix` to users.

## License

MIT

## Author

Built for the Kobo Translation Team
