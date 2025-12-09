# Question Types and Appearances

**📝 FORMATTING NOTE:**
- **Convert HTML heading tags to markdown:** `<h2>` → `##`, `<h3>` → `###`, etc.
- **Keep internal doc links as-is:** Relative links like `[text](article.md)` automatically resolve to the correct language folder
- **Update cross-language links:** Use directory paths like `../en/article.md`, `../es/article.md`, `../fr/article.md`
- Keep all other HTML tags intact (iframe, section, etc.)

## Question Types (PREFERRED)

These translations are preferred but can be adapted based on context.

| English | Spanish | XLSForm Type |
| --------- | --------- | -------------- |
| Select one | Seleccionar una | select_one |
| Select many | Seleccionar varias | select_multiple |
| Acknowledge | Consentimiento | acknowledge |
| Text | Texto | text |
| Note | Nota | note |
| Number | Número | integer |
| Decimal | Decimal | decimal |
| Range | Rango | range |
| Date | Fecha | date |
| Time | Hora | time |
| Date & time | Fecha y hora | datetime |
| Point | Punto | geopoint |
| Line | Línea | geotrace |
| Area | Área | geoshape |
| Photo | Foto | image |
| Audio | Audio | audio |
| Video | Video | video |
| File | Archivo | file |
| Barcode / QR Code | Código de barras / Código QR | barcode |
| Rating | Calificación | ––– |
| Ranking | Clasificación | rank |
| Question Matrix | Matriz de preguntas | ––– |
| Calculate | Cálculo | calculate |
| Hidden | Oculto | hidden |
| External XML | XML externo | xml-external |

## Question Appearances

**CRITICAL TRANSLATION APPROACH:**

Because appearance names must be used in English in XLSForm standard and Formbuilder:

- **Written content**: Include English followed by translation in parentheses
- **Video subtitles**: Use English only (character limits and video alignment)

**Example (French):** "Pour la question de type « Intervalle », vous pouvez choisir entre les options d'apparence vertical, picker (sélecteur), rating (notation) et distress (thermomètre)."

### Appearance Translations

| English | Spanish | Question Type | Notes |
| --------- | --------- | --------------- | ------- |
| minimal | Mínimo | Select one, Select many |  |
| likert | Likert | Select one |  |
| horizontal | Horizontal | Select one, Select many |  |
| quick | Rápida | Select one |  |
| quickcompact | Compacto rápida | Select one |  |
| thousands-sep | Separador de miles | Number |  |
| bearing | Rumbo (brújula) | Decimal |  |
| vertical | Vertical | Range |  |
| picker | Selector de fechas | Range |  |
| rating | Calificación | Range |  |
| distress | Termométro | Range |  |
| multiline | Multiples líneas | Text |  |
| numbers | Números | Text |  |
| month-year | Mes - año | Date |  |
| year | Año | Date |  |
| no-calendar | Sin Calendario | Date |  |
| coptic | Cóptico | Date |  |
| ethiopian | Etiope | Date |  |
| islamic | Islámico | Date |  |
| bikhram_sambat | Bikhram Sambat | Date |  |
| myanmar | Birman | Date |  |
| persian | Pérsico | Date |  |
| signature | Firma | Photo |  |
| draw | Dibujo | Photo |  |
| annotate | Anotación | Photo |  |
