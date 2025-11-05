# Next Steps: Completing the Arabic Translation Skill

## Quick Summary

**Problem:** Your Arabic translation skill (`kobo-translation-ar/`) has many incomplete sections, but you have 109 high-quality Arabic documentation files.

**Solution:** Extract patterns and terminology from existing translations to complete the skill guide.

**Time to Complete:** 2-3 days with the approach below.

---

## Option 1: Quick Manual Completion (Recommended)

If you need the Arabic skill completed quickly without building full automation:

### Step 1: Use Existing Translations as Reference (1-2 hours)

The good news: Your Arabic docs already demonstrate best practices. Let's extract them systematically.

**Key files to reference:**
- `docs/ar/about_kobotoolbox.md` - Good example of brand terms, RTL wrapping
- `docs/ar/formbuilder.md` - Technical terminology 
- `docs/ar/question_library.md` - UI terminology

**What to extract:**

#### Brand Terms Already in Use:
```yaml
KoboToolbox: KoboToolbox (unchanged)
Community Forum: المنتدى
Help Center: مركز المساعدة
data collection: جمع البيانات
social impact organizations: منظمات التأثير الاجتماعي
```

#### UI Terms Already in Use:
Look for Arabic equivalents of:
- FORM tab
- DATA tab
- Deploy button
- Draft status
- NEW button

#### Technical Terms Already in Use:
- survey/form: استبيان/نموذج
- submission: تقديم
- project: مشروع

### Step 2: Compare with French/Spanish Patterns (1 hour)

For each section in the French/Spanish skills that's missing in Arabic:

1. **Identify the pattern** (e.g., "First reference rule for Formbuilder")
2. **Check if it applies to Arabic** (e.g., does Arabic need English in parentheses?)
3. **Adapt or create equivalent rule**

**Example:**

French has: "Question Library" → "**La** bibliothèque de questions" (capital L)

Spanish has: "Question Library" → "**La** biblioteca de preguntas" (capital L)

Arabic should have: "Question Library" → Check your docs for how it's translated, then document the rule.

### Step 3: Fill Specific Gaps (2-3 hours)

#### A. Brand Terminology Reference (`references/brand-terminology.md`)

Currently has many empty tables. Fill with:

```markdown
### Server Names - USE EXACTLY AS SHOWN

| English | French | Spanish | Arabic | Notes |
|---------|--------|---------|--------|-------|
| Global KoboToolbox Server | Le serveur KoboToolbox mondial | Servidor Global | [CHECK DOCS] | |
| European Union KoboToolbox Server | Le serveur KoboToolbox Union européenne | Servidor con sede en la Unión Europea | [CHECK DOCS] | |
```

**Action:** Search your Arabic docs for "Global" or "Server" to find how they translate these.

#### B. UI Terminology Reference (`references/ui-terminology.md`)

Currently incomplete. Add Arabic column to tables:

```markdown
### Most Commonly Missed Capitalizations

| Term | Context | French | Spanish | Arabic | Common Error |
|------|---------|--------|---------|--------|--------------|
| Draft | UI element | **Brouillon** | **Borrador** | [TO ADD] | |
```

**Action:** Check your Arabic docs or KoboToolbox Arabic UI in Transifex.

#### C. Gender-Inclusive Language Section (in main SKILL.md)

Currently says: "**Arabic:** [To be specified based on project needs]"

**Needs:**
- How to handle gender in Arabic translations
- Examples of inclusive language
- Regional considerations (MSA vs. dialects)

**This requires a native Arabic speaker** who understands:
- Modern Standard Arabic conventions
- Gender neutrality in Arabic (or lack thereof)
- Cultural considerations for your audience

### Step 4: Document Arabic-Specific Rules (1-2 hours)

Add sections that are unique to Arabic:

#### RTL (Right-to-Left) Handling
```markdown
### Arabic-Specific Rules

**RTL Text Direction:**
- Wrap Arabic content in `<section dir="rtl">` tags
- Keep heading IDs: `<h1 id="ar">`
- Cross-reference links stay OUTSIDE the RTL section
- Example from existing docs: [show snippet from about_kobotoolbox.md]
```

#### Capitalization
```markdown
**Capitalization:**
- Arabic doesn't have capital/lowercase distinction
- Emphasis through bold or styling instead
- Latin terms (KoboToolbox, FORM, DATA) keep original casing
```

#### Number and Date Formatting
```markdown
**Numbers:**
- Arabic-Indic numerals (٠١٢٣٤٥٦٧٨٩) vs. Western numerals (0123456789)
- [Specify which your docs use - check existing files]

**Dates:**
- Format: DD/MM/YYYY or [check your convention]
- Month names: [Document if using Arabic or English month names]
```

### Step 5: Native Speaker Review (4-8 hours)

**Critical:** Even with extracted patterns, you need a native Arabic speaker who:
1. Understands technical/software terminology
2. Can review for:
   - Natural phrasing
   - Appropriate formality level
   - Gender considerations
   - Cultural appropriateness

**Review checklist for them:**
- [ ] All brand terms accurate and consistent
- [ ] UI terminology matches KoboToolbox Arabic interface
- [ ] Gender-inclusive language section is appropriate
- [ ] Examples are natural and clear
- [ ] No culturally insensitive language
- [ ] RTL implementation rules are correct

---

## Option 2: Use LLM-Assisted Generation (Faster but Requires Review)

Since you have 109 existing Arabic docs, you can use Claude to help:

### Prompt Template for Claude:

```
I have a translation skill guide for French and Spanish translations of KoboToolbox 
documentation. I need to create an equivalent guide for Arabic.

Here are the sections from the French/Spanish guide:
[paste relevant section]

Here are examples of how these terms appear in existing Arabic translations:
[paste snippets from docs/ar/]

Please generate the equivalent section for the Arabic translation skill, including:
1. The Arabic translations of the terms
2. Any Arabic-specific rules that differ from French/Spanish
3. Common pitfalls to avoid when translating to Arabic

Maintain the same structure and format as the French/Spanish examples.
```

### Sections to Generate with LLM:

1. **Brand terminology table** (fill in Arabic column)
2. **UI terminology table** (fill in Arabic column)
3. **Gender-inclusive language rules** (adapted for Arabic)
4. **Common translation pitfalls** (with Arabic examples)
5. **Translation decision tree** (adapted for Arabic)

### After LLM Generation:

**Still need human review** for:
- Accuracy of extracted terms
- Appropriateness of rules
- Completeness of coverage
- Cultural sensitivity

---

## Option 3: Run the Extraction Script (Most Thorough)

If you want a data-driven approach:

### Setup

```bash
cd /workspace
pip install pyyaml
python scripts/extract_arabic_terminology.py
```

This will:
1. Compare English and Arabic docs systematically
2. Extract consistently-used translations
3. Calculate confidence scores
4. Generate completion report
5. Export structured data

### Use the Output

The script generates:
- `extracted_terminology.yaml` - Machine-readable term database
- `COMPLETION_REPORT.md` - Shows what's missing
- Confidence scores for each term

### Then Fill Gaps

Use the extracted data to populate:
1. Brand terminology reference
2. UI terminology reference  
3. Examples in main SKILL.md

---

## Recommended Hybrid Approach

**For fastest, highest-quality results:**

1. **Day 1 Morning:** Run extraction script to get data
2. **Day 1 Afternoon:** Use LLM to generate initial fills for empty sections
3. **Day 2 Morning:** Manual review and refinement
4. **Day 2 Afternoon:** Native speaker review (most critical step!)
5. **Day 3:** Incorporate feedback and finalize

---

## Resources You Already Have

### Existing Arabic Docs (Great Reference!)
- ✅ 109 translated articles in `docs/ar/`
- ✅ Consistent terminology usage
- ✅ Proper RTL implementation
- ✅ Real-world examples

### Existing Skills (Templates!)
- ✅ Comprehensive French guide
- ✅ Comprehensive Spanish guide
- ✅ 6 reference files per language
- ✅ Proven structure

### What You're Missing
- ❌ Complete Arabic terminology tables
- ❌ Arabic-specific rules documented
- ❌ Gender-inclusive language guidance
- ❌ Common pitfalls section

---

## Key Questions for Your Team

Before starting, clarify:

### 1. **Terminology Authority**
- Do you have official Arabic UI strings from Transifex?
- Should we match existing KoboToolbox Arabic interface exactly?
- Or can we improve/standardize based on best practices?

### 2. **Target Audience**
- Modern Standard Arabic (MSA) or specific dialect?
- Regional preferences (Gulf, Levantine, North African)?
- Technical expertise level of readers?

### 3. **Formality Level**
- Spanish courses use informal "tú"
- French courses use formal "vous"
- Arabic should use [formal/informal address]?

### 4. **Gender Inclusivity**
- How important is gender-neutral language?
- What are culturally appropriate strategies in Arabic?
- Any organizational policies to follow?

### 5. **Review Resources**
- Who can do technical Arabic review?
- Timeline for review (days? weeks?)
- Process for incorporating feedback?

---

## Immediate Action Items

### This Week:

1. **Assign owner** for Arabic skill completion
2. **Identify native Arabic speaker** for review
3. **Decide approach:** Manual, LLM-assisted, or script-based
4. **Block time:** 8-16 hours for initial work + review time

### This Month:

5. **Complete Arabic skill** with all sections filled
6. **Test with sample translation** to validate guide works
7. **Incorporate feedback** from reviewers
8. **Document lessons learned** for next language

---

## Success Criteria

A completed Arabic translation skill should have:

- [ ] All terminology tables filled (no empty rows)
- [ ] Arabic-specific rules documented (RTL, gender, formality)
- [ ] Real examples from your docs referenced
- [ ] Common pitfalls section with Arabic examples
- [ ] Quality checklist adapted for Arabic
- [ ] Native speaker approval
- [ ] Tested with actual translation work

---

## Long-Term: Preventing This Problem

See `TRANSLATION_SKILL_ARCHITECTURE.md` for a scalable solution that:

1. **Extracts patterns automatically** from existing translations
2. **Generates complete skills** for new languages in days not weeks
3. **Maintains consistency** as terminology evolves
4. **Scales efficiently** to 5, 10, or 20 languages

**Investment:** 2-3 weeks to build framework
**ROI:** Save 2-3 weeks per language thereafter
**Break-even:** After 2nd new language

---

## Questions or Need Help?

If you want me to:
- Extract specific terminology from your Arabic docs
- Generate LLM prompts for missing sections
- Draft Arabic-specific rules based on patterns
- Review what you've completed so far

Just ask! I can assist with any part of this process.

---

## Appendix: Quick Reference

### Key Arabic Terms Already in Your Docs

From `docs/ar/about_kobotoolbox.md`:
- "data collection" = "جمع البيانات"
- "social impact" = "التأثير الاجتماعي"
- "Community Forum" = "المنتدى"
- "Help Center" = "مركز المساعدة"

From your docs structure:
- Consistent RTL wrapping: `<section dir="rtl">`
- Last Updated preserved in English (correct approach)
- Cross-language links outside RTL sections (correct)

### Comparison with French/Spanish

| Aspect | French | Spanish | Arabic (Current) | Arabic (Needs) |
|--------|--------|---------|------------------|----------------|
| Articles | Critical (Le/La) | Critical (La) | N/A | Document ال usage |
| Gender | Dual forms | Dual forms | [Undefined] | Define approach |
| Formality | Formal (vous) | Informal (tú) | [Undefined] | Define level |
| Capitalization | First word only | First word only | N/A | Note Latin terms |
| RTL | N/A | N/A | Implemented | Document rules |

### Files to Complete

Priority order:

1. `skills/kobo-translation-ar/SKILL.md`
   - Fill gender-inclusive language section
   - Complete Arabic-specific rules
   - Add more examples

2. `skills/kobo-translation-ar/references/brand-terminology.md`
   - Add Arabic column to all tables
   - Verify with UI strings

3. `skills/kobo-translation-ar/references/ui-terminology.md`
   - Add Arabic column to all tables
   - Document capitalization approach

4. Other reference files
   - form-building-terms.md
   - question-types.md
   - data-collection-terms.md
   - course-terminology.md

---

Ready to start? Pick an option above and let me know if you need any assistance!
