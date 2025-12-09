# SRT Translation Workflow - Quick Reference

## Overview

The SRT translation system translates video subtitles while:
- ✅ Preserving timing and formatting
- ✅ Maintaining context across chunks
- ✅ Respecting character limits for readability
- ✅ Following all KoboToolbox translation guidelines
- ✅ Minimizing hallucinations through smart chunking

## Quick Start

### 1. Validate Your SRT File

```bash
python scripts/srt_helper.py validate your_video.srt
```

### 2. Translate

```bash
python scripts/translate_srt.py your_video.srt \
  --language es \
  --video-title "Your Video Title"
```

Output: `your_video_es.srt`

### 3. Translate All Languages

```bash
for lang in es fr ar; do
  python scripts/translate_srt.py your_video.srt --language $lang
done
```

## Key Features

### Chunked Translation

Subtitles are processed in overlapping chunks:
- **Default**: 25 subtitles per chunk
- **Overlap**: 3 subtitles for context
- **Context**: Previous and next subtitles provided to AI

This prevents:
- ❌ Context loss across the video
- ❌ Hallucinations from large context windows
- ❌ Terminology drift

### Character Limits

Translations automatically compress to meet subtitle standards:
- **Ideal**: 35-42 characters per line
- **Maximum**: 50 characters per line
- **Lines**: Max 2 per subtitle

### Technical Term Handling

**Different from documentation:**

| Term Type | Documentation | Subtitles |
|-----------|--------------|-----------|
| XLSForm terms | list_name (nom de la liste) | list_name |
| Brand terms | Exact match required | Exact match required |
| UI elements | Exact match required | Exact match required |

**Why?** Character limits and on-screen visibility.

## Tools

### `srt_helper.py` - Utility Functions

**Parse SRT to JSON:**
```bash
python scripts/srt_helper.py parse video.srt --output video.json
```

**Convert JSON back to SRT:**
```bash
python scripts/srt_helper.py convert video.json --output video.srt
```

**Validate SRT file:**
```bash
python scripts/srt_helper.py validate video.srt
```

Checks for:
- Sequential numbering
- Valid timestamps
- No overlaps
- No empty subtitles

### `translate_srt.py` - Translation Agent

**Basic usage:**
```bash
python scripts/translate_srt.py SOURCE.srt --language LANG
```

**Full options:**
```bash
python scripts/translate_srt.py SOURCE.srt \
  --language es \                    # Target language (es/fr/ar)
  --output custom_output.srt \       # Custom output path
  --chunk-size 25 \                  # Subtitles per chunk
  --overlap 3 \                      # Overlap for context
  --video-title "Title" \            # For better context
  --api-key YOUR_KEY                 # Or use env var
```

## Parameters Guide

### Chunk Size

| Size | Use Case | Pros | Cons |
|------|----------|------|------|
| 15-20 | Long videos (>30 min) | Better consistency | More API calls, higher cost |
| 25 | **Default - most videos** | **Balanced** | **Recommended** |
| 30-40 | Short videos (<5 min) | Fewer API calls, cheaper | Risk of context loss |

### Overlap

| Size | Use Case | Benefit |
|------|----------|---------|
| 2-3 | Simple instructional videos | Basic continuity |
| 3-5 | **Default - most content** | **Good context preservation** |
| 5-7 | Complex narratives | Strong consistency, prevents drift |

## Cost Estimates

Based on Claude Sonnet 4 pricing ($3/M input, $15/M output tokens):

| Video Length | Subtitles | Cost per Language | All 3 Languages |
|--------------|-----------|-------------------|-----------------|
| 2 min | ~45 | $0.25-0.35 | $0.90 |
| 5 min | ~120 | $0.80-1.20 | $3.00 |
| 10 min | ~225 | $2.00-3.00 | $7.50 |
| 30 min | ~675 | $6.00-9.00 | $22.50 |
| 60 min | ~1350 | $12.00-18.00 | $45.00 |

**Factors affecting cost:**
- Video complexity (technical terms = more context needed)
- Chunk size (smaller = more API calls)
- Overlap size (more = more tokens)
- Language (Arabic slightly more expensive due to RTL)

## Workflow Examples

### Tutorial Video

```bash
# 1. Export subtitles from YouTube
# Download as .srt file

# 2. Validate
python scripts/srt_helper.py validate tutorial.srt

# 3. Translate
python scripts/translate_srt.py tutorial.srt \
  --language es \
  --video-title "Creating Forms in KoboToolbox"

# 4. Review in subtitle editor
# Check timing, character limits, terminology

# 5. Upload back to YouTube
```

### Webinar Recording

```bash
# Webinars are typically longer - adjust parameters

python scripts/translate_srt.py webinar.srt \
  --language es \
  --chunk-size 20 \      # Smaller chunks for long content
  --overlap 5 \          # More overlap for consistency
  --video-title "Q&A: Advanced Features"
```

### Batch Processing Multiple Videos

```bash
#!/bin/bash
# translate_all_tutorials.sh

VIDEOS_DIR="video_subtitles"

for srt_file in $VIDEOS_DIR/*.srt; do
  echo "Processing: $srt_file"
  
  # Extract video name for title
  video_name=$(basename "$srt_file" .srt)
  
  # Translate to all languages
  for lang in es fr ar; do
    python scripts/translate_srt.py "$srt_file" \
      --language "$lang" \
      --video-title "$video_name"
  done
  
  echo "Completed: $video_name"
done

echo "All videos translated!"
```

## Quality Assurance

### Automated Checks

```bash
# After translation, validate structure
python scripts/srt_helper.py validate output_es.srt

# Check subtitle count matches
wc -l original.srt output_es.srt
# Should have same number of subtitle blocks
```

### Manual Review Checklist

**Brand Terms:**
- [ ] "Servidor Global" (not "Servidor Global de KoboToolbox")
- [ ] "La biblioteca de preguntas" (capital L)
- [ ] "Formbuilder" appropriate for context
- [ ] All UI terms match official translations

**Technical Terms:**
- [ ] XLSForm terms in English (list_name, choice_filter)
- [ ] No parenthetical translations added
- [ ] Consistent across all chunks

**Subtitle Quality:**
- [ ] All lines under 50 characters
- [ ] Most lines 35-42 characters
- [ ] Natural spoken language
- [ ] Readable at normal playback speed
- [ ] Proper line breaks at natural pauses

**Context & Flow:**
- [ ] Narrative flows naturally
- [ ] No terminology drift
- [ ] Consistent formality (tú/vous)
- [ ] Gender-inclusive language maintained

### Review in Subtitle Editor

**Recommended tools:**
- **Subtitle Edit** (Windows/Linux) - Free, powerful
- **Aegisub** (All platforms) - Free, advanced features
- **Subtitle Workshop** (Windows) - Free, simple

**What to check:**
1. Open translated SRT in editor
2. Play video with subtitles
3. Check timing sync
4. Verify readability
5. Check character limits visually
6. Adjust if needed

## Troubleshooting

### "Subtitles too long"

If translations exceed character limits:

```bash
# Option 1: The AI should compress automatically,
# but you can manually edit in subtitle editor

# Option 2: Re-translate with stricter guidance
# (Currently handled automatically, but could be adjusted in translate_srt.py)
```

### "Context lost between chunks"

```bash
# Increase overlap
python scripts/translate_srt.py video.srt \
  --language es \
  --overlap 7  # More context

# Or decrease chunk size
python scripts/translate_srt.py video.srt \
  --language es \
  --chunk-size 15  # Smaller, more frequent chunks
```

### "Technical terms translated incorrectly"

```bash
# Search for problematic terms
grep -i "list_name\|cascading\|choice_filter" output_es.srt

# Should all be in English
# If translated, this is a bug - report it
```

### "Brand terms wrong"

```bash
# Check server names
grep -n "Servidor" output_es.srt

# Check Question Library
grep -n "biblioteca de preguntas" output_es.srt

# Should match brand-terminology.md exactly
```

### "Validation fails"

```bash
# Common issues:
# 1. Missing subtitle numbers
# 2. Malformed timestamps
# 3. Empty text blocks

# Re-run translation or fix manually in subtitle editor
```

## API Usage Tips

### Rate Limits

- Claude API has rate limits (varies by tier)
- For large batches, add delays between translations
- Monitor usage in Anthropic console

### Token Optimization

- Longer videos = more tokens
- Adjust chunk size to balance cost vs quality
- Use `--video-title` to give context without extra tokens

### Cost Management

```bash
# Estimate before translating
# Formula: (subtitle_count / chunk_size) * chunks * languages * ~$0.30

# Example: 120 subtitles, 25 per chunk, 3 languages
# (120 / 25) * 3 * $0.30 = ~$4.32

# Preview without translating (upcoming feature)
# python scripts/translate_srt.py video.srt --dry-run --language es
```

## Skills System

SRT translation uses a specialized skill extension:

**Main skill**: `skills/kobo-translation/SKILL.md`
- All base translation rules
- Brand terminology
- UI terminology
- Language-specific guidelines

**SRT extension**: `skills/kobo-translation-srt/SKILL.md`
- Inherits ALL base rules
- Adds subtitle-specific adaptations:
  - Character limits
  - Spoken language patterns
  - Chunked context management
  - Timing awareness

**References**: `skills/kobo-translation-srt/references/`
- `subtitle-guidelines.md` - Detailed subtitle best practices

The system automatically loads the appropriate skill based on file type.

## Integration with Existing Workflow

### Standalone Use

```bash
# Use SRT tools independently
python scripts/translate_srt.py video.srt --language es
```

### With Documentation Translation

```bash
# Translate documentation
python scripts/translation_agent.py doc.md --language es

# Translate matching video subtitles
python scripts/translate_srt.py video.srt --language es

# Both use same terminology and brand guidelines!
```

### GitHub Actions (future enhancement)

Could add `.github/workflows/translate-subtitles.yml` for automation similar to documentation workflow.

## Examples

### Sample Files

The repository includes example files in `examples/`:

```
examples/
├── sample_transcript_en.srt    # English tutorial (45 subtitles, 2.5 min)
└── [translated versions after running]
```

**Test the workflow:**

```bash
# Validate
python scripts/srt_helper.py validate examples/sample_transcript_en.srt

# Translate to Spanish
python scripts/translate_srt.py examples/sample_transcript_en.srt \
  --language es \
  --video-title "Creating Forms in KoboToolbox"

# Check output
cat examples/sample_transcript_en_es.srt

# Validate translation
python scripts/srt_helper.py validate examples/sample_transcript_en_es.srt
```

## Best Practices

1. **Always validate before translating**
   - Catch errors in source file first
   - Ensures proper formatting

2. **Use meaningful video titles**
   - Helps AI understand context
   - Improves terminology consistency

3. **Test with short videos first**
   - Verify quality before large batches
   - Check cost estimates

4. **Review brand terms carefully**
   - Most common source of errors
   - Use search to verify all instances

5. **Check character limits visually**
   - Open in subtitle editor with video
   - Verify readability at normal speed

6. **Maintain consistency across videos**
   - Same terminology throughout a series
   - Track how you translate recurring concepts

7. **Keep source files**
   - Always keep original English SRT
   - Version control for translations
   - Easy to re-translate if skill improves

## Support & Documentation

- **Main setup guide**: `SETUP.md` - Full workflow documentation
- **Quick start**: `QUICKSTART.md` - Get started in minutes
- **Translation skill**: `skills/kobo-translation/SKILL.md`
- **SRT skill extension**: `skills/kobo-translation-srt/SKILL.md`
- **Subtitle guidelines**: `skills/kobo-translation-srt/references/subtitle-guidelines.md`

## Summary

The SRT translation workflow provides:
- ✅ **Accurate** translations following KoboToolbox guidelines
- ✅ **Context-aware** chunking to prevent hallucinations
- ✅ **Character-limited** output for on-screen readability
- ✅ **Cost-effective** processing with smart chunk sizes
- ✅ **Consistent** terminology across all videos
- ✅ **Validated** output with automatic quality checks

Perfect for translating KoboToolbox video tutorials, webinars, and training content while maintaining brand integrity and technical accuracy.
