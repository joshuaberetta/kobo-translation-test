# Translation Skill Architecture & Maintenance Strategy

## Executive Summary

This document outlines a scalable system for creating and maintaining high-quality translation skills for KoboToolbox documentation across multiple languages.

**Current Challenge:** Your team has excellent French and Spanish translation guides, but the Arabic guide is incomplete. As you expand to more languages, manually creating and maintaining each language-specific guide becomes unsustainable.

**Solution:** A three-tier meta-skill architecture that:
1. Generates new language guides from patterns in existing ones
2. Maintains consistency as terminology expands
3. Scales efficiently to additional languages

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    TIER 1: Master Template                       │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  • Universal translation principles                     │    │
│  │  • Formatting rules (markdown, links, HTML)            │    │
│  │  • Brand term handling patterns                        │    │
│  │  • Quality checklists                                  │    │
│  └────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│           TIER 2: Language-Specific Generation                   │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  Script: generate_language_skill.py                    │    │
│  │  • Extracts terminology from existing translations     │    │
│  │  • Identifies language-specific patterns               │    │
│  │  • Generates complete skill + reference files          │    │
│  │  • Uses LLM to fill knowledge gaps                     │    │
│  └────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│        TIER 3: Quality & Consistency Maintenance                 │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  • Terminology sync checks                             │    │
│  │  • Cross-language validation                           │    │
│  │  • Update propagation system                           │    │
│  │  • Quality metrics & reporting                         │    │
│  └────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Tier 1: Master Translation Template

### Purpose
Extract universal patterns from French/Spanish guides that apply to ALL languages.

### Location
`skills/kobo-translation-template/`

### Components

#### 1. **MASTER_TEMPLATE.md**
Contains language-agnostic rules:
- Localization over literal translation
- Consistency principles
- Formatting rules (HTML → markdown, links, images)
- Quality checklist framework

#### 2. **reference-templates/**
Template structure for each reference file type:
- `brand-terminology.template.md` - How to handle brand terms
- `ui-terminology.template.md` - UI capitalization patterns
- `form-building-terms.template.md` - Technical term patterns
- etc.

#### 3. **patterns.yaml**
Machine-readable patterns extracted from existing skills:
```yaml
brand_terms:
  pattern: "Official translations, use EXACTLY"
  examples:
    - "KoboToolbox servers"
    - "Question Library"
  
formatting_rules:
  html_headings: "Convert <h2> to ##, <h3> to ###"
  internal_links: "Keep relative, auto-resolve"
  cross_language_links: "Use ../lang/ structure"
```

---

## Tier 2: Language-Specific Generation

### Purpose
Generate complete, high-quality language-specific skills from the master template plus existing translations.

### Script: `scripts/generate_language_skill.py`

### How It Works

#### Step 1: Terminology Extraction
```python
# Scan existing docs/ar/ translations
# Compare with docs/en/ originals
# Build terminology database:

terminology = {
    "KoboToolbox": "KoboToolbox",  # unchanged
    "data collection": "جمع البيانات",
    "Community Forum": "المنتدى",
    # ... extracted from 109+ Arabic docs
}
```

#### Step 2: Pattern Analysis
```python
# Identify language-specific patterns:
- RTL text direction
- Article usage patterns
- Gender handling
- Formality level (tu/vous/usted equivalent)
- Capitalization conventions
```

#### Step 3: LLM-Assisted Generation
For gaps in extracted data, use Claude with structured prompts:
```
Given these Arabic translations of KoboToolbox terms:
[extracted terminology]

And these patterns from Spanish/French:
[pattern examples]

Generate Arabic-specific rules for:
1. Gender-inclusive language
2. Technical term formality
3. Common translation pitfalls
```

#### Step 4: Quality Validation
- Check completeness of all sections
- Validate terminology consistency
- Compare with existing translations
- Flag uncertain translations for human review

### Output
```
skills/kobo-translation-[LANG]/
├── SKILL.md (complete, with all sections filled)
└── references/
    ├── brand-terminology.md (with language column populated)
    ├── ui-terminology.md
    ├── data-collection-terms.md
    ├── form-building-terms.md
    ├── question-types.md
    └── course-terminology.md
```

---

## Tier 3: Quality & Consistency Maintenance

### Challenge
When new terms are added to English docs:
- How do you know which language skills need updates?
- How do you maintain consistency across 4+ languages?
- How do you prevent terminology drift?

### Solution Components

#### 1. **Terminology Sync Checker**
`scripts/check_terminology_sync.py`

Compares terminology across all language skills:
```bash
$ python scripts/check_terminology_sync.py

⚠️  Found 3 terms in EN not yet in AR:
  - "Question Library" (missing Arabic translation)
  - "Formbuilder" (present but needs first-reference rule)
  - "REST Services" (completely missing)

✅ ES: All terms synced
✅ FR: All terms synced
```

#### 2. **Cross-Language Validation**
`scripts/validate_translations.py`

Checks for common mistakes:
```python
def validate_brand_terms(lang_code):
    """
    Validate that OFFICIAL terms match exactly
    Check capitalization rules
    Verify article usage (French: "Le serveur...", Spanish: "Servidor...")
    """
    
def validate_formatting(lang_code):
    """
    Check HTML → markdown conversion
    Verify link structure
    Check RTL wrapping (Arabic)
    """
```

#### 3. **Update Propagation System**
When English base docs change:

```yaml
# .github/workflows/translation-check.yml
on: 
  push:
    paths: ['docs/en/**']

jobs:
  check-translations:
    - name: Extract new/changed terms
    - name: Check if terms exist in language skills
    - name: Create issue if missing
    - name: Suggest translations from similar terms
```

#### 4. **Quality Metrics Dashboard**
`scripts/generate_quality_report.py`

Produces metrics:
- Translation coverage per language
- Terminology consistency score
- Common error patterns
- Skills needing updates

Output:
```markdown
## Translation Quality Report - 2024-11-05

| Language | Skill Completeness | Term Coverage | Last Updated |
|----------|-------------------|---------------|--------------|
| French   | 100%              | 156/156 terms | 2024-10-15   |
| Spanish  | 100%              | 156/156 terms | 2024-10-15   |
| Arabic   | 73%               | 114/156 terms | 2024-09-01   |

### Action Items:
1. 🔴 HIGH: Update Arabic brand-terminology.md (42 missing terms)
2. 🟡 MED: Add gender-inclusive rules for Arabic
3. 🟢 LOW: Review Portuguese terminology (future language)
```

---

## Implementation Roadmap

### Phase 1: Complete Arabic Skill (Immediate - Week 1)
**Goal:** Generate a complete, high-quality Arabic translation skill

**Tasks:**
1. Create master template from ES/FR patterns
2. Run terminology extraction on existing Arabic docs
3. Use LLM to fill knowledge gaps
4. Human review and refinement
5. Test with sample translations

**Outcome:** Complete `skills/kobo-translation-ar/` with all sections filled

### Phase 2: Validation & Quality Tools (Week 2-3)
**Goal:** Ensure consistency and catch errors

**Tasks:**
1. Build terminology sync checker
2. Create cross-language validator
3. Set up automated quality reports
4. Document common pitfalls per language

**Outcome:** Confidence that all languages are consistent

### Phase 3: Scalability Framework (Week 4)
**Goal:** Make adding new languages efficient

**Tasks:**
1. Finalize generation script
2. Create language addition guide
3. Set up update propagation
4. Train team on maintenance

**Outcome:** Can add Portuguese/Swahili/etc. in days, not months

---

## Maintenance Best Practices

### When Adding New English Terms

1. **Update Master Template First**
   - Add term to appropriate reference template
   - Document any special rules

2. **Run Sync Checker**
   ```bash
   python scripts/check_terminology_sync.py --new-term "REST Services"
   ```

3. **Get Translations**
   - Use generation script for first pass
   - Request review from language experts
   - Add to all language-specific skills

4. **Validate**
   ```bash
   python scripts/validate_translations.py --all-languages
   ```

### Quarterly Reviews

Every 3 months:
1. Run full quality report
2. Review translation consistency
3. Update common pitfalls documentation
4. Refine generation scripts based on lessons learned

### When Adding New Language

1. **Prerequisites Check**
   - At least 50 translated documentation files
   - Native speaker available for review
   - UI translations in Transifex

2. **Generate Initial Skill**
   ```bash
   python scripts/generate_language_skill.py --language pt --name Portuguese
   ```

3. **Human Review Cycle**
   - Technical translator reviews
   - Native speaker reviews
   - Test with actual translations

4. **Production Ready**
   - All sections complete
   - Quality validation passes
   - Added to main kobo-translation skill description

---

## Benefits of This Architecture

### For Your Team
✅ **Faster**: Generate complete language skills in hours, not weeks
✅ **Consistent**: Automated checks prevent terminology drift
✅ **Scalable**: Adding new languages becomes straightforward
✅ **Maintainable**: Clear ownership and update procedures

### For Translation Quality
✅ **Comprehensive**: No more incomplete sections
✅ **Accurate**: Terminology extracted from actual usage
✅ **Validated**: Cross-checks against existing translations
✅ **Living**: Easy to update as needs evolve

### For Arabic Specifically
✅ **Immediate**: Can generate complete guide using existing translations
✅ **Accurate**: 109 existing docs provide rich terminology database
✅ **Expert-Level**: LLM fills gaps based on linguistic patterns
✅ **Reviewable**: Clear sections for native speaker validation

---

## Technical Requirements

### Tools Needed
- Python 3.8+
- Libraries: `pyyaml`, `anthropic` (for Claude API), `pandas`, `gitpython`
- Claude API access (for LLM-assisted generation)
- Git for version control

### Infrastructure
- GitHub Actions for automation (optional but recommended)
- Documentation review workflow
- Translation memory system (future enhancement)

### Skills Needed
- Python scripting
- YAML/Markdown manipulation
- LLM prompt engineering
- Translation/localization knowledge (for review)

---

## Cost-Benefit Analysis

### Time Investment
- **Setup**: 2-3 weeks for full framework
- **Arabic completion**: 2-3 days with tool assistance
- **Maintenance**: ~4 hours/month across all languages

### Ongoing Costs
- Claude API: ~$5-20/month (for new language generation)
- Developer time: Reduced by 80% compared to manual approach
- Quality assurance: Same or better with automated checks

### ROI
**Without framework:**
- Manual Arabic skill: 2-3 weeks
- Future languages: 2-3 weeks each
- Maintenance: Inconsistent, error-prone
- Total for 3 more languages: ~10 weeks

**With framework:**
- Arabic skill: 2-3 days (with review)
- Future languages: 3-5 days each (with review)
- Maintenance: Automated detection, targeted fixes
- Total for 3 more languages: ~2 weeks

**Savings: 8 weeks of expert time (~$20-40k value)**

---

## Next Steps

### Immediate Actions (This Week)
1. Review this architecture with your team
2. Prioritize which components to build first
3. Allocate resources (dev time, API access, reviewers)

### Quick Win (Arabic Completion)
If you need the Arabic skill completed ASAP:
1. I can extract terminology from your existing docs
2. Generate complete reference files
3. Use patterns from French/Spanish to fill gaps
4. Provide a complete draft for native speaker review

**Timeline: 24-48 hours for first draft**

### Questions to Discuss
1. Who will maintain the master template?
2. What's your budget for Claude API usage?
3. Do you have native Arabic speakers for review?
4. Which language should we add next after Arabic?
5. How often do English base docs add new terms?

---

## Appendix: Terminology Extraction Examples

### From Existing Arabic Docs

Extracted from `docs/ar/about_kobotoolbox.md`:
```yaml
English: "data collection"
Arabic: "جمع البيانات"
Context: "data collection practitioners" → "ممارسي جمع البيانات"
Confidence: HIGH (appears 3+ times)

English: "Community Forum"  
Arabic: "المنتدى"
Context: UI element name
Confidence: HIGH (official term)

English: "Help Center"
Arabic: "مركز المساعدة"  
Context: UI element name
Confidence: HIGH (official term)
```

### Pattern Analysis

**Gender Inclusivity:**
- Spanish uses: "los/as usuarios/as" (dual forms)
- French uses: "utilisatrices et utilisateurs" (both forms)
- Arabic needs: [To be determined with native speaker]
  - Possible: dual/plural forms
  - Or: gender-neutral terms where applicable

**Formality Level:**
- Spanish courses: informal "tú"
- French courses: formal "vous"  
- Arabic needs: [To be determined]
  - Likely: formal address for instructional content
  - Consider regional variations (MSA vs. dialects)

**RTL-Specific Rules:**
- Arabic docs use: `<section dir="rtl">` wrapping
- Heading structure maintained
- Links stay outside RTL sections
- Already implemented correctly in existing docs

---

## Conclusion

This meta-skill architecture transforms translation guide maintenance from a manual, inconsistent process into a **scalable, automated system** that:

1. ✅ Generates complete Arabic skill immediately
2. ✅ Maintains quality across all languages  
3. ✅ Scales efficiently to new languages
4. ✅ Reduces maintenance burden by 80%

The investment in this framework pays dividends with every new language added and every terminology update required.

**Ready to implement?** Let me know which phase you'd like to start with, and I can begin building the tools.
