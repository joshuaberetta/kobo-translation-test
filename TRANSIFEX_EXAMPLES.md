# Transifex Integration - Quick Start Examples

This document provides quick copy-paste examples for using the Transifex integration.

## Prerequisites

```bash
# 1. Install dependencies
cd scripts
pip install -r requirements.txt

# 2. Set your Transifex API token
# Add to .env file:
echo "TRANSIFEX_API_TOKEN=your_token_here" >> .env
```

## Test the Connection

```bash
# Run the test script to verify everything works
python test_transifex_integration.py
```

Expected output:
```
🧪 Testing Transifex Integration
============================================================

1. Initializing TransifexSync...
   ✅ Connected successfully

2. Fetching available resources...
   ✅ Found 3 resources:
      - main-interface: Main UI (450 strings)
      ...

3. Fetching sample Spanish translations...
   ✅ Retrieved 450 Spanish UI terms

   Sample terms:
      Submit → Enviar
      Save → Guardar
      ...

4. Saving to skill reference file...
   ✅ Saved to: skills/kobo-translation-es/references/transifex-ui-terminology.md

✨ Test complete! Transifex integration is working.
```

## Usage Examples

### 1. Translate SRT with Transifex (Automatic)

```bash
# Auto-syncs Transifex before translating
python scripts/translate_srt.py \
  transcripts/en/webinar.srt \
  --language es \
  --output transcripts/es/webinar.srt
```

Output includes:
```
🎬 SRT Translation Agent
============================================================
📄 Source: transcripts/en/webinar.srt
🌐 Target: ES
============================================================

📚 Loading translation skills for ES...
  🔄 Syncing Transifex terminology for ES...
    ✅ Synced 450 UI terms from Transifex
  📖 Loading base skill: kobo-translation-es
    ✓ transifex-ui-terminology.md    ← FRESH FROM TRANSIFEX!
    ✓ brand-terminology.md
    ✓ ui-terminology.md
    ...
```

### 2. Translate Documentation with Transifex

```bash
# Auto-syncs Transifex before translating
python scripts/translation_agent.py \
  --file docs/en/creating_account.md \
  --language fr \
  --save
```

### 3. Manual Transifex Sync (All Languages)

```bash
# Sync all languages at once
python scripts/transifex_sync.py

# Output
🌐 Syncing terminology for 3 languages...
============================================================

🔄 Syncing ES terminology from Transifex...
   Organization: kobotoolbox
   Project: kobotoolbox

📋 Fetching resources from kobotoolbox/kobotoolbox...
✅ Found 3 resources
  📥 Fetching ES translations for resource 'main-interface'...
    ✓ Retrieved 450 translations

✅ Total translations retrieved: 450
💾 Saved to: skills/kobo-translation-es/references/transifex-ui-terminology.md

... (repeats for FR and AR)

============================================================
✅ Synced 3/3 languages successfully
```

### 4. Sync Specific Language Only

```bash
# Just Spanish
python scripts/transifex_sync.py --language es

# Multiple specific languages
python scripts/transifex_sync.py --language es --language fr
```

### 5. Work Offline (Skip Transifex Sync)

```bash
# SRT translation without sync (uses cached files)
python scripts/translate_srt.py \
  transcripts/en/video.srt \
  --language es \
  --no-transifex-sync

# Documentation translation without sync
python scripts/translation_agent.py \
  --file docs/en/test.md \
  --language es \
  --no-transifex-sync
```

### 6. List Available Transifex Resources

```bash
# See what's in the Transifex project
python scripts/transifex_sync.py --list-resources

# Output:
Available resources:
  - main-interface: Main Interface Strings (450 strings)
  - form-builder: Form Builder UI (320 strings)
  - data-viewer: Data Table Interface (180 strings)
```

### 7. Use Custom Transifex Project

```bash
# Sync from different organization/project
python scripts/transifex_sync.py \
  --organization your-org \
  --project your-project \
  --language es
```

## Workflow Examples

### A. Daily Translation Workflow

```bash
# 1. Start day by syncing latest Transifex
python scripts/transifex_sync.py

# 2. Translate all your content (sync is cached)
python scripts/translate_srt.py video1.srt --language es --no-transifex-sync
python scripts/translate_srt.py video2.srt --language es --no-transifex-sync
python scripts/translate_srt.py video3.srt --language es --no-transifex-sync

# 3. Commit updated terminology
git add skills/*/references/transifex-ui-terminology.md
git commit -m "Update Transifex terminology"
```

### B. Bulk Translation Workflow

```bash
# Sync once for all languages
python scripts/transifex_sync.py

# Translate many files without re-syncing
for file in transcripts/en/*.srt; do
    basename=$(basename "$file" .srt)
    python scripts/translate_srt.py "$file" \
      --language es \
      --output "transcripts/es/${basename}.srt" \
      --no-transifex-sync
done
```

### C. CI/CD Integration

```bash
# In your CI pipeline
- name: Sync Transifex
  env:
    TRANSIFEX_API_TOKEN: ${{ secrets.TRANSIFEX_API_TOKEN }}
  run: python scripts/transifex_sync.py

- name: Translate Content
  env:
    ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
  run: |
    python scripts/translate_srt.py transcripts/en/video.srt \
      --language es \
      --no-transifex-sync  # Already synced above
```

## Programmatic Usage

### Python Script Example

```python
#!/usr/bin/env python3
"""Custom translation script with Transifex"""

from pathlib import Path
from scripts.transifex_sync import TransifexSync
from scripts.translate_srt import SRTTranslationAgent

# 1. Sync Transifex for Spanish
print("Syncing Transifex...")
sync = TransifexSync()
translations = sync.sync_language_terminology('es')
sync.save_terminology_file(translations, 'es')

# 2. Translate SRT (will use fresh Transifex terms)
print("Translating SRT...")
agent = SRTTranslationAgent(sync_transifex=False)  # Already synced
output = agent.translate_file(
    'transcripts/en/video.srt',
    'es',
    video_title='Introduction to KoboToolbox'
)

print(f"✅ Translated: {output}")
```

### Batch Processing Example

```python
#!/usr/bin/env python3
"""Batch translate with Transifex sync"""

from pathlib import Path
from scripts.transifex_sync import TransifexSync
from scripts.translate_srt import SRTTranslationAgent

# Sync all languages once
print("Syncing Transifex for all languages...")
sync = TransifexSync()
for lang in ['es', 'fr', 'ar']:
    translations = sync.sync_language_terminology(lang)
    sync.save_terminology_file(translations, lang)

# Translate multiple files
agent = SRTTranslationAgent(sync_transifex=False)

videos = Path('transcripts/en').glob('*.srt')
for video in videos:
    for lang in ['es', 'fr', 'ar']:
        print(f"\nTranslating {video.name} to {lang.upper()}...")
        output = agent.translate_file(
            str(video),
            lang,
            output_path=f'transcripts/{lang}/{video.name}'
        )
        print(f"  ✅ Saved: {output}")
```

## Troubleshooting Examples

### Check if Token is Set

```bash
# Verify token is loaded
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✅ Token set' if os.getenv('TRANSIFEX_API_TOKEN') else '❌ Token missing')"
```

### Test API Connection

```bash
# Quick connection test
python -c "
from scripts.transifex_sync import TransifexSync
try:
    sync = TransifexSync()
    resources = sync.get_project_resources('kobotoolbox', 'kobotoolbox')
    print(f'✅ Connected! Found {len(resources)} resources')
except Exception as e:
    print(f'❌ Error: {e}')
"
```

### Force Fresh Sync

```bash
# Delete cached terminology and sync fresh
rm skills/kobo-translation-*/references/transifex-ui-terminology.md
python scripts/transifex_sync.py
```

## Cost Optimization

### With Transifex + Prompt Caching

Example: 30-minute video with Transifex terminology

```
First chunk:
  - Skill context (with Transifex): ~15K tokens
  - Cache write cost: $0.056
  
Chunks 2-60:
  - Cache read cost: $0.0045 each
  - Total: $0.27
  
Total: $0.33 (instead of $3.30 without caching!)
```

The Transifex terminology adds context but costs almost nothing thanks to caching!

## Next Steps

1. **Test the integration**: Run `python test_transifex_integration.py`
2. **Review synced terms**: Check `skills/kobo-translation-es/references/transifex-ui-terminology.md`
3. **Try a translation**: Use one of the examples above
4. **Set up automation**: Add Transifex sync to your workflow

For more details, see [TRANSIFEX_INTEGRATION.md](TRANSIFEX_INTEGRATION.md)
