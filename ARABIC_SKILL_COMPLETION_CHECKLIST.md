# Arabic Translation Skill Completion Checklist

**Goal:** Complete `skills/kobo-translation-ar/` with all sections filled and validated

**Timeline:** 2-3 days with native speaker review

**Owner:** [Assign owner]  
**Reviewer:** [Assign native Arabic speaker]  
**Started:** [Date]  
**Target Completion:** [Date]

---

## Pre-Work (Before Starting)

### Resources Needed
- [ ] Native Arabic speaker identified and scheduled (8-16 hours)
- [ ] Access to KoboToolbox Arabic UI (Transifex or live interface)
- [ ] Time blocked for completion work (16-24 hours)
- [ ] Review time scheduled with native speaker

### Decision Points
- [ ] **Formality level decided:** Formal/Informal address for instructional content
- [ ] **Gender approach decided:** How to handle gender-inclusive language in Arabic
- [ ] **Dialect/register decided:** MSA vs. regional dialect preference
- [ ] **UI terminology source:** Using Transifex strings or defining new standards

---

## Phase 1: Extract Existing Terminology (2-3 hours)

### From Your Existing Arabic Docs

#### Brand Terms
Scan `docs/ar/about_kobotoolbox.md` and similar files:

- [ ] KoboToolbox → [Found: _____________]
- [ ] Community Forum → [Found: المنتدى]  
- [ ] Help Center → [Found: مركز المساعدة]
- [ ] Question Library → [Found: _____________]
- [ ] Formbuilder → [Found: _____________]
- [ ] Global Server → [Found: _____________]
- [ ] EU Server → [Found: _____________]

**File to update:** `references/brand-terminology.md`

#### UI Terms
Scan UI-related docs or check Transifex:

- [ ] FORM tab → [Found: _____________]
- [ ] DATA tab → [Found: _____________]
- [ ] DEPLOY button → [Found: _____________]
- [ ] Draft status → [Found: _____________]
- [ ] NEW button → [Found: _____________]

**File to update:** `references/ui-terminology.md`

#### Technical Terms  
Scan various docs:

- [ ] data collection → [Found: جمع البيانات]
- [ ] form building → [Found: _____________]
- [ ] survey/questionnaire → [Found: _____________]
- [ ] submission → [Found: _____________]
- [ ] deployment → [Found: _____________]
- [ ] skip logic → [Found: _____________]
- [ ] validation → [Found: _____________]

**Files to update:** Multiple reference files

#### Data Collection Terms
- [ ] record/response → [Found: _____________]
- [ ] upload → [Found: _____________]
- [ ] download → [Found: _____________]
- [ ] export → [Found: _____________]

**File to update:** `references/data-collection-terms.md`

---

## Phase 2: Fill Reference Files (4-6 hours)

### File 1: `references/brand-terminology.md`

**Current state:** Many empty tables

**Tasks:**
- [ ] Add Arabic column to "Most Frequently Misused Terms" table
- [ ] Add Arabic column to "Server Names" table  
- [ ] Add Arabic column to "Question Library" table
- [ ] Add Arabic column to "Formbuilder" table
- [ ] Add Arabic translations to "Core Brand Terms" table
- [ ] Update "Translation Examples" with Arabic examples
- [ ] Document any Arabic-specific rules for brand terms

**Validation:**
- [ ] All brand terms have Arabic translations
- [ ] Server names verified against actual usage
- [ ] No empty cells in tables
- [ ] Examples are correct and natural

---

### File 2: `references/ui-terminology.md`

**Current state:** Missing Arabic columns

**Tasks:**
- [ ] Add Arabic column to "Most Commonly Missed Capitalizations" table
- [ ] Add Arabic to "Formbuilder UI Terminology" tables
- [ ] Add Arabic to "KoboCollect UI Terminology" tables
- [ ] Document Arabic capitalization approach (since Arabic has no caps)
- [ ] Note how to handle Latin capitals (FORM, DATA, etc.)
- [ ] Add Arabic examples for UI translation

**Special considerations for Arabic:**
- [ ] Document that Arabic has no case distinction
- [ ] Explain how to handle all-caps UI terms
- [ ] Note any bold/emphasis conventions

**Validation:**
- [ ] All UI terms have Arabic equivalents
- [ ] Capitalization rules documented
- [ ] Verified against actual KoboToolbox Arabic UI
- [ ] Examples provided

---

### File 3: `references/form-building-terms.md`

**Current state:** [Check and document]

**Tasks:**
- [ ] Add Arabic translations for XLSForm terms
- [ ] Document whether Arabic uses "English + translation" pattern
- [ ] Add cascading select terminology
- [ ] Include examples

---

### File 4: `references/question-types.md`

**Current state:** [Check and document]

**Tasks:**
- [ ] Add Arabic translations for question types
- [ ] Add Arabic for question appearances
- [ ] Document how to handle technical terms

---

### File 5: `references/data-collection-terms.md`

**Current state:** [Check and document]

**Tasks:**
- [ ] Add Arabic translations for data collection concepts
- [ ] Document context-specific usage rules
- [ ] Include examples

---

### File 6: `references/course-terminology.md`

**Current state:** [Check and document]

**Tasks:**
- [ ] Add Arabic translations for learning platform terms
- [ ] Document any platform-specific conventions
- [ ] Include examples

---

## Phase 3: Complete Main SKILL.md (4-6 hours)

### Section 1: Overview (Lines 1-55)

**Current state:** Mostly complete but references other languages

**Tasks:**
- [ ] Update description to focus on "English to Arabic"
- [ ] Remove French/Spanish examples if not relevant
- [ ] Ensure overview is clear for Arabic translators

---

### Section 2: Gender-Inclusive Language (Lines 155-159)

**Current state:** Says "[To be specified based on project needs]"

**THIS REQUIRES NATIVE SPEAKER INPUT**

**Tasks:**
- [ ] Schedule session with native speaker to discuss:
  - [ ] How to handle gender in Arabic translations
  - [ ] Whether dual/plural forms are appropriate
  - [ ] Cultural considerations for your audience
  - [ ] Examples of inclusive language in Arabic
- [ ] Document agreed-upon approach
- [ ] Provide at least 3 examples
- [ ] Add to quality checklist

**Possible approaches to discuss:**
1. Use plural forms which can be gender-neutral
2. Use dual forms when addressing two genders
3. Use masculine as default (traditional approach)
4. Use both forms explicitly when relevant
5. Context-dependent strategy

---

### Section 3: Arabic-Specific Rules

**Current state:** Partially covered but needs expansion

**Tasks:**

#### RTL (Right-to-Left) Handling
- [ ] Document `<section dir="rtl">` wrapper requirement
- [ ] Explain heading placement within RTL sections
- [ ] Show examples from existing docs
- [ ] Note: Links stay outside RTL sections

**Example to add:**
```markdown
### Arabic-Specific: RTL Text Direction

All Arabic content must be wrapped in RTL sections:

\`\`\`html
<section dir="rtl">
<h1 id="ar">العنوان بالعربية</h1>

المحتوى هنا...
</section>
\`\`\`

**Critical rules:**
- Cross-language links go OUTSIDE the RTL section
- Heading IDs remain: `<h1 id="ar">`
- Code blocks and technical content may need special handling
```

#### Capitalization
- [ ] Document that Arabic has no uppercase/lowercase
- [ ] Explain how to handle Latin terms (KoboToolbox, FORM, DATA)
- [ ] Note bold/emphasis alternatives

**Example to add:**
```markdown
### Arabic-Specific: Capitalization

Unlike French and Spanish, Arabic has no capital/lowercase distinction.

**For Latin terms:**
- Brand names: Keep original (KoboToolbox, Kobo)
- UI elements: Keep capitals (FORM, DATA, DEPLOY)
- Acronyms: Keep as-is (API, CSV, GPS)

**For emphasis:**
- Use **bold** instead of capitals
- Or use larger font size
- Or use different color (in UI contexts)
```

#### Numbers and Dates
- [ ] Document which numerals to use (Arabic-Indic ٠١٢٣ or Western 0123)
- [ ] Document date format convention
- [ ] Provide examples

---

### Section 4: Common Translation Pitfalls

**Current state:** Has French/Spanish examples

**Tasks:**
- [ ] Add "Arabic-Specific Pitfalls" section
- [ ] Document common errors Arabic translators make
- [ ] Provide ❌ Wrong / ✅ Correct examples in Arabic

**Potential pitfalls to document:**
- Literal vs. natural translation
- Over-formality or under-formality
- Gender agreement issues
- Preposition choices
- Verb tense consistency

---

### Section 5: Translation Examples

**Current state:** Has FR/ES examples

**Tasks:**
- [ ] Add Arabic examples to existing ones
- [ ] Create Arabic-specific example section
- [ ] Show before/after translations
- [ ] Highlight key decision points

---

### Section 6: Quality Checklist

**Current state:** Generic checklist

**Tasks:**
- [ ] Add Arabic-specific checklist items:
  - [ ] RTL wrapping applied correctly
  - [ ] Gender approach applied consistently  
  - [ ] Formality level appropriate
  - [ ] Numbers/dates formatted correctly
  - [ ] Latin terms handled properly
  - [ ] Natural phrasing (not too literal)

---

## Phase 4: Native Speaker Review (4-8 hours)

### Preparation for Reviewer

**Send reviewer:**
- [ ] Complete draft of SKILL.md
- [ ] All 6 reference files
- [ ] Sample translation using the guide
- [ ] Specific questions/concerns
- [ ] Review checklist (below)

### Reviewer Checklist

**For the reviewer to verify:**

#### Terminology Accuracy
- [ ] All brand terms accurate and consistent
- [ ] UI terminology matches KoboToolbox Arabic interface
- [ ] Technical terms are industry-standard
- [ ] No awkward or unnatural phrasings

#### Language Quality
- [ ] Appropriate formality level throughout
- [ ] Gender-inclusive language approach is culturally appropriate
- [ ] Examples are clear and natural
- [ ] Grammar and syntax are correct

#### Completeness
- [ ] All sections filled (no placeholders)
- [ ] All tables have Arabic columns
- [ ] Examples provided where needed
- [ ] Arabic-specific rules documented

#### Cultural Appropriateness
- [ ] No culturally insensitive language
- [ ] Appropriate for international audience
- [ ] Respects regional variations where relevant
- [ ] Suitable for professional/technical context

#### Usability
- [ ] Can a translator use this guide independently?
- [ ] Are the examples helpful?
- [ ] Are the rules clear and unambiguous?
- [ ] Is the structure logical?

---

## Phase 5: Incorporate Feedback (2-4 hours)

### Review Session

**During review meeting:**
- [ ] Go through reviewer's comments systematically
- [ ] Discuss any disagreements or ambiguities
- [ ] Prioritize changes (critical vs. nice-to-have)
- [ ] Assign owners for each change

### Implementation

- [ ] Make all critical changes
- [ ] Make high-priority improvements
- [ ] Update examples based on feedback
- [ ] Re-check all modified sections

### Validation

- [ ] Reviewer approves final version
- [ ] Spot-check against actual translations
- [ ] Verify all changes incorporated

---

## Phase 6: Testing & Finalization (2-4 hours)

### Real-World Test

**Pick a sample English article:**
- [ ] Choose mid-complexity article from docs/en/
- [ ] Have someone translate it using ONLY the Arabic skill guide
- [ ] Document any confusion or missing information
- [ ] Make final adjustments

**Test translation for:**
- [ ] Completeness (could translator finish without asking questions?)
- [ ] Consistency (did they use correct terminology?)
- [ ] Quality (is output up to your standards?)
- [ ] Efficiency (did guide help or hinder?)

### Final Checklist

- [ ] All reference files 100% complete
- [ ] Main SKILL.md has no placeholders
- [ ] Native speaker approval obtained
- [ ] Test translation successful
- [ ] Documentation clear and usable
- [ ] Files committed to repository
- [ ] Team notified of completion

---

## Success Metrics

### Quantitative
- [ ] 0 empty tables in reference files
- [ ] 0 "[To be specified]" placeholders
- [ ] 100% of terminology extracted from existing docs
- [ ] Native speaker confidence rating: ____/10

### Qualitative  
- [ ] Reviewer: "This guide is comprehensive" ✅/❌
- [ ] Test translator: "I could work independently" ✅/❌
- [ ] Team: "Quality meets our standards" ✅/❌
- [ ] Sustainable: "Easy to update/maintain" ✅/❌

---

## Post-Completion

### Documentation
- [ ] Update main `kobo-translation` skill description to note Arabic is complete
- [ ] Add Arabic examples to main skill where appropriate
- [ ] Document lessons learned for next language
- [ ] Create "How to add a new language" guide based on this experience

### Communication
- [ ] Announce completion to translation team
- [ ] Brief translators on how to use the guide  
- [ ] Gather feedback after first few uses
- [ ] Make iterative improvements

### Maintenance Plan
- [ ] Assign long-term owner for Arabic skill
- [ ] Schedule quarterly reviews
- [ ] Set up process for updates when English terms change
- [ ] Plan how to propagate improvements to other language skills

---

## Blockers & Issues Log

**Use this section to track problems as they arise:**

| Date | Issue | Owner | Resolution | Status |
|------|-------|-------|------------|--------|
| [Date] | Can't find Arabic UI strings | [Name] | Accessed Transifex | ✅ Resolved |
| [Date] | Gender approach unclear | [Name] | Consulted native speaker | ⏳ In progress |
|  |  |  |  |  |

---

## Resources & References

### Existing Files to Reference
- `docs/ar/about_kobotoolbox.md` - Brand terms, RTL examples
- `docs/ar/formbuilder.md` - Technical terminology
- `skills/kobo-translation-fr/` - Structure reference
- `skills/kobo-translation-es/` - Structure reference

### External Resources
- KoboToolbox Arabic UI (Transifex)
- UN Arabic style guide (if applicable)
- Your organization's Arabic style guide
- Arabic localization best practices

### Tools Available
- `scripts/extract_arabic_terminology.py` - Automated extraction
- Claude for gap-filling (if using LLM approach)
- Comparison with FR/ES patterns

---

## Time Tracking

**Actual time spent (update as you go):**

| Phase | Estimated | Actual | Notes |
|-------|-----------|--------|-------|
| Pre-work | 1 hour | ___ hours | |
| Phase 1: Extract | 2-3 hours | ___ hours | |
| Phase 2: Reference files | 4-6 hours | ___ hours | |
| Phase 3: Main SKILL.md | 4-6 hours | ___ hours | |
| Phase 4: Native review | 4-8 hours | ___ hours | |
| Phase 5: Feedback | 2-4 hours | ___ hours | |
| Phase 6: Testing | 2-4 hours | ___ hours | |
| **Total** | **19-32 hours** | **___ hours** | |

---

## Sign-off

### Completion Approval

**I certify that:**
- [ ] All sections are complete
- [ ] Native speaker has reviewed and approved
- [ ] Testing has been performed successfully
- [ ] Documentation is ready for production use

**Completed by:** _________________  
**Date:** _________________

**Native Reviewer:** _________________  
**Date:** _________________

**Final Approver:** _________________  
**Date:** _________________

---

## Next Language Planning

**Based on this experience, for the next language we should:**

1. What worked well:
   - 
   -
   -

2. What could be improved:
   -
   -
   -

3. Estimated time for next language: ___ hours

4. Process improvements to implement:
   -
   -
   -

---

Ready to start? Print this checklist and work through it systematically. Update it as you go to track progress and document learnings for the next language!
