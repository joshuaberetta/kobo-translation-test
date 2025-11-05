#!/bin/bash
# Test script for voice generation POC
# This script validates the setup and provides example usage

set -e

echo "========================================="
echo "Voice Generation POC - Test Script"
echo "========================================="
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi
echo "✅ Python 3 is available"

# Check if generate_voice.py exists
if [ ! -f "scripts/generate_voice.py" ]; then
    echo "❌ generate_voice.py not found"
    exit 1
fi
echo "✅ generate_voice.py exists"

# Check if requirements.txt is updated
if grep -q "elevenlabs" scripts/requirements.txt; then
    echo "✅ elevenlabs added to requirements.txt"
else
    echo "❌ elevenlabs not in requirements.txt"
    exit 1
fi

# Check if skills directory exists
if [ -d "skills/voice-generation" ]; then
    echo "✅ Voice generation skill directory exists"
else
    echo "❌ Voice generation skill directory not found"
    exit 1
fi

# Check skill files
if [ -f "skills/voice-generation/SKILL.md" ]; then
    echo "✅ SKILL.md exists"
else
    echo "❌ SKILL.md not found"
fi

if [ -f "skills/voice-generation/references/voice-styles.md" ]; then
    echo "✅ voice-styles.md exists"
else
    echo "❌ voice-styles.md not found"
fi

if [ -f "skills/voice-generation/references/pronunciation-guide.md" ]; then
    echo "✅ pronunciation-guide.md exists"
else
    echo "❌ pronunciation-guide.md not found"
fi

# Check documentation
if [ -f "VOICE_GENERATION_POC.md" ]; then
    echo "✅ POC documentation exists"
else
    echo "❌ POC documentation not found"
fi

echo ""
echo "========================================="
echo "Setup Validation: PASSED"
echo "========================================="
echo ""

echo "📦 To install dependencies:"
echo "   cd scripts && pip install -r requirements.txt"
echo ""

echo "🔑 To set up API key:"
echo "   export ELEVENLABS_API_KEY='your_api_key_here'"
echo ""

echo "🎙️ Example usage:"
echo "   # Single file"
echo "   python scripts/generate_voice.py transcripts/es/webinar-es.srt"
echo ""
echo "   # Multiple files"
echo "   python scripts/generate_voice.py transcripts/es/*.srt"
echo ""
echo "   # With custom settings"
echo "   python scripts/generate_voice.py transcripts/es/webinar-es.srt --stability 0.6 --similarity 0.8"
echo ""

echo "📚 For complete documentation, see:"
echo "   VOICE_GENERATION_POC.md"
echo ""

echo "========================================="
echo "POC Status: Ready for Testing"
echo "========================================="
