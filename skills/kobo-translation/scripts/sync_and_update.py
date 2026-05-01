#!/usr/bin/env python3
"""
Sync source files into the skill and regenerate.

Usage:
    # Pull latest glossary from Google Sheets, then validate and regenerate:
    python scripts/sync_and_update.py --fetch

    # Copy local files manually, then validate and regenerate:
    python scripts/sync_and_update.py <glossary.xlsx> <style-guide.md>
    python scripts/sync_and_update.py <directory_containing_both>

Examples:
    python scripts/sync_and_update.py --fetch
    python scripts/sync_and_update.py ~/Downloads/Translation_Glossary.xlsx ~/Downloads/Translation_Guide.md
    python scripts/sync_and_update.py ~/kobo-translations/
"""

import shutil
import subprocess
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent
SOURCES_DIR = SKILL_ROOT / "sources"
SCRIPTS_DIR = SKILL_ROOT / "scripts"


def find_source_files(args: list[str]) -> tuple[Path | None, Path | None]:
    """Find glossary and style guide from provided arguments."""
    glossary = None
    style_guide = None

    for arg in args:
        path = Path(arg)

        if path.is_dir():
            for f in path.iterdir():
                if f.suffix == ".xlsx" and glossary is None:
                    glossary = f
                elif f.suffix == ".md" and style_guide is None:
                    style_guide = f
        elif path.is_file():
            if path.suffix == ".xlsx":
                glossary = path
            elif path.suffix == ".md":
                style_guide = path

    return glossary, style_guide


def run_script(script_name: str) -> bool:
    result = subprocess.run([sys.executable, str(SCRIPTS_DIR / script_name)])
    return result.returncode == 0


def main():
    args = sys.argv[1:]

    if not args:
        print(__doc__)
        sys.exit(1)

    if "--fetch" in args:
        print("🌐 Fetching glossary from Google Sheets...")
        print("-" * 40)
        if not run_script("fetch_glossary.py"):
            print()
            print("❌ Fetch failed. Check your internet connection.")
            sys.exit(1)
        print()
        print("🔄 Running update...")
        print("-" * 40)
        if not run_script("update_skill.py"):
            sys.exit(1)
        return

    # Manual file copy path
    print("🔄 Syncing source files...")
    print()

    glossary, style_guide = find_source_files(args)

    if glossary is None:
        print("❌ Error: No .xlsx glossary file found")
        sys.exit(1)

    if style_guide is None:
        print("❌ Error: No .md style guide file found")
        sys.exit(1)

    print(f"📊 Glossary: {glossary}")
    print(f"📄 Style guide: {style_guide}")
    print()

    SOURCES_DIR.mkdir(exist_ok=True)

    print("📂 Copying to sources/...")
    shutil.copy2(glossary, SOURCES_DIR / "glossary.xlsx")
    shutil.copy2(style_guide, SOURCES_DIR / "style-guide.md")
    print("   ✅ Files copied")
    print()

    print("🔄 Running update...")
    print("-" * 40)
    if not run_script("update_skill.py"):
        sys.exit(1)


if __name__ == "__main__":
    main()
