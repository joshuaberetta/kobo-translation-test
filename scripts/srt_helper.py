#!/usr/bin/env python3
"""
SRT Helper - Parse and manipulate SRT subtitle files
Converts between SRT format and JSON for easy processing
"""

import json
import re
from typing import List, Dict, Optional
from datetime import timedelta
from pathlib import Path


class SRTSubtitle:
    """Represents a single subtitle entry"""
    
    def __init__(self, index: int, start_time: str, end_time: str, text: str):
        """
        Initialize a subtitle entry
        
        Args:
            index: Subtitle number (1-indexed)
            start_time: Start timestamp (HH:MM:SS,mmm)
            end_time: End timestamp (HH:MM:SS,mmm)
            text: Subtitle text (may be multiple lines)
        """
        self.index = index
        self.start_time = start_time
        self.end_time = end_time
        self.text = text.strip()
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            'index': self.index,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'text': self.text,
            'duration_ms': self.get_duration_ms()
        }
    
    def to_srt(self) -> str:
        """Convert to SRT format"""
        return f"{self.index}\n{self.start_time} --> {self.end_time}\n{self.text}\n"
    
    def get_duration_ms(self) -> int:
        """Calculate duration in milliseconds"""
        start_ms = self._timestamp_to_ms(self.start_time)
        end_ms = self._timestamp_to_ms(self.end_time)
        return end_ms - start_ms
    
    @staticmethod
    def _timestamp_to_ms(timestamp: str) -> int:
        """Convert SRT timestamp to milliseconds"""
        # Format: HH:MM:SS,mmm
        time_part, ms_part = timestamp.split(',')
        h, m, s = map(int, time_part.split(':'))
        ms = int(ms_part)
        return (h * 3600 + m * 60 + s) * 1000 + ms
    
    def __repr__(self):
        return f"SRTSubtitle({self.index}, {self.start_time}->{self.end_time}, '{self.text[:30]}...')"


class SRTParser:
    """Parse SRT files into structured data"""
    
    # SRT timestamp pattern: HH:MM:SS,mmm --> HH:MM:SS,mmm
    TIMESTAMP_PATTERN = re.compile(
        r'(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})'
    )
    
    @classmethod
    def parse_file(cls, file_path: str) -> List[SRTSubtitle]:
        """
        Parse an SRT file into subtitle objects
        
        Args:
            file_path: Path to SRT file
        
        Returns:
            List of SRTSubtitle objects
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return cls.parse_string(content)
    
    @classmethod
    def parse_string(cls, srt_content: str) -> List[SRTSubtitle]:
        """
        Parse SRT content string into subtitle objects
        
        Args:
            srt_content: SRT formatted string
        
        Returns:
            List of SRTSubtitle objects
        """
        subtitles = []
        
        # Split by double newlines (subtitle separator)
        blocks = re.split(r'\n\s*\n', srt_content.strip())
        
        for block in blocks:
            if not block.strip():
                continue
            
            lines = block.strip().split('\n')
            
            if len(lines) < 3:
                # Invalid block, skip
                continue
            
            # First line: index
            try:
                index = int(lines[0].strip())
            except ValueError:
                # Not a valid index, skip this block
                continue
            
            # Second line: timestamps
            timestamp_match = cls.TIMESTAMP_PATTERN.match(lines[1])
            if not timestamp_match:
                # Invalid timestamp format, skip
                continue
            
            start_time = timestamp_match.group(1)
            end_time = timestamp_match.group(2)
            
            # Remaining lines: text
            text = '\n'.join(lines[2:])
            
            subtitle = SRTSubtitle(index, start_time, end_time, text)
            subtitles.append(subtitle)
        
        return subtitles
    
    @classmethod
    def validate_srt(cls, file_path: str) -> Dict:
        """
        Validate an SRT file and return diagnostics
        
        Args:
            file_path: Path to SRT file
        
        Returns:
            Dictionary with validation results
        """
        try:
            subtitles = cls.parse_file(file_path)
        except Exception as e:
            return {
                'valid': False,
                'error': str(e),
                'subtitle_count': 0
            }
        
        issues = []
        
        # Check sequential numbering
        for i, sub in enumerate(subtitles, 1):
            if sub.index != i:
                issues.append(f"Subtitle {i}: Expected index {i}, got {sub.index}")
        
        # Check timestamp ordering
        for i in range(len(subtitles) - 1):
            curr = subtitles[i]
            next_sub = subtitles[i + 1]
            
            curr_end = SRTSubtitle._timestamp_to_ms(curr.end_time)
            next_start = SRTSubtitle._timestamp_to_ms(next_sub.start_time)
            
            if curr_end > next_start:
                issues.append(
                    f"Subtitle {curr.index}: Overlaps with next subtitle "
                    f"(ends at {curr.end_time}, next starts at {next_sub.start_time})"
                )
        
        # Check for empty text
        for sub in subtitles:
            if not sub.text.strip():
                issues.append(f"Subtitle {sub.index}: Empty text")
        
        return {
            'valid': len(issues) == 0,
            'subtitle_count': len(subtitles),
            'issues': issues,
            'total_duration_ms': subtitles[-1].get_duration_ms() if subtitles else 0
        }


class SRTWriter:
    """Write subtitle objects back to SRT format"""
    
    @staticmethod
    def write_file(subtitles: List[SRTSubtitle], output_path: str):
        """
        Write subtitles to SRT file
        
        Args:
            subtitles: List of SRTSubtitle objects
            output_path: Path to output SRT file
        """
        content = SRTWriter.to_string(subtitles)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    @staticmethod
    def to_string(subtitles: List[SRTSubtitle]) -> str:
        """
        Convert subtitles to SRT formatted string
        
        Args:
            subtitles: List of SRTSubtitle objects
        
        Returns:
            SRT formatted string
        """
        srt_blocks = []
        
        for subtitle in subtitles:
            srt_blocks.append(subtitle.to_srt())
        
        return '\n'.join(srt_blocks)


class SRTConverter:
    """Convert between SRT and JSON formats"""
    
    @staticmethod
    def srt_to_json(srt_path: str, json_path: Optional[str] = None) -> Dict:
        """
        Convert SRT file to JSON
        
        Args:
            srt_path: Path to input SRT file
            json_path: Optional path to output JSON file (if None, returns dict)
        
        Returns:
            Dictionary containing subtitle data
        """
        subtitles = SRTParser.parse_file(srt_path)
        
        data = {
            'source_file': Path(srt_path).name,
            'subtitle_count': len(subtitles),
            'subtitles': [sub.to_dict() for sub in subtitles]
        }
        
        if json_path:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        
        return data
    
    @staticmethod
    def json_to_srt(json_path: str, srt_path: Optional[str] = None) -> str:
        """
        Convert JSON file back to SRT
        
        Args:
            json_path: Path to input JSON file
            srt_path: Optional path to output SRT file (if None, returns string)
        
        Returns:
            SRT formatted string
        """
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        subtitles = []
        for sub_dict in data['subtitles']:
            subtitle = SRTSubtitle(
                index=sub_dict['index'],
                start_time=sub_dict['start_time'],
                end_time=sub_dict['end_time'],
                text=sub_dict['text']
            )
            subtitles.append(subtitle)
        
        srt_content = SRTWriter.to_string(subtitles)
        
        if srt_path:
            with open(srt_path, 'w', encoding='utf-8') as f:
                f.write(srt_content)
        
        return srt_content
    
    @staticmethod
    def json_dict_to_srt(json_data: Dict) -> str:
        """
        Convert JSON dictionary to SRT string
        
        Args:
            json_data: Dictionary with 'subtitles' key containing subtitle data
        
        Returns:
            SRT formatted string
        """
        subtitles = []
        for sub_dict in json_data['subtitles']:
            subtitle = SRTSubtitle(
                index=sub_dict['index'],
                start_time=sub_dict['start_time'],
                end_time=sub_dict['end_time'],
                text=sub_dict['text']
            )
            subtitles.append(subtitle)
        
        return SRTWriter.to_string(subtitles)


def main():
    """Command-line interface for SRT helper"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='SRT Helper - Parse and convert SRT subtitle files'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Parse command
    parse_parser = subparsers.add_parser('parse', help='Parse SRT to JSON')
    parse_parser.add_argument('input', help='Input SRT file')
    parse_parser.add_argument('--output', '-o', help='Output JSON file (optional)')
    
    # Convert command
    convert_parser = subparsers.add_parser('convert', help='Convert JSON back to SRT')
    convert_parser.add_argument('input', help='Input JSON file')
    convert_parser.add_argument('--output', '-o', help='Output SRT file (optional)')
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate SRT file')
    validate_parser.add_argument('input', help='Input SRT file')
    
    args = parser.parse_args()
    
    if args.command == 'parse':
        print(f"📄 Parsing SRT file: {args.input}")
        data = SRTConverter.srt_to_json(args.input, args.output)
        print(f"✅ Found {data['subtitle_count']} subtitles")
        
        if args.output:
            print(f"💾 Saved to: {args.output}")
        else:
            print("\n" + json.dumps(data, indent=2, ensure_ascii=False))
    
    elif args.command == 'convert':
        print(f"📄 Converting JSON to SRT: {args.input}")
        srt_content = SRTConverter.json_to_srt(args.input, args.output)
        
        if args.output:
            print(f"✅ SRT file created: {args.output}")
        else:
            print("\n" + srt_content)
    
    elif args.command == 'validate':
        print(f"🔍 Validating SRT file: {args.input}")
        result = SRTParser.validate_srt(args.input)
        
        print(f"\n{'✅ Valid' if result['valid'] else '❌ Invalid'}")
        print(f"Subtitle count: {result['subtitle_count']}")
        
        if result.get('issues'):
            print(f"\n⚠️  Issues found:")
            for issue in result['issues']:
                print(f"  • {issue}")
        
        if result.get('error'):
            print(f"\n❌ Error: {result['error']}")
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
