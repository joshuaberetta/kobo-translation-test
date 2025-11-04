# Transifex Integration - Quick Reference Card

## 🚀 Quick Start (3 Steps)

```bash
# 1. Add token to .env
echo "TRANSIFEX_API_TOKEN=your_token_here" >> .env

# 2. Test connection
python test_transifex_integration.py

# 3. Translate (auto-syncs Transifex)
python scripts/translate_srt.py video.srt --language es
```

## 📋 Common Commands

```bash
# Auto-sync + translate (DEFAULT)
python scripts/translate_srt.py video.srt --language es

# Manual sync all languages
python scripts/transifex_sync.py

# Manual sync specific language
python scripts/transifex_sync.py --language es

# Translate without sync (offline mode)
python scripts/translate_srt.py video.srt --language es --no-transifex-sync

# List Transifex resources
python scripts/transifex_sync.py --list-resources

# Test connection
python test_transifex_integration.py
```

## 🎯 Use Cases

| Scenario | Command |
|----------|---------|
| **Single translation** | `python scripts/translate_srt.py video.srt -l es` |
| **Batch processing** | Sync once with `transifex_sync.py`, then use `--no-transifex-sync` |
| **Offline work** | Use `--no-transifex-sync` (uses cached files) |
| **CI/CD pipeline** | Sync in setup step, disable in translation steps |
| **Development/testing** | Use `--no-transifex-sync` to avoid API calls |

## 💡 How It Works

1. **First translation** for a language → Auto-syncs Transifex
2. **Subsequent translations** in same session → Uses cached sync
3. **Terminology included** in Claude prompt with caching
4. **Cost optimized** via prompt caching (90% savings)

## 📊 Cost Impact

| Without Caching | With Caching | Savings |
|----------------|--------------|---------|
| $3.60 per video | $0.32 per video | 91% |

Adding Transifex terminology costs almost nothing thanks to caching! 💰

## ⚙️ Environment Variables

```bash
# Required for translation
ANTHROPIC_API_KEY=your_anthropic_key

# Optional for Transifex (skips sync if not set)
TRANSIFEX_API_TOKEN=your_transifex_token

# Optional for GitHub automation
GITHUB_TOKEN=your_github_token
```

## 📁 Generated Files

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

**Tip**: Commit these files for offline access!

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `TRANSIFEX_API_TOKEN not set` | Add token to `.env` file |
| `No translations found` | Check org/project name, verify API access |
| `API rate limit` | Wait a few minutes, or use `--no-transifex-sync` |
| `Sync failed` | Script continues with cached files (non-blocking) |

## ✅ What Gets Synced

- **From**: KoboToolbox Transifex project (`kobotoolbox/kobotoolbox`)
- **What**: All UI interface strings
- **Languages**: Spanish (es), French (fr), Arabic (ar)
- **When**: Once per language per session (cached)
- **Where**: `skills/kobo-translation-{lang}/references/transifex-ui-terminology.md`

## 🎨 Integration Points

Both translation scripts support Transifex:

```bash
# SRT translations
python scripts/translate_srt.py video.srt -l es
python scripts/translate_srt.py video.srt -l es --no-transifex-sync

# Documentation translations  
python scripts/translation_agent.py --file doc.md -l es --save
python scripts/translation_agent.py --file doc.md -l es --no-transifex-sync
```

## 📚 Full Documentation

- **Setup Guide**: [TRANSIFEX_INTEGRATION.md](TRANSIFEX_INTEGRATION.md)
- **Usage Examples**: [TRANSIFEX_EXAMPLES.md](TRANSIFEX_EXAMPLES.md)
- **Architecture**: [TRANSIFEX_ARCHITECTURE.md](TRANSIFEX_ARCHITECTURE.md)
- **Summary**: [TRANSIFEX_SETUP_SUMMARY.md](TRANSIFEX_SETUP_SUMMARY.md)

## 🎯 Key Benefits

✅ **Consistency** - UI terms match KoboToolbox interface exactly  
✅ **Accuracy** - Professional, validated translations  
✅ **Efficiency** - Auto-sync, cached, cost-optimized  
✅ **Reliability** - Non-blocking, graceful fallbacks  
✅ **Flexibility** - Auto or manual, online or offline  

## 🔗 Quick Links

- Get Transifex token: https://app.transifex.com/user/settings/api/
- Transifex API docs: https://transifex.github.io/openapi/
- Claude API docs: https://docs.anthropic.com/

---

**Pro Tip**: For batch processing, sync once manually then use `--no-transifex-sync` for all translations to maximize efficiency! 🚀
