#!/bin/bash
# Quick script to extract UI strings and rebuild extension

set -e  # Exit on error

echo "==================================="
echo "UI Strings Extraction & Build"
echo "==================================="
echo ""

# Get repository root
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

# Step 1: Extract UI strings
echo "📦 Step 1: Extracting UI strings from PO file..."
python3 scripts/extract_msgids.py

if [ $? -eq 0 ]; then
    echo "✅ Extraction successful!"
    
    # Show statistics
    if command -v jq &> /dev/null; then
        COUNT=$(jq '.count' external/form-builder-translations/ui-strings.json)
        echo "   → Extracted $COUNT UI strings"
    fi
else
    echo "❌ Extraction failed!"
    exit 1
fi

echo ""

# Step 2: Compile extension
echo "🔨 Step 2: Compiling VS Code extension..."
cd vscode-ui-template-autocomplete
npm run compile

if [ $? -eq 0 ]; then
    echo "✅ Compilation successful!"
else
    echo "❌ Compilation failed!"
    exit 1
fi

echo ""
echo "==================================="
echo "✅ All done!"
echo "==================================="
echo ""
echo "Next steps:"
echo "1. Press F5 in VS Code to test the extension"
echo "2. Or run: vsce package (to create VSIX)"
echo ""
