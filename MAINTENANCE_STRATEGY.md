# Multi-Language Translation Guide Maintenance Strategy

## Overview

This document outlines the strategy for maintaining high-quality translation guides across multiple languages (English, French, Spanish, Arabic, and future languages) as they expand to cover more terms and concepts.

## Current State

- **English (Base)**: `skills/kobo-translation/` - Source of truth
- **French**: `skills/kobo-translation-fr/` - Comprehensive, well-developed
- **Spanish**: `skills/kobo-translation-es/` - Comprehensive, well-developed  
- **Arabic**: `skills/kobo-translation-ar/` - Needs completion (being generated via meta skill)

## Core Principles

### 1. Single Source of Truth Model

**English guide is the master reference**
- All new terms and concepts are defined first in English
- English guides establish the structure and organization
- Other language guides adapt from English, not from each other

**Why?** Prevents translation drift and ensures consistency across all languages.

### 2. Meta Skill Approach

**Use existing high-quality guides to bootstrap new languages**
- Analyze patterns from French/Spanish guides
- Extract translation principles and workflows
- Generate initial drafts for new languages
- Then refine with language-specific expertise

**Benefits:**
- Faster initial development
- Consistency in structure and approach
- Captures best practices from mature guides

### 3. Structured Reference Files

**Organize terminology by category:**
- `brand-terminology.md` - OFFICIAL translations (exact matches required)
- `ui-terminology.md` - OFFICIAL translations (UI elements)
- `form-building-terms.md` - OFFICIAL translations (XLSForm terms)
- `question-types.md` - PREFERRED translations (can adapt)
- `data-collection-terms.md` - PREFERRED translations (can adapt)
- `course-terminology.md` - PREFERRED translations (can adapt)

**Why separate files?**
- Clear separation between OFFICIAL (must be exact) vs PREFERRED (can adapt)
- Easier to maintain and update
- Makes it clear which terms require special attention

## Maintenance Workflow

### Adding New Terms or Concepts

When adding new terminology or concepts:

#### Step 1: Add to English Base Guide

1. **Identify the category** (brand, UI, form-building, etc.)
2. **Add to appropriate reference file** in `skills/kobo-translation/references/`
3. **Mark as OFFICIAL or PREFERRED**:
   - **OFFICIAL**: Must be translated exactly (brand terms, UI elements)
   - **PREFERRED**: Can be adapted for context (general terminology)
4. **Include examples** and usage notes
5. **Update main SKILL.md** if new principles or patterns emerge

#### Step 2: Propagate to Other Languages

**Option A: Automated Meta Skill (Recommended for bulk updates)**

Use the meta skill script to generate initial translations:

```bash
python scripts/generate_arabic_guide.py --reference brand-terminology.md
```

Then:
1. Review generated translations
2. Refine with language-specific expertise
3. Validate against UI and actual usage
4. Update reference files

**Option B: Manual Translation (For critical or complex terms)**

1. Translate directly in each language's reference file
2. Follow existing patterns and formatting
3. Include same examples and warnings
4. Get native speaker review

#### Step 3: Update SKILL.md if Needed

If new terms require new principles or workflows:
1. Update English SKILL.md first
2. Use meta skill to adapt for other languages
3. Review and refine language-specific sections

### Updating Existing Terms

When correcting or refining existing translations:

1. **Update English first** (if English changed)
2. **Update each language** systematically:
   - Check if change affects OFFICIAL vs PREFERRED status
   - Update translation accordingly
   - Update examples if needed
3. **Document the change** in a changelog (see below)

### Handling Language-Specific Issues

When a language-specific issue is discovered:

1. **Add to language-specific guide** (e.g., Arabic-specific pitfalls)
2. **Consider if it applies to other languages** - may indicate a missing pattern
3. **Update English guide** if it's a general principle
4. **Add to examples** for future reference

## Quality Assurance

### Pre-Update Checklist

Before updating any guide:

- [ ] Is the change needed in English base guide?
- [ ] Does this affect OFFICIAL or PREFERRED status?
- [ ] Are examples included to clarify usage?
- [ ] Does this require updates to SKILL.md workflow?
- [ ] Will this affect other languages?

### Post-Update Validation

After updating:

- [ ] Formatting preserved (markdown, tables, code blocks)
- [ ] Cross-references updated if structure changed
- [ ] Examples still valid and helpful
- [ ] No broken links
- [ ] Consistency check with other reference files

### Language-Specific Review

For each language:

- [ ] Native speaker review for naturalness
- [ ] Technical accuracy verified
- [ ] Brand terms match official translations
- [ ] UI terms match actual UI
- [ ] Examples are culturally appropriate

## Automated Tools

### Meta Skill Generator

**Purpose**: Generate initial drafts for new languages or bulk updates

**Usage**:
```bash
# Generate complete Arabic guide
python scripts/generate_arabic_guide.py --all

# Generate specific reference file
python scripts/generate_arabic_guide.py --reference brand-terminology.md

# Dry run (preview without saving)
python scripts/generate_arabic_guide.py --all --dry-run
```

**When to use**:
- Initial guide creation for new languages
- Bulk updates when adding many new terms
- Structural updates that need propagation

**When NOT to use**:
- Single term corrections
- Language-specific refinements
- Critical brand terms (always review manually)

### Translation Agent

**Purpose**: Translate actual documentation using the guides

**Usage**: See `scripts/translation_agent.py`

**Integration**: The agent loads language-specific skills automatically

## Maintenance Schedule

### Regular Reviews

**Monthly**: 
- Review for new terms added to KoboToolbox UI
- Check for inconsistencies across languages
- Update examples based on actual usage

**Quarterly**:
- Comprehensive review of each language guide
- Validate against current UI translations
- Update patterns based on translation feedback

**When major features launch**:
- Update guides immediately with new terminology
- Use meta skill for bulk updates
- Prioritize OFFICIAL terms (brand, UI)

## Version Control Strategy

### File Structure

```
skills/
├── kobo-translation/          # English base (source of truth)
├── kobo-translation-fr/       # French (complete)
├── kobo-translation-es/       # Spanish (complete)
├── kobo-translation-ar/       # Arabic (generated + refined)
└── kobo-translation-[lang]/   # Future languages
```

### Change Documentation

**Changelog approach**: Maintain a simple changelog in each language's directory:

```markdown
# CHANGELOG.md

## 2025-01-15
- Added "Question Library" translations (OFFICIAL)
- Updated Formbuilder first-reference rule
- Added Arabic-specific RTL formatting examples

## 2024-12-10
- Initial Arabic guide generation via meta skill
- Completed brand-terminology.md Arabic column
```

### Git Workflow

1. **English changes first**: Commit to `kobo-translation/`
2. **Propagate to languages**: Use meta skill or manual updates
3. **Review and refine**: Each language gets separate review
4. **Commit language updates**: One commit per language for clarity

## Scaling to More Languages

### Adding Language N+1

When adding support for a new language:

1. **Generate initial guide**:
   ```bash
   python scripts/generate_arabic_guide.py --all
   # Adapt command for new language
   ```

2. **Review and refine**:
   - Native speaker review
   - Validate against UI
   - Add language-specific examples

3. **Test with translation agent**:
   - Translate sample documents
   - Review quality
   - Refine guide based on results

4. **Document language-specific patterns**:
   - Formality levels
   - Gender-inclusive language
   - Cultural adaptations
   - RTL/LTR considerations

### Maintaining Consistency Across Languages

**Pattern matching**:
- Use same structure across all languages
- Same categories (brand, UI, forms, etc.)
- Same OFFICIAL vs PREFERRED distinction
- Same example format

**Regular audits**:
- Check that all languages have same terms
- Verify OFFICIAL translations are consistent
- Ensure examples follow same patterns

## Best Practices

### Do's ✅

- **Always update English first** when adding new concepts
- **Use meta skill for bulk updates** to maintain consistency
- **Document language-specific patterns** in each guide
- **Include examples** for every new term or pattern
- **Mark OFFICIAL vs PREFERRED** clearly
- **Review with native speakers** before finalizing
- **Test translations** with actual documents

### Don'ts ❌

- **Don't translate from other languages** - use English as source
- **Don't skip meta skill review** - always refine generated content
- **Don't mix OFFICIAL and PREFERRED** - be clear about which is which
- **Don't skip examples** - they're critical for clarity
- **Don't update in isolation** - coordinate across languages
- **Don't forget to update SKILL.md** if principles change

## Troubleshooting

### Issue: Translations drift across languages

**Solution**: 
- Re-generate from English base using meta skill
- Review and refine with language expertise
- Establish clear OFFICIAL term guidelines

### Issue: New terms added inconsistently

**Solution**:
- Use structured workflow (English → Meta Skill → Review)
- Maintain checklist for all languages
- Regular audits to catch inconsistencies

### Issue: Quality varies across languages

**Solution**:
- Use meta skill to ensure structural consistency
- Native speaker review for each language
- Regular validation against UI and usage

### Issue: Updates become overwhelming

**Solution**:
- Batch updates when possible
- Use meta skill for bulk changes
- Prioritize OFFICIAL terms (critical for brand consistency)

## Future Enhancements

### Potential Improvements

1. **Automated validation**:
   - Check that all languages have same terms
   - Validate OFFICIAL translations match
   - Verify examples follow patterns

2. **Translation memory**:
   - Store validated translations
   - Reuse across documents
   - Learn from reviewer corrections

3. **Cross-language consistency checker**:
   - Automated tool to find inconsistencies
   - Flag missing translations
   - Suggest updates

4. **Interactive guide builder**:
   - Web interface for editing guides
   - Real-time validation
   - Preview generated translations

## Conclusion

The meta skill approach enables rapid creation of high-quality translation guides for new languages while maintaining consistency across all languages. By:

1. Using English as single source of truth
2. Leveraging meta skill for initial generation
3. Refining with language-specific expertise
4. Following structured maintenance workflows

We can scale to many languages while maintaining quality and consistency.

## Quick Reference

**Add new term**:
1. Add to English `skills/kobo-translation/references/[category].md`
2. Run meta skill: `python scripts/generate_arabic_guide.py --reference [category].md`
3. Review and refine each language
4. Update SKILL.md if principles changed

**Update existing term**:
1. Update English first
2. Update each language systematically
3. Validate against UI/usage
4. Document in changelog

**Add new language**:
1. Generate initial guide: `python scripts/generate_arabic_guide.py --all`
2. Review with native speaker
3. Refine language-specific sections
4. Test with translation agent
5. Add to maintenance workflow
