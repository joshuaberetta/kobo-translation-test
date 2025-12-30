# Installation Guide

## Quick Start

### Step 1: Open the Extension in VS Code

From the `kobo-translation-test` repository root:

```bash
code vscode-ui-template-autocomplete
```

### Step 2: Press F5 to Launch Extension Development Host

This will:
1. Compile the extension
2. Launch a new VS Code window with the extension loaded
3. Show "[Extension Development Host]" in the title bar

### Step 3: Open Your Workspace

In the Extension Development Host window:

1. File → Open Folder
2. Navigate to `kobo-translation-test` (the root of this repository)
3. Click "Open"

### Step 4: Test the Extension

1. Open any markdown file (e.g., `docs/en/quick_start.md`)
2. Start typing: `{{ui:`
3. Autocomplete suggestions should appear!
4. Type to filter: `{{ui:da` → shows "DATA", "Date deployed", etc.

## Permanent Installation (For Daily Use)

### Option 1: Install from Source (Development)

If you're actively developing the extension:

1. Navigate to the extension directory:
   ```bash
   cd vscode-ui-template-autocomplete
   ```

2. Install dependencies (if not already done):
   ```bash
   npm install
   ```

3. Create a symlink to your VS Code extensions folder:

   **Linux/Mac:**
   ```bash
   ln -s $(pwd) ~/.vscode/extensions/kobo-ui-template-autocomplete
   ```

   **Windows (PowerShell as Admin):**
   ```powershell
   New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.vscode\extensions\kobo-ui-template-autocomplete" -Target (Get-Location)
   ```

4. Restart VS Code

### Option 2: Package and Install VSIX (Recommended)

For a more permanent, production-like installation:

1. Install vsce (VS Code Extension packaging tool):
   ```bash
   npm install -g @vscode/vsce
   ```

2. Package the extension:
   ```bash
   cd vscode-ui-template-autocomplete
   vsce package
   ```

   This creates: `kobo-ui-template-autocomplete-0.1.0.vsix`

3. Install the VSIX in VS Code:
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
   - Type "Install from VSIX"
   - Select `kobo-ui-template-autocomplete-0.1.0.vsix`
   - Restart VS Code

## Verification

To verify the extension is working:

1. Open a markdown file
2. Look for the message in the bottom right: "Loaded X UI strings"
3. Type `{{ui:` and autocomplete should appear

## Troubleshooting

### "No UI strings loaded" warning

**Cause:** PO file not found

**Fix:**
```bash
# From kobo-translation-test root
git submodule update --init --recursive
```

### Autocomplete not appearing

**Cause:** Extension not activated

**Fix:**
1. Open a `.md` file (must have markdown file open)
2. Try manually triggering: `Ctrl+Space` after typing `{{ui:`
3. Check VS Code Output panel: View → Output → select "Kobo UI Template Autocomplete"

### Changes not reflecting

**After editing extension code:**
1. Recompile: `npm run compile`
2. Reload window: `Ctrl+Shift+P` → "Developer: Reload Window"

**Or use watch mode:**
```bash
npm run watch
```

## Uninstallation

### If installed from VSIX:
1. Extensions panel (`Ctrl+Shift+X`)
2. Find "Kobo UI Template Autocomplete"
3. Click gear icon → Uninstall

### If installed via symlink:
```bash
# Linux/Mac
rm ~/.vscode/extensions/kobo-ui-template-autocomplete

# Windows (PowerShell)
Remove-Item "$env:USERPROFILE\.vscode\extensions\kobo-ui-template-autocomplete"
```

## Next Steps

After installation, see [README.md](README.md) for usage instructions.
