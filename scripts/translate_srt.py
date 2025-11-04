#!/usr/bin/env python3
"""
SRT Translation Agent - Translate subtitle files using chunked context-aware approach
Minimizes hallucinations by processing appropriately-sized chunks with overlap
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Tuple
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

try:
    import anthropic
    from srt_helper import SRTParser, SRTSubtitle, SRTWriter, SRTConverter
except ImportError:
    print("❌ Missing dependencies. Install with: pip install -r requirements.txt")
    sys.exit(1)


class SRTTranslationAgent:
    """
    Translates SRT subtitle files using chunked, context-aware approach
    to minimize hallucinations while preserving overall coherence
    """
    
    # Optimal chunk sizes to balance context and hallucination risk
    # Based on testing: 20-30 subtitles per chunk works well for most content
    DEFAULT_CHUNK_SIZE = 25
    DEFAULT_OVERLAP = 3  # Number of subtitles to overlap between chunks for context
    
    def __init__(self, api_key: str = None, chunk_size: int = None, overlap: int = None):
        """
        Initialize the SRT translation agent
        
        Args:
            api_key: Anthropic API key (or uses ANTHROPIC_API_KEY env var)
            chunk_size: Number of subtitles per chunk (default: 25)
            overlap: Number of overlapping subtitles for context (default: 3)
        """
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")
        
        self.claude = anthropic.Anthropic(api_key=self.api_key)
        
        self.chunk_size = chunk_size or self.DEFAULT_CHUNK_SIZE
        self.overlap = overlap or self.DEFAULT_OVERLAP
        
        # Skill context cache
        self.skill_cache = {}
        
        # Track token usage
        self.total_input_tokens = 0
        self.total_output_tokens = 0
    
    def _load_skill_context(self, target_lang: str) -> Dict[str, str]:
        """
        Load translation skill context for subtitle translation
        
        Args:
            target_lang: Target language code (es, fr, ar)
        
        Returns:
            Dictionary containing skill content
        """
        if target_lang in self.skill_cache:
            return self.skill_cache[target_lang]
        
        print(f"📚 Loading kobo-translation-srt skill for {target_lang.upper()}...", file=sys.stderr)
        
        # Try SRT-specific skill first
        srt_skill_base = Path(f'skills/kobo-translation-srt-{target_lang}')
        if not srt_skill_base.exists():
            srt_skill_base = Path('skills/kobo-translation-srt')
        
        # Fall back to main skill if SRT skill doesn't exist
        if not srt_skill_base.exists():
            print(f"  ⚠️  SRT-specific skill not found, using main translation skill", file=sys.stderr)
            srt_skill_base = Path(f'skills/kobo-translation-{target_lang}')
            if not srt_skill_base.exists():
                srt_skill_base = Path('skills/kobo-translation')
        
        if not srt_skill_base.exists():
            raise FileNotFoundError(
                f"Translation skill not found. Tried:\n"
                f"  - skills/kobo-translation-srt-{target_lang}\n"
                f"  - skills/kobo-translation-srt\n"
                f"  - skills/kobo-translation-{target_lang}\n"
                f"  - skills/kobo-translation"
            )
        
        context = {}
        
        # Read main skill file
        main_skill = srt_skill_base / 'SKILL.md'
        if main_skill.exists():
            context['main'] = main_skill.read_text(encoding='utf-8')
        else:
            raise FileNotFoundError(f"SKILL.md not found in {srt_skill_base}")
        
        # Read reference files if they exist
        refs_dir = srt_skill_base / 'references'
        if refs_dir.exists():
            ref_files = [
                'brand-terminology.md',
                'ui-terminology.md',
                'subtitle-guidelines.md',  # SRT-specific
            ]
            
            for filename in ref_files:
                file_path = refs_dir / filename
                if file_path.exists():
                    key = filename.replace('.md', '').replace('-', '_')
                    context[key] = file_path.read_text(encoding='utf-8')
        
        self.skill_cache[target_lang] = context
        print(f"✅ Skill loaded successfully ({len(context)} files)", file=sys.stderr)
        
        return context
    
    def chunk_subtitles(self, subtitles: List[SRTSubtitle]) -> List[Dict]:
        """
        Split subtitles into overlapping chunks for translation
        
        Args:
            subtitles: List of SRTSubtitle objects
        
        Returns:
            List of chunk dictionaries with 'subtitles', 'start_index', 'end_index'
        """
        chunks = []
        
        i = 0
        while i < len(subtitles):
            chunk_end = min(i + self.chunk_size, len(subtitles))
            
            chunk = {
                'chunk_number': len(chunks) + 1,
                'start_index': i,
                'end_index': chunk_end,
                'subtitles': subtitles[i:chunk_end],
                # Previous context (for continuity)
                'prev_context': subtitles[max(0, i - self.overlap):i] if i > 0 else [],
                # Next context (for better understanding)
                'next_context': subtitles[chunk_end:min(chunk_end + self.overlap, len(subtitles))] if chunk_end < len(subtitles) else []
            }
            
            chunks.append(chunk)
            
            # Move to next chunk, accounting for overlap to avoid context loss
            i = chunk_end
        
        return chunks
    
    def translate_chunk(self, chunk: Dict, target_lang: str, 
                       total_chunks: int, video_title: str = None) -> List[SRTSubtitle]:
        """
        Translate a single chunk of subtitles
        
        Args:
            chunk: Chunk dictionary with subtitles and context
            target_lang: Target language code
            total_chunks: Total number of chunks (for context)
            video_title: Optional video title for better context
        
        Returns:
            List of translated SRTSubtitle objects
        """
        skill_context = self._load_skill_context(target_lang)
        
        # Build context information
        context_info = []
        if video_title:
            context_info.append(f"Video title: {video_title}")
        
        context_info.append(
            f"This is chunk {chunk['chunk_number']} of {total_chunks} "
            f"(subtitles {chunk['start_index'] + 1}-{chunk['end_index']})"
        )
        
        # Format previous context
        prev_context_str = ""
        if chunk['prev_context']:
            prev_lines = []
            for sub in chunk['prev_context']:
                prev_lines.append(f"[{sub.index}] {sub.text}")
            prev_context_str = f"""
PREVIOUS CONTEXT (already translated, for continuity):
{chr(10).join(prev_lines)}
"""
        
        # Format next context
        next_context_str = ""
        if chunk['next_context']:
            next_lines = []
            for sub in chunk['next_context']:
                next_lines.append(f"[{sub.index}] {sub.text}")
            next_context_str = f"""
UPCOMING CONTEXT (will be translated next, for flow):
{chr(10).join(next_lines)}
"""
        
        # Format subtitles to translate
        subtitle_lines = []
        for sub in chunk['subtitles']:
            subtitle_lines.append(
                f"[{sub.index}] {sub.start_time} --> {sub.end_time}\n{sub.text}"
            )
        
        subtitles_str = '\n\n'.join(subtitle_lines)
        
        # Build comprehensive prompt
        prompt = f"""{skill_context.get('main', '')}

TARGET LANGUAGE: {target_lang.upper()}

## SUBTITLE TRANSLATION GUIDELINES

You are translating VIDEO SUBTITLES for a KoboToolbox tutorial.

CRITICAL RULES:
1. **Preserve subtitle structure**: Each subtitle must have same [index] and timestamps
2. **Concise translation**: Subtitles must be readable on screen (aim for similar length)
3. **Natural spoken language**: Translate as if speaking, not writing
4. **Context awareness**: Consider previous and upcoming subtitles for flow
5. **Character limits**: Keep lines under 42 characters when possible for readability
6. **Technical terms**: Follow brand terminology exactly (see skill above)
7. **NO explanations**: Output ONLY the translated subtitles in exact same format

CHARACTER LIMIT GUIDELINES:
- Ideal: 35-42 characters per line
- Maximum: 50 characters per line
- Break long sentences into multiple subtitle entries if needed

{chr(10).join(context_info)}

{prev_context_str}

---BEGIN SUBTITLES TO TRANSLATE---
{subtitles_str}
---END SUBTITLES TO TRANSLATE---

{next_context_str}

Now translate ONLY the subtitles between the BEGIN/END markers.
Output format (EXACTLY like this):

[index] HH:MM:SS,mmm --> HH:MM:SS,mmm
Translated text here

[next_index] HH:MM:SS,mmm --> HH:MM:SS,mmm
Translated text here

Translation:"""

        print(f"  🤖 Translating chunk {chunk['chunk_number']}/{total_chunks} "
              f"({len(chunk['subtitles'])} subtitles)...", file=sys.stderr)
        
        try:
            response = self.claude.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=8000,
                temperature=0.3,
                system="""You are a precise subtitle translator. You MUST:
1. Preserve all subtitle numbers and timestamps EXACTLY
2. Translate text naturally for spoken language
3. Keep translations concise for on-screen readability
4. Output ONLY the translated subtitles with NO additional text
5. Maintain the exact format: [index] timestamp --> timestamp\\ntext""",
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            # Extract translation
            translation = ""
            for block in response.content:
                if block.type == "text":
                    translation += block.text
            
            # Track usage
            usage = response.usage
            self.total_input_tokens += usage.input_tokens
            self.total_output_tokens += usage.output_tokens
            
            print(f"    ✓ Tokens: {usage.input_tokens} in, {usage.output_tokens} out", file=sys.stderr)
            
            # Parse translated subtitles
            translated_subs = self._parse_translated_chunk(translation, chunk['subtitles'])
            
            return translated_subs
            
        except Exception as e:
            print(f"  ❌ Translation failed for chunk {chunk['chunk_number']}: {e}", file=sys.stderr)
            raise
    
    def _parse_translated_chunk(self, translation: str, original_subs: List[SRTSubtitle]) -> List[SRTSubtitle]:
        """
        Parse translated chunk back into SRTSubtitle objects
        
        Args:
            translation: Translated text from Claude
            original_subs: Original subtitles (for timestamps/index validation)
        
        Returns:
            List of translated SRTSubtitle objects
        """
        translated_subs = []
        
        # Pattern to match: [index] timestamp --> timestamp\ntext
        import re
        pattern = r'\[(\d+)\]\s*(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})\s*\n((?:(?!\[\d+\]).)*)'
        
        matches = re.finditer(pattern, translation, re.DOTALL)
        
        for match in matches:
            index = int(match.group(1))
            start_time = match.group(2)
            end_time = match.group(3)
            text = match.group(4).strip()
            
            translated_sub = SRTSubtitle(index, start_time, end_time, text)
            translated_subs.append(translated_sub)
        
        # Validation: check we got all subtitles
        if len(translated_subs) != len(original_subs):
            print(f"  ⚠️  Warning: Expected {len(original_subs)} subtitles, got {len(translated_subs)}", 
                  file=sys.stderr)
            
            # Try to map what we have
            if len(translated_subs) == 0:
                # Fallback: try simpler parsing
                print(f"  🔄 Attempting fallback parsing...", file=sys.stderr)
                translated_subs = self._fallback_parse(translation, original_subs)
        
        return translated_subs
    
    def _fallback_parse(self, translation: str, original_subs: List[SRTSubtitle]) -> List[SRTSubtitle]:
        """
        Fallback parser if primary parsing fails
        
        Attempts to extract just the translated text and map to original subtitles
        """
        # Split by double newlines
        blocks = [b.strip() for b in translation.split('\n\n') if b.strip()]
        
        translated_subs = []
        
        for i, original in enumerate(original_subs):
            if i < len(blocks):
                # Try to extract text from block
                lines = blocks[i].split('\n')
                # Skip timestamp lines, take remaining as text
                text_lines = [l for l in lines if '-->' not in l and not re.match(r'^\[\d+\]', l)]
                text = '\n'.join(text_lines).strip()
                
                if text:
                    translated_sub = SRTSubtitle(
                        original.index,
                        original.start_time,
                        original.end_time,
                        text
                    )
                    translated_subs.append(translated_sub)
            else:
                # No translation found, keep original
                print(f"  ⚠️  No translation for subtitle {original.index}, keeping original", 
                      file=sys.stderr)
                translated_subs.append(original)
        
        return translated_subs
    
    def translate_file(self, source_path: str, target_lang: str, 
                      output_path: str = None, video_title: str = None) -> str:
        """
        Translate a complete SRT file
        
        Args:
            source_path: Path to source SRT file
            target_lang: Target language code (es, fr, ar)
            output_path: Optional output path (default: auto-generate)
            video_title: Optional video title for context
        
        Returns:
            Path to translated SRT file
        """
        print(f"\n🎬 SRT Translation Agent", file=sys.stderr)
        print(f"=" * 60, file=sys.stderr)
        print(f"📄 Source: {source_path}", file=sys.stderr)
        print(f"🌐 Target: {target_lang.upper()}", file=sys.stderr)
        print(f"📦 Chunk size: {self.chunk_size} subtitles", file=sys.stderr)
        print(f"🔄 Overlap: {self.overlap} subtitles", file=sys.stderr)
        print(f"=" * 60, file=sys.stderr)
        
        # Parse source file
        print(f"\n📖 Parsing source SRT file...", file=sys.stderr)
        subtitles = SRTParser.parse_file(source_path)
        print(f"✅ Found {len(subtitles)} subtitles", file=sys.stderr)
        
        # Calculate total duration
        if subtitles:
            last_sub = subtitles[-1]
            duration_ms = SRTSubtitle._timestamp_to_ms(last_sub.end_time)
            duration_min = duration_ms / 1000 / 60
            print(f"⏱️  Total duration: {duration_min:.1f} minutes", file=sys.stderr)
        
        # Chunk subtitles
        print(f"\n✂️  Creating chunks...", file=sys.stderr)
        chunks = self.chunk_subtitles(subtitles)
        print(f"✅ Created {len(chunks)} chunks", file=sys.stderr)
        
        # Translate each chunk
        print(f"\n🔄 Translating chunks...", file=sys.stderr)
        all_translated = []
        
        for chunk in chunks:
            translated_chunk = self.translate_chunk(
                chunk, 
                target_lang, 
                len(chunks),
                video_title
            )
            all_translated.extend(translated_chunk)
        
        print(f"\n✅ Translation complete! Translated {len(all_translated)} subtitles", file=sys.stderr)
        
        # Generate output path if not provided
        if not output_path:
            source_file = Path(source_path)
            output_path = source_file.parent / f"{source_file.stem}_{target_lang}{source_file.suffix}"
        
        # Write output
        print(f"\n💾 Writing translated SRT file...", file=sys.stderr)
        SRTWriter.write_file(all_translated, output_path)
        print(f"✅ Saved to: {output_path}", file=sys.stderr)
        
        # Report statistics
        self._print_statistics()
        
        return output_path
    
    def _print_statistics(self):
        """Print translation statistics and cost estimate"""
        print(f"\n📊 Translation Statistics", file=sys.stderr)
        print(f"=" * 60, file=sys.stderr)
        print(f"Total input tokens: {self.total_input_tokens:,}", file=sys.stderr)
        print(f"Total output tokens: {self.total_output_tokens:,}", file=sys.stderr)
        
        # Cost calculation (Claude Sonnet 4 pricing)
        input_cost = self.total_input_tokens / 1_000_000 * 3.00
        output_cost = self.total_output_tokens / 1_000_000 * 15.00
        total_cost = input_cost + output_cost
        
        print(f"💰 Estimated cost: ${total_cost:.4f}", file=sys.stderr)
        print(f"   (Input: ${input_cost:.4f}, Output: ${output_cost:.4f})", file=sys.stderr)
        print(f"=" * 60, file=sys.stderr)


def main():
    """Command-line interface"""
    parser = argparse.ArgumentParser(
        description='SRT Translation Agent - Translate subtitle files with context awareness'
    )
    
    parser.add_argument(
        'source',
        help='Source SRT file to translate'
    )
    parser.add_argument(
        '--language', '-l',
        required=True,
        choices=['es', 'fr', 'ar'],
        help='Target language'
    )
    parser.add_argument(
        '--output', '-o',
        help='Output SRT file path (default: auto-generate)'
    )
    parser.add_argument(
        '--chunk-size',
        type=int,
        default=25,
        help='Number of subtitles per chunk (default: 25)'
    )
    parser.add_argument(
        '--overlap',
        type=int,
        default=3,
        help='Number of overlapping subtitles for context (default: 3)'
    )
    parser.add_argument(
        '--video-title',
        help='Video title for better context (optional)'
    )
    parser.add_argument(
        '--api-key',
        help='Anthropic API key (or use ANTHROPIC_API_KEY env var)'
    )
    
    args = parser.parse_args()
    
    # Verify source file exists
    if not Path(args.source).exists():
        print(f"❌ Source file not found: {args.source}", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Initialize agent
        agent = SRTTranslationAgent(
            api_key=args.api_key,
            chunk_size=args.chunk_size,
            overlap=args.overlap
        )
        
        # Translate
        output_path = agent.translate_file(
            args.source,
            args.language,
            args.output,
            args.video_title
        )
        
        print(f"\n✨ Translation complete! Output: {output_path}", file=sys.stderr)
        
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
