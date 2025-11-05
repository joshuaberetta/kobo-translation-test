# Translation Guide Maintenance System

**A scalable, maintainable approach to managing multilingual translation guides**

## 🎯 Overview

This system provides a **meta-skill** approach to maintaining translation guides across multiple languages. Instead of manually updating each language guide when adding new terminology, you maintain a **single source of truth** that automatically propagates to all language guides.

## 🏗️ Architecture

```
kobo-translation-test/
├── terminology/
│   └── master_terminology.yaml    # ⭐ SOURCE OF TRUTH - All terms defined here
│
├── skills/
│   ├── kobo-translation-fr/       # French guide (auto-generated from master)
│   ├── kobo-translation-es/       # Spanish guide (auto-generated from master)
│   └── kobo-translation-ar/       # Arabic guide (auto-generated from master)
│
└── scripts/
    ├── generate_arabic_guide.py   # 🤖 Meta-skill generator for Arabic
    ├── sync_terminology.py        # 🔄 Sync master → all languages
    └── validate_guides.py         # ✅ Quality assurance checks
```

## 🚀 Quick Start

### 1. Generate Comprehensive Arabic Guide

The Arabic guide currently has gaps. Use the meta-skill generator to create a complete first draft:

```bash
# Set your Anthropic API key
export ANTHROPIC_API_KEY='your-key-here'

# Generate complete Arabic guide using French/Spanish as templates
python scripts/generate_arabic_guide.py

# Or do a dry run first to preview
python scripts/generate_arabic_guide.py --dry-run
```

**What this does:**
- Analyzes French and Spanish guides to understand patterns
- Uses Claude API to generate Arabic-specific content
- Fills in all empty tables and sections
- Adds Arabic-specific guidance (RTL, punctuation, gender-inclusive language)
- Creates comprehensive examples

**Options:**
```bash
# Generate only the main SKILL.md file
python scripts/generate_arabic_guide.py --skill-only

# Generate only reference files
python scripts/generate_arabic_guide.py --references-only

# Preview without saving
python scripts/generate_arabic_guide.py --dry-run
```

### 2. Validate All Guides

Check for completeness and consistency across all language guides:

```bash
# Validate all languages
python scripts/validate_guides.py

# Validate specific language
python scripts/validate_guides.py --language ar

# Strict mode (warnings become errors)
python scripts/validate_guides.py --strict
```

**Checks performed:**
- ✅ All required sections present
- ✅ Tables have complete content
- ✅ Language-specific content appropriate
- ✅ Cross-references valid
- ✅ Terminology consistent with master database

### 3. Sync Terminology Across Languages

When you add new terms to the master database, sync them to all guides:

```bash
# Validate terminology completeness
python scripts/sync_terminology.py --validate-only

# Auto-generate missing translations
python scripts/sync_terminology.py --auto-generate

# Sync specific language
python scripts/sync_terminology.py --language ar
```

## 📖 Workflows

### Workflow 1: Adding a New Term to All Languages

**Old way** (manual, error-prone):
1. Edit French guide
2. Edit Spanish guide
3. Edit Arabic guide
4. Hope you didn't miss anything or introduce inconsistencies

**New way** (automated, consistent):

1. **Add to master database** (`terminology/master_terminology.yaml`):

```yaml
brand_terms:
  - english: "Data Sharing"
    category: "OFFICIAL"
    translations:
      fr: "Partage de données"
      es: "Compartir datos"
      ar: "مشاركة البيانات"
    notes: "Feature name, capitalize appropriately"
```

2. **Sync to all guides**:
```bash
python scripts/sync_terminology.py
```

3. **Validate**:
```bash
python scripts/validate_guides.py
```

4. **Done!** All guides updated consistently.

### Workflow 2: Expanding Arabic Guide

**Goal:** Create a comprehensive Arabic guide equivalent to French/Spanish

1. **Generate initial content**:
```bash
python scripts/generate_arabic_guide.py
```

2. **Review generated content** (CRITICAL):
   - Have an Arabic language expert review
   - Check cultural appropriateness
   - Verify technical accuracy
   - Test with real translations

3. **Refine and iterate**:
```bash
# Make manual edits to skills/kobo-translation-ar/SKILL.md
# Re-run generator for specific sections if needed
python scripts/generate_arabic_guide.py --references-only
```

4. **Validate quality**:
```bash
python scripts/validate_guides.py --language ar
```

### Workflow 3: Adding a New Language (e.g., Portuguese)

1. **Update master terminology** to include Portuguese:

```yaml
metadata:
  languages:
    - fr
    - es
    - ar
    - pt  # Add Portuguese
```

2. **Create language directory**:
```bash
mkdir -p skills/kobo-translation-pt/references
```

3. **Generate Portuguese translations**:
```bash
# This will prompt you to generate missing translations
python scripts/sync_terminology.py --auto-generate
```

4. **Create Portuguese guide** (adapt `generate_arabic_guide.py`):
```python
# Create generate_portuguese_guide.py based on arabic version
# Or extend to support multiple target languages
```

5. **Validate**:
```bash
python scripts/validate_guides.py --language pt
```

## 🗂️ Master Terminology Database

### Structure

The master database (`terminology/master_terminology.yaml`) contains:

```yaml
metadata:
  version: "1.0"
  last_updated: "2025-11-05"
  languages: [fr, es, ar]
  categories: [brand, ui, form-building, question-types, data-collection, course]

brand_terms:
  - english: "Global KoboToolbox Server"
    category: "OFFICIAL"  # Must use EXACT translation
    translations:
      fr: "Le serveur KoboToolbox mondial"
      es: "Servidor Global"
      ar: "الخادم العالمي لـ KoboToolbox"
    notes: |
      FR: Must include definite article "Le" (capitalized)
      ES: Do NOT add "de KoboToolbox"
    pitfalls:
      fr_wrong: "serveur KoboToolbox mondial"
      fr_reason: "Missing definite article 'Le'"

ui_terms: [...]
form_building_terms: [...]
data_collection_terms: [...]
cross_language_rules: [...]
language_specific: [...]
```

### Categories

- **OFFICIAL**: Must use EXACT translation character-for-character
  - Brand names
  - UI elements
  - XLSForm technical terms

- **PREFERRED**: Can adapt for context
  - General terminology
  - Course content
  - Data collection concepts

### Adding New Terms

1. Determine category (OFFICIAL vs PREFERRED)
2. Add English source term
3. Add translations for all languages
4. Include usage notes
5. Document common pitfalls
6. Run sync script

## 🤖 Meta-Skill Generator Details

### How It Works

The `generate_arabic_guide.py` script:

1. **Loads** French and Spanish guides as templates
2. **Analyzes** patterns, structure, and style
3. **Calls Claude API** with comprehensive prompt:
   - Extracts translation patterns
   - Identifies language-specific sections
   - Learns from examples and pitfalls
4. **Generates** Arabic-specific content:
   - RTL text handling
   - Arabic punctuation (،, ؛, ؟)
   - Gender-inclusive strategies
   - Cultural adaptations
5. **Outputs** complete, ready-to-review content

### Customization

Edit the prompt in `generate_arabic_guide.py` to:
- Focus on specific sections
- Adjust tone and style
- Include additional context
- Change model parameters (temperature, max_tokens)

### Quality Considerations

**Generated content is a FIRST DRAFT**. Always:
- ✅ Have native speakers review
- ✅ Test with real translation tasks
- ✅ Verify cultural appropriateness
- ✅ Check technical accuracy
- ✅ Iterate based on feedback

## ✅ Validation System

### What It Checks

The validation system (`validate_guides.py`) ensures:

1. **Structural completeness**
   - All required sections present
   - Proper heading hierarchy
   - Required examples included

2. **Content quality**
   - Tables have no empty cells
   - Language-specific content appropriate
   - Examples show both ✅ CORRECT and ❌ WRONG

3. **Cross-references**
   - Internal links valid
   - Reference files exist
   - External links accessible

4. **Terminology consistency**
   - Terms match master database
   - No incorrect translations used
   - OFFICIAL vs PREFERRED followed

### Exit Codes

- `0`: All validations passed
- `1`: Errors found (or warnings in strict mode)

Use in CI/CD:
```bash
# In .github/workflows/validate-guides.yml
- name: Validate translation guides
  run: python scripts/validate_guides.py --strict
```

## 🔄 Maintenance Best Practices

### Regular Updates

```bash
# Weekly: Validate all guides
python scripts/validate_guides.py

# Monthly: Sync terminology
python scripts/sync_terminology.py --validate-only

# As needed: Re-generate when major changes occur
python scripts/generate_arabic_guide.py
```

### Version Control

**Always commit:**
- Master terminology changes
- Generated guide updates
- Validation reports

**Track:**
- When terms were added
- Why translations were chosen
- Decisions about OFFICIAL vs PREFERRED

### Documentation

Update this file when:
- Adding new workflows
- Supporting new languages
- Changing validation rules
- Updating scripts

## 🎓 Training New Contributors

### For Translation Experts

1. **Start here**: Read existing French/Spanish guides
2. **Understand categories**: OFFICIAL vs PREFERRED
3. **Learn the system**: Master terminology → Language guides
4. **Make changes**: Edit master YAML, run sync
5. **Validate**: Check with validation script

### For Developers

1. **Architecture**: Understand the three-script system
2. **API usage**: Set up Anthropic API key
3. **Testing**: Run scripts with --dry-run first
4. **CI/CD**: Integrate validation into pipelines

### For Language Coordinators

1. **Review process**: Generated → Expert review → Refinement
2. **Quality assurance**: Use validation checklists
3. **Feedback loop**: Iterate based on translator feedback
4. **Documentation**: Keep master terminology updated

## 📊 Scaling to More Languages

### Current Support
- ✅ French (comprehensive)
- ✅ Spanish (comprehensive)
- 🚧 Arabic (being expanded)

### Adding Language #4, #5, #6...

**Easy scaling** because:
1. Master terminology already complete
2. Validation framework in place
3. Generator can be adapted for any language
4. Structure proven across 3 languages

**Steps for new language**:
1. Add to `metadata.languages` in master YAML
2. Create `skills/kobo-translation-{lang}/` directory
3. Run sync to generate terminology
4. Create/adapt generator script
5. Have native experts review
6. Integrate into workflows

### Automation Opportunities

**Future enhancements**:
- Auto-detect terminology gaps
- Suggest translations based on patterns
- Generate diff reports when master changes
- Batch-update all languages simultaneously
- CI/CD integration with PR previews

## 🔧 Troubleshooting

### API Key Issues

```bash
# Error: ANTHROPIC_API_KEY not found
export ANTHROPIC_API_KEY='your-key-here'

# Or pass directly
python scripts/generate_arabic_guide.py --api-key your-key-here
```

### Empty Generated Content

**Cause**: Prompt too large, context exceeded
**Solution**: Use `--skill-only` or `--references-only` to generate in parts

### Validation Failures

```bash
# See details
python scripts/validate_guides.py --language ar

# Auto-fix where possible
python scripts/validate_guides.py --fix
```

### Merge Conflicts

When multiple people edit guides:
1. Use master terminology as truth
2. Re-generate from master
3. Manually merge custom sections
4. Validate after merge

## 📞 Support

**Issues?**
- Check validation output for specific errors
- Review generated content carefully
- Consult French/Spanish guides as examples
- Test with small changes first

**Questions?**
- Refer to this document
- Check script help: `python script.py --help`
- Review master terminology structure
- Examine existing guide examples

## 🎉 Success Metrics

**You'll know the system is working when:**
- ✅ Arabic guide is as comprehensive as French/Spanish
- ✅ Adding new terms takes minutes, not hours
- ✅ All languages stay synchronized
- ✅ Validation catches issues automatically
- ✅ New languages can be added quickly
- ✅ Quality remains high across all guides

## 📝 Next Steps

1. **Immediate**: Generate comprehensive Arabic guide
2. **Short-term**: Validate and refine all guides
3. **Medium-term**: Add remaining planned languages
4. **Long-term**: Fully automate with CI/CD integration

---

**Remember**: This system is designed to be **maintainable** and **scalable**. The upfront investment in structure pays off as you add more languages and terms.
