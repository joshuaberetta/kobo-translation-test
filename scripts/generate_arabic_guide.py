#!/usr/bin/env python3
"""
Meta Skill: Generate Arabic Translation Guide from French/Spanish Guides

This script analyzes the existing French and Spanish translation guides
and uses AI to generate a comprehensive Arabic guide that follows the same
patterns, principles, and structure while adapting for Arabic-specific
linguistic and cultural considerations.
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List

try:
    import anthropic
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("❌ Missing dependencies. Install with: pip install -r requirements.txt")
    sys.exit(1)


class ArabicGuideGenerator:
    """Meta skill to generate Arabic translation guide from French/Spanish guides"""
    
    def __init__(self):
        """Initialize the generator with Claude API"""
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")
        
        self.claude = anthropic.Anthropic(api_key=api_key)
        
        # Paths
        self.base_path = Path('.')
        self.fr_skill = self.base_path / 'skills/kobo-translation-fr'
        self.es_skill = self.base_path / 'skills/kobo-translation-es'
        self.ar_skill = self.base_path / 'skills/kobo-translation-ar'
        self.en_skill = self.base_path / 'skills/kobo-translation'
    
    def load_skill_file(self, skill_path: Path, filename: str) -> str:
        """Load a skill file"""
        file_path = skill_path / filename
        if file_path.exists():
            return file_path.read_text(encoding='utf-8')
        return ""
    
    def load_all_reference_files(self, skill_path: Path) -> Dict[str, str]:
        """Load all reference files from a skill directory"""
        refs_dir = skill_path / 'references'
        references = {}
        
        if not refs_dir.exists():
            return references
        
        ref_files = [
            'brand-terminology.md',
            'ui-terminology.md',
            'data-collection-terms.md',
            'form-building-terms.md',
            'question-types.md',
            'course-terminology.md',
        ]
        
        for filename in ref_files:
            content = self.load_skill_file(refs_dir, filename)
            if content:
                references[filename] = content
        
        return references
    
    def generate_arabic_skill(self) -> str:
        """Generate comprehensive Arabic SKILL.md from French/Spanish patterns"""
        
        # Load reference materials
        fr_skill = self.load_skill_file(self.fr_skill, 'SKILL.md')
        es_skill = self.load_skill_file(self.es_skill, 'SKILL.md')
        en_skill = self.load_skill_file(self.en_skill, 'SKILL.md')
        
        # Load reference files for context
        fr_refs = self.load_all_reference_files(self.fr_skill)
        es_refs = self.load_all_reference_files(self.es_skill)
        
        # Current Arabic skill (for context on what exists)
        ar_skill_current = self.load_skill_file(self.ar_skill, 'SKILL.md')
        
        print("📚 Loaded reference materials:", file=sys.stderr)
        print(f"  - French SKILL.md: {len(fr_skill)} chars", file=sys.stderr)
        print(f"  - Spanish SKILL.md: {len(es_skill)} chars", file=sys.stderr)
        print(f"  - English SKILL.md: {len(en_skill)} chars", file=sys.stderr)
        print(f"  - Current Arabic SKILL.md: {len(ar_skill_current)} chars", file=sys.stderr)
        print(f"  - French references: {len(fr_refs)} files", file=sys.stderr)
        print(f"  - Spanish references: {len(es_refs)} files", file=sys.stderr)
        
        # Build the prompt for generating Arabic guide
        message_content = [
            {
                "type": "text",
                "text": f"""You are a meta-translation expert specializing in creating comprehensive translation guides for new languages by analyzing and adapting patterns from existing high-quality guides.

## TASK

Generate a complete, comprehensive Arabic translation guide (SKILL.md) for KoboToolbox content translation. This guide should:
1. Follow the same structure and depth as the French and Spanish guides
2. Adapt translation principles for Arabic-specific linguistic features (RTL, different formality levels, etc.)
3. Include Arabic-specific examples and patterns
4. Maintain consistency with the overall approach used in French/Spanish guides

## REFERENCE MATERIALS

### English Base Guide (Multi-language)
```markdown
{en_skill[:8000]}
```

### French Guide (Comprehensive, Well-Developed)
```markdown
{fr_skill[:12000]}
```

### Spanish Guide (Comprehensive, Well-Developed)
```markdown
{es_skill[:12000]}
```

### Current Arabic Guide (Incomplete - use as reference for what exists)
```markdown
{ar_skill_current[:2000]}
```

## KEY PATTERNS TO EXTRACT AND ADAPT

From analyzing the French and Spanish guides, identify:

1. **Structure**: How they organize content (workflow steps, principles, examples, checklists)
2. **Translation Principles**: Core principles that apply across languages
3. **Language-Specific Rules**: How each guide handles language-specific features
4. **Examples**: How they structure examples (correct vs incorrect patterns)
5. **Common Pitfalls**: Recurring mistakes and how to address them
6. **Quality Checklists**: Validation approaches

## ARABIC-SPECIFIC CONSIDERATIONS

When adapting for Arabic, consider:

1. **RTL (Right-to-Left)**: Arabic is written right-to-left
   - Formatting rules for RTL content
   - HTML structure: `<section dir="rtl">` tags
   - Cross-references and links placement

2. **Formality Levels**: Arabic has different formality levels than French/Spanish
   - Formal: أنت/أنتم (ant/antum) - equivalent to vous/Usted
   - More formal: أنت/أنتم with honorifics
   - Note: Arabic formality is context-dependent

3. **Gender-Inclusive Language**: 
   - Arabic has different gender structures
   - Use gender-neutral constructions where possible
   - Plural forms can be gender-neutral
   - Examples: "المستخدمون" (users - masculine plural, can be inclusive), "المستخدمون والمستخدمات" (users - both genders)

4. **Technical Terms**:
   - Many technical terms stay in English (XLSForm, Formbuilder on first reference)
   - Arabic transliteration patterns for technical terms
   - When to use Arabic vs English

5. **Cultural Adaptation**:
   - Tone and style appropriate for Arabic-speaking audiences
   - Regional variations (MSA - Modern Standard Arabic vs dialects)
   - Use MSA for documentation

6. **Formatting**:
   - RTL section wrapping
   - Heading hierarchy
   - Link placement (cross-language links outside RTL sections)
   - Number formatting (Arabic-Indic vs Western numerals)

## OUTPUT REQUIREMENTS

Generate a complete Arabic SKILL.md that:

1. **Has the same comprehensive structure** as French/Spanish guides:
   - Overview section
   - Translation approach (NEW vs UPDATES)
   - Pre-translation checklist
   - Translation workflow (Step 0, 1, 2, 3, 4)
   - Core translation principles
   - Language-specific rules for Arabic
   - Terminology references
   - Quality checklist
   - Translation error examples

2. **Includes Arabic-specific sections**:
   - RTL formatting rules
   - Arabic formality guidelines
   - Arabic gender-inclusive language patterns
   - Arabic-specific pitfalls and common errors

3. **Uses Arabic examples** throughout:
   - Real translation examples showing correct vs incorrect patterns
   - Arabic examples for brand terms, UI elements, etc.
   - Examples showing proper RTL formatting

4. **Maintains consistency** with the overall approach:
   - Same level of detail and comprehensiveness
   - Same structure for decision trees and checklists
   - Same emphasis on brand terminology accuracy

5. **Provides practical guidance**:
   - Clear Arabic-specific rules
   - Actionable checklists
   - Common pitfalls with Arabic examples

## STYLE NOTES

- Write in English (this is a guide for translators, not end users)
- Include Arabic script examples where demonstrating translation patterns
- Be comprehensive - this should be a complete guide ready for use
- Reference the same terminology files as French/Spanish guides
- Include references to Arabic reference files (even if they need to be completed separately)

Now generate the complete Arabic SKILL.md guide:""",
                "cache_control": {"type": "ephemeral"}
            }
        ]
        
        print("\n🤖 Generating Arabic SKILL.md guide...", file=sys.stderr)
        print("   This may take a few minutes...", file=sys.stderr)
        
        try:
            response = self.claude.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=16000,
                temperature=0.3,
                messages=[{
                    "role": "user",
                    "content": message_content
                }]
            )
            
            # Extract generated guide
            arabic_guide = ""
            for block in response.content:
                if block.type == "text":
                    arabic_guide += block.text
            
            # Report usage
            usage = response.usage
            print(f"\n📊 Tokens used: {usage.input_tokens} input, {usage.output_tokens} output", file=sys.stderr)
            
            return arabic_guide
            
        except Exception as e:
            print(f"❌ Generation failed: {e}", file=sys.stderr)
            raise
    
    def generate_arabic_reference(self, ref_filename: str) -> str:
        """Generate an Arabic reference file from French/Spanish patterns"""
        
        # Load reference files
        fr_ref = self.load_skill_file(self.fr_skill / 'references', ref_filename)
        es_ref = self.load_skill_file(self.es_skill / 'references', ref_filename)
        en_ref = self.load_skill_file(self.en_skill / 'references', ref_filename)
        ar_ref_current = self.load_skill_file(self.ar_skill / 'references', ref_filename)
        
        if not fr_ref and not es_ref:
            print(f"⚠️  No French or Spanish reference found for {ref_filename}", file=sys.stderr)
            return ""
        
        print(f"\n📝 Generating Arabic reference: {ref_filename}", file=sys.stderr)
        
        # Build prompt
        message_content = [
            {
                "type": "text",
                "text": f"""You are generating an Arabic translation reference file for KoboToolbox terminology.

## TASK

Generate a complete Arabic version of the reference file: {ref_filename}

This file should:
1. Follow the same structure as the French/Spanish versions
2. Include Arabic translations in the appropriate columns
3. Maintain all formatting, notes, and critical warnings
4. Include Arabic-specific examples and notes where relevant

## REFERENCE MATERIALS

### English Base Reference
```markdown
{en_ref[:6000]}
```

### French Reference (Complete)
```markdown
{fr_ref[:8000]}
```

### Spanish Reference (Complete)
```markdown
{es_ref[:8000]}
```

### Current Arabic Reference (Incomplete - what exists)
```markdown
{ar_ref_current[:2000]}
```

## INSTRUCTIONS

1. **Extract all terms** from the English/French/Spanish references
2. **Generate Arabic translations** for each term:
   - Use Modern Standard Arabic (MSA)
   - Follow Arabic translation conventions
   - Maintain consistency with existing Arabic terms if present
   - For brand terms: Use exact translations specified (if any exist)
   - For UI terms: Match UI capitalization and formatting

3. **Preserve structure**:
   - Keep all tables with Arabic column populated
   - Maintain all warnings and critical notes
   - Keep formatting guidelines
   - Preserve examples sections

4. **Add Arabic-specific notes** where relevant:
   - RTL formatting considerations
   - Arabic-specific translation patterns
   - Cultural adaptations

5. **Fill in missing Arabic translations**:
   - Generate high-quality translations for all terms
   - Use context from French/Spanish to understand term usage
   - Ensure consistency across related terms

Now generate the complete Arabic reference file:""",
                "cache_control": {"type": "ephemeral"}
            }
        ]
        
        try:
            response = self.claude.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=16000,
                temperature=0.3,
                messages=[{
                    "role": "user",
                    "content": message_content
                }]
            )
            
            arabic_ref = ""
            for block in response.content:
                if block.type == "text":
                    arabic_ref += block.text
            
            usage = response.usage
            print(f"  📊 Tokens: {usage.input_tokens} input, {usage.output_tokens} output", file=sys.stderr)
            
            return arabic_ref
            
        except Exception as e:
            print(f"  ❌ Generation failed: {e}", file=sys.stderr)
            raise
    
    def save_file(self, content: str, filepath: Path, backup: bool = True):
        """Save generated content to file"""
        if backup and filepath.exists():
            backup_path = filepath.with_suffix('.md.backup')
            backup_path.write_text(filepath.read_text(encoding='utf-8'), encoding='utf-8')
            print(f"  💾 Backed up existing file to {backup_path.name}", file=sys.stderr)
        
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(content, encoding='utf-8')
        print(f"  ✅ Saved to {filepath}", file=sys.stderr)


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Generate Arabic translation guide from French/Spanish guides'
    )
    parser.add_argument(
        '--skill-only',
        action='store_true',
        help='Generate only SKILL.md (not reference files)'
    )
    parser.add_argument(
        '--reference',
        type=str,
        help='Generate specific reference file (e.g., brand-terminology.md)'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Generate SKILL.md and all reference files'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='skills/kobo-translation-ar',
        help='Output directory (default: skills/kobo-translation-ar)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Generate but do not save files'
    )
    
    args = parser.parse_args()
    
    generator = ArabicGuideGenerator()
    
    try:
        if args.all or args.skill_only or not (args.reference or args.all):
            print("=" * 60, file=sys.stderr)
            print("Generating Arabic SKILL.md", file=sys.stderr)
            print("=" * 60, file=sys.stderr)
            
            arabic_skill = generator.generate_arabic_skill()
            
            if not args.dry_run:
                output_path = Path(args.output_dir) / 'SKILL.md'
                generator.save_file(arabic_skill, output_path)
            else:
                print("\n" + "=" * 60)
                print("GENERATED ARABIC SKILL.MD (DRY RUN - NOT SAVED):")
                print("=" * 60)
                print(arabic_skill)
        
        if args.all or args.reference:
            ref_files = [
                'brand-terminology.md',
                'ui-terminology.md',
                'data-collection-terms.md',
                'form-building-terms.md',
                'question-types.md',
                'course-terminology.md',
            ]
            
            if args.reference:
                ref_files = [args.reference]
            
            for ref_file in ref_files:
                print("\n" + "=" * 60, file=sys.stderr)
                print(f"Generating Arabic reference: {ref_file}", file=sys.stderr)
                print("=" * 60, file=sys.stderr)
                
                arabic_ref = generator.generate_arabic_reference(ref_file)
                
                if not args.dry_run:
                    output_path = Path(args.output_dir) / 'references' / ref_file
                    generator.save_file(arabic_ref, output_path)
                else:
                    print(f"\n{'=' * 60}")
                    print(f"GENERATED {ref_file} (DRY RUN - NOT SAVED):")
                    print("=" * 60)
                    print(arabic_ref[:2000] + "...")
        
        print("\n✨ Generation complete!", file=sys.stderr)
        
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
