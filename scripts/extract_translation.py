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
            content = f.read()
        
        # Since we now output to stdout cleanly, just return the content
        # But strip any remaining metadata that might have leaked through
        lines = content.split('\n')
        clean_lines = []
        
        for line in lines:
            # Skip separator lines
            if '====' in line:
                continue
            # Skip lines with log emojis
            if any(emoji in line for emoji in ['📄', '🌐', '⚡', '📚', '✅', '🔄', '📏', '📊', '🤖', '✨', 'ℹ️', '💰', '⚠️']):
                continue
            # Skip common log phrases
            if any(phrase in line for phrase in ['Source:', 'Target language:', 'Mode:', 'Loading', 'Skill loaded', 'Translating', 'Tokens used', 'Estimated cost', 'Translation test complete', 'UPDATE MODE', 'Calling Claude']):
                continue
            # Keep actual content
            if line.strip():
                clean_lines.append(line)
        
        result = '\n'.join(clean_lines).strip()
        
        if result:
            print(result)
        else:
            # Empty translation
            print("", file=sys.stderr)
            sys.exit(1)
        
    except Exception as e:
        print(f"Error extracting translation: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: extract_translation.py <log_file>", file=sys.stderr)
        sys.exit(1)
    
    extract_translation(sys.argv[1])
