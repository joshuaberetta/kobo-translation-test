# Translation Agent Output Handling

## Problem

When running the translation agent in update mode, all output (logs, metadata, and the actual translation) was being mixed together, making it difficult to extract just the translation for automated workflows.

## Solution: stdout/stderr Separation

The translation agent now separates output streams:

### stderr (Standard Error) - Metadata & Logs
All informational output goes to stderr:
- 📚 Loading messages
- 🔄 Progress indicators  
- 📊 Token usage statistics
- 💰 Cost estimates
- ✅ Success messages
- ❌ Error messages

### stdout (Standard Output) - Clean Translation
Only the actual translation content goes to stdout:
- For diff mode: Just the translated diff text
- For full mode: Just the full translated document (when not using --save)

## Benefits

### 1. Easy Extraction in Workflows
```bash
# Capture translation (stdout) and logs (stderr) separately
python scripts/translation_agent.py \
  --update-mode \
  --diff "$CONTENT" \
  --test > translation.txt 2> translation.log

# Translation is clean in translation.txt
TRANSLATED=$(cat translation.txt)

# Logs/metadata are in translation.log for debugging
grep "Estimated cost" translation.log
```

### 2. Pipe-Friendly
```bash
# Pipe translation directly to other tools
python scripts/translation_agent.py --update-mode --diff "$TEXT" --test | \
  python apply_diff_translation.py --target file.md --new -
```

### 3. Human-Readable Logs
User can see progress on stderr while stdout remains clean:
```
📚 Loading kobo-translation skill...
✅ Skill loaded successfully
🔄 UPDATE MODE: Translating diff only
📏 Diff size: 93 characters
📊 Translation mode: DIFF-BASED (changes only)
🤖 Calling Claude API...
📊 Tokens used: 3684 input, 34 output
💰 Estimated cost: $0.0116
✨ Translation test complete!

[stdout contains only: "Comienza creando el archivo de imagen..."]
```

## Implementation

All `print()` statements in `translation_agent.py` now use `file=sys.stderr` for metadata:

```python
# Metadata/logs to stderr
print("📚 Loading skill...", file=sys.stderr)
print(f"💰 Cost: ${cost}", file=sys.stderr)

# Translation to stdout (default)
print(translated_diff)  # No file= parameter = stdout
```

## Workflow Integration

### GitHub Actions
```yaml
# Separate stdout and stderr
if python scripts/translation_agent.py \
  --update-mode \
  --diff "$NEW_CONTENT" \
  --test > "translation_${LANG}.txt" 2> "translation_${LANG}.log"; then
  
  # Get clean translation
  TRANSLATED_CONTENT=$(cat "translation_${LANG}.txt")
  
  # Get cost from logs
  COST=$(grep "Estimated cost" "translation_${LANG}.log" | grep -oP '\$\K[0-9.]+')
fi
```

### Local Testing
```bash
# See logs in terminal, save translation to file
python scripts/translation_agent.py \
  --update-mode \
  --diff "New content" \
  --test > output.txt

# Or hide logs entirely
python scripts/translation_agent.py \
  --update-mode \
  --diff "New content" \
  --test > output.txt 2>/dev/null
```

## Removed Scripts

The `extract_translation.py` helper script is now **optional** - with clean stdout, workflows can simply capture the output directly using shell redirection.

The script remains available for edge cases where additional filtering might be needed.

## Testing

To verify the separation:

```bash
# Should show ONLY the translation
python scripts/translation_agent.py --file docs/en/test.md --language es --update-mode --diff "Test" --test 2>/dev/null

# Should show ONLY logs (no translation)
python scripts/translation_agent.py --file docs/en/test.md --language es --update-mode --diff "Test" --test >/dev/null
```
