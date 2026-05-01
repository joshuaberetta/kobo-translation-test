# Translation Quality Review — Sample 20 Articles (ES + FR)

**Scope:** First 20 EN docs articles translated to ES and FR  
**Date:** 2026-05-01  
**Files reviewed:** about_kobotoolbox, acknowledge, activation_link, activity_logs, add_logo, adding_skip_to_matrix, advanced_calculate, advanced_export, alternative_enketo, api, appearances_xls, archiving_projects, article_template, audit_logging, barcode_qrcode_questions, calculate_questions, calculations_constraints_matrix, calculations_xls, cascading_select, choice_filters_xls

---

## CRITICAL

### C1 — FR: Formbuilder first-reference rule fires on ~40% of articles

**Rule:** The first mention of the Formbuilder in any French article must be `interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**`.

**Failing files:**
| File | First Formbuilder mention |
|------|--------------------------|
| `fr/advanced_calculate.md` | `l'interface de création de formulaires` (no parenthetical) |
| `fr/barcode_qrcode_questions.md` | `le Formbuilder` (bare) |
| `fr/cascading_select.md` | `le Formbuilder` in H1 then bare in body |
| `fr/article_template.md` | bare `Formbuilder` in a `<details>` block |

**Passing:** adding_skip_to_matrix, alternative_enketo, appearances_xls, calculations_constraints_matrix, calculations_xls, choice_filters_xls.

**Root cause:** The rule is applied correctly in most articles but fails when the first mention occurs in (a) a heading, (b) a `<details>` element, or (c) an article where the model uses "interface de création de formulaires" shorthand from the start without the parenthetical.

---

### C2 — ES + FR: Article H1 titles don't match `article-titles.md`

Several H1 titles diverge from the official entries in `article-titles.md`. These affect cross-article link text and must be verbatim.

| File | Actual H1 | Official title |
|------|-----------|----------------|
| `es/calculate_questions.md` | `Tipo de pregunta Cálculo` | `Agregar cálculos con el Formbuilder` |
| `es/calculations_xls.md` | `Agregar cálculos en XLSForm` | `Agregar cálculos a un XLSForm` |
| `es/alternative_enketo.md` | `Usar estilos alternativos de formularios web de Enketo` | `Diseñar formularios web usando el Formbuilder` |
| `es/api.md` | `Comenzar con la API` | `Introducción a la API` |
| `es/audit_logging.md` | `Tipo de Metapregunta de Registro de Auditoría` | *(not in article-titles.md)* |
| `fr/calculate_questions.md` | `Question de type calcul` | `Ajouter des calculs avec le Formbuilder` |
| `fr/advanced_calculate.md` | `Type de question Calcul avancé` | *(not in article-titles.md)* |

**Note:** Several article-title entries are missing from `article-titles.md` entirely (audit_logging, advanced_calculate, barcode_qrcode_questions, archiving_projects). Those should be added to the glossary source.

---

### C3 — ES: `worksheet` labels translated inconsistently and incorrectly

XLSForm worksheet labels like `**survey worksheet**` are being translated as `**hoja de trabajo survey**`. Per the XLSForm rules, these are technical terms and must remain in English: `**survey worksheet**` (or match the FR convention: `**onglet survey**`).

- FR correctly uses `**onglet survey**` / `**onglet choices**` consistently ✅
- ES uses `**hoja de trabajo survey**` across: acknowledge, add_logo, appearances_xls, audit_logging, calculations_xls, choice_filters_xls, alternative_enketo (`**hoja settings**`)

The `onglet` convention in FR is acceptable because it pairs the translated word with the untranslated sheet name. ES should follow the same pattern: `**hoja survey**` or, better, leave as `**survey worksheet**`. This needs a rule in the skill.

---

## HIGH

### H1 — ES: Formbuilder parenthetical inconsistently applied

**Rule:** First mention should be `editor de formularios de KoboToolbox **(Formbuilder)**`.

**Failing files:** adding_skip_to_matrix, advanced_calculate, alternative_enketo, article_template, barcode_qrcode_questions, cascading_select, choice_filters_xls (7 of 15 applicable files).

**Passing:** appearances_xls, calculations_constraints_matrix, calculations_xls ✅

The pattern: articles that use `el editor de formularios` or `el Formbuilder` without the first-reference parenthetical. The rule is being applied in newer articles but missed in older-style articles.

---

### H2 — FR: Bare `utilisateur(s)` appears in `article_template.md`

Lines 38, 74, 144 of `fr/article_template.md` use bare `utilisateur` or `utilisateurs` without gender-inclusive form. This article is the template used for all new articles — errors here propagate to anything based on it.

---

### H3 — ES: `su` as third-person possessive in two cases

The usted-leakage check flagged three hits. Two are false positives (`en su lugar` = "instead", `su forma más básica` = "its most basic form" — both referring to the expression, not the user). One is a genuine concern:

- `barcode_qrcode_questions.md` line 28: `capturar su número de identificación` — here `su` refers to a beneficiary's ID number. The fix is: `capturar el número de identificación del/la beneficiario/a`.

The validator's regex pattern ` su ` is catching too many false positives. It should be tightened to look for `su cuenta`, `su formulario`, `su proyecto` (user-directed possessives) rather than all occurrences of ` su `.

---

### H4 — ES: `choice_filter` translated as `filtro de selección` instead of `filtro de opciones`

In `es/choice_filters_xls.md`, the document title and body consistently use "filtro de selección" but the official term from `form-building-terms.md` is "filtro de opciones" (or the XLSForm column name `choice_filter` should remain untranslated). The article title is also `Agregar filtros de selección a un XLSForm` but article-titles.md says it should stay closer to the EN title. This is a terminology consistency issue across the article.

---

## MEDIUM

### M1 — FR: `nom_utilisateur` in API code examples should stay untranslated

`fr/api.md` line 50: `` `curl -u nom_utilisateur:mot_de_passe ...` ``

API credentials in code blocks are technical placeholders. The EN source uses `username:password`. Translating them to French (`nom_utilisateur`, `mot_de_passe`) is inconsistent with the XLSForm rule (never translate technical terms). Should remain as `username:password` or use a neutral placeholder like `<username>:<password>`.

---

### M2 — FR: `cascading_select.md` — Formbuilder in H1 not parenthetical-eligible but body references bare

The article title `# Ajouter des questions à sélection en cascade dans le Formbuilder` correctly uses "Formbuilder" as a proper noun in the title. However, the body text (lines 8, 13, 30, 32, 34, etc.) uses bare "Formbuilder" without the first-reference parenthetical ever appearing. The first *body* mention of Formbuilder should still include the parenthetical.

---

### M3 — ES: `adding_skip_to_matrix.md` uses `editor de formularios` throughout without parenthetical

The article uses `editor de formularios` (short form) as if it were the first-reference expanded form. The first occurrence should be `editor de formularios de KoboToolbox **(Formbuilder)**`.

---

### M4 — ES/FR: `archiving_projects.md` — not yet checked against article-titles.md

`audit_logging.md`, `advanced_calculate.md`, `barcode_qrcode_questions.md`, and `archiving_projects.md` have no entries in `article-titles.md`. The H1 titles were generated by the model and may not match what other articles use when linking to them. These titles need to be added to the glossary source and propagated.

---

### M5 — FR: `article_template.md` line 144 — bare `utilisateurs` in a `<li>` note block

> `tous les utilisateurs travaillant sur un projet partagé doivent utiliser le même serveur`

Should be `tous les utilisateur(rice)s`. This is the template article so it's high-impact if copied.

---

## LOW / NICE-TO-HAVE

### L1 — ES: `advanced_export.md` — mixed use of `exportar` vs `descargar`

The EN source distinguishes "export" (to file) from "download" (retrieve the file). The ES translation uses `exportar` and `descargar` somewhat interchangeably in a few places, which could confuse users. The skill glossary maps `importer` → `importar` but doesn't enforce `exportar` vs `descargar` distinction.

---

### L2 — FR: `advanced_calculate.md` — section heading `Utilisation de l'interface de création de formulaires` (line 11) omits the Formbuilder English name

Even though this is a heading (not body text), the parenthetical convention should apply on the first body reference immediately following.

---

### L3 — ES: `alternative_enketo.md` — translated as `estilos alternativos de formularios web de Enketo`

The official title from article-titles.md is `Diseñar formularios web usando el Formbuilder`. The H1 used by the translation (`Usar estilos alternativos de formularios web de Enketo`) is a literal translation of the EN source title, which itself was updated. The official ES title should be used.

---

### L4 — ES: Line-broken prose in `add_logo.md`

The ES translation of `add_logo.md` has mid-sentence line breaks (lines 3-4, 10-12, 20-21, 32-35) that don't appear in the source. These are cosmetic but create awkward wrapping in rendered output. The model appears to have reflow-wrapped at ~80 chars. The source has no such wrapping.

---

### L5 — FR: `calculate_questions.md` H1 is `Question de type calcul` 

The official title is `Ajouter des calculs avec le Formbuilder`. The model generated a literal translation of the older EN title `Adding calculations in the Formbuilder` → `Question de type calcul` which doesn't match either version.

---

## Summary by severity

| Severity | Count | Key issues |
|----------|-------|------------|
| Critical | 3 | FR Formbuilder parenthetical missing (4 files), H1 title mismatches (7 files), ES worksheet label translation |
| High | 4 | ES Formbuilder parenthetical missing (7 files), FR article_template gender, ES `su` false positive pattern, `choice_filter` terminology |
| Medium | 5 | FR API code placeholder translated, cascading_select bare Formbuilder, missing article-titles entries, article_template `utilisateurs` |
| Low | 5 | Mixed export/download, heading parenthetical, wrong H1 title, line-wrapped prose, calculate_questions H1 |

---

## Recommended skill/tooling fixes

1. **Add XLSForm worksheet label rule to ES skill:** "Never translate `**survey worksheet**`, `**choices worksheet**`, `**settings worksheet**` labels — keep English names, prefix with `**hoja**` only: `**hoja survey**`."
2. **Add explicit heading/details/title exception for Formbuilder parenthetical:** "The first reference in *body text* (not headings or titles) must include the parenthetical — even if the heading already uses the term."
3. **Add `audit_logging`, `advanced_calculate`, `barcode_qrcode_questions`, `archiving_projects` to `article-titles.md` in the glossary source.**
4. **Tighten the usted validator regex** to target user-directed possessives (`su cuenta`, `su formulario`, `su proyecto`) rather than all ` su ` occurrences, reducing false positives.
5. **Add H1 title validation step** that compares the generated H1 against `article-titles.md` and warns if no match is found.
