#!/usr/bin/env python3
"""
Apply translated diff to existing translation file.
This handles the intelligent merging of newly translated content into existing files.
"""
import sys
import argparse
from pathlib import Path


def find_best_match(lines, old_lines):
    """Find the best matching location for old content in existing file."""
    if not old_lines:
        return -1, 0.0
    
    best_idx = -1
    best_score = 0.0
    
    for i in range(len(lines) - len(old_lines) + 1):
        segment = '\n'.join(lines[i:i+len(old_lines)])
        
        # Calculate similarity score
        segment_words = set(segment.lower().split())
        old_words = set('\n'.join(old_lines).lower().split())
        
        if old_words:
            score = len(segment_words & old_words) / len(old_words)
            if score > best_score:
                best_score = score
                best_idx = i
    
    return best_idx, best_score


def apply_translation(target_file, old_content, new_translation, mode='smart'):
    """
    Apply translated content to existing file.
    
    Args:
        target_file: Path to existing translation file
        old_content: Original English content that was changed (empty for new additions)
        new_translation: Newly translated content to insert
        mode: 'smart' (default), 'replace', or 'append'
    
    Returns:
        bool: Success status
    """
    target_path = Path(target_file)
    
    if not target_path.exists():
        print(f"Error: Target file not found: {target_file}", file=sys.stderr)
        return False
    
    # Read existing translation
    with open(target_path, 'r', encoding='utf-8') as f:
        existing = f.read()
    
    old_content = old_content.strip()
    new_translation = new_translation.strip()
    
    if not new_translation:
        print("Warning: Empty translation content", file=sys.stderr)
        return False
    
    # Smart mode: try different strategies
    if mode == 'smart':
        if old_content and old_content in existing:
            # Direct replacement - exact match found
            updated = existing.replace(old_content, new_translation, 1)
            print("✓ Direct replacement successful", file=sys.stderr)
        elif old_content:
            # Fuzzy matching
            lines = existing.split('\n')
            old_lines = old_content.split('\n')
            
            best_idx, best_score = find_best_match(lines, old_lines)
            
            if best_idx >= 0 and best_score > 0.5:
                # Replace at best match location
                new_lines = new_translation.split('\n')
                lines[best_idx:best_idx+len(old_lines)] = new_lines
                updated = '\n'.join(lines)
                print(f"✓ Fuzzy replacement successful (score: {best_score:.2f})", file=sys.stderr)
            else:
                # Append to end as fallback
                updated = existing.rstrip() + '\n\n' + new_translation + '\n'
                print("⚠ Appended to end (couldn't find good match)", file=sys.stderr)
        else:
            # No old content - append new
            updated = existing.rstrip() + '\n\n' + new_translation + '\n'
            print("✓ Appended new content", file=sys.stderr)
    
    elif mode == 'replace':
        if old_content and old_content in existing:
            updated = existing.replace(old_content, new_translation, 1)
            print("✓ Replaced content", file=sys.stderr)
        else:
            print("Error: Could not find old content for replacement", file=sys.stderr)
            return False
    
    elif mode == 'append':
        updated = existing.rstrip() + '\n\n' + new_translation + '\n'
        print("✓ Appended content", file=sys.stderr)
    
    else:
        print(f"Error: Unknown mode: {mode}", file=sys.stderr)
        return False
    
    # Write updated file
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(updated)
    
    return True


def main():
    parser = argparse.ArgumentParser(description='Apply translated diff to existing file')
    parser.add_argument('--target', required=True, help='Target translation file')
    parser.add_argument('--old', default='', help='Old content (what was replaced in English)')
    parser.add_argument('--new', required=True, help='New translated content')
    parser.add_argument('--mode', choices=['smart', 'replace', 'append'], default='smart',
                        help='Application mode')
    
    args = parser.parse_args()
    
    success = apply_translation(args.target, args.old, args.new, args.mode)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
