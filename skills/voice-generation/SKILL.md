# Voice Generation Skill

## Purpose
This skill provides guidelines and configurations for generating realistic AI voices from translated content using Eleven Labs API. It ensures consistent voice quality, appropriate voice selection, and optimal settings for Spanish, French, and Arabic content.

## Overview
The voice generation system converts translated text (from SRT files or other sources) into natural-sounding audio using Eleven Labs' multilingual v2 model. This model supports 29 languages with high-quality, expressive voices.

## Supported Languages

### Spanish (es)
- **Primary Use Case**: Latin American Spanish content
- **Recommended Voice**: Pablo (Male, natural tone)
- **Alternative Voices**:
  - Mateo (Male, warm)
  - Valentina (Female, professional)
  - Isabella (Female, energetic)
- **Voice Settings**:
  - Stability: 0.5-0.6 (balanced expressiveness)
  - Similarity: 0.75-0.85 (high quality)
  - Style: 0.0-0.2 (subtle emphasis)
  - Speaker Boost: Enabled

### French (fr)
- **Primary Use Case**: Standard French (France)
- **Recommended Voice**: Jessica (Female, natural)
- **Alternative Voices**:
  - Thomas (Male, professional)
  - Charlotte (Female, warm)
  - Antoine (Male, authoritative)
- **Voice Settings**:
  - Stability: 0.6-0.7 (more stable for formal content)
  - Similarity: 0.75-0.85 (high quality)
  - Style: 0.0 (minimal emphasis, professional)
  - Speaker Boost: Enabled

### Arabic (ar)
- **Primary Use Case**: Modern Standard Arabic (MSA)
- **Recommended Voice**: Lily (Female, natural)
- **Alternative Voices**:
  - Khalid (Male, authoritative)
  - Layla (Female, warm)
  - Omar (Male, professional)
- **Voice Settings**:
  - Stability: 0.5-0.6 (balanced)
  - Similarity: 0.75-0.85 (high quality)
  - Style: 0.0-0.1 (subtle)
  - Speaker Boost: Enabled

## Voice Settings Guide

### Stability (0.0 - 1.0)
- **0.0-0.3**: Very expressive, may vary more between generations
- **0.4-0.6**: Balanced (RECOMMENDED for most content)
- **0.7-1.0**: Very stable, consistent but less expressive

**Use Cases**:
- Training/Educational content: 0.5-0.6
- Marketing/Promotional: 0.3-0.5
- Technical documentation: 0.6-0.7

### Similarity Boost (0.0 - 1.0)
- **0.0-0.5**: Lower similarity, more generic
- **0.6-0.8**: Balanced (RECOMMENDED)
- **0.9-1.0**: High similarity, very close to original voice

**Recommendation**: Use 0.75-0.85 for best quality

### Style (0.0 - 1.0) - Multilingual v2 Model Only
- **0.0**: Natural, minimal style exaggeration (RECOMMENDED)
- **0.1-0.3**: Subtle emphasis
- **0.4-0.6**: Moderate style
- **0.7-1.0**: High exaggeration (use sparingly)

**Use Cases**:
- Professional content: 0.0-0.1
- Storytelling: 0.2-0.4
- Dramatic content: 0.4-0.6

### Speaker Boost
- **Enabled (Default)**: Enhances clarity and similarity
- **Disabled**: Use only if voice sounds unnatural

**Recommendation**: Keep enabled for all content types

## Content-Specific Guidelines

### Subtitle/Video Content
- **Chunk Size**: Process full subtitle text (script handles this)
- **Pacing**: Natural speech rate is automatically applied
- **Punctuation**: Preserve all punctuation for proper pausing
- **Special Characters**: Remove SRT formatting tags before generation

### Educational/Training Content
- **Voice Settings**:
  - Stability: 0.5-0.6
  - Similarity: 0.75-0.8
  - Style: 0.0-0.1
- **Tone**: Professional, clear, approachable
- **Pacing**: Moderate speed for comprehension

### Marketing/Promotional Content
- **Voice Settings**:
  - Stability: 0.3-0.5
  - Similarity: 0.75-0.8
  - Style: 0.2-0.4
- **Tone**: Energetic, engaging, persuasive
- **Pacing**: Dynamic, with natural emphasis

### Technical Documentation
- **Voice Settings**:
  - Stability: 0.6-0.7
  - Similarity: 0.75-0.85
  - Style: 0.0
- **Tone**: Clear, professional, authoritative
- **Pacing**: Steady, allowing time for complex terms

## Quality Assurance

### Pre-Generation Checks
1. ✅ Validate source text has no formatting artifacts
2. ✅ Verify language code matches content language
3. ✅ Confirm voice ID is appropriate for content type
4. ✅ Check character count for cost estimation

### Post-Generation Checks
1. ✅ Listen to first 30 seconds for quality
2. ✅ Verify audio duration roughly matches text length
3. ✅ Check for pronunciation issues on technical terms
4. ✅ Confirm no audio artifacts or glitches

### Common Issues & Solutions

**Issue**: Voice sounds robotic
- **Solution**: Decrease stability (0.3-0.5), increase style (0.1-0.3)

**Issue**: Inconsistent voice between chunks
- **Solution**: Increase stability (0.6-0.7), decrease style (0.0-0.1)

**Issue**: Pronunciation errors on technical terms
- **Solution**: Add phonetic spelling in text, or use custom dictionary

**Issue**: Audio too fast/slow
- **Solution**: Adjust text spacing, add punctuation for pacing

## Cost Optimization

### Eleven Labs Pricing Tiers (Reference)
- **Starter**: $5/month = 30,000 chars
- **Creator**: $22/month = 100,000 chars
- **Pro**: $99/month = 500,000 chars
- **Scale**: $330/month = 2,000,000 chars

### Cost Estimation
- **Average video subtitle**: 5,000-15,000 characters
- **Estimated cost per video** (Creator tier): $1.10-3.30
- **Optimization**: Batch process multiple files to maximize API efficiency

### Best Practices
1. ✅ Remove empty subtitles before processing
2. ✅ Combine short subtitle chunks where appropriate
3. ✅ Use the same voice settings for consistency (reduces testing costs)
4. ✅ Process all languages in one batch

## Integration with Translation Workflow

### Recommended Workflow
```
1. Translate content (translate_srt.py)
   ↓
2. Review translation quality
   ↓
3. Generate voices (generate_voice.py)
   ↓
4. Quality check audio
   ↓
5. Deliver final audio files
```

### Automation Considerations
- Voice generation can be added as optional step in translation workflows
- Consider user opt-in for voice generation (additional cost)
- Store generated audio in `audio/{lang}/` directory structure

## Environment Configuration

### Required Environment Variables
```bash
ELEVENLABS_API_KEY          # Your Eleven Labs API key (required)
```

### Optional Environment Variables
```bash
ELEVENLABS_VOICE_ES         # Custom Spanish voice ID
ELEVENLABS_VOICE_FR         # Custom French voice ID
ELEVENLABS_VOICE_AR         # Custom Arabic voice ID
ELEVENLABS_VOICE_EN         # Custom English voice ID
```

## Voice Selection Guide

### Finding the Right Voice
1. Visit Eleven Labs Voice Library
2. Filter by language
3. Listen to samples
4. Consider:
   - Gender (male/female)
   - Age range (young/mature)
   - Tone (warm/professional/energetic)
   - Accent (regional variations)

### Custom Voices
- Users can clone their own voices
- Requires voice samples (minimum 1 minute)
- Professional Voice Cloning available in Pro+ tiers
- Use voice_id parameter to specify custom voices

## Technical Specifications

### Supported Output Formats
- **MP3**:
  - 44.1kHz @ 128kbps (default, balanced)
  - 44.1kHz @ 192kbps (higher quality)
- **PCM**:
  - 16kHz (telephony)
  - 22.05kHz (standard)
  - 24kHz (high quality)
  - 44.1kHz (CD quality)

### API Model
- **Model ID**: `eleven_multilingual_v2`
- **Languages Supported**: 29 languages
- **Features**:
  - Multilingual voice consistency
  - Advanced emotional range
  - Natural pronunciation
  - Context awareness

## References
- See `references/voice-styles.md` for detailed voice style examples
- See `references/pronunciation-guide.md` for technical term pronunciation
- See `references/audio-quality-standards.md` for quality benchmarks

## Support & Troubleshooting

### Common Questions

**Q: Can I use multiple voices in one video?**
A: Yes, but requires splitting the SRT file by speaker first

**Q: How long does generation take?**
A: Approximately 1-2 seconds per 100 characters

**Q: Can I adjust speed/pitch?**
A: Not directly via API, use audio editing tools post-generation

**Q: What if a voice sounds wrong for my content?**
A: Try different voice IDs or adjust voice settings (stability/style)

### Getting Help
- Eleven Labs Documentation: https://docs.elevenlabs.io/
- Voice Generation Script: `scripts/generate_voice.py --help`
- Report issues: Add to project issue tracker
