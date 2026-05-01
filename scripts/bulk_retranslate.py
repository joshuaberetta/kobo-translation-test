#!/usr/bin/env python3
"""
Bulk Retranslation Script for KoboToolbox Documentation

Use this script to retranslate all docs or a specific list of files when skills are updated.
This is useful for testing how skill changes affect translation quality across the entire corpus.

Dependencies:
  - Same as translation_agent.py (anthropic, github, dotenv)
  - Run: pip install -r scripts/requirements.txt

Usage:
  # Retranslate all docs to Spanish
  python scripts/bulk_retranslate.py --language es
  
  # Retranslate specific files to multiple languages
  python scripts/bulk_retranslate.py --language es fr ar --files about_kobotoolbox.md quick_start.md
  
  # Dry run to preview
  python scripts/bulk_retranslate.py --language es --dry-run
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Optional
import time
from datetime import datetime

# Add scripts directory to path for imports
scripts_dir = Path(__file__).parent
if str(scripts_dir) not in sys.path:
    sys.path.insert(0, str(scripts_dir))

# Import the translation agent
try:
    from translation_agent import TranslationAgent
except ImportError:
    print("❌ Error: Could not import translation_agent.py", file=sys.stderr)
    print("Make sure you're running this script from the repository root or scripts directory.", file=sys.stderr)
    sys.exit(1)


class BulkRetranslator:
    """Handles bulk retranslation of documentation files"""
    
    def __init__(self, languages: List[str], dry_run: bool = False,
                 verbose: bool = False, delay: float = 0.5,
                 include_transifex: bool = False, auto_transifex: bool = False,
                 include_collect: bool = False):
        """
        Initialize bulk retranslator

        Args:
            languages: List of target languages (e.g., ['es', 'fr', 'ar'])
            dry_run: If True, only show what would be translated without doing it
            verbose: Show detailed output
            delay: Delay in seconds between translations (to avoid rate limits)
            include_transifex: Always include Transifex UI strings for every file
            auto_transifex: Per-file heuristic — include Transifex only when needed
            include_collect: Always include KoboCollect strings
        """
        self.languages = languages
        self.dry_run = dry_run
        self.verbose = verbose
        self.delay = delay
        self.include_transifex = include_transifex
        self.auto_transifex = auto_transifex
        self.include_collect = include_collect
        self.agent = None if dry_run else TranslationAgent(
            test_mode=True,
            include_transifex=include_transifex,
            include_collect=include_collect,
        )
        
        # Track statistics
        self.stats = {
            'total_files': 0,
            'total_translations': 0,
            'successful': 0,
            'failed': 0,
            'skipped': 0,
            'total_cost': 0.0,
            'start_time': None,
            'end_time': None,
        }
        self.failed_files = []
    
    def get_source_files(self, source_dir: Path = None, 
                        file_list: Optional[List[str]] = None) -> List[Path]:
        """
        Get list of source files to translate
        
        Args:
            source_dir: Directory containing source files (default: docs/en)
            file_list: Optional list of specific files to translate
        
        Returns:
            List of Path objects for files to translate
        """
        if source_dir is None:
            source_dir = Path('docs/en')
        
        if file_list:
            # Use specific file list
            files = []
            for f in file_list:
                file_path = source_dir / f if not Path(f).is_absolute() else Path(f)
                if file_path.exists():
                    files.append(file_path)
                else:
                    print(f"⚠️  File not found: {file_path}", file=sys.stderr)
        else:
            # Get all markdown files in source directory
            files = sorted(source_dir.glob('*.md'))
        
        return files
    
    def translate_file(self, source_file: Path, target_lang: str) -> tuple[bool, float]:
        """
        Translate a single file to target language
        
        Args:
            source_file: Path to source file
            target_lang: Target language code
        
        Returns:
            Tuple of (success: bool, cost: float)
        """
        if self.dry_run:
            print(f"  [DRY RUN] Would translate {source_file.name} → {target_lang}")
            return True, 0.0

        # Per-file auto-transifex: rebuild agent if needed
        agent = self.agent
        if self.auto_transifex and not self.include_transifex:
            needs_tx = TranslationAgent.needs_transifex(str(source_file))
            if needs_tx != agent.include_transifex:
                if self.verbose:
                    flag = "ON" if needs_tx else "OFF"
                    print(f"  🔍 auto-transifex {flag} for {source_file.name}", file=sys.stderr)
                agent = TranslationAgent(
                    test_mode=True,
                    include_transifex=needs_tx,
                    include_collect=self.include_collect,
                )

        try:
            # Translate the file
            translation = agent.translate_file(
                str(source_file),
                target_lang,
                complexity=None  # Auto-detect
            )
            
            # Save translation
            target_path = agent.save_translation(
                translation,
                str(source_file),
                target_lang
            )
            
            if self.verbose:
                print(f"  ✅ Saved to: {target_path}", file=sys.stderr)
            
            # Estimate cost (rough approximation based on typical usage)
            # You could enhance this by tracking actual costs from the agent
            cost = 0.15  # Placeholder - actual cost varies by file size
            
            return True, cost
            
        except Exception as e:
            print(f"  ❌ Failed: {e}", file=sys.stderr)
            return False, 0.0
    
    def run(self, source_dir: Path = None, file_list: Optional[List[str]] = None):
        """
        Run bulk retranslation
        
        Args:
            source_dir: Directory containing source files (default: docs/en)
            file_list: Optional list of specific files to translate
        """
        self.stats['start_time'] = datetime.now()
        
        # Get files to translate
        source_files = self.get_source_files(source_dir, file_list)
        
        if not source_files:
            print("❌ No files found to translate", file=sys.stderr)
            return
        
        self.stats['total_files'] = len(source_files)
        total_translations = len(source_files) * len(self.languages)
        self.stats['total_translations'] = total_translations
        
        # Print header
        print("=" * 70)
        print("🔄 BULK RETRANSLATION")
        print("=" * 70)
        print(f"Files: {len(source_files)}")
        print(f"Languages: {', '.join(self.languages)}")
        print(f"Total translations: {total_translations}")
        if self.dry_run:
            print("⚠️  DRY RUN MODE - No actual translations will be performed")
        print("=" * 70)
        print()
        
        # List files if verbose
        if self.verbose:
            print("Files to translate:")
            for f in source_files:
                print(f"  • {f.name}")
            print()
        
        # Process each file
        for i, source_file in enumerate(source_files, 1):
            print(f"[{i}/{len(source_files)}] {source_file.name}")
            
            # Translate to each language
            for lang in self.languages:
                print(f"  → {lang.upper()}", end=" ", flush=True)
                
                success, cost = self.translate_file(source_file, lang)
                
                if success:
                    self.stats['successful'] += 1
                    self.stats['total_cost'] += cost
                    print("✅")
                else:
                    self.stats['failed'] += 1
                    self.failed_files.append((source_file.name, lang))
                    print("❌")
                
                # Delay between translations to avoid rate limits
                if not self.dry_run and self.delay > 0:
                    time.sleep(self.delay)
            
            print()
        
        self.stats['end_time'] = datetime.now()
        self._print_summary()
    
    def _print_summary(self):
        """Print summary statistics"""
        duration = (self.stats['end_time'] - self.stats['start_time']).total_seconds()
        
        print("=" * 70)
        print("📊 SUMMARY")
        print("=" * 70)
        print(f"Total files: {self.stats['total_files']}")
        print(f"Total translations: {self.stats['total_translations']}")
        print(f"✅ Successful: {self.stats['successful']}")
        print(f"❌ Failed: {self.stats['failed']}")
        print(f"⏱️  Duration: {duration:.1f} seconds ({duration/60:.1f} minutes)")
        
        if not self.dry_run:
            print(f"💰 Estimated cost: ${self.stats['total_cost']:.2f}")
            if self.stats['successful'] > 0:
                avg_time = duration / self.stats['successful']
                print(f"⚡ Avg time per translation: {avg_time:.1f} seconds")
        
        if self.failed_files:
            print("\n❌ Failed translations:")
            for filename, lang in self.failed_files:
                print(f"  • {filename} → {lang}")
        
        print("=" * 70)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Bulk retranslate documentation files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Retranslate all docs to Spanish
  python bulk_retranslate.py --language es
  
  # Retranslate all docs to all languages
  python bulk_retranslate.py --language es fr ar
  
  # Retranslate specific files to Spanish and French
  python bulk_retranslate.py --language es fr --files about_kobotoolbox.md quick_start.md
  
  # Dry run to see what would be translated
  python bulk_retranslate.py --language es --dry-run
  
  # Retranslate with custom source directory
  python bulk_retranslate.py --language es --source-dir docs/en
"""
    )
    
    parser.add_argument(
        '--language', '-l',
        nargs='+',
        choices=['es', 'fr', 'ar'],
        required=True,
        help='Target language(s) to translate to'
    )
    
    parser.add_argument(
        '--files', '-f',
        nargs='+',
        help='Specific files to translate (default: all files in source directory)'
    )
    
    parser.add_argument(
        '--source-dir', '-s',
        type=str,
        default='docs/en',
        help='Source directory containing files to translate (default: docs/en)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be translated without actually translating'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed output'
    )
    
    parser.add_argument(
        '--delay',
        type=float,
        default=0.5,
        help='Delay in seconds between translations (default: 0.5, to avoid rate limits)'
    )
    
    parser.add_argument(
        '--no-delay',
        action='store_true',
        help='Disable delay between translations (use with caution)'
    )
    parser.add_argument(
        '--include-transifex',
        action='store_true',
        help='Include Transifex UI strings for every file (~150k chars per call). '
             'Use for corpora heavy with UI element references.'
    )
    parser.add_argument(
        '--auto-transifex',
        action='store_true',
        help='Per-file heuristic: include Transifex strings only for articles '
             'that reference enough UI elements to need them.'
    )
    parser.add_argument(
        '--include-collect',
        action='store_true',
        help='Include KoboCollect Android strings for every file (~60-70k chars per call).'
    )

    args = parser.parse_args()

    # Handle delay
    delay = 0 if args.no_delay else args.delay

    # Verify source directory exists
    source_dir = Path(args.source_dir)
    if not source_dir.exists():
        print(f"❌ Source directory not found: {source_dir}", file=sys.stderr)
        sys.exit(1)

    # Create retranslator
    retranslator = BulkRetranslator(
        languages=args.language,
        dry_run=args.dry_run,
        verbose=args.verbose,
        delay=delay,
        include_transifex=args.include_transifex,
        auto_transifex=args.auto_transifex,
        include_collect=args.include_collect,
    )
    
    # Run bulk retranslation
    try:
        retranslator.run(source_dir=source_dir, file_list=args.files)
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user", file=sys.stderr)
        retranslator.stats['end_time'] = datetime.now()
        retranslator._print_summary()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
