#!/usr/bin/env python3
"""
Extract translated content from translation agent log file.
"""
import sys
import re


def extract_translation(log_file):
    """Extract the actual translation from log output."""
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Strategy 1: Look for explicit translation markers
        in_translation = False
        result = []
        for line in lines:
            if 'Translation:' in line or 'TRANSLATION:' in line or 'translated diff content' in line.lower():
                in_translation = True
                continue
            if in_translation and not line.startswith('[') and not line.startswith('Estimated'):
                result.append(line)
        
        output = ''.join(result).strip()
        if output:
            print(output)
            return
        
        # Strategy 2: Get last non-log lines
        non_empty = [l for l in lines if l.strip() and not l.startswith('[') and not 'Estimated' in l and not 'INFO' in l]
        if non_empty:
            # Take last 20 lines as potential translation
            print(''.join(non_empty[-20:]).strip())
            return
        
        # Strategy 3: Just return the file content (fallback)
        print(''.join(lines).strip())
        
    except Exception as e:
        print(f"Error extracting translation: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: extract_translation.py <log_file>", file=sys.stderr)
        sys.exit(1)
    
    extract_translation(sys.argv[1])
