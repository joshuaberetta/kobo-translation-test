# Voice Styles Reference

## Overview
This document provides detailed examples and use cases for different voice styles across Spanish, French, and Arabic content.

## Spanish (es) Voice Styles

### Professional/Educational - Pablo
**Voice ID**: `onwK4e9ZLuTAKqWW03F9`
- **Characteristics**: Clear, authoritative, trustworthy
- **Best For**:
  - Training videos
  - Product demonstrations
  - Technical documentation
  - Corporate communications
- **Settings**:
  ```
  stability: 0.6
  similarity_boost: 0.8
  style: 0.0
  speaker_boost: true
  ```

### Warm/Friendly - Valentina
**Voice ID**: Example ID (configure per user)
- **Characteristics**: Approachable, conversational, empathetic
- **Best For**:
  - Customer onboarding
  - User guides
  - Community content
  - Help documentation
- **Settings**:
  ```
  stability: 0.5
  similarity_boost: 0.75
  style: 0.2
  speaker_boost: true
  ```

### Energetic/Marketing - Isabella
**Voice ID**: Example ID (configure per user)
- **Characteristics**: Dynamic, engaging, enthusiastic
- **Best For**:
  - Product launches
  - Feature announcements
  - Marketing videos
  - Event promotions
- **Settings**:
  ```
  stability: 0.4
  similarity_boost: 0.75
  style: 0.3
  speaker_boost: true
  ```

## French (fr) Voice Styles

### Professional/Formal - Jessica
**Voice ID**: `cgSgspJ2msm6clMCkdW9`
- **Characteristics**: Polished, sophisticated, professional
- **Best For**:
  - Business presentations
  - Professional training
  - Official communications
  - Technical content
- **Settings**:
  ```
  stability: 0.7
  similarity_boost: 0.8
  style: 0.0
  speaker_boost: true
  ```
- **Note**: French typically uses formal "vous" form, matches formal voice tone

### Conversational - Charlotte
**Voice ID**: Example ID (configure per user)
- **Characteristics**: Friendly, clear, approachable
- **Best For**:
  - User onboarding
  - Tutorial videos
  - FAQ content
  - Support materials
- **Settings**:
  ```
  stability: 0.5
  similarity_boost: 0.75
  style: 0.1
  speaker_boost: true
  ```

### Authoritative - Thomas
**Voice ID**: Example ID (configure per user)
- **Characteristics**: Commanding, confident, clear
- **Best For**:
  - Executive communications
  - Policy announcements
  - Important updates
  - Compliance training
- **Settings**:
  ```
  stability: 0.6
  similarity_boost: 0.8
  style: 0.0
  speaker_boost: true
  ```

## Arabic (ar) Voice Styles

### Professional/Standard - Lily
**Voice ID**: `pFZP5JQG7iQjIQuC4Bku`
- **Characteristics**: Clear, professional, neutral
- **Best For**:
  - Technical documentation
  - Training materials
  - Business content
  - Educational videos
- **Settings**:
  ```
  stability: 0.6
  similarity_boost: 0.8
  style: 0.0
  speaker_boost: true
  ```
- **Note**: Uses Modern Standard Arabic (MSA) pronunciation

### Warm/Engaging - Layla
**Voice ID**: Example ID (configure per user)
- **Characteristics**: Warm, friendly, engaging
- **Best For**:
  - User guides
  - Community content
  - Onboarding materials
  - Help documentation
- **Settings**:
  ```
  stability: 0.5
  similarity_boost: 0.75
  style: 0.1
  speaker_boost: true
  ```

### Authoritative - Khalid
**Voice ID**: Example ID (configure per user)
- **Characteristics**: Strong, confident, professional
- **Best For**:
  - Corporate communications
  - Official announcements
  - Leadership messages
  - Policy content
- **Settings**:
  ```
  stability: 0.6
  similarity_boost: 0.8
  style: 0.0
  speaker_boost: true
  ```

## Content-Type Recommendations

### Training & Educational Videos
**Goal**: Clear instruction, easy to follow, professional

**Spanish**:
- Voice: Pablo (Professional)
- Settings: stability=0.6, similarity=0.8, style=0.0

**French**:
- Voice: Jessica (Professional)
- Settings: stability=0.7, similarity=0.8, style=0.0

**Arabic**:
- Voice: Lily (Professional)
- Settings: stability=0.6, similarity=0.8, style=0.0

### Product Demonstrations
**Goal**: Engaging, clear, helpful

**Spanish**:
- Voice: Valentina (Warm)
- Settings: stability=0.5, similarity=0.75, style=0.2

**French**:
- Voice: Charlotte (Conversational)
- Settings: stability=0.5, similarity=0.75, style=0.1

**Arabic**:
- Voice: Layla (Warm)
- Settings: stability=0.5, similarity=0.75, style=0.1

### Technical Documentation
**Goal**: Precise, professional, authoritative

**Spanish**:
- Voice: Pablo (Professional)
- Settings: stability=0.7, similarity=0.8, style=0.0

**French**:
- Voice: Thomas (Authoritative)
- Settings: stability=0.6, similarity=0.8, style=0.0

**Arabic**:
- Voice: Khalid (Authoritative)
- Settings: stability=0.6, similarity=0.8, style=0.0

### Marketing & Promotional
**Goal**: Energetic, engaging, persuasive

**Spanish**:
- Voice: Isabella (Energetic)
- Settings: stability=0.4, similarity=0.75, style=0.3

**French**:
- Voice: Charlotte (Conversational) with higher style
- Settings: stability=0.4, similarity=0.75, style=0.2

**Arabic**:
- Voice: Layla (Warm) with moderate style
- Settings: stability=0.4, similarity=0.75, style=0.2

### Customer Support & Help
**Goal**: Friendly, patient, clear

**Spanish**:
- Voice: Valentina (Warm)
- Settings: stability=0.5, similarity=0.75, style=0.1

**French**:
- Voice: Charlotte (Conversational)
- Settings: stability=0.5, similarity=0.75, style=0.1

**Arabic**:
- Voice: Layla (Warm)
- Settings: stability=0.5, similarity=0.75, style=0.1

## Testing Voice Styles

### Quick Test Script
```bash
# Test Spanish voice
python scripts/generate_voice.py transcripts/es/sample-es.srt --stability 0.6 --similarity 0.8

# Test French voice
python scripts/generate_voice.py transcripts/fr/sample-fr.srt --stability 0.7 --similarity 0.8

# Test Arabic voice
python scripts/generate_voice.py transcripts/ar/sample-ar.srt --stability 0.6 --similarity 0.8
```

### A/B Testing Approach
1. Generate same content with 2-3 different voice settings
2. Listen to first minute of each version
3. Gather feedback from native speakers
4. Document preferred settings for content type
5. Apply consistently across project

## Voice Consistency Guidelines

### Within a Series
- ✅ Use same voice ID across all videos in a series
- ✅ Use same voice settings for consistency
- ✅ Maintain same stability level
- ✅ Keep speaker boost setting consistent

### Across Languages
- ✅ Choose similar voice "personalities" (all professional or all warm)
- ✅ Use similar stability settings (±0.1)
- ✅ Match formality levels
- ❌ Don't drastically change tone between languages

### Brand Voice Alignment
- Match voice style to brand personality
- Consider target audience preferences
- Maintain consistency with written tone
- Get stakeholder approval on voice selection

## Regional Variations

### Spanish
- **Latin American Spanish**: Use neutral accent voices (Pablo, Valentina)
- **European Spanish**: Select Spain-specific voices if needed
- **Regional Terms**: Ensure translation matches voice accent

### French
- **France French**: Standard voices (Jessica, Thomas)
- **Canadian French**: Select Quebec-specific voices if needed
- **African French**: Consider dialect-appropriate voices

### Arabic
- **Modern Standard Arabic (MSA)**: Default for formal content (Lily, Khalid)
- **Egyptian Arabic**: Select regional voice if needed
- **Gulf Arabic**: Use if targeting Gulf region
- **Levantine Arabic**: Consider for Syrian/Lebanese content

## Advanced Voice Selection

### Finding Custom Voices

1. **Browse Eleven Labs Voice Library**:
   - Filter by language
   - Filter by gender
   - Listen to all samples
   - Note voice IDs you like

2. **Test with Your Content**:
   - Generate 30-second sample
   - Listen for:
     - Natural pronunciation
     - Appropriate pacing
     - Emotional tone fit
     - Technical term clarity

3. **Voice Cloning (Pro+)**:
   - Clone your own voice or brand voice
   - Requires 1+ minute of clean audio samples
   - Maintains brand consistency
   - Higher cost but unique identity

### Voice Selection Checklist
- [ ] Language matches content
- [ ] Gender appropriate for brand
- [ ] Age range fits target audience
- [ ] Tone matches content type
- [ ] Accent is neutral/appropriate
- [ ] Pronunciation of key terms is clear
- [ ] Voice sounds natural, not robotic
- [ ] Native speaker approved (if possible)

## Troubleshooting Voice Issues

### Problem: Voice sounds too monotone
**Solutions**:
- Decrease stability to 0.3-0.5
- Increase style to 0.2-0.4
- Try a different voice ID
- Add more expressive punctuation in text

### Problem: Voice is inconsistent
**Solutions**:
- Increase stability to 0.6-0.8
- Decrease style to 0.0-0.1
- Ensure consistent text formatting
- Use speaker boost

### Problem: Pronunciation errors
**Solutions**:
- Add phonetic spellings in text
- Try different voice ID
- Use custom pronunciation dictionary (Pro feature)
- Break up complex technical terms

### Problem: Voice doesn't match brand
**Solutions**:
- Test multiple voices from library
- Consider voice cloning
- Adjust voice settings
- Get stakeholder feedback early

## Resources

### Eleven Labs Voice Library
- Browse all available voices: https://elevenlabs.io/voice-library
- Filter by language and characteristics
- Download voice IDs for your favorites

### Voice Testing Tools
- Eleven Labs Speech Synthesis: Test voices directly in platform
- Compare voices side-by-side
- Save custom presets

### Community Resources
- Eleven Labs Discord: Share tips and get recommendations
- Reddit r/ElevenLabs: User experiences and best practices
- Project team: Document successful voice selections for reuse
