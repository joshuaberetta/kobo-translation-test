# Transifex Integration

This project integrates with KoboToolbox's Transifex project to automatically sync the latest UI terminology before translating documentation and subtitles.

## Overview

The translation agents (`translate_srt.py` and `translation_agent.py`) can automatically fetch the latest UI translations from Transifex and incorporate them into the translation process. This ensures that UI elements, buttons, and interface terms are always translated consistently with the official KoboToolbox interface.

## Setup

### 1. Get Your Transifex API Token

1. Go to [Transifex User Settings](https://app.transifex.com/user/settings/api/)
2. Generate a new API token
3. Copy the token

### 2. Configure Environment Variable

Add your Transifex API token to your `.env` file:

```bash
# .env
ANTHROPIC_API_KEY=your_anthropic_key_here
TRANSIFEX_API_TOKEN=your_transifex_token_here
```

### 3. Install Dependencies

Make sure you have all required dependencies:

```bash
cd scripts
pip install -r requirements.txt
```

## Usage

### Automatic Sync (Recommended)

By default, both translation scripts will automatically sync Transifex terminology before translating:

```bash
# SRT translation with auto-sync
python scripts/translate_srt.py transcripts/en/webinar.srt --language es

# Documentation translation with auto-sync
python scripts/translation_agent.py --file docs/en/creating_account.md --language fr --save
```

The sync happens **once per language per session** and is cached for efficiency.

### Manual Sync

You can also manually sync terminology for all languages:

```bash
# Sync all languages (es, fr, ar)
python scripts/transifex_sync.py

# Sync specific language
python scripts/transifex_sync.py --language es

# Sync multiple specific languages
python scripts/transifex_sync.py --language es --language fr
```

### Disable Transifex Sync

If you want to skip Transifex syncing (e.g., for testing or offline work):

```bash
# SRT translation without Transifex sync
python scripts/translate_srt.py transcripts/en/webinar.srt --language es --no-transifex-sync

# Documentation translation without Transifex sync
python scripts/translation_agent.py --file docs/en/test.md --language es --no-transifex-sync
```

## How It Works

### 1. Fetching Translations

The `TransifexSync` class fetches translations from the Transifex API:

```python
from transifex_sync import TransifexSync

sync = TransifexSync()
translations = sync.sync_language_terminology('es')  # Returns dict of English -> Spanish
```

### 2. Saving to Skill References

Synced terminology is saved as markdown files in the skill references:

```
skills/
  kobo-translation-es/
    references/
      transifex-ui-terminology.md  ← Auto-generated
      brand-terminology.md
      ui-terminology.md
      ...
```

### 3. Integration with Claude API

The synced terminology is loaded with other skill files and included in the Claude API prompt using **prompt caching** for efficiency:

```python
# Cached skill context includes Transifex terminology
message_content = [
    {
        "type": "text",
        "text": skill_context,  # Includes Transifex UI terms
        "cache_control": {"type": "ephemeral"}  # Cached!
    },
    {
        "type": "text", 
        "text": content_to_translate
    }
]
```

## Benefits

### 1. **Consistency**
- UI terms match exactly what users see in KoboToolbox
- No more manual lookups in Transifex
- Terminology stays up-to-date automatically

### 2. **Efficiency**
- Synced terminology is cached with Claude's prompt caching (90% cost savings)
- Sync happens once per language per session
- Files are saved locally for offline reference

### 3. **Accuracy**
- Official translations from professional translators
- Community-validated terminology
- Includes context and usage notes

## Transifex Project Structure

The integration targets the KoboToolbox Transifex project:

- **Organization**: `kobotoolbox`
- **Project**: `kobotoolbox`
- **Resources**: All UI interface strings

To customize which resources to sync, modify `transifex_sync.py`:

```python
# In sync_language_terminology method
resources = ['main-interface', 'form-builder', 'data-table']  # Specify resources
```

## Advanced Usage

### List Available Resources

To see what resources are available in the Transifex project:

```bash
python scripts/transifex_sync.py --list-resources
```

### Custom Organization/Project

If you're working with a different Transifex project:

```bash
python scripts/transifex_sync.py \
  --organization your-org \
  --project your-project \
  --language es
```

### Programmatic Usage

Use the `TransifexSync` class in your own scripts:

```python
from transifex_sync import TransifexSync

sync = TransifexSync(api_token="your_token")

# Get translations
translations = sync.sync_language_terminology('es')

# Format as markdown
markdown = sync.format_terminology_markdown(translations, 'es')

# Save to custom location
from pathlib import Path
output_path = sync.save_terminology_file(
    translations, 
    'es',
    base_skill_path=Path('custom/path')
)
```

## Caching & Cost Optimization

The Transifex integration works seamlessly with Claude's prompt caching:

1. **First chunk**: Synced terminology is sent to Claude with `cache_control`
   - Cache write cost: $3.75/MTok (25% premium)

2. **Subsequent chunks**: Cached terminology is reused
   - Cache read cost: $0.30/MTok (90% discount)
   - Massive savings for long translations!

### Example Savings

For a 30-minute video (60 chunks):
- Without caching: $0.18 for terminology context per chunk = **$10.80 total**
- With caching: $0.18 write + ($0.018 × 59) = **$1.24 total**
- **Savings: $9.56 (88%)**

## Troubleshooting

### Missing API Token

If you see:
```
⚠️  Skipping Transifex sync: TRANSIFEX_API_TOKEN not set
```

Add your token to `.env`:
```bash
TRANSIFEX_API_TOKEN=your_token_here
```

### No Translations Found

If you see:
```
⚠️  No Transifex translations found
```

Possible causes:
1. Wrong organization/project name
2. Resource doesn't exist for this language
3. API token doesn't have access to the project

Use `--list-resources` to verify the project structure.

### API Rate Limits

Transifex has rate limits. If you hit them:
1. The script will warn and continue without fresh sync
2. It will use previously synced files (if available)
3. Wait a few minutes and try again

### Slow Syncing

If syncing is slow:
1. Reduce the number of resources to sync
2. Sync only the languages you need: `--language es`
3. The sync is cached per session, so it only happens once

## Best Practices

### 1. Sync Before Bulk Translations

If you're translating many files, sync once first:

```bash
# Sync all languages upfront
python scripts/transifex_sync.py

# Now translate without sync delays
python scripts/translate_srt.py video1.srt --language es --no-transifex-sync
python scripts/translate_srt.py video2.srt --language es --no-transifex-sync
```

### 2. Commit Synced Files

Commit the auto-generated terminology files to version control:

```bash
git add skills/*/references/transifex-ui-terminology.md
git commit -m "Update Transifex terminology"
```

This provides:
- History of terminology changes
- Offline access
- Reproducible translations

### 3. Scheduled Syncs

Set up a scheduled job to keep terminology fresh:

```bash
# cron job (daily at 2am)
0 2 * * * cd /path/to/project && python scripts/transifex_sync.py
```

Or use GitHub Actions:

```yaml
name: Sync Transifex Terminology
on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2am
  workflow_dispatch:  # Manual trigger

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          cd scripts
          pip install -r requirements.txt
      
      - name: Sync Transifex
        env:
          TRANSIFEX_API_TOKEN: ${{ secrets.TRANSIFEX_API_TOKEN }}
        run: python scripts/transifex_sync.py
      
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add skills/*/references/transifex-ui-terminology.md
          git diff --staged --quiet || git commit -m "Update Transifex terminology"
          git push
```

## API Reference

### TransifexSync Class

#### `__init__(api_token: str = None)`
Initialize with API token (or from env var).

#### `sync_language_terminology(language: str) -> Dict[str, str]`
Fetch all UI translations for a language.

#### `save_terminology_file(translations: Dict, language: str) -> Path`
Save translations to skill reference file.

#### `sync_all_languages(languages: List[str] = None) -> Dict[str, Path]`
Sync multiple languages at once.

#### `get_project_resources(organization: str, project: str) -> List[Dict]`
List all resources in a Transifex project.

## Support

For issues with:
- **Transifex API**: Check [Transifex API docs](https://transifex.github.io/openapi/)
- **This integration**: Open an issue on GitHub
- **KoboToolbox terminology**: Contact the KoboToolbox team

## Related Documentation

- [SRT Translation Guide](SRT_IMPLEMENTATION.md)
- [Prompt Caching Implementation](PROMPT_CACHING_IMPLEMENTATION.md)
- [Translation Agent Quickstart](QUICKSTART.md)
