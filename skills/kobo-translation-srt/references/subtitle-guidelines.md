# Subtitle Translation Guidelines

## Character Limits and Timing

### Reading Speed Standards

**Comfortable reading speed:**
- 15-20 characters per second
- For a 3-second subtitle: 45-60 characters maximum
- Ideal: Stay under 42 characters per line

### Line Breaking Rules

**Break at natural pauses:**
- Between clauses
- After prepositions when possible
- At punctuation marks

**Good line breaks:**
```
Line 1: "To create a new form,"
Line 2: "click on the NEW button."
```

**Bad line breaks:**
```
Line 1: "To create a new form, click on the"
Line 2: "NEW button."
```

### Single vs Double Line

**Single line (preferred when possible):**
- Faster to read
- Less visual clutter
- Use when subtitle text is under 42 characters

**Double line (when needed):**
- Split at natural pauses
- Keep each line under 42 characters
- Balance line lengths when possible

## Compression Techniques

### Remove Redundancy

**Before:**
"Now we're going to go ahead and click on the NEW button here"

**After:**
"Click on NEW"

### Use Active Voice

**Before:**
"The form will be created by clicking this button"

**After:**  
"This button creates the form"

### Simplify Structures

**Before:**
"What you need to do is navigate to the settings"

**After:**
"Go to settings"

### Combine Ideas

**Before (2 subtitles):**
```
[5] "This is very important."
[6] "You need to remember this."
```

**After (1 subtitle):**
```
[5] "Remember this - it's important."
```

## Language-Specific Subtitle Guidelines

### Spanish (Informal)

**Contractions and shortcuts:**
- "vas a" → can stay (natural)
- "tienes que" → can stay (natural)
- Remove "pues", "bueno", "entonces" when filler

**Keep natural spoken patterns:**
- ✅ "Fíjate en esto"
- ✅ "Ahora vamos a ver"
- ✅ "Mira aquí"

### French (Formal but Natural)

**Common compressions:**
- "vous allez devoir" → "vous devez"
- "il est nécessaire de" → "vous devez"
- "maintenant nous allons" → "nous allons"

**Keep natural flow:**
- ✅ "Vous verrez ici"
- ✅ "Cliquez sur"
- ✅ "Regardez"

### Arabic (RTL Considerations)

**Text direction:**
- Subtitles display right-to-left
- English technical terms stay left-to-right within the text
- Test with actual video player

## Technical Term Display

### XLSForm Terms

**In subtitles: English only**
```
English: "Enter the list_name here"
Spanish: "Escribe aquí el list_name"
French: "Saisissez le list_name ici"
```

**Why no translations?**
- Character limits
- Screen shows English term
- Viewers need to recognize the English term

### Brand Terms

**Follow base skill exactly:**
```
✅ "el Servidor Global"
✅ "La biblioteca de preguntas"
✅ "le serveur KoboToolbox mondial"
```

**Even in subtitles, brand terms are non-negotiable**

### UI Elements

**Match UI translation:**
```
Button labeled "DEPLOY" in interface:
✅ Spanish subtitle: "haz clic en IMPLEMENTAR"
✅ French subtitle: "cliquez sur DÉPLOYER"
```

## Subtitle Synchronization

### Speech-Text Alignment

**Start subtitle when speaker starts:**
- Don't start too early (confusing)
- Don't start too late (missing content)

**End subtitle when speech ends:**
- Or when next subtitle needs to start
- Brief pause between subtitles (when possible)

### Handling Fast Speech

**If speaker talks very fast:**
1. Prioritize key information
2. Compress aggressively
3. May need to combine multiple statements
4. Keep technical terms always

**Example:**
```
Speaker says (fast):
"Okay so now what we're gonna do is we're gonna go ahead 
and click on this NEW button right here at the top and 
that's gonna open up the form builder interface for us"

Subtitle:
"Click NEW to open the Formbuilder"
```

### Handling Slow Speech

**If speaker talks slowly:**
- Can use more complete translations
- Still keep under character limits
- Don't add extra information

## Common Subtitle Scenarios

### Demonstration Instructions

**Pattern: Action → Location → Result**

```
[10] "Click on this icon here"
[11] "at the top of the page"
[12] "and the menu will open"
```

Keep this pattern in translation, adjust for natural language flow.

### Technical Explanations

**Pattern: Concept → Definition → Usage**

```
[20] "This is called a cascading select"
[21] "It filters choices based on previous answers"
[22] "Very useful for location data"
```

Compress definitions but keep core meaning.

### Problem-Solution

**Pattern: Issue → Solution**

```
[30] "If you don't see the option,"
[31] "click on Show Advanced"
```

Keep the logical connection clear.

## Quality Assurance for Subtitles

### Self-Review Checklist

For each subtitle, verify:
- [ ] Under 50 characters per line
- [ ] Reads naturally at normal speed
- [ ] Technical terms correct
- [ ] Brand terms exact
- [ ] Natural spoken language
- [ ] Matches video timing (if checking with video)

### Chunk-Level Review

After translating a chunk:
- [ ] Terminology consistent throughout chunk
- [ ] Natural flow maintained
- [ ] No awkward transitions
- [ ] Speaker's voice/tone preserved
- [ ] Previous context considered
- [ ] Smooth transition to next context

### Full-File Review

After translating entire file:
- [ ] No terminology drift across chunks
- [ ] Consistent formality level throughout
- [ ] All brand terms correct everywhere
- [ ] Natural narrative flow from start to finish

## Subtitle Translation Tools

### Character Counter

**Quick estimation:**
- Count including spaces
- Each line: target 35-42, max 50
- Two lines: total target 70-84, max 100

### Reading Time Test

**Read aloud test:**
1. Read the subtitle aloud at normal speed
2. Time it
3. Should match or be slightly under subtitle duration
4. If too long, compress further

### Consistency Tracker

**For longer videos, track:**
- How you translate recurring terms
- Formality level
- Common phrases
- UI element translations

## Examples by Content Type

### Tutorial Video (How-To)

**Characteristics:**
- Step-by-step instructions
- Frequent UI references
- Needs precision

**Example:**
```
[1] "Welcome to this tutorial"
[2] "on creating forms in KoboToolbox"
[3] "First, click on NEW"
```

### Webinar/Presentation

**Characteristics:**
- More conversational
- Conceptual explanations
- Less UI interaction

**Example:**
```
[50] "KoboToolbox helps organizations"
[51] "collect data in challenging settings"
[52] "with tools that are easy to use"
```

### Live Demo

**Characteristics:**
- Real-time narration
- May have corrections/backtracking
- Informal tone

**Example:**
```
[100] "Let me show you..."
[101] "Actually, first we need to..."
[102] "Okay, now click here"
```

## Advanced Subtitle Techniques

### Handling Multiple Speakers

**If video has multiple speakers:**
- Maintain consistency for each speaker
- May use speaker labels if needed: "[Instructor]", "[Student]"
- Keep label format consistent

### Handling Questions from Audience

**Q&A sections:**
```
[200] "[Question] How do I export my data?"
[201] "[Answer] Click on the DATA tab"
```

Or simply:
```
[200] "Q: How do I export my data?"
[201] "A: Click on DATA"
```

### Handling On-Screen Text

**If video shows text on screen:**
- Subtitle can be shorter (text is visible)
- Reference the on-screen text: "as shown here"
- Don't duplicate what's clearly readable

## Error Prevention

### Most Common Subtitle Translation Errors

1. **Too long** → Always compress
2. **Too literal** → Adapt for spoken language
3. **Wrong technical terms** → Check references
4. **Inconsistent across chunks** → Track terminology
5. **Lost brand term rules** → Review before each chunk

### Before Submitting Translation

**Final check:**
1. Run through all brand terms → Exact matches?
2. Spot check character limits → Under 50?
3. Read first/middle/last chunk aloud → Natural?
4. Check consistency → Same terms throughout?
5. Verify technical terms → English only for XLSForm?

## Notes

This reference document provides **subtitle-specific** guidance that extends the base kobo-translation skill. All base terminology rules still apply - this document focuses on how to adapt those rules for subtitle constraints.
