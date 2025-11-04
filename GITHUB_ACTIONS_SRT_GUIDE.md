# GitHub Actions SRT Translation - Quick Start

## 🚀 How to Translate Video Subtitles via GitHub Actions

### Step 1: Add Your English SRT File

1. Create or export your English subtitle file (`.srt` format)
2. Upload it to: `transcripts/en/your_video.srt`
3. Commit and push to GitHub

```bash
# Example
cp ~/Downloads/my_tutorial.srt transcripts/en/
git add transcripts/en/my_tutorial.srt
git commit -m "Add English subtitles for tutorial"
git push
```

### Step 2: Trigger the Workflow

1. Go to your GitHub repository
2. Click on the **Actions** tab
3. Select **Translate SRT Subtitles** from the left sidebar
4. Click the **Run workflow** button (top right)
5. Fill in the form:

**Example Configuration:**

| Field | Value | Notes |
|-------|-------|-------|
| **SRT file** | `my_tutorial.srt` | Just the filename, not the full path |
| **Languages** | `es,fr,ar` | All three, or just `es` for Spanish only |
| **Video title** | `Creating Forms Tutorial` | Helps AI understand context |
| **Chunk size** | `25` | Default is fine for most videos |
| **Overlap** | `3` | Default is fine for most videos |

6. Click **Run workflow** (green button)

### Step 3: Monitor Progress

- The workflow will appear in the Actions list
- Click on it to see real-time logs
- Takes 5-15 minutes depending on video length
- You'll see progress for each language

### Step 4: Download Translations

1. Once complete, scroll down to **Artifacts** section
2. Click **translated-subtitles** to download
3. Extract the ZIP file
4. Review the translations

### Step 5: Review Quality

Check each translated file:

**Brand Terms:**
```bash
# Check Spanish
grep -i "servidor" transcripts/es/my_tutorial.srt
# Should show "Servidor Global" NOT "Servidor Global de KoboToolbox"

# Check for Question Library
grep -i "biblioteca" transcripts/es/my_tutorial.srt
# Should show "La biblioteca de preguntas" (capital L)
```

**Character Limits:**
```bash
# Check line lengths
python scripts/srt_helper.py validate transcripts/es/my_tutorial.srt
```

**Subtitle Count:**
```bash
# Should match source
wc -l transcripts/en/my_tutorial.srt
wc -l transcripts/es/my_tutorial.srt
```

### Step 6: Commit Translations (if satisfied)

```bash
git add transcripts/es/ transcripts/fr/ transcripts/ar/
git commit -m "Add Spanish, French, and Arabic subtitles for my_tutorial"
git push
```

## 📋 Real Example

### Translating the Test Webinar

Let's translate the included test webinar to all languages:

**Step 1 - Already done**: `transcripts/en/test_webinar.srt` is in repo

**Step 2 - Run workflow**:
- **SRT file**: `test_webinar.srt`
- **Languages**: `es,fr,ar`
- **Video title**: `Kobo 10 Year Milestone Webinar`
- **Chunk size**: `25`
- **Overlap**: `3`

**Expected Result**:
- 3 files created
- Cost: ~$0.90 total
- Time: ~5 minutes
- Files:
  - `transcripts/es/test_webinar.srt`
  - `transcripts/fr/test_webinar.srt`
  - `transcripts/ar/test_webinar.srt`

## 🎯 Tips for Success

### Before Translation

✅ **DO:**
- Validate your source SRT file first
- Use descriptive video titles
- Start with one language to test quality
- Check estimated cost before translating

❌ **DON'T:**
- Translate without validating source first
- Use generic titles (reduces context quality)
- Skip the video title field
- Translate all languages without reviewing one first

### Choosing Parameters

**Chunk Size:**
- 2-5 min video → `30-40`
- 5-15 min video → `25` (default)
- 15-30 min video → `20`
- 30+ min video → `15-20`

**Overlap:**
- Simple tutorial → `3` (default)
- Standard content → `3-5`
- Complex topic → `5-7`

**Languages:**
- Test first → `es` only
- After review → `es,fr,ar` all at once
- Or one at a time → Run workflow 3 times

### Cost Management

**Estimate before translating:**

| Your Video | Approx. Subtitles | Cost/Lang | All 3 |
|------------|-------------------|-----------|-------|
| 5 min | ~120 | $1.00 | $3.00 |
| 10 min | ~240 | $2.50 | $7.50 |
| 20 min | ~480 | $5.00 | $15.00 |
| 30 min | ~720 | $7.50 | $22.50 |

**Ways to reduce cost:**
- Translate to one language first, review, then do others
- Use larger chunk sizes for simple content
- Split very long videos into parts

## 🔍 Troubleshooting

### "File not found" Error

**Problem**: Workflow can't find your SRT file

**Solutions:**
1. Check file is in `transcripts/en/` directory
2. Enter ONLY the filename (e.g., `video.srt`)
3. Don't include the directory path
4. Ensure file is committed and pushed

### Translation Quality Issues

**Problem**: Translations have errors

**Solutions:**
1. Add or improve the video title
2. Increase overlap (try `5` or `7`)
3. Decrease chunk size (try `20` or `15`)
4. Check source file for errors first

### Workflow Times Out

**Problem**: Very long video causes timeout

**Solutions:**
1. Split video into multiple SRT files
2. Translate one language at a time
3. Use smaller chunk size to reduce memory usage

### Character Limits Exceeded

**Problem**: Subtitles too long after translation

**Solutions:**
1. Review source - may already be too long
2. AI should compress automatically
3. Manually edit in subtitle editor if needed
4. Split long subtitles in source file

## 📊 Workflow Status Meanings

| Status | Icon | Meaning |
|--------|------|---------|
| Queued | 🟡 | Waiting to start |
| In Progress | 🔵 | Currently translating |
| Success | ✅ | All translations complete |
| Failed | ❌ | Error occurred, check logs |
| Cancelled | ⚪ | Manually stopped |

## 🎬 What Happens During Translation

1. **Validate** - Checks source SRT file is valid
2. **Parse languages** - Processes your language list
3. **Create directories** - Makes output folders (es, fr, ar)
4. **Translate** - For each language:
   - Loads translation skill
   - Chunks subtitles (25 at a time by default)
   - Translates each chunk with context
   - Validates output
5. **Generate summary** - Creates report
6. **Upload artifacts** - Makes translations downloadable

Total time depends on:
- Video length (more subtitles = longer)
- Number of languages (3x longer for all three)
- Chunk size (smaller = more API calls = longer)

## 📚 Additional Resources

- **Full workflow guide**: `SRT_WORKFLOW.md`
- **Translation guidelines**: `skills/kobo-translation-srt/SKILL.md`
- **Transcripts directory**: `transcripts/README.md`
- **Setup documentation**: `SETUP.md`

## ✨ Next Steps

1. Try with `test_webinar.srt` first
2. Review translation quality
3. Adjust parameters if needed
4. Translate your real videos
5. Upload to YouTube or your video platform

**That's it!** Your video subtitles will be professionally translated in minutes. 🎉
