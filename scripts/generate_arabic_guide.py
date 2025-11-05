#!/usr/bin/env python3
"""
Meta-Skill Generator: Expand Arabic Translation Guide

This script uses the existing French and Spanish translation guides as templates
to generate a comprehensive Arabic translation guide. It leverages Claude API
to analyze patterns and create culturally appropriate, high-quality Arabic content.

Usage:
    python scripts/generate_arabic_guide.py [--dry-run] [--api-key YOUR_KEY]
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional
import anthropic

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
SKILLS_DIR = PROJECT_ROOT / "skills"


def load_guide_content(language: str) -> Dict[str, str]:
    """Load the SKILL.md and all reference files for a language."""
    lang_dir = SKILLS_DIR / f"kobo-translation-{language}"

    content = {
        'skill': (lang_dir / 'SKILL.md').read_text(encoding='utf-8'),
        'references': {}
    }

    ref_dir = lang_dir / 'references'
    if ref_dir.exists():
        for ref_file in ref_dir.glob('*.md'):
            content['references'][ref_file.name] = ref_file.read_text(encoding='utf-8')

    return content


def generate_arabic_guide_content(fr_content: Dict, es_content: Dict, ar_content: Dict, api_key: str) -> str:
    """Generate expanded Arabic guide using Claude API."""

    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""You are an expert in Arabic translation and localization, with deep knowledge of:
- Modern Standard Arabic (MSA) and its use in technical documentation
- Arabic UI/UX conventions and right-to-left (RTL) text handling
- Gender-inclusive language approaches in Arabic
- Arabic typography and punctuation conventions
- Cultural adaptation for Arabic-speaking audiences

I have comprehensive translation guides for French and Spanish that were carefully developed by experts.
I need you to create an equally comprehensive Arabic guide by analyzing the patterns in the French and Spanish guides.

## FRENCH GUIDE (kobo-translation-fr/SKILL.md):
{fr_content['skill'][:30000]}

## SPANISH GUIDE (kobo-translation-es/SKILL.md):
{es_content['skill'][:30000]}

## CURRENT ARABIC GUIDE (kobo-translation-ar/SKILL.md) - INCOMPLETE:
{ar_content['skill']}

## YOUR TASK:

Generate a COMPLETE Arabic translation guide that:

1. **Fills in ALL empty tables and sections** with appropriate Arabic content
2. **Maintains the same structure** as French and Spanish guides
3. **Adds Arabic-specific guidance** including:
   - Formality levels (formal vs informal address in Arabic)
   - Gender-inclusive language strategies for Arabic
   - RTL text handling and HTML dir="rtl" usage
   - Arabic punctuation conventions (Arabic comma ،, Arabic semicolon ؛, Arabic question mark ؟)
   - Number formatting in Arabic contexts
   - Honorifics and respectful address
   - Cultural considerations for Arabic audiences

4. **Creates Arabic translation examples** for:
   - Server names (should these have Arabic articles? What's natural?)
   - Question Library (مكتبة الأسئلة? With or without ال?)
   - Formbuilder (should first reference include English?)
   - UI terminology
   - Common translation pitfalls specific to Arabic

5. **Provides Arabic-specific rules** such as:
   - When to use MSA vs regional variations (if any)
   - Handling of English technical terms in Arabic text
   - Verb tense preferences
   - Sentence structure adaptations from English
   - Common false friends or mistranslations

## IMPORTANT GUIDELINES:

- Use the French and Spanish guides as structural templates
- Study their patterns for handling OFFICIAL vs PREFERRED translations
- Note how they handle technical terms, brand names, and UI elements
- Observe their approach to gender-inclusive language
- Learn from their "Translation Pitfalls" sections

- Keep all the existing Arabic terminology that's already in the current guide
- Preserve the cross-language references to French and Spanish
- Maintain consistency with the terminology reference files

- Focus on creating **actionable, practical guidance** for translators
- Include **concrete examples** with ✅ CORRECT and ❌ WRONG patterns
- Provide **cultural context** where Arabic differs from Romance languages

## OUTPUT FORMAT:

Return ONLY the complete SKILL.md content for Arabic, ready to save to file.
Use the same markdown structure as the French and Spanish guides.
Include all sections: Overview, Checklist, Pitfalls, Workflow, Principles, etc.

Start with the YAML frontmatter and include everything through to the final Notes section."""

    print("🤖 Calling Claude API to generate Arabic guide content...")
    print(f"   Analyzing {len(fr_content['skill'])} chars of French guide")
    print(f"   Analyzing {len(es_content['skill'])} chars of Spanish guide")
    print(f"   Expanding {len(ar_content['skill'])} chars of Arabic guide")

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=16000,
        temperature=0.3,  # Lower temperature for more consistent terminology
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    return response.content[0].text


def generate_arabic_reference(ref_name: str, fr_ref: str, es_ref: str, ar_ref: str, api_key: str) -> str:
    """Generate expanded Arabic reference file using Claude API."""

    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""You are an expert Arabic translator working on a technical translation project.

I need you to complete an Arabic terminology reference file by analyzing the French and Spanish versions.

## FRENCH VERSION ({ref_name}):
{fr_ref}

## SPANISH VERSION ({ref_name}):
{es_ref}

## CURRENT ARABIC VERSION ({ref_name}) - INCOMPLETE:
{ar_ref}

## YOUR TASK:

Fill in ALL missing Arabic translations in the tables. For each English term, provide:

1. **Accurate Arabic translation** that's natural and commonly used
2. **Usage notes** specific to Arabic (if needed)
3. **Consistency** with the patterns established in French and Spanish

## GUIDELINES:

**For Brand Terms:**
- Determine if Arabic needs articles (e.g., "الخادم العالمي" or just "خادم عالمي")
- Consider whether to transliterate brand names or keep them in English
- Maintain consistency with any existing Arabic UI translations

**For Technical Terms:**
- Follow the pattern of English + Arabic translation in parentheses (for technical docs)
- Use commonly accepted Arabic technical terminology
- Consider readability for Arabic-speaking technical users

**For UI Elements:**
- Match capitalization conventions in Arabic (though less relevant than in Romance languages)
- Ensure translations work in RTL context
- Keep terms short enough to fit in UI contexts

## OUTPUT FORMAT:

Return ONLY the complete markdown content for this reference file, ready to save.
Maintain the exact same table structure as the French and Spanish versions.
Fill in ALL empty cells in the Arabic column."""

    print(f"   📄 Generating Arabic content for {ref_name}...")

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8000,
        temperature=0.2,  # Very low temperature for terminology consistency
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    return response.content[0].text


def main():
    parser = argparse.ArgumentParser(description='Generate comprehensive Arabic translation guide')
    parser.add_argument('--dry-run', action='store_true',
                       help='Generate content but don\'t save files')
    parser.add_argument('--api-key', type=str,
                       help='Anthropic API key (or set ANTHROPIC_API_KEY env var)')
    parser.add_argument('--skill-only', action='store_true',
                       help='Only generate SKILL.md, skip reference files')
    parser.add_argument('--references-only', action='store_true',
                       help='Only generate reference files, skip SKILL.md')

    args = parser.parse_args()

    # Get API key
    api_key = args.api_key or os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ Error: ANTHROPIC_API_KEY not found in environment")
        print("   Set it with: export ANTHROPIC_API_KEY='your-key-here'")
        print("   Or use: --api-key YOUR_KEY")
        sys.exit(1)

    print("🚀 Meta-Skill Generator: Expanding Arabic Translation Guide\n")

    # Load all content
    print("📖 Loading existing guides...")
    fr_content = load_guide_content('fr')
    es_content = load_guide_content('es')
    ar_content = load_guide_content('ar')
    print(f"   ✓ French: {len(fr_content['skill'])} chars, {len(fr_content['references'])} references")
    print(f"   ✓ Spanish: {len(es_content['skill'])} chars, {len(es_content['references'])} references")
    print(f"   ✓ Arabic (current): {len(ar_content['skill'])} chars, {len(ar_content['references'])} references\n")

    # Generate SKILL.md
    if not args.references_only:
        print("🔮 Generating comprehensive Arabic SKILL.md...")
        arabic_skill = generate_arabic_guide_content(fr_content, es_content, ar_content, api_key)

        if args.dry_run:
            print("\n" + "="*80)
            print("DRY RUN - Generated Arabic SKILL.md content:")
            print("="*80)
            print(arabic_skill[:2000])
            print("\n... (truncated) ...\n")
            print(f"Total length: {len(arabic_skill)} characters")
        else:
            ar_skill_path = SKILLS_DIR / 'kobo-translation-ar' / 'SKILL.md'
            ar_skill_path.write_text(arabic_skill, encoding='utf-8')
            print(f"   ✅ Saved to: {ar_skill_path}")
            print(f"   📊 Generated {len(arabic_skill)} characters")

    # Generate reference files
    if not args.skill_only:
        print("\n📚 Generating Arabic reference files...")

        ref_files = [
            'brand-terminology.md',
            'ui-terminology.md',
            'form-building-terms.md',
            'question-types.md',
            'data-collection-terms.md',
            'course-terminology.md'
        ]

        for ref_file in ref_files:
            if ref_file in fr_content['references'] and ref_file in es_content['references']:
                fr_ref = fr_content['references'][ref_file]
                es_ref = es_content['references'][ref_file]
                ar_ref = ar_content['references'].get(ref_file, '')

                arabic_ref = generate_arabic_reference(ref_file, fr_ref, es_ref, ar_ref, api_key)

                if args.dry_run:
                    print(f"      [DRY RUN] Would save {len(arabic_ref)} chars to {ref_file}")
                else:
                    ar_ref_path = SKILLS_DIR / 'kobo-translation-ar' / 'references' / ref_file
                    ar_ref_path.parent.mkdir(parents=True, exist_ok=True)
                    ar_ref_path.write_text(arabic_ref, encoding='utf-8')
                    print(f"      ✅ {ref_file}: {len(arabic_ref)} characters")

    print("\n✨ Arabic guide generation complete!")

    if args.dry_run:
        print("\n💡 This was a dry run. Run without --dry-run to save the files.")
    else:
        print("\n📋 Next steps:")
        print("   1. Review the generated Arabic content carefully")
        print("   2. Have an Arabic language expert validate translations")
        print("   3. Test with actual translation tasks")
        print("   4. Iterate and refine based on feedback")
        print("\n💾 Files updated:")
        if not args.references_only:
            print("   - skills/kobo-translation-ar/SKILL.md")
        if not args.skill_only:
            print("   - skills/kobo-translation-ar/references/*.md")


if __name__ == '__main__':
    main()
