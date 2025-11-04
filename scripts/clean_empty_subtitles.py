#!/usr/bin/env python3
"""
Clean empty subtitle entries from SRT files.
Removes subtitles that only contain whitespace and re-numbers sequentially.
"""
import sys
import argparse

def clean_srt_file(file_path):
    """
    Clean empty subtitles from an SRT file.
    
    Args:
        file_path: Path to the SRT file to clean
        
    Returns:
        Number of empty subtitles removed
    """
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into subtitle blocks
    blocks = content.split('\n\n')

    cleaned_blocks = []
    removed_count = 0

    for block in blocks:
        if not block.strip():
            continue
        
        lines = block.strip().split('\n')
        if len(lines) >= 3:
            # Check if text content (lines after timestamp) is not just whitespace
            text_content = '\n'.join(lines[2:])
            if text_content.strip():
                cleaned_blocks.append(block.strip())
            else:
                removed_count += 1

    # Re-number the subtitles
    final_blocks = []
    for i, block in enumerate(cleaned_blocks, 1):
        lines = block.split('\n')
        lines[0] = str(i)
        final_blocks.append('\n'.join(lines))

    # Write back with proper formatting
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(final_blocks))
        f.write('\n')

    return removed_count, len(cleaned_blocks)


def main():
    parser = argparse.ArgumentParser(
        description='Clean empty subtitle entries from SRT files'
    )
    parser.add_argument(
        'file_path',
        help='Path to the SRT file to clean'
    )
    
    args = parser.parse_args()
    
    try:
        removed_count, final_count = clean_srt_file(args.file_path)
        
        if removed_count > 0:
            print(f"✅ Cleaned {removed_count} empty subtitle(s)")
        else:
            print("✅ No empty subtitles found")
        
        print(f"📊 Final subtitle count: {final_count}")
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
