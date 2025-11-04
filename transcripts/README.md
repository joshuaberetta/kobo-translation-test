# Video Transcripts Directory

This directory contains video subtitles/transcripts in SRT format organized by language.

## Directory Structure

```
transcripts/
├── en/          # English source transcripts (original)
├── es/          # Spanish translations
├── fr/          # French translations
└── ar/          # Arabic translations
```

## How to Use the Translation Workflow

### Option 1: GitHub Actions UI (Recommended)

1. Go to your repository on GitHub
2. Click on **Actions** tab
3. Select **Translate SRT Subtitles** workflow
4. Click **Run workflow** button
5. Fill in the form:
   - **SRT file**: Enter filename (e.g., `intro_tutorial.srt`)
   - **Languages**: Enter comma-separated languages (e.g., `es,fr,ar` or just `es`)
   - **Video title**: Optional but recommended (e.g., "Introduction to KoboToolbox")
   - **Chunk size**: Default 25 (adjust for video length)
   - **Overlap**: Default 3 (increase for long videos)
6. Click **Run workflow**
7. Wait for completion (5-15 minutes depending on video length)
8. **A Pull Request will be automatically created** with the translations
9. Review the PR, check the quality checklist
10. Merge the PR when satisfied

### Option 2: Local Translation

```bash
# Translate a single file to one language
python scripts/translate_srt.py transcripts/en/video.srt \
  --language es \
  --video-title "Video Title"

# Output will be: transcripts/en/video_es.srt
# Move it to: transcripts/es/video.srt
```

### Option 3: Batch Local Translation

```bash
#!/bin/bash
# Script to translate all languages locally

SOURCE="transcripts/en/video.srt"
TITLE="Video Title"

for lang in es fr ar; do
  mkdir -p "transcripts/$lang"
  python scripts/translate_srt.py "$SOURCE" \
    --language "$lang" \
    --output "transcripts/$lang/$(basename $SOURCE)" \
    --video-title "$TITLE"
done
```

## Naming Convention

**Important**: Use consistent filenames across languages:

```
transcripts/en/intro_tutorial.srt      # English
transcripts/es/intro_tutorial.srt      # Spanish
transcripts/fr/intro_tutorial.srt      # French
transcripts/ar/intro_tutorial.srt      # Arabic
```

Do NOT use language suffixes (like `intro_tutorial_es.srt`) in the translated directories.

## Workflow Parameters

### Languages
- `es` - Spanish
- `fr` - French
- `ar` - Arabic
- `es,fr,ar` - All three languages

### Chunk Size
Adjust based on video length:
- **Short videos (<5 min)**: 30-40 subtitles
- **Medium videos (5-15 min)**: 25 subtitles (default)
- **Long videos (15-30 min)**: 20 subtitles
- **Very long videos (>30 min)**: 15-20 subtitles

### Overlap
Context between chunks:
- **Simple content**: 2-3 subtitles
- **Standard content**: 3-5 subtitles (default)
- **Complex content**: 5-7 subtitles

## Quality Checklist

After translation, verify:

**Brand Terms:**
- [ ] Server names correct (e.g., "Servidor Global" not "Servidor Global de KoboToolbox")
- [ ] Question Library capitalized (e.g., "La biblioteca de preguntas")
- [ ] Formbuilder referenced correctly
- [ ] All UI terms match official translations

**Subtitle Quality:**
- [ ] Character limits respected (<50 chars per line)
- [ ] Natural spoken language (not overly formal)
- [ ] Technical terms in English (list_name, cascading select, etc.)
- [ ] Consistent terminology throughout
- [ ] Readable at normal playback speed

**Technical:**
- [ ] Same number of subtitles as source
- [ ] No timing changes
- [ ] No missing or empty subtitles
- [ ] Valid SRT format

## Cost Estimates

Based on Claude Sonnet 4 pricing:

| Video Length | Subtitles | Cost/Language | All 3 Languages |
|--------------|-----------|---------------|-----------------|
| 2 min | ~45 | $0.25-0.35 | $0.90 |
| 5 min | ~120 | $0.80-1.20 | $3.00 |
| 10 min | ~225 | $2.00-3.00 | $7.50 |
| 30 min | ~675 | $6.00-9.00 | $22.50 |
| 60 min | ~1350 | $12.00-18.00 | $45.00 |

## Troubleshooting

### Workflow fails with "File not found"
- Check the filename is correct
- Ensure file is in `transcripts/en/` directory
- Filename should NOT include `transcripts/en/` prefix in the input

### Translation quality issues
- Increase overlap for better context
- Decrease chunk size for tighter control
- Add video title for better AI context
- Review brand terminology in source file

### Cost concerns
- Use larger chunk sizes for shorter videos
- Translate one language at a time to test first
- Review sample before full translation

## Examples

### Example 1: Short Tutorial (5 minutes)

**Input:**
- File: `transcripts/en/quick_start.srt`
- Languages: `es,fr,ar`
- Video Title: "Quick Start Guide"
- Chunk Size: 30
- Overlap: 3

**Result:**
- Cost: ~$3.00 (all 3 languages)
- Time: ~5-8 minutes
- Output: 3 files in respective directories

### Example 2: Long Webinar (60 minutes)

**Input:**
- File: `transcripts/en/annual_webinar.srt`
- Languages: `es`
- Video Title: "Annual Community Webinar 2025"
- Chunk Size: 20
- Overlap: 5

**Result:**
- Cost: ~$15.00 (one language)
- Time: ~20-30 minutes
- Output: `transcripts/es/annual_webinar.srt`

### Example 3: Test Single Language First

**Workflow 1 - Test Spanish:**
- File: `transcripts/en/new_video.srt`
- Languages: `es`
- Review quality

**Workflow 2 - Full Translation:**
- File: `transcripts/en/new_video.srt`
- Languages: `es,fr,ar`
- After Spanish review passed

## Additional Resources

- **SRT Workflow Guide**: See `SRT_WORKFLOW.md` in repository root
- **Translation Guidelines**: See `skills/kobo-translation-srt/SKILL.md`
- **Parser Documentation**: See `scripts/srt_helper.py` comments

## Support

If you encounter issues:
1. Check workflow logs in GitHub Actions
2. Validate source SRT file: `python scripts/srt_helper.py validate transcripts/en/file.srt`
3. Test locally before using workflow
4. Review cost estimates before large batches
