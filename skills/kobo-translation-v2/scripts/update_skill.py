#!/usr/bin/env python3
"""
Update kobo-translation-v2 skill from source files.

Usage:
    python scripts/update_skill.py [--skip-validation]

This is a convenience wrapper that:
1. Validates source files (unless --skip-validation)
2. Regenerates the skill from sources

Use this after updating the glossary or style guide.
"""

import subprocess
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = SKILL_ROOT / "scripts"


def run_script(script_name: str) -> bool:
    """Run a Python script and return success status."""
    script_path = SCRIPTS_DIR / script_name
    result = subprocess.run([sys.executable, str(script_path)])
    return result.returncode == 0


def main():
    skip_validation = "--skip-validation" in sys.argv
    
    print("=" * 60)
    print("  KoboToolbox Translation Skill Updater")
    print("=" * 60)
    print()
    
    # Validation
    if not skip_validation:
        print("Step 1: Validating source files...")
        print("-" * 40)
        if not run_script("validate_sources.py"):
            print()
            print("❌ Validation failed. Fix errors and try again.")
            print("   Use --skip-validation to bypass (not recommended)")
            sys.exit(1)
        print()
    else:
        print("⚠️  Skipping validation (--skip-validation)")
        print()
    
    # Regeneration
    print("Step 2: Regenerating skill...")
    print("-" * 40)
    if not run_script("regenerate_skill.py"):
        print()
        print("❌ Regeneration failed.")
        sys.exit(1)
    
    print()
    print("=" * 60)
    print("  ✅ Skill update complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
