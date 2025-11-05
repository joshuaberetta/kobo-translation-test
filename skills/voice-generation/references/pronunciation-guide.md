# Pronunciation Guide for Technical Terms

## Overview
This guide provides pronunciation tips for KoboToolbox-specific terms and technical vocabulary to ensure consistent and accurate voice generation across languages.

## General Principles

### English Technical Terms in Translated Content
Many technical terms are kept in English even in translated content. The voice model should pronounce these naturally:

**Keep in English**:
- XLSForm
- API
- CSV
- JSON
- XML
- REST
- HTTP/HTTPS
- URL

### Brand Names
Always preserve original pronunciation:
- **KoboToolbox**: "Kobo Toolbox" (two words in speech)
- **Enketo**: "En-keh-to"
- **ODK**: "O-D-K" (spell out letters)

## Language-Specific Pronunciation

## Spanish (es)

### Technical Terms (Keep in English)
These terms should be pronounced with English pronunciation:
- **XLSForm** → "EKS-el-ES Form"
- **API** → "ah-pee-EE" or "A-P-I"
- **CSV** → "see-ese-VEE" or "C-S-V"
- **JSON** → "JAY-son"
- **REST** → "REST" (English)

### KoboToolbox Terms (Spanish Translation)
- **Formbuilder** → "Form-builder" (English first reference, then:)
  - "Constructor de formularios" → "cons-trook-TOR deh for-moo-LAH-ree-os"
- **Biblioteca de preguntas** → "bee-blee-oh-TEH-kah deh preh-GOON-tahs"
  - Capital B: "Biblioteca" when referring to Question Library feature
- **Servidor Global** → "sehr-vee-DOR glo-BAHL"
- **Servidor Humanitario** → "sehr-vee-DOR oo-mah-nee-TAH-ree-oh"

### Common UI Terms
- **Hacer clic** → "ah-SEHR cleek"
- **Menú** → "meh-NOO"
- **Pestaña** → "peh-STAHN-yah"
- **Botón** → "boh-TONE"

### Question Types
- **Texto** → "TEHKS-toh"
- **Número** → "NOO-meh-roh"
- **Fecha** → "FEH-chah"
- **Ubicación** → "oo-bee-kah-see-OWN"
- **Foto** → "FOH-toh"

## French (fr)

### Technical Terms (Keep in English)
Pronounce with French accent:
- **XLSForm** → "eeks-EL-ESS form"
- **API** → "ah-pay-EE" or "A-P-I"
- **CSV** → "say-ESS-vay" or "C-S-V"
- **JSON** → "djay-SONE"
- **REST** → "REST" (anglicized)

### KoboToolbox Terms (French Translation)
- **Formbuilder** → "Form-builder" (English first reference, then:)
  - "Créateur de formulaires" → "kray-ah-TUR duh for-mew-LAIR"
- **La bibliothèque de questions** → "lah bee-blee-oh-TEHK duh kess-tee-ON"
  - Capital L + B: "La bibliothèque" for Question Library
- **Serveur Global** → "sehr-VUR glo-BAHL"
- **Serveur Humanitaire** → "sehr-VUR ew-mah-nee-TAIR"

### Common UI Terms
- **Cliquer** → "klee-KAY"
- **Menu** → "muh-NEW"
- **Onglet** → "on-GLEH"
- **Bouton** → "boo-TON"

### Question Types
- **Texte** → "tekst"
- **Nombre** → "NOM-bruh"
- **Date** → "daht"
- **Emplacement** → "om-plah-suh-MON"
- **Photo** → "foh-TOH"

## Arabic (ar)

### Technical Terms (Keep in English)
In Arabic content, technical terms often remain in English:
- **XLSForm** → Use English pronunciation
- **API** → "ay-pee-ay" or spell out in Arabic
- **CSV** → "see-ess-vee" or spell out
- **JSON** → "jay-sawn"
- **REST** → "rest" (anglicized)

### KoboToolbox Terms (Arabic Translation)
- **Formbuilder** → "Form-builder" (English first reference)
  - "منشئ النماذج" (munshi' al-namadhij)
- **مكتبة الأسئلة** (maktabat al-as'ila) → "Question Library"
- **الخادم العالمي** (al-khadim al-'alami) → "Global Server"
- **الخادم الإنساني** (al-khadim al-insani) → "Humanitarian Server"

### Common UI Terms
- **انقر** (unqur) → "click"
- **القائمة** (al-qa'ima) → "menu"
- **علامة التبويب** ('alamat al-tabwib) → "tab"
- **زر** (zirr) → "button"

### Question Types
- **نص** (nass) → "text"
- **رقم** (raqm) → "number"
- **تاريخ** (tarikh) → "date"
- **موقع** (mawqi') → "location"
- **صورة** (sura) → "photo"

### Arabic-Specific Considerations
1. **Diacritical Marks**: Remove for voice generation (model handles pronunciation)
2. **MSA vs. Dialects**: Use Modern Standard Arabic for professional content
3. **English Insertions**: Expect natural code-switching for technical terms
4. **Right-to-Left**: Text direction doesn't affect audio generation

## Acronyms and Abbreviations

### How to Handle
1. **Spell Out on First Use**: "Application Programming Interface or API"
2. **Subsequent Uses**: Just "API" (model will learn from context)
3. **Well-Known Acronyms**: Can use directly (CSV, JSON, API)

### Common Acronyms
| Acronym | English | Spanish | French | Arabic |
|---------|---------|---------|--------|--------|
| API | A-P-I or "ay-pee-eye" | A-P-I | A-P-I | Spell out |
| CSV | C-S-V or "cee-ess-vee" | C-S-V | C-S-V | Spell out |
| JSON | "jay-sawn" | "jay-sawn" | "djay-sawn" | "jay-sawn" |
| XML | X-M-L or "ex-em-el" | X-M-L | X-M-L | Spell out |
| URL | U-R-L or "you-are-el" | U-R-L | U-R-L | Spell out |
| HTTP | H-T-T-P | H-T-T-P | H-T-T-P | Spell out |
| ODK | O-D-K | O-D-K | O-D-K | O-D-K |

## Handling Special Characters

### In Text Before Voice Generation
Remove or convert these for better pronunciation:

**Remove**:
- SRT formatting: `<i>`, `<b>`, `<u>`, etc.
- Markup: `**`, `__`, `#`, etc.
- Special symbols: `©`, `®`, `™` (replace with text: "copyright", "registered", "trademark")

**Convert**:
- `&` → "and" / "y" / "et" / "و"
- `@` → "at" / "arroba" / "arobase" / "في"
- `#` → "hashtag" / "hashtag" / "hashtag" / "وسم"
- `%` → "percent" / "por ciento" / "pour cent" / "في المئة"

### URLs and Emails
**Options**:
1. **Remove entirely** if not essential for audio
2. **Simplify**: "visit our website" instead of reading full URL
3. **Natural language**: "email us at support" instead of reading full email

**Example**:
```
Original: "Visit https://www.kobotoolbox.org for more info"
Audio: "Visit www dot kobotoolbox dot org for more info"
Better: "Visit kobotoolbox.org for more info"
Best: "Visit our website for more info"
```

## Numbers and Dates

### Numbers
**Spanish**:
- Write as words for clarity: "uno", "dos", "tres"
- Or keep digits: model will pronounce correctly

**French**:
- Write as words: "un", "deux", "trois"
- Watch for liaison: "un_ami" (careful with word boundaries)

**Arabic**:
- Use Eastern Arabic numerals: ١، ٢، ٣
- Or Western numerals: 1, 2, 3 (model converts)

### Dates
**Spanish**: "1 de enero de 2024" (natural format)
**French**: "1er janvier 2024" (natural format)
**Arabic**: "١ يناير ٢٠٢٤" (natural format)

### Times
Use natural language:
- ✅ "2:00 PM" → "two PM" / "las dos de la tarde" / "deux heures" / "الثانية ظهراً"
- ❌ Don't use 24-hour format in audio unless necessary

## Pacing and Punctuation

### Use Punctuation for Pacing
- **Period (.)**: Natural pause
- **Comma (,)**: Short pause
- **Ellipsis (...)**: Longer pause, trailing thought
- **Em dash (—)**: Break in thought
- **Semicolon (;)**: Medium pause

### Add Breathing Room
```
Before: "To create a form click the plus button then select form type and enter the form name"

After: "To create a form, click the plus button. Then select the form type and enter the form name."
```

### Emphasis
- Use punctuation, not ALL CAPS
- Use italics in source text (though removed for TTS)
- Rely on voice model's natural emphasis

## Testing Pronunciation

### Testing Script
```bash
# Generate a sample with technical terms
python scripts/generate_voice.py test_sample.srt --lang es --stability 0.6

# Listen for:
# - Technical term pronunciation
# - Brand name accuracy
# - Acronym clarity
# - Natural pacing
```

### Quality Checks
- [ ] Technical terms pronounced correctly
- [ ] Brand names sound natural
- [ ] Acronyms are clear
- [ ] No awkward pauses
- [ ] Consistent pronunciation throughout
- [ ] Native speaker approved

## Common Pronunciation Issues

### Problem: Acronyms sound unclear
**Solution**:
- Spell out on first use: "Application Programming Interface, or A-P-I"
- Add spaces: "A P I" forces letter-by-letter

### Problem: Technical terms mispronounced
**Solution**:
- Use phonetic spelling: "XLS Form" → "Excel-ess form"
- Add pronunciation hints in parentheses (removed post-generation)

### Problem: Brand names sound wrong
**Solution**:
- Test with different voices
- Use custom pronunciation dictionary (Pro feature)
- Add subtle hints: "Kobo Toolbox" (two words)

### Problem: Numbers sound awkward
**Solution**:
- Write out numbers as words for important values
- Use natural language: "more than 100" vs "100+"

## Best Practices

### Pre-Generation Text Cleanup
1. Remove all markup and formatting
2. Expand acronyms on first use
3. Simplify URLs and emails
4. Add punctuation for pacing
5. Write out special characters
6. Test a sample before full generation

### During Generation
1. Use appropriate voice settings
2. Choose voice with clear pronunciation
3. Enable speaker boost for clarity
4. Match stability to content type

### Post-Generation Review
1. Listen to first 2 minutes
2. Check technical term pronunciation
3. Verify pacing and pauses
4. Confirm natural flow
5. Get native speaker feedback

## Language-Specific Resources

### Spanish Pronunciation
- IPA Reference: https://en.wikipedia.org/wiki/Help:IPA/Spanish
- Regional Variations: Consider target audience (Latin America vs Spain)

### French Pronunciation
- IPA Reference: https://en.wikipedia.org/wiki/Help:IPA/French
- Liaison Rules: Voice model handles naturally

### Arabic Pronunciation
- IPA Reference: https://en.wikipedia.org/wiki/Help:IPA/Arabic
- MSA Standard: Most formal content
- Regional: Consider dialect for specific audiences

## Updates and Maintenance

### When to Update This Guide
- New technical terms introduced
- Pronunciation issues discovered
- New languages added
- Voice model improvements change handling

### Feedback Loop
1. Track pronunciation issues
2. Document solutions
3. Update guide
4. Share with team
5. Retest periodically
