#!/usr/bin/env python3
"""
Voice Generation Agent - Generate realistic AI voices from translated SRT files using Eleven Labs

Converts translated subtitle content into natural-sounding audio files for Spanish, French, and Arabic.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

try:
    from elevenlabs import ElevenLabs, VoiceSettings
    from srt_helper import SRTParser, SRTSubtitle
except ImportError:
    print("❌ Missing dependencies. Install with: pip install -r requirements.txt")
    sys.exit(1)


class VoiceGenerator:
    """
    Generates AI voices from translated SRT files using Eleven Labs API
    """

    # Default voice IDs for multilingual v2 model (high quality, natural voices)
    # These are example voice IDs - users should configure their preferred voices
    DEFAULT_VOICES = {
        'es': 'onwK4e9ZLuTAKqWW03F9',  # Spanish - Pablo (Male, natural)
        'fr': 'cgSgspJ2msm6clMCkdW9',  # French - Jessica (Female, natural)
        'ar': 'pFZP5JQG7iQjIQuC4Bku',  # Arabic - Lily (Female, natural)
        'en': 'EXAVITQu4vr4xnSDxMaL',  # English - Sarah (Female, natural)
    }

    # Voice model to use (multilingual-v2 supports 29 languages)
    DEFAULT_MODEL = "eleven_multilingual_v2"

    def __init__(self, api_key: str = None, output_dir: str = "audio"):
        """
        Initialize the Voice Generation agent

        Args:
            api_key: Eleven Labs API key (or uses ELEVENLABS_API_KEY env var)
            output_dir: Directory to save generated audio files (default: audio/)
        """
        self.api_key = api_key or os.getenv('ELEVENLABS_API_KEY')
        if not self.api_key:
            raise ValueError("ELEVENLABS_API_KEY environment variable not set")

        self.client = ElevenLabs(api_key=self.api_key)
        self.output_dir = Path(output_dir)

        # Track character usage for cost estimation
        self.total_characters = 0

    def _get_voice_id(self, lang: str, voice_id: str = None) -> str:
        """
        Get voice ID for a given language

        Args:
            lang: Language code (es, fr, ar, en)
            voice_id: Optional custom voice ID to override default

        Returns:
            Voice ID string
        """
        if voice_id:
            return voice_id

        # Check environment variable for custom voice
        env_voice = os.getenv(f'ELEVENLABS_VOICE_{lang.upper()}')
        if env_voice:
            return env_voice

        # Fall back to default
        if lang in self.DEFAULT_VOICES:
            return self.DEFAULT_VOICES[lang]

        raise ValueError(f"No voice configured for language: {lang}")

    def _extract_text_from_srt(self, srt_file: Path) -> Tuple[str, List[Dict]]:
        """
        Extract text content from SRT file

        Args:
            srt_file: Path to SRT file

        Returns:
            Tuple of (full_text, subtitles_data)
        """
        parser = SRTParser()
        subtitles = parser.parse_file(str(srt_file))

        # Extract all text while preserving timing info
        text_parts = []
        subtitle_data = []

        for sub in subtitles:
            text = sub.text.strip()
            if text:  # Skip empty subtitles
                text_parts.append(text)
                subtitle_data.append({
                    'index': sub.index,
                    'start': sub.start,
                    'end': sub.end,
                    'text': text
                })

        full_text = " ".join(text_parts)
        return full_text, subtitle_data

    def generate_audio(
        self,
        srt_file: Path,
        target_lang: str,
        voice_id: str = None,
        voice_settings: Dict = None,
        output_format: str = "mp3_44100_128"
    ) -> Path:
        """
        Generate audio from SRT file

        Args:
            srt_file: Path to translated SRT file
            target_lang: Target language code (es, fr, ar)
            voice_id: Optional custom voice ID
            voice_settings: Optional voice settings (stability, similarity_boost, style, use_speaker_boost)
            output_format: Audio format (mp3_44100_128, mp3_44100_192, pcm_16000, pcm_22050, pcm_24000, pcm_44100)

        Returns:
            Path to generated audio file
        """
        print(f"🎙️  Generating voice for: {srt_file.name}")
        print(f"   Language: {target_lang.upper()}", file=sys.stderr)

        # Extract text from SRT
        full_text, subtitle_data = self._extract_text_from_srt(srt_file)

        if not full_text:
            raise ValueError(f"No text content found in SRT file: {srt_file}")

        char_count = len(full_text)
        self.total_characters += char_count
        print(f"   Characters: {char_count:,}", file=sys.stderr)

        # Get voice ID
        voice = self._get_voice_id(target_lang, voice_id)
        print(f"   Voice ID: {voice}", file=sys.stderr)

        # Set up voice settings
        if voice_settings is None:
            voice_settings = {
                'stability': 0.5,           # 0-1: Lower = more expressive, Higher = more stable
                'similarity_boost': 0.75,   # 0-1: Higher = closer to original voice
                'style': 0.0,               # 0-1: Higher = more exaggerated style (v2 model only)
                'use_speaker_boost': True   # Boost clarity and similarity
            }

        settings = VoiceSettings(
            stability=voice_settings.get('stability', 0.5),
            similarity_boost=voice_settings.get('similarity_boost', 0.75),
            style=voice_settings.get('style', 0.0),
            use_speaker_boost=voice_settings.get('use_speaker_boost', True)
        )

        # Create output directory
        output_lang_dir = self.output_dir / target_lang
        output_lang_dir.mkdir(parents=True, exist_ok=True)

        # Generate output filename
        base_name = srt_file.stem.replace(f'-{target_lang}', '')
        output_file = output_lang_dir / f"{base_name}-{target_lang}.mp3"

        print(f"   📡 Calling Eleven Labs API...", file=sys.stderr)

        try:
            # Generate audio using Eleven Labs API
            audio_generator = self.client.text_to_speech.convert(
                voice_id=voice,
                text=full_text,
                model_id=self.DEFAULT_MODEL,
                voice_settings=settings,
                output_format=output_format
            )

            # Write audio to file
            print(f"   💾 Saving audio to: {output_file}", file=sys.stderr)
            with open(output_file, 'wb') as f:
                for chunk in audio_generator:
                    f.write(chunk)

            print(f"   ✅ Audio generated successfully!")
            print(f"   📁 Output: {output_file}")

            return output_file

        except Exception as e:
            print(f"   ❌ Error generating audio: {str(e)}", file=sys.stderr)
            raise

    def generate_batch(
        self,
        srt_files: List[Path],
        target_langs: List[str] = None,
        voice_ids: Dict[str, str] = None,
        voice_settings: Dict = None
    ) -> Dict[str, List[Path]]:
        """
        Generate audio for multiple SRT files and/or languages

        Args:
            srt_files: List of SRT file paths
            target_langs: List of target language codes (if None, infer from filenames)
            voice_ids: Optional dict of custom voice IDs per language
            voice_settings: Optional voice settings to apply to all

        Returns:
            Dictionary mapping language codes to list of generated audio files
        """
        results = {}
        voice_ids = voice_ids or {}

        print(f"\n🎵 Starting batch voice generation for {len(srt_files)} file(s)")
        print("=" * 70)

        for srt_file in srt_files:
            # Try to infer language from filename
            if target_langs is None:
                # Expect format: filename-{lang}.srt
                lang_suffix = srt_file.stem.split('-')[-1]
                if lang_suffix in ['es', 'fr', 'ar', 'en']:
                    langs_to_process = [lang_suffix]
                else:
                    print(f"⚠️  Cannot infer language from {srt_file.name}, skipping")
                    continue
            else:
                langs_to_process = target_langs

            for lang in langs_to_process:
                try:
                    voice_id = voice_ids.get(lang)
                    output_file = self.generate_audio(
                        srt_file=srt_file,
                        target_lang=lang,
                        voice_id=voice_id,
                        voice_settings=voice_settings
                    )

                    if lang not in results:
                        results[lang] = []
                    results[lang].append(output_file)

                except Exception as e:
                    print(f"❌ Failed to generate audio for {srt_file.name} ({lang}): {e}")
                    continue

        return results

    def print_usage_summary(self):
        """
        Print summary of character usage and estimated costs
        """
        print("\n" + "=" * 70)
        print("📊 VOICE GENERATION SUMMARY")
        print("=" * 70)
        print(f"Total characters processed: {self.total_characters:,}")

        # Eleven Labs pricing (as of 2024):
        # Starter: $5/month = 30,000 chars/month
        # Creator: $22/month = 100,000 chars/month
        # Pro: $99/month = 500,000 chars/month
        # Scale: $330/month = 2,000,000 chars/month
        # Business: Custom pricing

        # Approximate cost per character (using Creator tier as reference)
        cost_per_char = 22 / 100000  # $0.00022 per character
        estimated_cost = self.total_characters * cost_per_char

        print(f"💰 Estimated cost: ${estimated_cost:.4f} (based on Creator tier pricing)")
        print(f"   Note: Actual cost depends on your Eleven Labs subscription tier")
        print("=" * 70)


def main():
    """
    Command-line interface for voice generation
    """
    parser = argparse.ArgumentParser(
        description="Generate AI voices from translated SRT files using Eleven Labs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate voice for a single Spanish SRT file
  python generate_voice.py transcripts/es/webinar-es.srt

  # Generate voices for multiple files
  python generate_voice.py transcripts/es/*.srt

  # Generate with custom voice ID
  python generate_voice.py transcripts/es/webinar-es.srt --voice-id "your_voice_id"

  # Generate with custom voice settings
  python generate_voice.py transcripts/es/webinar-es.srt --stability 0.7 --similarity 0.8

  # Specify output directory
  python generate_voice.py transcripts/es/webinar-es.srt --output-dir custom_audio/

  # Generate for specific language (overrides filename inference)
  python generate_voice.py transcripts/es/webinar-es.srt --lang es

Environment Variables:
  ELEVENLABS_API_KEY        - Eleven Labs API key (required)
  ELEVENLABS_VOICE_ES       - Custom Spanish voice ID
  ELEVENLABS_VOICE_FR       - Custom French voice ID
  ELEVENLABS_VOICE_AR       - Custom Arabic voice ID
  ELEVENLABS_VOICE_EN       - Custom English voice ID

Voice Settings:
  --stability               - Voice stability (0.0-1.0, default: 0.5)
                              Lower = more expressive, Higher = more stable
  --similarity              - Similarity boost (0.0-1.0, default: 0.75)
                              Higher = closer to original voice
  --style                   - Style exaggeration (0.0-1.0, default: 0.0)
                              Higher = more exaggerated style (v2 model only)
  --speaker-boost           - Enable speaker boost for clarity (default: True)
        """
    )

    parser.add_argument(
        'srt_files',
        nargs='+',
        type=Path,
        help='SRT file(s) to generate voices for'
    )

    parser.add_argument(
        '--lang',
        type=str,
        choices=['es', 'fr', 'ar', 'en'],
        help='Target language code (if not inferring from filename)'
    )

    parser.add_argument(
        '--voice-id',
        type=str,
        help='Custom voice ID to use (overrides default for language)'
    )

    parser.add_argument(
        '--output-dir',
        type=str,
        default='audio',
        help='Output directory for audio files (default: audio/)'
    )

    parser.add_argument(
        '--stability',
        type=float,
        default=0.5,
        help='Voice stability 0.0-1.0 (default: 0.5)'
    )

    parser.add_argument(
        '--similarity',
        type=float,
        default=0.75,
        help='Similarity boost 0.0-1.0 (default: 0.75)'
    )

    parser.add_argument(
        '--style',
        type=float,
        default=0.0,
        help='Style exaggeration 0.0-1.0 (default: 0.0)'
    )

    parser.add_argument(
        '--no-speaker-boost',
        action='store_true',
        help='Disable speaker boost'
    )

    parser.add_argument(
        '--output-format',
        type=str,
        default='mp3_44100_128',
        choices=['mp3_44100_128', 'mp3_44100_192', 'pcm_16000', 'pcm_22050', 'pcm_24000', 'pcm_44100'],
        help='Audio output format (default: mp3_44100_128)'
    )

    args = parser.parse_args()

    # Validate SRT files exist
    for srt_file in args.srt_files:
        if not srt_file.exists():
            print(f"❌ SRT file not found: {srt_file}")
            sys.exit(1)

    # Initialize generator
    try:
        generator = VoiceGenerator(output_dir=args.output_dir)
    except ValueError as e:
        print(f"❌ {e}")
        print("   Set ELEVENLABS_API_KEY environment variable or pass via --api-key")
        sys.exit(1)

    # Prepare voice settings
    voice_settings = {
        'stability': args.stability,
        'similarity_boost': args.similarity,
        'style': args.style,
        'use_speaker_boost': not args.no_speaker_boost
    }

    # Prepare voice IDs if custom voice specified
    voice_ids = {}
    if args.voice_id:
        if args.lang:
            voice_ids[args.lang] = args.voice_id
        else:
            # Apply to all inferred languages
            voice_ids = {lang: args.voice_id for lang in ['es', 'fr', 'ar', 'en']}

    # Generate voices
    try:
        target_langs = [args.lang] if args.lang else None
        results = generator.generate_batch(
            srt_files=args.srt_files,
            target_langs=target_langs,
            voice_ids=voice_ids,
            voice_settings=voice_settings
        )

        # Print summary
        generator.print_usage_summary()

        print("\n✅ Voice generation completed successfully!")
        print(f"   Generated {sum(len(files) for files in results.values())} audio file(s)")

    except Exception as e:
        print(f"\n❌ Voice generation failed: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
