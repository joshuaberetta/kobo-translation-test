#!/usr/bin/env python3
"""
Remove "Last updated" lines from markdown documentation files.

This script removes lines matching the pattern:
  **Last updated:** <a href="...">...</a>
  **Last updated:**
  
from all English source files in docs/en/

Usage:
    python scripts/remove_last_updated.py           # Dry run (shows what would be removed)
    python scripts/remove_last_updated.py --apply   # Actually remove the lines
"""

import re
import argparse
from pathlib import Path
from typing import List, Tuple


def find_last_updated_line(content: str) -> Tuple[bool, int, str]:
    """
    Find the "Last updated" line in content.
    
    Returns:
        (found, line_number, matched_line)
    """
    lines = content.split('\n')
    
    # Pattern matches:
    # **Last updated:** <a href="...">...</a>
    # **Last updated:**
    pattern = re.compile(r'^\*\*Last updated:\*\*.*$', re.IGNORECASE)
    
    for i, line in enumerate(lines):
        if pattern.match(line):
            return (True, i, line)
    
    return (False, -1, "")


def remove_last_updated(file_path: Path, dry_run: bool = True) -> bool:
    """
    Remove "Last updated" line from a file.
    
    Args:
        file_path: Path to the markdown file
        dry_run: If True, only show what would be changed
        
    Returns:
        True if changes were made (or would be made), False otherwise
    """
    try:
        content = file_path.read_text(encoding='utf-8')
        
        found, line_num, matched_line = find_last_updated_line(content)
        
        if not found:
            return False
        
        # Remove the line
        lines = content.split('\n')
        
        if dry_run:
            print(f"  📄 {file_path.name}")
            print(f"     Line {line_num + 1}: {matched_line[:80]}{'...' if len(matched_line) > 80 else ''}")
            return True
        else:
            # Remove the line
            del lines[line_num]
            
            # Check if the previous line is an H1 heading
            is_after_h1 = (line_num > 0 and lines[line_num - 1].startswith('# '))
            
            # If we removed the "Last updated" line after an H1 heading,
            # we need to ensure there's exactly one blank line
            if is_after_h1:
                # Check if there's already a blank line at current position
                if line_num < len(lines) and lines[line_num].strip() == '':
                    # Already has a blank line, keep it
                    pass
                else:
                    # No blank line, insert one to preserve spacing
                    lines.insert(line_num, '')
            else:
                # Not after H1, remove any trailing blank line to avoid double spacing
                if line_num < len(lines) and lines[line_num].strip() == '':
                    del lines[line_num]
            
            # Write back
            new_content = '\n'.join(lines)
            file_path.write_text(new_content, encoding='utf-8')
            
            print(f"  ✅ {file_path.name}")
            print(f"     Removed: {matched_line[:80]}{'...' if len(matched_line) > 80 else ''}")
            return True
            
    except Exception as e:
        print(f"  ❌ Error processing {file_path.name}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Remove "Last updated" lines from English documentation files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/remove_last_updated.py              # Dry run
  python scripts/remove_last_updated.py --apply      # Actually remove
  python scripts/remove_last_updated.py --file docs/en/about_kobotoolbox.md --apply
        """
    )
    parser.add_argument(
        '--apply',
        action='store_true',
        help='Actually remove the lines (default is dry run)'
    )
    parser.add_argument(
        '--file',
        type=str,
        help='Process only a specific file (default: all files in docs/en/)'
    )
    
    args = parser.parse_args()
    
    # Determine which files to process
    if args.file:
        files = [Path(args.file)]
        if not files[0].exists():
            print(f"❌ File not found: {args.file}")
            return 1
    else:
        en_dir = Path('docs/en')
        if not en_dir.exists():
            print(f"❌ Directory not found: {en_dir}")
            print("   Make sure you're running from the repository root")
            return 1
        
        files = sorted(en_dir.glob('*.md'))
    
    if not files:
        print("❌ No markdown files found")
        return 1
    
    # Process files
    mode = "APPLY" if args.apply else "DRY RUN"
    print(f"\n{'='*70}")
    print(f"  🔍 Remove 'Last Updated' Lines - {mode}")
    print(f"{'='*70}\n")
    
    if not args.apply:
        print("ℹ️  This is a DRY RUN - no files will be modified")
        print("   Use --apply to actually remove the lines\n")
    
    print(f"📁 Processing {len(files)} file(s)...\n")
    
    changed_count = 0
    unchanged_count = 0
    
    for file_path in files:
        changed = remove_last_updated(file_path, dry_run=not args.apply)
        if changed:
            changed_count += 1
        else:
            unchanged_count += 1
    
    # Summary
    print(f"\n{'='*70}")
    print(f"  📊 Summary")
    print(f"{'='*70}")
    print(f"  {'Modified' if args.apply else 'Would modify'}: {changed_count} file(s)")
    print(f"  No changes: {unchanged_count} file(s)")
    print(f"  Total: {len(files)} file(s)")
    print(f"{'='*70}\n")
    
    if not args.apply and changed_count > 0:
        print("✨ To apply these changes, run:")
        print(f"   python scripts/remove_last_updated.py --apply\n")
    elif args.apply and changed_count > 0:
        print("✅ Changes have been applied!")
        print("   Don't forget to commit the changes:\n")
        print("   git add docs/en/")
        print('   git commit -m "Remove Last updated sections from documentation"')
        print("   git push\n")
    
    return 0


if __name__ == '__main__':
    exit(main())
