# Voice Generation POC - Eleven Labs Integration

## Overview
This Proof of Concept (POC) demonstrates integration with Eleven Labs API to generate realistic AI voices from translated content. It supports Spanish, French, and Arabic voice generation from translated SRT subtitle files.

## Features

### ✅ Implemented in POC
- 🎙️ Text-to-speech generation using Eleven Labs multilingual v2 model
- 🌍 Support for Spanish (es), French (fr), and Arabic (ar)
- 📊 Character usage tracking and cost estimation
- ⚙️ Configurable voice settings (stability, similarity, style)
- 🎯 Automatic language detection from SRT filenames
- 📁 Organized output structure (`audio/{lang}/`)
- 🔄 Batch processing for multiple files
- 📝 Comprehensive documentation and skills

### 🎯 Key Capabilities
- Converts translated SRT files to natural-sounding audio
- Preserves subtitle timing information for synchronization
- Customizable voice selection per language
- Environment-based configuration for voice IDs
- CLI interface matching existing translation tools

## Installation

### 1. Install Dependencies
```bash
cd scripts/
pip install -r requirements.txt
```

This will install:
- `elevenlabs>=1.0.0` - Eleven Labs Python SDK
- `anthropic>=0.39.0` - Claude API (for translations)
- `PyGithub>=2.1.1` - GitHub integration
- `python-dotenv>=1.0.0` - Environment configuration

### 2. Set Up API Key
Get your Eleven Labs API key from: https://elevenlabs.io/

Add to your environment:
```bash
# Add to .env file
echo "ELEVENLABS_API_KEY=your_api_key_here" >> .env

# Or export directly
export ELEVENLABS_API_KEY="your_api_key_here"
```

### 3. (Optional) Configure Custom Voices
```bash
# Set custom voice IDs per language
export ELEVENLABS_VOICE_ES="your_spanish_voice_id"
export ELEVENLABS_VOICE_FR="your_french_voice_id"
export ELEVENLABS_VOICE_AR="your_arabic_voice_id"
```

## Quick Start

### Basic Usage

#### Generate voice for a single SRT file:
```bash
python scripts/generate_voice.py transcripts/es/webinar-es.srt
```

#### Generate for multiple files:
```bash
python scripts/generate_voice.py transcripts/es/*.srt
```

#### Generate for all languages:
```bash
python scripts/generate_voice.py transcripts/es/webinar-es.srt transcripts/fr/webinar-fr.srt transcripts/ar/webinar-ar.srt
```

### Output
Generated audio files are saved to:
```
audio/
├── es/
│   └── webinar-es.mp3
├── fr/
│   └── webinar-fr.mp3
└── ar/
    └── webinar-ar.mp3
```

## Advanced Usage

### Custom Voice Settings
```bash
# More expressive voice (lower stability)
python scripts/generate_voice.py transcripts/es/webinar-es.srt --stability 0.3 --style 0.3

# More stable voice (higher stability)
python scripts/generate_voice.py transcripts/fr/sample-fr.srt --stability 0.7 --similarity 0.85

# Professional/educational content
python scripts/generate_voice.py transcripts/ar/training-ar.srt --stability 0.6 --similarity 0.8 --style 0.0
```

### Custom Voice ID
```bash
# Use a specific voice from Eleven Labs library
python scripts/generate_voice.py transcripts/es/webinar-es.srt --voice-id "onwK4e9ZLuTAKqWW03F9"
```

### Specify Language Explicitly
```bash
# Override language detection
python scripts/generate_voice.py transcripts/custom.srt --lang es
```

### Different Output Directory
```bash
# Save to custom location
python scripts/generate_voice.py transcripts/es/webinar-es.srt --output-dir custom_audio/
```

### High-Quality Audio
```bash
# Use higher bitrate MP3
python scripts/generate_voice.py transcripts/es/webinar-es.srt --output-format mp3_44100_192
```

## Complete CLI Reference

```bash
python scripts/generate_voice.py --help
```

### Arguments
- `srt_files` - One or more SRT files to process (required)
- `--lang` - Target language code: es, fr, ar, en (optional, auto-detected)
- `--voice-id` - Custom voice ID (optional, uses defaults)
- `--output-dir` - Output directory (default: audio/)
- `--stability` - Voice stability 0.0-1.0 (default: 0.5)
- `--similarity` - Similarity boost 0.0-1.0 (default: 0.75)
- `--style` - Style exaggeration 0.0-1.0 (default: 0.0)
- `--no-speaker-boost` - Disable speaker boost
- `--output-format` - Audio format (default: mp3_44100_128)

## Voice Settings Guide

### Stability (0.0 - 1.0)
Controls consistency and expressiveness:
- **0.0-0.3**: Very expressive, varies between generations
- **0.4-0.6**: Balanced (recommended for most content)
- **0.7-1.0**: Very stable and consistent

**Recommendations**:
- Training videos: 0.5-0.6
- Marketing content: 0.3-0.5
- Technical docs: 0.6-0.7

### Similarity Boost (0.0 - 1.0)
Controls how close the voice stays to the original:
- **0.0-0.5**: More generic
- **0.6-0.8**: Balanced (recommended)
- **0.9-1.0**: Very close to original voice

**Recommendation**: Use 0.75-0.85 for best quality

### Style (0.0 - 1.0)
Controls style exaggeration (v2 model only):
- **0.0**: Natural, minimal exaggeration (recommended)
- **0.1-0.3**: Subtle emphasis
- **0.4-0.6**: Moderate style
- **0.7-1.0**: High exaggeration

**Recommendations**:
- Professional content: 0.0-0.1
- Storytelling: 0.2-0.4
- Dramatic content: 0.4-0.6

### Speaker Boost
Enhances clarity and similarity:
- **Enabled (default)**: Better clarity
- **Disabled**: Only if voice sounds unnatural

## Default Voices

The POC comes with default voice IDs for testing:

| Language | Voice Name | ID | Characteristics |
|----------|------------|-----|-----------------|
| Spanish (es) | Pablo | `onwK4e9ZLuTAKqWW03F9` | Male, natural, professional |
| French (fr) | Jessica | `cgSgspJ2msm6clMCkdW9` | Female, natural, professional |
| Arabic (ar) | Lily | `pFZP5JQG7iQjIQuC4Bku` | Female, natural, professional |
| English (en) | Sarah | `EXAVITQu4vr4xnSDxMaL` | Female, natural, professional |

**Note**: These are example IDs. For production use:
1. Browse Eleven Labs Voice Library: https://elevenlabs.io/voice-library
2. Test voices with your content
3. Configure your preferred voices via environment variables

## Cost Estimation

### Eleven Labs Pricing (Reference)
- **Starter**: $5/month = 30,000 characters
- **Creator**: $22/month = 100,000 characters
- **Pro**: $99/month = 500,000 characters
- **Scale**: $330/month = 2,000,000 characters

### Cost Per Video (Approximate)
- **5-minute video**: ~3,000-5,000 characters = $0.66-1.10 (Creator tier)
- **15-minute video**: ~9,000-15,000 characters = $1.98-3.30 (Creator tier)
- **30-minute video**: ~18,000-25,000 characters = $3.96-5.50 (Creator tier)

### The script automatically displays:
```
📊 VOICE GENERATION SUMMARY
Total characters processed: 12,450
💰 Estimated cost: $2.74 (based on Creator tier pricing)
```

## Example Workflows

### Workflow 1: Single Video, All Languages
```bash
# Translate SRT (if not already done)
python scripts/translate_srt.py transcripts/en/webinar-en.srt --languages es fr ar

# Generate voices for all translations
python scripts/generate_voice.py \
  transcripts/es/webinar-es.srt \
  transcripts/fr/webinar-fr.srt \
  transcripts/ar/webinar-ar.srt

# Output:
# audio/es/webinar-es.mp3
# audio/fr/webinar-fr.mp3
# audio/ar/webinar-ar.mp3
```

### Workflow 2: Batch Process Multiple Videos
```bash
# Generate for all Spanish translations
python scripts/generate_voice.py transcripts/es/*.srt

# Results saved to audio/es/
```

### Workflow 3: Custom Voice Per Language
```bash
# Set custom voices
export ELEVENLABS_VOICE_ES="your_preferred_spanish_voice"
export ELEVENLABS_VOICE_FR="your_preferred_french_voice"
export ELEVENLABS_VOICE_AR="your_preferred_arabic_voice"

# Generate with custom voices
python scripts/generate_voice.py transcripts/es/webinar-es.srt
```

### Workflow 4: Marketing vs Technical Content
```bash
# Marketing content (more expressive)
python scripts/generate_voice.py \
  transcripts/es/promo-es.srt \
  --stability 0.4 \
  --similarity 0.75 \
  --style 0.3

# Technical content (more stable)
python scripts/generate_voice.py \
  transcripts/es/docs-es.srt \
  --stability 0.7 \
  --similarity 0.8 \
  --style 0.0
```

## Integration with Existing Workflows

### Translation → Voice Pipeline
```bash
# Step 1: Translate subtitles
python scripts/translate_srt.py transcripts/en/video.srt --languages es fr ar

# Step 2: Generate voices
python scripts/generate_voice.py transcripts/{es,fr,ar}/video-*.srt

# Step 3: Review and deliver
ls -la audio/
```

### GitHub Actions Integration (Future)
The voice generation can be added to `.github/workflows/translate-srt.yml`:

```yaml
- name: Generate Voices (Optional)
  if: inputs.generate_voices == 'true'
  run: |
    python scripts/generate_voice.py transcripts/${{ matrix.lang }}/*.srt
  env:
    ELEVENLABS_API_KEY: ${{ secrets.ELEVENLABS_API_KEY }}
```

## Testing the POC

### Test with Sample Data
```bash
# Use existing translated samples
python scripts/generate_voice.py transcripts/es/webinar-es.srt --stability 0.6

# Check output
ls -la audio/es/
play audio/es/webinar-es.mp3  # or open in media player
```

### Quality Checks
After generation:
1. ✅ Listen to first 30 seconds
2. ✅ Verify audio duration matches content
3. ✅ Check pronunciation of technical terms
4. ✅ Confirm no audio artifacts
5. ✅ Get native speaker feedback

### Common Issues & Solutions

**Issue**: "ELEVENLABS_API_KEY environment variable not set"
```bash
# Solution: Set your API key
export ELEVENLABS_API_KEY="your_key"
```

**Issue**: Voice sounds robotic
```bash
# Solution: Decrease stability, increase style
python scripts/generate_voice.py file.srt --stability 0.3 --style 0.2
```

**Issue**: Inconsistent voice
```bash
# Solution: Increase stability
python scripts/generate_voice.py file.srt --stability 0.7 --style 0.0
```

**Issue**: Pronunciation errors
```bash
# Solution: Try different voice ID or edit source text
python scripts/generate_voice.py file.srt --voice-id "alternative_voice"
```

## Documentation Structure

The POC includes comprehensive documentation:

```
skills/voice-generation/
├── SKILL.md                              # Main skill documentation
└── references/
    ├── voice-styles.md                   # Voice style guide per language
    ├── pronunciation-guide.md            # Technical term pronunciation
    └── (audio-quality-standards.md)      # Future: Quality benchmarks
```

### Key Documents
- **SKILL.md**: Complete voice generation guidelines
- **voice-styles.md**: Voice selection and style recommendations
- **pronunciation-guide.md**: Technical term pronunciation for each language
- **VOICE_GENERATION_POC.md** (this file): POC setup and usage

## File Structure

```
kobo-translation-test/
├── scripts/
│   ├── generate_voice.py          # Main voice generation script
│   ├── translate_srt.py            # SRT translation (existing)
│   ├── srt_helper.py               # SRT utilities (existing)
│   └── requirements.txt            # Updated with elevenlabs
├── skills/
│   └── voice-generation/           # Voice generation skill (new)
│       ├── SKILL.md
│       └── references/
│           ├── voice-styles.md
│           └── pronunciation-guide.md
├── transcripts/                    # Translated SRT files (existing)
│   ├── en/, es/, fr/, ar/
│   └── ...
├── audio/                          # Generated audio (new)
│   ├── es/
│   ├── fr/
│   └── ar/
└── VOICE_GENERATION_POC.md         # This documentation
```

## Next Steps / Future Enhancements

### Phase 2 Enhancements
1. **GitHub Actions Integration**
   - Add voice generation step to `translate-srt.yml` workflow
   - Optional flag to enable/disable voice generation
   - Automatic artifact upload

2. **Voice Synchronization**
   - Generate individual audio clips per subtitle
   - Preserve exact timing from SRT
   - Create timed audio tracks

3. **Multi-Speaker Support**
   - Detect speaker changes in SRT
   - Use different voices per speaker
   - Maintain consistency per character

4. **Custom Pronunciation Dictionary**
   - Build KoboToolbox-specific term dictionary
   - Pre-process text with phonetic corrections
   - Improve technical term pronunciation

5. **Quality Metrics**
   - Automated pronunciation accuracy checks
   - Native speaker review workflow
   - A/B testing framework

6. **Cost Optimization**
   - Cache frequently used phrases
   - Reuse common segments across videos
   - Batch API calls more efficiently

### Configuration Improvements
1. Voice selection UI/tool
2. Voice comparison/preview before generation
3. Project-wide voice presets
4. Per-content-type voice configurations

## FAQ

### Q: How much does voice generation cost?
**A**: Depends on your Eleven Labs tier. Example: 15-minute video (~12,000 chars) = ~$2.64 on Creator tier.

### Q: Can I use my own voice?
**A**: Yes! Eleven Labs supports voice cloning (Pro+ tiers). Upload voice samples and use the custom voice ID.

### Q: What languages are supported?
**A**: This POC focuses on Spanish, French, and Arabic, but Eleven Labs v2 model supports 29 languages total.

### Q: How do I change the voice for a language?
**A**: Set environment variable: `export ELEVENLABS_VOICE_ES="your_voice_id"` or use `--voice-id` flag.

### Q: Can I generate audio for non-SRT content?
**A**: Currently, the script is designed for SRT files. For other formats, you can modify the script or convert to SRT first.

### Q: How long does generation take?
**A**: Approximately 1-2 seconds per 100 characters. A 15-minute video (~12,000 chars) takes 2-4 minutes.

### Q: Can I adjust speaking speed?
**A**: The API doesn't directly control speed. Use audio editing tools post-generation if needed.

### Q: What if pronunciation is wrong?
**A**: Try different voice IDs, adjust voice settings, or edit source text with phonetic hints.

### Q: Can I generate multiple voices for one video (e.g., dialog)?
**A**: Not in current POC. Future enhancement could support speaker-tagged SRT files.

### Q: Is this production-ready?
**A**: This is a POC. For production, consider adding error handling, retry logic, caching, and quality validation.

## Support & Contributions

### Getting Help
- Script help: `python scripts/generate_voice.py --help`
- Eleven Labs docs: https://docs.elevenlabs.io/
- Project issues: [GitHub issue tracker]

### Providing Feedback
- Test the POC with your content
- Document issues and pronunciation problems
- Suggest voice improvements
- Share successful voice configurations

### Contributing
- Improve error handling
- Add new features (see Next Steps)
- Expand documentation
- Create voice presets

## Credits

- **Eleven Labs**: Text-to-speech API provider
- **KoboToolbox**: Source content and translation system
- **Integration**: Built to complement existing translation workflow

## License

Same as main project.

---

**POC Status**: ✅ Complete and ready for testing

**Last Updated**: 2025-11-05

**Contact**: See main project README for contact information
