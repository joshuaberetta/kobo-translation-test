#!/usr/bin/env python3
"""
Fetch the latest glossary from the published Google Sheet.

Usage:
    python scripts/fetch_glossary.py

Downloads the Google Sheet as xlsx and saves it to sources/glossary.xlsx,
overwriting the previous cached copy. The local file is kept in version control
as an offline fallback; run this script to refresh it before regenerating.

After fetching, run:
    python scripts/regenerate_skill.py
"""

import sys
import urllib.request
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent
SOURCES_DIR = SKILL_ROOT / "sources"

GOOGLE_SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/e/"
    "2PACX-1vTn5JHMRlVqh8z5DTflmRJgDmhyRmFDogzRol7ESs2nY67ROZVbHiFfEmTptcP4seGxZ_WQ72ui-5R_"
    "/pub?output=xlsx"
)

DEST_PATH = SOURCES_DIR / "glossary.xlsx"


def main():
    print("Fetching glossary from Google Sheets...")
    print(f"  URL: {GOOGLE_SHEET_URL[:80]}...")
    print()

    try:
        with urllib.request.urlopen(GOOGLE_SHEET_URL, timeout=30) as response:
            data = response.read()
    except urllib.error.URLError as e:
        print(f"❌ Download failed: {e}")
        print("   Check your internet connection or verify the sheet is published.")
        sys.exit(1)

    if len(data) < 1000:
        print(f"❌ Downloaded file is suspiciously small ({len(data)} bytes) — aborting.")
        sys.exit(1)

    SOURCES_DIR.mkdir(exist_ok=True)
    DEST_PATH.write_bytes(data)
    print(f"✅ Saved to {DEST_PATH} ({len(data):,} bytes)")
    print()

    # Print sheet names so the user can confirm the download looks right
    try:
        import pandas as pd
        xl = pd.ExcelFile(DEST_PATH)
        print(f"Sheets found ({len(xl.sheet_names)}):")
        for name in xl.sheet_names:
            print(f"  - {name}")
    except ImportError:
        print("(Install pandas to see sheet names)")
    except Exception as e:
        print(f"⚠️  Could not read sheet names: {e}")

    print()
    print("Run 'python scripts/regenerate_skill.py' to rebuild the skill.")


if __name__ == "__main__":
    main()
