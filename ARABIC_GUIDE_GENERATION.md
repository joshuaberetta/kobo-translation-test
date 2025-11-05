# Arabic Guide Generation - Quick Start

## Overview

The `generate_arabic_guide.py` script uses AI to analyze the existing French and Spanish translation guides and generate a comprehensive Arabic guide that follows the same patterns, principles, and structure.

## Prerequisites

1. **Python dependencies**:
   ```bash
   pip install -r scripts/requirements.txt
   ```

2. **API Key**:
   - Set `ANTHROPIC_API_KEY` in your environment or `.env` file
   - This requires a Claude API key from Anthropic

3. **Existing guides**:
   - French guide: `skills/kobo-translation-fr/`
   - Spanish guide: `skills/kobo-translation-es/`
   - English base: `skills/kobo-translation/`

## Usage

### Generate Complete Arabic Guide

Generate both SKILL.md and all reference files:

```bash
python scripts/generate_arabic_guide.py --all
```

This will:
- Generate comprehensive Arabic SKILL.md
- Generate all 6 reference files with Arabic translations
- Save to `skills/kobo-translation-ar/`
- Create backups of existing files

### Generate Only SKILL.md

```bash
python scripts/generate_arabic_guide.py --skill-only
```

### Generate Specific Reference File

```bash
python scripts/generate_arabic_guide.py --reference brand-terminology.md
```

Available reference files:
- `brand-terminology.md`
- `ui-terminology.md`
- `data-collection-terms.md`
- `form-building-terms.md`
- `question-types.md`
- `course-terminology.md`

### Preview Without Saving (Dry Run)

```bash
python scripts/generate_arabic_guide.py --all --dry-run
```

This shows what would be generated without saving files.

## What Gets Generated

### SKILL.md

A comprehensive Arabic translation guide including:

- **Overview**: Translation approach and principles
- **Pre-Translation Checklist**: Critical steps before translating
- **Translation Workflow**: Step-by-step process
- **Arabic-Specific Rules**: 
  - RTL formatting guidelines
  - Formality levels
  - Gender-inclusive language
  - Cultural adaptations
- **Core Principles**: Localization over literal translation
- **Quality Checklist**: Validation criteria
- **Examples**: Correct vs incorrect patterns

### Reference Files

Each reference file includes:

- **Complete Arabic translations** for all terms
- **Arabic-specific notes** and considerations
- **Examples** with Arabic script
- **Same structure** as French/Spanish versions
- **Preserved formatting** and warnings

## Post-Generation Steps

After generating the Arabic guide:

### 1. Review Generated Content

- ✅ Check Arabic translations for accuracy
- ✅ Verify RTL formatting examples
- ✅ Validate brand terms match official translations
- ✅ Review examples for naturalness

### 2. Refine with Native Speaker

- Native Arabic speaker should review:
  - Technical accuracy
  - Natural language flow
  - Cultural appropriateness
  - Formality levels

### 3. Validate Against UI

- Check that UI terms match actual KoboToolbox Arabic UI
- Verify capitalization and formatting
- Update any discrepancies

### 4. Test with Translation Agent

```bash
python scripts/translation_agent.py \
    --file docs/en/test_document.md \
    --language ar \
    --save
```

Review the translation quality and refine the guide if needed.

## Maintenance Workflow

### Adding New Terms

1. Add to English guide first
2. Regenerate Arabic reference:
   ```bash
   python scripts/generate_arabic_guide.py --reference brand-terminology.md
   ```
3. Review and refine Arabic translations
4. Update if needed

### Updating Existing Terms

1. Update English guide
2. Regenerate affected reference file
3. Review Arabic translations
4. Refine if needed

## Cost Estimate

Approximate costs per generation:

- **SKILL.md only**: ~$0.50-1.00
- **Single reference file**: ~$0.30-0.70
- **Complete guide (all files)**: ~$3.00-6.00

Costs depend on:
- Length of reference materials
- Complexity of translations needed
- Model used (Claude Sonnet 4.5)

## Troubleshooting

### "API key not found"

Set the environment variable:
```bash
export ANTHROPIC_API_KEY=your_key_here
```

Or create `.env` file:
```
ANTHROPIC_API_KEY=your_key_here
```

### "Skill directory not found"

Ensure you're running from the workspace root:
```bash
cd /workspace
python scripts/generate_arabic_guide.py --all
```

### Generated translations seem off

- Review the generated content carefully
- Refine with native speaker expertise
- Some terms may need manual adjustment
- Use dry-run to preview before saving

### Need to regenerate specific section

Regenerate just that reference file:
```bash
python scripts/generate_arabic_guide.py --reference ui-terminology.md
```

## Best Practices

1. **Always review generated content** - AI generates good first drafts but needs human review
2. **Validate against UI** - Check actual Arabic UI translations
3. **Get native speaker review** - Essential for quality
4. **Test translations** - Use translation agent to validate
5. **Maintain consistency** - Follow same patterns as French/Spanish guides

## Example Workflow

```bash
# 1. Generate complete Arabic guide
python scripts/generate_arabic_guide.py --all

# 2. Review generated files
# - Check SKILL.md for completeness
# - Review reference files for accuracy

# 3. Refine with manual edits
# - Update Arabic translations based on review
# - Add Arabic-specific examples

# 4. Test translation quality
python scripts/translation_agent.py \
    --file docs/en/sample.md \
    --language ar \
    --test

# 5. Finalize and commit
git add skills/kobo-translation-ar/
git commit -m "Add comprehensive Arabic translation guide"
```

## Next Steps

After generating the Arabic guide:

1. ✅ Review all generated files
2. ✅ Get native speaker review
3. ✅ Validate against UI
4. ✅ Test with translation agent
5. ✅ Refine based on feedback
6. ✅ Update maintenance workflow
7. ✅ Document Arabic-specific patterns

See `MAINTENANCE_STRATEGY.md` for ongoing maintenance guidelines.
