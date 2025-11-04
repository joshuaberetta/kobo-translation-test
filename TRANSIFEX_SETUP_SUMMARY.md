# Transifex Integration Summary

## What's Been Set Up

I've integrated Transifex API with your translation workflow so that the latest KoboToolbox UI translations are automatically pulled before translating docs and SRTs.

## Key Files Created/Modified

### New Files
1. **`scripts/transifex_sync.py`** - Main integration module
   - Fetches UI translations from Transifex API
   - Saves to skill reference files
   - Can be run standalone or integrated

2. **`test_transifex_integration.py`** - Quick test script
   - Verifies API connection
   - Shows sample translations
   - Tests end-to-end workflow

3. **`TRANSIFEX_INTEGRATION.md`** - Complete documentation
   - Setup instructions
   - How it works
   - API reference
   - Troubleshooting

4. **`TRANSIFEX_EXAMPLES.md`** - Usage examples
   - Copy-paste examples
   - Workflow patterns
   - Batch processing scripts

### Modified Files
1. **`scripts/translate_srt.py`** - Updated for Transifex
   - Auto-syncs before translation (optional)
   - Includes synced terminology in Claude prompts
   - Works with prompt caching

2. **`scripts/translation_agent.py`** - Updated for Transifex
   - Same auto-sync capability
   - Cached terminology loaded per-language

3. **`scripts/requirements.txt`** - Added `requests` library

4. **`.env`** - Added `TRANSIFEX_API_TOKEN` placeholder

## How It Works

### 1. **Before Translation** (Automatic)
```python
# When you run a translation, it automatically:
agent = SRTTranslationAgent()  # sync_transifex=True by default

# 1. Checks if language is already synced this session
# 2. If not, fetches latest UI translations from Transifex
# 3. Saves to: skills/kobo-translation-{lang}/references/transifex-ui-terminology.md
# 4. Loads into skill context
```

### 2. **During Translation** (Cached)
```python
# Transifex terminology included in prompt with caching
message_content = [
    {
        "type": "text",
        "text": skill_context,  # ← Includes fresh Transifex terms
        "cache_control": {"type": "ephemeral"}  # ← Cached!
    },
    {
        "type": "text",
        "text": content_to_translate
    }
]
```

### 3. **Cost Savings**
- First chunk: Cache write (~$0.056 for 15K tokens)
- Subsequent chunks: Cache read (~90% cheaper)
- **Example**: 60-chunk video saves ~$9.56 vs. non-cached

## Quick Start

### 1. Set Up API Token

```bash
# Add to .env file
TRANSIFEX_API_TOKEN=your_token_here
```

Get token at: https://app.transifex.com/user/settings/api/

### 2. Test Connection

```bash
python test_transifex_integration.py
```

### 3. Use It!

```bash
# Automatic sync (default)
python scripts/translate_srt.py transcripts/en/video.srt --language es

# Manual sync first (for batch work)
python scripts/transifex_sync.py
python scripts/translate_srt.py video.srt --language es --no-transifex-sync
```

## Key Features

✅ **Automatic** - Syncs before first translation per language  
✅ **Cached** - Only syncs once per session per language  
✅ **Cost-Effective** - Uses Claude's prompt caching (90% savings)  
✅ **Optional** - Can disable with `--no-transifex-sync`  
✅ **Offline-Ready** - Falls back to cached files if sync fails  
✅ **Up-to-Date** - Always uses latest Transifex translations  

## Benefits

### 1. **Consistency**
UI terms match exactly what users see in KoboToolbox interface

### 2. **Accuracy**  
Professional, community-validated translations from Transifex

### 3. **Efficiency**
- No manual lookups needed
- Terminology updates automatically
- Massive cost savings with caching

### 4. **Flexibility**
- Works with both SRT and docs translation
- Can sync manually or automatically
- Falls back gracefully if Transifex unavailable

## Usage Patterns

### Pattern 1: Daily Workflow (Auto-sync)
```bash
# Just translate - sync happens automatically
python scripts/translate_srt.py video.srt --language es
```

### Pattern 2: Bulk Processing (Manual sync)
```bash
# Sync once
python scripts/transifex_sync.py

# Translate many files
python scripts/translate_srt.py video1.srt --language es --no-transifex-sync
python scripts/translate_srt.py video2.srt --language es --no-transifex-sync
```

### Pattern 3: Offline Work
```bash
# Use previously synced terminology
python scripts/translate_srt.py video.srt --language es --no-transifex-sync
```

## What Gets Synced

The integration fetches UI translations from KoboToolbox's Transifex project:

- **Organization**: kobotoolbox
- **Project**: kobotoolbox
- **Resources**: All UI interface strings
- **Languages**: es (Spanish), fr (French), ar (Arabic)

Synced files are saved to:
```
skills/
  kobo-translation-es/
    references/
      transifex-ui-terminology.md  ← Auto-generated
  kobo-translation-fr/
    references/
      transifex-ui-terminology.md  ← Auto-generated
  kobo-translation-ar/
    references/
      transifex-ui-terminology.md  ← Auto-generated
```

## Error Handling

The integration is designed to **never block** translation work:

- ❌ **No token?** → Warns and continues without sync
- ❌ **API error?** → Warns and uses cached files
- ❌ **No translations?** → Warns and continues
- ❌ **Rate limited?** → Uses cached files

Translation always proceeds, with or without fresh Transifex data.

## Monitoring

Track sync status in output:

```
📚 Loading translation skills for ES...
  🔄 Syncing Transifex terminology for ES...
    ✅ Synced 450 UI terms from Transifex  ← Success!
  📖 Loading base skill: kobo-translation-es
    ✓ transifex-ui-terminology.md
```

Or:

```
📚 Loading translation skills for ES...
  🔄 Syncing Transifex terminology for ES...
    ⚠️  Transifex sync failed: API error  ← Failed gracefully
  📖 Loading base skill: kobo-translation-es
    ✓ brand-terminology.md  ← Continues with other files
```

## Documentation

- **Setup & How-To**: [TRANSIFEX_INTEGRATION.md](TRANSIFEX_INTEGRATION.md)
- **Examples**: [TRANSIFEX_EXAMPLES.md](TRANSIFEX_EXAMPLES.md)
- **Test Script**: `test_transifex_integration.py`

## Next Steps

1. **Get Transifex API token** from https://app.transifex.com/user/settings/api/
2. **Add to .env**: `TRANSIFEX_API_TOKEN=your_token_here`
3. **Test connection**: `python test_transifex_integration.py`
4. **Try a translation**: Use any of the examples above
5. **Review synced terms**: Check generated markdown files
6. **Commit synced files**: Add to version control for offline access

## Support

- Transifex API issues → Check [Transifex docs](https://transifex.github.io/openapi/)
- Integration questions → See documentation files
- KoboToolbox terminology → Contact KoboToolbox team

---

**That's it!** The integration is ready to use. Just add your Transifex token and you're good to go. 🚀
