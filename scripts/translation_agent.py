#!/usr/bin/env python3
"""
KoboToolbox Translation Agent - Simplified Test Version
Translates documentation using Claude API with embedded kobo-translation skill
"""

import os
import sys
import json
import hashlib
import argparse
from pathlib import Path
from typing import Dict, Tuple
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()  # This loads .env file automatically

try:
    import anthropic
    from github import Github
    from transifex_sync import TransifexSync
except ImportError:
    print("❌ Missing dependencies. Install with: pip install -r requirements.txt")
    sys.exit(1)


class TranslationAgent:
    """Simplified AI agent for testing automated documentation translation"""
    
    def __init__(self, test_mode: bool = False, sync_transifex: bool = True, 
                 transifex_token: str = None):
        """
        Initialize the translation agent
        
        Args:
            test_mode: If True, run locally without GitHub integration
            sync_transifex: Whether to sync Transifex before translating (default: True)
            transifex_token: Transifex API token (or uses TRANSIFEX_API_TOKEN env var)
        """
        self.test_mode = test_mode
        
        # Load API key
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")
        
        self.claude = anthropic.Anthropic(api_key=api_key)
        
        # Transifex integration
        self.sync_transifex = sync_transifex
        self.transifex_token = transifex_token
        self.transifex_synced = set()  # Track which languages we've synced
        
        # GitHub integration (only if not in test mode)
        if not test_mode:
            github_token = os.getenv('GITHUB_TOKEN')
            if not github_token:
                raise ValueError("GITHUB_TOKEN environment variable not set")
            
            self.github = Github(github_token)
            repo_name = os.getenv('GITHUB_REPOSITORY')
            if repo_name:
                self.repo = self.github.get_repo(repo_name)
            else:
                self.repo = None
        
        # Target languages
        self.languages = ['es', 'fr', 'ar']
        
        # Skill context cache (will be loaded per-language as needed)
        self.skill_cache = {}
    
    def _get_skill_context(self, target_lang: str) -> Dict[str, str]:
        """
        Get skill context for a specific language, with caching
        
        Args:
            target_lang: Target language code (es, fr, ar)
        
        Returns:
            Dictionary containing skill content
        """
        if target_lang not in self.skill_cache:
            print(f"📚 Loading kobo-translation skill for {target_lang.upper()}...", file=sys.stderr)
            
            # Sync Transifex terminology first (once per language)
            if self.sync_transifex and target_lang not in self.transifex_synced:
                self._sync_transifex_terminology(target_lang)
                self.transifex_synced.add(target_lang)
            
            self.skill_cache[target_lang] = self._load_skill_context(target_lang)
            print(f"✅ Skill loaded successfully ({len(self.skill_cache[target_lang])} files)", file=sys.stderr)
        
        return self.skill_cache[target_lang]
    
    def _sync_transifex_terminology(self, target_lang: str):
        """
        Sync latest UI terminology from Transifex
        
        Args:
            target_lang: Target language code
        """
        print(f"  🔄 Syncing Transifex terminology for {target_lang.upper()}...", file=sys.stderr)
        
        try:
            sync = TransifexSync(api_token=self.transifex_token)
            
            # Fetch latest translations
            translations = sync.sync_language_terminology(target_lang)
            
            if translations:
                # Save to skill reference file
                sync.save_terminology_file(translations, target_lang)
                print(f"    ✅ Synced {len(translations)} UI terms from Transifex", file=sys.stderr)
            else:
                print(f"    ⚠️  No Transifex translations found", file=sys.stderr)
                
        except ValueError as e:
            # Missing API token - warn but continue
            print(f"    ⚠️  Skipping Transifex sync: {e}", file=sys.stderr)
        except Exception as e:
            # Other errors - warn but continue
            print(f"    ⚠️  Transifex sync failed: {e}", file=sys.stderr)
    
    def _load_skill_context(self, target_lang: str = None) -> Dict[str, str]:
        """
        Load skill files from repository into memory
        
        Args:
            target_lang: Target language code (es, fr, ar). If provided, loads language-specific skill.
                        If None, loads the generic multi-language skill.
        """
        # Try to load language-specific skill first if target_lang is provided
        if target_lang:
            skill_base = Path(f'skills/kobo-translation-{target_lang}')
            if skill_base.exists():
                print(f"  📚 Loading language-specific skill for {target_lang.upper()}...", file=sys.stderr)
            else:
                print(f"  ⚠️  Language-specific skill not found for {target_lang}, falling back to generic skill", file=sys.stderr)
                skill_base = Path('skills/kobo-translation')
        else:
            skill_base = Path('skills/kobo-translation')
        
        if not skill_base.exists():
            raise FileNotFoundError(
                f"Skill directory not found: {skill_base}\n"
                "Make sure you've copied the kobo-translation skill to skills/"
            )
        
        context = {}
        
        # Read main skill file
        main_skill = skill_base / 'SKILL.md'
        if main_skill.exists():
            context['main'] = main_skill.read_text(encoding='utf-8')
        else:
            raise FileNotFoundError(f"SKILL.md not found in {skill_base}")
        
        # Read reference files
        refs_dir = skill_base / 'references'
        if refs_dir.exists():
            ref_files = {
                'brand': 'brand-terminology.md',
                'ui': 'ui-terminology.md',
                'data': 'data-collection-terms.md',
                'forms': 'form-building-terms.md',
                'questions': 'question-types.md',
                'course': 'course-terminology.md',
            }
            
            for key, filename in ref_files.items():
                file_path = refs_dir / filename
                if file_path.exists():
                    context[key] = file_path.read_text(encoding='utf-8')
                else:
                    print(f"⚠️  Reference file not found: {filename}", file=sys.stderr)
        
        return context
    
    def determine_complexity(self, file_path: str) -> str:
        """
        Determine translation complexity based on file content
        
        Returns: 'simple', 'standard', or 'complex'
        """
        content = Path(file_path).read_text(encoding='utf-8')
        
        # Count brand terms
        brand_terms = [
            'KoboToolbox', 'Formbuilder', 'Question Library',
            'Global Server', 'European Union', 'XLSForm'
        ]
        brand_count = sum(content.count(term) for term in brand_terms)
        
        # Count UI elements
        ui_elements = ['DEPLOY', 'NEW', 'FORM', 'DATA', 'Settings', 'Save']
        ui_count = sum(content.count(term) for term in ui_elements)
        
        length = len(content)
        
        # Simple: Short with no brand terms
        if length < 1000 and brand_count == 0:
            return 'simple'
        
        # Complex: Long or many brand/UI terms
        if length > 3000 or brand_count > 5 or ui_count > 5:
            return 'complex'
        
        # Standard: Most documents
        return 'standard'
    
    def translate_diff(self, diff_content: str, target_lang: str,
                      context: str = None) -> str:
        """
        Translate only a diff (changed content) using Claude
        
        Args:
            diff_content: Only the changed lines/paragraphs to translate
            target_lang: Target language (es, fr, ar)
            context: Optional surrounding context for better translation
        """
        print(f"  📊 Translation mode: DIFF-BASED (changes only)", file=sys.stderr)
        
        # Load language-specific skill context
        skill_context = self._get_skill_context(target_lang)
        
        # Build context note
        context_note = ""
        if context:
            context_note = f"""
SURROUNDING CONTEXT (for reference only - DO NOT translate):
```
{context}
```
"""
        
        # Build message content with prompt caching
        message_content = [
            {
                "type": "text",
                "text": f"""{skill_context.get('main', '')}

## BRAND TERMINOLOGY REFERENCE
{skill_context.get('brand', '')}

## UI TERMINOLOGY REFERENCE
{skill_context.get('ui', '')}

## DATA COLLECTION TERMS
{skill_context.get('data', '')}

## FORM BUILDING TERMS
{skill_context.get('forms', '')}

## QUESTION TYPES
{skill_context.get('questions', '')}

## COURSE TERMINOLOGY
{skill_context.get('course', '')}""",
                "cache_control": {"type": "ephemeral"}  # Cache skill content
            },
            {
                "type": "text",
                "text": f"""
TARGET LANGUAGE: {target_lang.upper()}

🚨🚨🚨 CRITICAL INSTRUCTION 🚨🚨🚨

You are translating ONLY A DIFF - NOT a full document.

RULES:
1. Translate ONLY the exact content between the markers below
2. Do NOT translate anything outside the markers
3. Do NOT translate any context provided for reference
4. Do NOT add any explanations, comments, or meta-text
5. Output ONLY the translated version of the diff content
6. Do NOT translate the markers themselves
7. Do NOT modify, add to, or expand the content
8. ONLY translate what is explicitly between the BEGIN and END markers

This is an UPDATE to an existing translation. The rest of the document is already translated correctly.
Your job is to translate ONLY this small change.

{context_note}

---BEGIN DIFF TO TRANSLATE---
{diff_content}
---END DIFF TO TRANSLATE---

Now provide ONLY the translated diff content (nothing else):"""
            }
        ]
        
        print(f"  🤖 Calling Claude API...", file=sys.stderr)
        
        try:
            # Call Claude API with system message to reinforce diff-only behavior
            response = self.claude.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=8000,
                temperature=0.3,  # Lower for consistency
                system="""You are a precise translation tool. When translating a DIFF (partial content), you MUST:
1. Translate ONLY the content between the BEGIN and END markers
2. Output ONLY the translated text with NO additional content
3. NOT translate anything outside the markers
4. NOT add explanations, comments, or metadata
This is critical - translate ONLY what is explicitly marked for translation.""",
                messages=[{
                    "role": "user",
                    "content": message_content
                }]
            )
            
            # Extract translation
            translation = ""
            for block in response.content:
                if block.type == "text":
                    translation += block.text
            
            # Report token usage (including cache metrics)
            usage = response.usage
            cache_read = getattr(usage, 'cache_read_input_tokens', 0)
            cache_write = getattr(usage, 'cache_creation_input_tokens', 0)
            
            print(f"  📊 Tokens used: {usage.input_tokens} input, {usage.output_tokens} output", file=sys.stderr)
            if cache_read > 0 or cache_write > 0:
                print(f"  💾 Cache: {cache_read} read, {cache_write} write", file=sys.stderr)
            
            # Calculate cost with prompt caching
            input_cost = usage.input_tokens / 1_000_000 * 3
            cache_write_cost = cache_write / 1_000_000 * 3.75  # 25% premium
            cache_read_cost = cache_read / 1_000_000 * 0.30  # 90% discount
            output_cost = usage.output_tokens / 1_000_000 * 15
            
            cost = input_cost + cache_write_cost + cache_read_cost + output_cost
            print(f"  💰 Estimated cost: ${cost:.4f}", file=sys.stderr)
            
            return translation
            
        except Exception as e:
            print(f"  ❌ Translation failed: {e}", file=sys.stderr)
            raise
    
    def translate_file(self, source_path: str, target_lang: str,
                      complexity: str = None, is_update: bool = False,
                      diff_content: str = None) -> str:
        """
        Translate a markdown file using Claude with embedded skill
        
        Args:
            source_path: Path to source markdown file
            target_lang: Target language (es, fr, ar)
            complexity: Force complexity level, or auto-detect if None
            is_update: If True, expects diff_content to be provided
            diff_content: Only the changed content (for updates)
        """
        # Handle diff-based updates
        if is_update:
            if not diff_content:
                raise ValueError("diff_content must be provided when is_update=True")
            
            print(f"  🔄 UPDATE MODE: Translating diff only", file=sys.stderr)
            print(f"  📏 Diff size: {len(diff_content)} characters", file=sys.stderr)
            
            # Safety check - if diff is suspiciously large, warn user
            if len(diff_content) > 5000:
                print(f"  ⚠️  WARNING: Diff is very large ({len(diff_content)} chars)", file=sys.stderr)
                print(f"  ⚠️  Are you sure this is just a diff and not the full file?", file=sys.stderr)
                response = input("  Continue? (y/n): ")
                if response.lower() != 'y':
                    raise ValueError("Translation cancelled by user")
            
            return self.translate_diff(diff_content, target_lang)
        
        # Full file translation (NEW content)
        # Read source file
        source_content = Path(source_path).read_text(encoding='utf-8')
        
        # Determine complexity if not specified
        if complexity is None:
            complexity = self.determine_complexity(source_path)
        
        print(f"  📊 Complexity level: {complexity}")
        
        # Load language-specific skill context
        skill_context = self._get_skill_context(target_lang)
        
        # Build final prompt with prompt caching
        message_content = [
            {
                "type": "text",
                "text": f"""{skill_context.get('main', '')}

## BRAND TERMINOLOGY REFERENCE
{skill_context.get('brand', '')}

## UI TERMINOLOGY REFERENCE
{skill_context.get('ui', '')}

## DATA COLLECTION TERMS
{skill_context.get('data', '')}

## FORM BUILDING TERMS
{skill_context.get('forms', '')}

## QUESTION TYPES
{skill_context.get('questions', '')}

## COURSE TERMINOLOGY
{skill_context.get('course', '')}""",
                "cache_control": {"type": "ephemeral"}  # Cache skill content
            },
            {
                "type": "text",
                "text": f"""
TARGET LANGUAGE: {target_lang.upper()}

Now translate this COMPLETE NEW document following ALL rules above.
Provide ONLY the translated markdown. No explanations, comments, or meta-text.

---BEGIN SOURCE DOCUMENT---
{source_content}
---END SOURCE DOCUMENT---

Translation:"""
            }
        ]

        print(f"  🤖 Calling Claude API...")
        
        try:
            # Call Claude API
            response = self.claude.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=16000,
                temperature=0.3,  # Lower for consistency
                messages=[{
                    "role": "user",
                    "content": message_content
                }]
            )
            
            # Extract translation
            translation = ""
            for block in response.content:
                if block.type == "text":
                    translation += block.text
            
            # Report token usage (including cache metrics)
            usage = response.usage
            cache_read = getattr(usage, 'cache_read_input_tokens', 0)
            cache_write = getattr(usage, 'cache_creation_input_tokens', 0)
            
            print(f"  📊 Tokens used: {usage.input_tokens} input, {usage.output_tokens} output")
            if cache_read > 0 or cache_write > 0:
                print(f"  💾 Cache: {cache_read} read, {cache_write} write")
            
            # Calculate cost with prompt caching
            input_cost = usage.input_tokens / 1_000_000 * 3
            cache_write_cost = cache_write / 1_000_000 * 3.75  # 25% premium
            cache_read_cost = cache_read / 1_000_000 * 0.30  # 90% discount
            output_cost = usage.output_tokens / 1_000_000 * 15
            
            cost = input_cost + cache_write_cost + cache_read_cost + output_cost
            print(f"  💰 Estimated cost: ${cost:.4f}")
            
            return translation
            
        except Exception as e:
            print(f"  ❌ Translation failed: {e}")
            raise
    
    def apply_translated_diff(self, existing_translation: str, 
                             translated_diff: str,
                             line_number: int = None,
                             old_content: str = None) -> str:
        """
        Apply a translated diff to an existing translation
        
        Args:
            existing_translation: Current translated document
            translated_diff: The newly translated diff content
            line_number: Line number where to apply change (optional)
            old_content: Old content to replace (optional, for search-replace)
        
        Returns:
            Updated translation with diff applied
        """
        if old_content:
            # Search and replace mode
            if old_content not in existing_translation:
                raise ValueError("old_content not found in existing translation")
            return existing_translation.replace(old_content, translated_diff, 1)
        
        elif line_number is not None:
            # Line number mode
            lines = existing_translation.split('\n')
            diff_lines = translated_diff.split('\n')
            
            # Replace at specific line
            lines[line_number:line_number+len(diff_lines)] = diff_lines
            return '\n'.join(lines)
        
        else:
            raise ValueError("Either old_content or line_number must be provided")
    
    def validate_translation(self, source_path: str, translation: str,
                           target_lang: str) -> Dict:
        """
        Perform basic validation checks on translation
        
        Returns: Dictionary with validation results
        """
        source_content = Path(source_path).read_text(encoding='utf-8')
        
        checks = {
            'has_content': len(translation.strip()) > 0,
            'preserves_headers': translation.count('#') == source_content.count('#'),
            'preserves_links': translation.count('[') >= source_content.count('[') * 0.9,
            'has_brand_term': 'KoboToolbox' in translation,
            'no_english_artifacts': 'TODO' not in translation and 'FIXME' not in translation,
        }
        
        # Language-specific checks
        if target_lang == 'es':
            checks['uses_informal'] = 'tú' in translation.lower() or 'tu ' in translation.lower()
            checks['gender_inclusive'] = 'los/as' in translation or 'las/os' in translation
        elif target_lang == 'fr':
            checks['uses_formal'] = 'vous' in translation.lower()
            checks['gender_inclusive'] = 'utilisatrices' in translation or 'utilisateurs' in translation
        
        checks['passed'] = all(checks.values())
        
        return checks
    
    def save_translation(self, translation: str, source_path: str,
                        target_lang: str) -> Path:
        """
        Save translation to appropriate location
        
        Returns: Path where translation was saved
        """
        source = Path(source_path)
        target_dir = Path('docs') / target_lang
        target_dir.mkdir(parents=True, exist_ok=True)
        
        target_path = target_dir / source.name
        target_path.write_text(translation, encoding='utf-8')
        
        return target_path


def main():
    """Main entry point for testing"""
    parser = argparse.ArgumentParser(
        description='KoboToolbox Translation Agent - Test Version'
    )
    parser.add_argument(
        '--file',
        required=True,
        help='Path to source file to translate (e.g., docs/en/test_simple.md)'
    )
    parser.add_argument(
        '--language',
        choices=['es', 'fr', 'ar'],
        required=True,
        help='Target language'
    )
    parser.add_argument(
        '--complexity',
        choices=['simple', 'standard', 'complex'],
        help='Force complexity level (auto-detect if not specified)'
    )
    parser.add_argument(
        '--save',
        action='store_true',
        help='Save translation to file (default: just display)'
    )
    parser.add_argument(
        '--test',
        action='store_true',
        help='Test mode - run locally without GitHub'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed output'
    )
    parser.add_argument(
        '--no-transifex-sync',
        action='store_true',
        help='Skip syncing latest UI terminology from Transifex'
    )
    parser.add_argument(
        '--transifex-token',
        help='Transifex API token (or use TRANSIFEX_API_TOKEN env var)'
    )
    parser.add_argument(
        '--diff',
        type=str,
        help='Diff content to translate (for update mode). Use with --update-mode'
    )
    parser.add_argument(
        '--update-mode',
        action='store_true',
        help='Update mode: translate only the diff and apply to existing translation'
    )
    parser.add_argument(
        '--old-content',
        type=str,
        help='Old content to replace (used with --update-mode to find where to apply diff)'
    )
    
    args = parser.parse_args()
    
    # Verify source file exists
    if not Path(args.file).exists():
        print(f"❌ Source file not found: {args.file}")
        sys.exit(1)
    
    # Validate update mode arguments
    if args.update_mode and not args.diff:
        print("❌ --update-mode requires --diff to be provided", file=sys.stderr)
        sys.exit(1)
    
    # Output metadata to stderr so stdout is clean for piping
    print("🚀 KoboToolbox Translation Agent - Test Mode", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    print(f"📄 Source: {args.file}", file=sys.stderr)
    print(f"🌐 Target language: {args.language.upper()}", file=sys.stderr)
    if args.update_mode:
        print(f"⚡ Mode: UPDATE (diff-based translation)", file=sys.stderr)
    else:
        print(f"📝 Mode: NEW (full file translation)", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    
    try:
        # Initialize agent
        agent = TranslationAgent(
            test_mode=True, 
            sync_transifex=not args.no_transifex_sync,
            transifex_token=args.transifex_token
        )
        
        # Translate
        if args.update_mode:
            print(f"\n🔄 Translating diff to {args.language.upper()}...", file=sys.stderr)
            translated_diff = agent.translate_file(
                args.file,
                args.language,
                is_update=True,
                diff_content=args.diff
            )
            
            # Apply to existing translation if it exists
            target_dir = Path('docs') / args.language
            target_file = target_dir / Path(args.file).name
            
            if target_file.exists() and args.save:
                print(f"\n📝 Applying translated diff to existing translation...", file=sys.stderr)
                existing = target_file.read_text(encoding='utf-8')
                
                if args.old_content:
                    updated = agent.apply_translated_diff(
                        existing,
                        translated_diff,
                        old_content=args.old_content
                    )
                else:
                    # If no old_content specified, append or manual application needed
                    print("⚠️  No --old-content specified. Showing diff for manual application.", file=sys.stderr)
                    updated = None
                
                if updated:
                    target_file.write_text(updated, encoding='utf-8')
                    print(f"✅ Updated translation saved to: {target_file}", file=sys.stderr)
                else:
                    print("\n" + "=" * 60, file=sys.stderr)
                    print("TRANSLATED DIFF (apply manually):", file=sys.stderr)
                    print("=" * 60, file=sys.stderr)
                    print(translated_diff)
                    print("=" * 60, file=sys.stderr)
            else:
                # In test mode without save, just output the translation cleanly
                # This makes it easy to extract in automated workflows
                print(translated_diff)
        else:
            # Full file translation
            print(f"\n🔄 Translating complete file to {args.language.upper()}...")
            translation = agent.translate_file(
                args.file,
                args.language,
                args.complexity
            )
            
            # Validate
            print(f"\n✓ Translation complete!")
            print(f"\n🔍 Validating translation...")
            validation = agent.validate_translation(args.file, translation, args.language)
            
            print("\nValidation Results:")
            for check, passed in validation.items():
                if check == 'passed':
                    continue
                status = "✅" if passed else "❌"
                print(f"  {status} {check}")
            
            if validation['passed']:
                print(f"\n✅ All validation checks passed!")
            else:
                print(f"\n⚠️  Some validation checks failed - review translation carefully", file=sys.stderr)
            
            # Save or display
            if args.save:
                target_path = agent.save_translation(translation, args.file, args.language)
                print(f"\n💾 Translation saved to: {target_path}", file=sys.stderr)
            else:
                print("\n" + "=" * 60, file=sys.stderr)
                print("TRANSLATION OUTPUT:", file=sys.stderr)
                print("=" * 60, file=sys.stderr)
                print(translation)
                print("=" * 60, file=sys.stderr)
                print("\nℹ️  Use --save to write translation to file", file=sys.stderr)
        
        print("\n✨ Translation test complete!", file=sys.stderr)
        
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
