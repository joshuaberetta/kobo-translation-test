# Transifex Integration Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                      TRANSLATION WORKFLOW                           │
└─────────────────────────────────────────────────────────────────────┘

1. USER INITIATES TRANSLATION
   │
   ├── python scripts/translate_srt.py video.srt --language es
   │   OR
   └── python scripts/translation_agent.py --file doc.md --language es

2. AGENT INITIALIZATION
   │
   ├── SRTTranslationAgent(sync_transifex=True)  ← Default
   └── TranslationAgent(sync_transifex=True)

3. LOAD SKILL CONTEXT (per language)
   │
   ├── Check if language already synced this session?
   │   │
   │   ├── YES → Skip Transifex sync (use cached)
   │   │
   │   └── NO → Sync Transifex terminology
   │       │
   │       ├── TransifexSync()
   │       ├── Fetch UI translations from API
   │       ├── Save to transifex-ui-terminology.md
   │       └── Mark language as synced
   │
   ├── Load base skill files
   │   ├── SKILL.md
   │   ├── brand-terminology.md
   │   ├── ui-terminology.md
   │   ├── transifex-ui-terminology.md  ← Fresh from Transifex!
   │   └── other reference files
   │
   └── Cache skill context

4. TRANSLATE WITH CLAUDE
   │
   ├── Build message with prompt caching:
   │   │
   │   ├── [Cached Block 1: Skill Context]
   │   │   ├── Base translation skill
   │   │   ├── Brand terminology
   │   │   ├── UI terminology  
   │   │   ├── Transifex UI terms  ← Included & cached!
   │   │   └── Other references
   │   │   └── cache_control: ephemeral  ← 90% savings!
   │   │
   │   └── [Block 2: Content to Translate]
   │       └── Current chunk/file
   │
   ├── First chunk: Cache WRITE ($3.75/MTok)
   └── Chunks 2-N: Cache READ ($0.30/MTok)  ← 90% cheaper!

5. OUTPUT
   │
   └── Translated content with consistent UI terminology
```

## Data Flow

```
┌─────────────────┐
│   Transifex     │  Official UI translations
│   (KoboToolbox) │  kobotoolbox/kobotoolbox
└────────┬────────┘
         │ HTTPS API
         │ (once per language per session)
         ↓
┌─────────────────────────┐
│  transifex_sync.py      │  Fetch & format translations
│  TransifexSync class    │
└────────┬────────────────┘
         │ Save markdown
         ↓
┌────────────────────────────────────────┐
│  skills/kobo-translation-{lang}/       │  Skill files
│    references/                         │
│      ├── transifex-ui-terminology.md   │  ← Auto-generated
│      ├── brand-terminology.md          │
│      ├── ui-terminology.md             │
│      └── ...                           │
└────────┬───────────────────────────────┘
         │ Read all files
         ↓
┌─────────────────────────┐
│  translate_srt.py       │  SRT translator
│  OR                     │
│  translation_agent.py   │  Docs translator
└────────┬────────────────┘
         │ Build prompt with caching
         ↓
┌─────────────────────────┐
│  Claude API             │  Translate with context
│  (Anthropic)            │
│  with Prompt Caching    │
└────────┬────────────────┘
         │ Translation
         ↓
┌─────────────────────────┐
│  Output Files           │
│  ├── transcripts/es/    │
│  ├── transcripts/fr/    │
│  ├── docs/es/           │
│  └── docs/fr/           │
└─────────────────────────┘
```

## Caching Strategy

```
SESSION LIFECYCLE:

┌─────────────────────────────────────────────────────────────┐
│ Session Start                                               │
└─────────────────────────────────────────────────────────────┘
  │
  ├── Translation 1: Spanish video
  │   ├── Sync Transifex ES (API call)
  │   ├── Load skill context
  │   ├── Translate chunk 1 (cache WRITE)
  │   ├── Translate chunk 2 (cache READ) ← 90% cheaper
  │   └── Translate chunk 3 (cache READ)
  │
  ├── Translation 2: Another Spanish video (same session)
  │   ├── Skip Transifex sync (already synced ES)
  │   ├── Use cached skill context
  │   ├── Translate chunk 1 (cache WRITE)
  │   └── Translate chunks 2-N (cache READ)
  │
  ├── Translation 3: French video
  │   ├── Sync Transifex FR (API call)
  │   ├── Load skill context
  │   ├── Translate chunk 1 (cache WRITE)
  │   └── Translate chunks 2-N (cache READ)
  │
  └── Translation 4: Another French video (same session)
      ├── Skip Transifex sync (already synced FR)
      └── Translate with caching...

┌─────────────────────────────────────────────────────────────┐
│ Session End (or 5 minutes of cache inactivity)             │
│ Cache expires automatically                                 │
└─────────────────────────────────────────────────────────────┘
```

## Cost Comparison

```
WITHOUT TRANSIFEX INTEGRATION:
────────────────────────────────
Translation relies on:
- Manual terminology lookup
- Generic translation patterns  
- Risk of inconsistent UI terms
Cost: $X for translation only

WITH TRANSIFEX INTEGRATION (No Caching):
─────────────────────────────────────────
Translation includes:
+ Transifex UI terminology (15K tokens)
+ Full skill context per chunk
Cost per chunk: $0.045 input + $0.015 output = $0.060
60 chunks: $3.60

WITH TRANSIFEX INTEGRATION + PROMPT CACHING:
─────────────────────────────────────────────
Translation includes:
+ Transifex UI terminology (15K tokens)
+ Full skill context (CACHED!)

Chunk 1: Cache WRITE
  15K tokens × $3.75/MTok = $0.056

Chunks 2-60: Cache READ  
  15K tokens × $0.30/MTok × 59 = $0.265

Total: $0.321 (instead of $3.60!)
Savings: $3.28 (91% reduction!)

┌──────────────────────────────────────────────────┐
│  TRANSIFEX ADDS ACCURACY WITH MINIMAL COST       │
│  Thanks to prompt caching! 🚀                    │
└──────────────────────────────────────────────────┘
```

## File Structure

```
kobo-translation-test/
│
├── .env                           ← TRANSIFEX_API_TOKEN here
│
├── scripts/
│   ├── transifex_sync.py         ← NEW: Transifex integration
│   ├── translate_srt.py           ← UPDATED: Auto-sync
│   ├── translation_agent.py       ← UPDATED: Auto-sync
│   └── requirements.txt           ← UPDATED: Added requests
│
├── skills/
│   ├── kobo-translation-es/
│   │   └── references/
│   │       ├── transifex-ui-terminology.md  ← Auto-generated
│   │       ├── brand-terminology.md
│   │       └── ui-terminology.md
│   │
│   ├── kobo-translation-fr/
│   │   └── references/
│   │       ├── transifex-ui-terminology.md  ← Auto-generated
│   │       └── ...
│   │
│   └── kobo-translation-ar/
│       └── references/
│           ├── transifex-ui-terminology.md  ← Auto-generated
│           └── ...
│
├── test_transifex_integration.py  ← NEW: Test script
│
├── TRANSIFEX_INTEGRATION.md       ← NEW: Full documentation
├── TRANSIFEX_EXAMPLES.md          ← NEW: Usage examples
└── TRANSIFEX_SETUP_SUMMARY.md     ← NEW: Quick summary
```

## API Interactions

```
┌──────────────────────────┐
│  Your Script             │
│  translate_srt.py        │
└──────┬───────────────────┘
       │
       │ 1. Check if sync needed
       ↓
┌──────────────────────────┐
│  transifex_sync.py       │
│  TransifexSync()         │
└──────┬───────────────────┘
       │
       │ 2. GET /resources
       ↓
┌──────────────────────────────────┐
│  Transifex API                   │
│  https://rest.api.transifex.com  │
└──────┬───────────────────────────┘
       │ 3. Resources list
       ↓
┌──────────────────────────┐
│  transifex_sync.py       │
└──────┬───────────────────┘
       │
       │ 4. GET /resource_translations
       ↓
┌──────────────────────────────────┐
│  Transifex API                   │
└──────┬───────────────────────────┘
       │ 5. UI translations
       ↓
┌──────────────────────────┐
│  transifex_sync.py       │
│  Format & Save           │
└──────┬───────────────────┘
       │ 6. Write markdown
       ↓
┌──────────────────────────────────┐
│  skills/.../references/          │
│  transifex-ui-terminology.md     │
└──────┬───────────────────────────┘
       │ 7. Load context
       ↓
┌──────────────────────────┐
│  translate_srt.py        │
│  Build Claude prompt     │
└──────┬───────────────────┘
       │
       │ 8. POST /messages (with caching)
       ↓
┌──────────────────────────────────┐
│  Claude API (Anthropic)          │
│  with Prompt Caching             │
└──────┬───────────────────────────┘
       │ 9. Translation
       ↓
┌──────────────────────────┐
│  Output File             │
│  transcripts/es/*.srt    │
└──────────────────────────┘
```

## Error Handling Flow

```
┌──────────────────────────┐
│  Attempt Transifex Sync  │
└──────┬───────────────────┘
       │
       ├─→ Success? ────→ Use fresh translations
       │
       ├─→ No token? ──→ Warn → Use cached files
       │
       ├─→ API error? ─→ Warn → Use cached files
       │
       ├─→ No data? ───→ Warn → Use cached files
       │
       └─→ Rate limit? ─→ Warn → Use cached files
              ↓
       ┌──────────────────────────┐
       │  Translation continues   │
       │  (never blocked!)        │
       └──────────────────────────┘
```

## Key Design Principles

1. **Non-Blocking**: Transifex issues never prevent translation
2. **Cached**: Sync once per language per session
3. **Cost-Effective**: Leverage Claude's prompt caching
4. **Graceful Degradation**: Falls back to cached files
5. **Developer-Friendly**: Clear error messages
6. **Automatic**: Works by default, optional to disable
7. **Transparent**: Shows sync status in output

## Summary

The Transifex integration seamlessly adds official UI terminology to your translations:

✅ Automatic sync before first use  
✅ Cached for efficiency (once per language)  
✅ Integrated with prompt caching (90% cost savings)  
✅ Non-blocking error handling  
✅ Works with both SRT and docs translation  
✅ Can be disabled for offline work  

**Result**: More accurate translations with KoboToolbox UI consistency, at minimal extra cost! 🎯
