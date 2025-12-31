#!/usr/bin/env python3
"""
Extract all msgid entries from a PO file into a simple JSON reference file.
This creates a clean list of UI strings for autocomplete without the complexity
of parsing the full PO format at runtime.
"""

import json
import re
import sys
from pathlib import Path


def extract_msgids_from_po(po_file_path: Path) -> list[str]:
    """
    Extract all msgid values from a PO file.
    
    Args:
        po_file_path: Path to the PO file
        
    Returns:
        List of msgid strings (without duplicates, sorted)
    """
    msgids = []
    current_msgid = []
    in_msgid = False
    
    with open(po_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # Start of msgid
            if line.startswith('msgid "'):
                in_msgid = True
                current_msgid = []
                # Extract text between quotes
                match = re.match(r'msgid\s+"(.*)"', line)
                if match:
                    text = match.group(1)
                    if text:  # Only add non-empty
                        current_msgid.append(text)
            
            # Continuation line (multi-line msgid)
            elif in_msgid and line.startswith('"') and not line.startswith('msgstr'):
                match = re.match(r'"(.*)"', line)
                if match:
                    current_msgid.append(match.group(1))
            
            # End of msgid (when we hit msgstr)
            elif line.startswith('msgstr'):
                in_msgid = False
                
                if current_msgid:
                    # Join multi-line msgids
                    msgid_text = ''.join(current_msgid)
                    
                    # Decode escape sequences
                    msgid_text = (msgid_text
                                  .replace('\\n', '\n')
                                  .replace('\\t', '\t')
                                  .replace('\\"', '"')
                                  .replace('\\\\', '\\'))
                    
                    # Only add non-empty msgids
                    if msgid_text.strip():
                        msgids.append(msgid_text)
                
                current_msgid = []
    
    # Remove duplicates and sort
    msgids = sorted(set(msgids))
    
    return msgids


def main():
    """Extract msgids and save to JSON."""
    # Default paths
    repo_root = Path(__file__).parent.parent
    po_file = repo_root / "external/form-builder-translations/en/LC_MESSAGES/djangojs.po"
    output_file = repo_root / "external/form-builder-translations/ui-strings.json"
    
    # Allow custom paths from command line
    if len(sys.argv) > 1:
        po_file = Path(sys.argv[1])
    if len(sys.argv) > 2:
        output_file = Path(sys.argv[2])
    
    if not po_file.exists():
        print(f"Error: PO file not found: {po_file}")
        sys.exit(1)
    
    print(f"Extracting msgids from: {po_file}")
    msgids = extract_msgids_from_po(po_file)
    
    print(f"Found {len(msgids)} unique msgid entries")
    
    # Save to JSON
    output_data = {
        "source": str(po_file),
        "count": len(msgids),
        "strings": msgids
    }
    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(msgids)} UI strings to: {output_file}")
    
    # Show some examples
    print("\nSample strings:")
    for msgid in msgids[:10]:
        print(f"  - {msgid}")
    
    if len(msgids) > 10:
        print(f"  ... and {len(msgids) - 10} more")


if __name__ == "__main__":
    main()
