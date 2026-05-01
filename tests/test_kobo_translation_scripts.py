"""
Tests for the kobo-translation skill scripts:
  - fetch_glossary.py  (URL constant, download error handling)
  - regenerate_skill.py (Article titles tab → article-titles.md, full generate flow)
  - validate_sources.py (Article titles sheet validation, column checks)
"""

import io
import sys
import tempfile
import urllib.error
from pathlib import Path
from unittest import mock

import pandas as pd
import pytest

# Put scripts on path so we can import them directly
SCRIPTS_DIR = Path(__file__).parent.parent / "skills" / "kobo-translation" / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import fetch_glossary
import regenerate_skill
import validate_sources


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

GLOSSARY_SHEETS = [
    "Proper & Kobo specific",
    "Academy",
    "Documentation",
    "Data collection",
    "Form building",
    "Data management",
    "Formbuilder question types",
    "Appearances",
    "Formbuilder UI ",
    "KoboCollect",
    "XLSForm",
    "Sentence structures",
    "Article titles",
]


def make_minimal_xlsx(tmp_path: Path, extra_sheets: dict | None = None) -> Path:
    """Write a minimal xlsx with all expected sheets to tmp_path/glossary.xlsx."""
    dest = tmp_path / "glossary.xlsx"
    with pd.ExcelWriter(dest, engine="openpyxl") as writer:
        # All required terminology sheets (minimal content)
        for sheet in GLOSSARY_SHEETS:
            if sheet == "Article titles":
                df = pd.DataFrame({
                    "File name": ["getting-started", "form-builder-intro"],
                    "English": ["Getting Started", "Introduction to the Form Builder"],
                    "French": ["Premiers pas", "Introduction au créateur de formulaires"],
                    "Spanish": ["Primeros pasos", "Introducción al editor de formularios"],
                    "Arabic": ["البدء", "مقدمة إلى منشئ النماذج"],
                    "Notes": ["", ""],
                })
            elif sheet == "Proper & Kobo specific":
                # Must include all CRITICAL_TERMS from validate_sources
                df = pd.DataFrame({
                    "English": [
                        "Global KoboToolbox Server",
                        "European Union KoboToolbox Server",
                        "Question Library",
                        "KoboToolbox Academy",
                        "Community Forum",
                        "Help Center",
                    ],
                    "French": ["Le serveur KoboToolbox mondial", "Le serveur UE", "La bibliothèque de questions", "", "", ""],
                    "Spanish": ["Servidor Global", "Servidor UE", "La biblioteca de preguntas", "", "", ""],
                    "Arabic": ["", "", "", "", "", ""],
                    "Notes": ["", "", "", "", "", ""],
                })
            else:
                df = pd.DataFrame({
                    "English": ["Sample term"],
                    "French": ["Terme exemple"],
                    "Spanish": ["Término de ejemplo"],
                    "Arabic": [""],
                    "Notes": [""],
                })
            df.to_excel(writer, sheet_name=sheet, index=False)

        if extra_sheets:
            for sheet, df in extra_sheets.items():
                df.to_excel(writer, sheet_name=sheet, index=False)

    return dest


# ---------------------------------------------------------------------------
# fetch_glossary tests
# ---------------------------------------------------------------------------

class TestFetchGlossary:
    def test_url_constant_is_set(self):
        assert fetch_glossary.GOOGLE_SHEET_URL.startswith("https://")
        assert "spreadsheets" in fetch_glossary.GOOGLE_SHEET_URL
        assert "output=xlsx" in fetch_glossary.GOOGLE_SHEET_URL

    def test_dest_path_is_glossary_xlsx(self):
        assert fetch_glossary.DEST_PATH.name == "glossary.xlsx"
        assert fetch_glossary.DEST_PATH.parent.name == "sources"

    def test_network_error_exits_nonzero(self):
        with mock.patch("urllib.request.urlopen", side_effect=urllib.error.URLError("no network")):
            with pytest.raises(SystemExit) as exc:
                fetch_glossary.main()
            assert exc.value.code != 0

    def test_suspiciously_small_response_exits_nonzero(self, tmp_path):
        tiny_data = b"x" * 500  # < 1000 byte threshold

        cm = mock.mock_open(read_data=tiny_data)
        cm.return_value.__enter__ = lambda s: s
        cm.return_value.__exit__ = mock.Mock(return_value=False)
        cm.return_value.read = lambda: tiny_data

        with mock.patch("urllib.request.urlopen", return_value=cm.return_value):
            with mock.patch.object(fetch_glossary, "DEST_PATH", tmp_path / "glossary.xlsx"):
                with mock.patch.object(fetch_glossary, "SOURCES_DIR", tmp_path):
                    with pytest.raises(SystemExit) as exc:
                        fetch_glossary.main()
                    assert exc.value.code != 0

    def test_successful_download_writes_file(self, tmp_path):
        # Use the real local glossary as fake "download" content
        real_xlsx = SCRIPTS_DIR.parent / "sources" / "glossary.xlsx"
        if not real_xlsx.exists():
            pytest.skip("sources/glossary.xlsx not present")

        data = real_xlsx.read_bytes()

        cm = mock.MagicMock()
        cm.__enter__ = lambda s: s
        cm.__exit__ = mock.Mock(return_value=False)
        cm.read = mock.Mock(return_value=data)

        dest = tmp_path / "glossary.xlsx"
        with mock.patch("urllib.request.urlopen", return_value=cm):
            with mock.patch.object(fetch_glossary, "DEST_PATH", dest):
                with mock.patch.object(fetch_glossary, "SOURCES_DIR", tmp_path):
                    fetch_glossary.main()

        assert dest.exists()
        assert dest.stat().st_size == len(data)


# ---------------------------------------------------------------------------
# regenerate_skill tests — Article titles tab
# ---------------------------------------------------------------------------

class TestArticleTitlesGeneration:
    def _make_df(self):
        return pd.DataFrame({
            "File name": ["getting-started", "collect-data"],
            "English": ["Getting Started", "Collecting Data"],
            "French": ["Premiers pas", "Collecte de données"],
            "Spanish": ["Primeros pasos", "Recolección de datos"],
            "Arabic": ["البدء", "جمع البيانات"],
            "Notes": ["", "key article"],
        })

    def test_generates_official_header(self):
        content = regenerate_skill.generate_article_titles_file(self._make_df())
        assert "OFFICIAL" in content

    def test_generates_verbatim_instruction(self):
        content = regenerate_skill.generate_article_titles_file(self._make_df())
        assert "verbatim" in content.lower() or "VERBATIM" in content

    def test_all_language_columns_present(self):
        content = regenerate_skill.generate_article_titles_file(self._make_df())
        for col in ("File name", "English", "French", "Spanish", "Arabic"):
            assert col in content

    def test_rows_rendered(self):
        content = regenerate_skill.generate_article_titles_file(self._make_df())
        assert "getting-started" in content
        assert "Premiers pas" in content
        assert "Primeros pasos" in content

    def test_notes_column_included_when_present(self):
        content = regenerate_skill.generate_article_titles_file(self._make_df())
        assert "key article" in content

    def test_notes_omitted_when_empty(self):
        df = self._make_df().drop(columns=["Notes"])
        content = regenerate_skill.generate_article_titles_file(df)
        assert "Notes" not in content

    def test_pipe_in_title_escaped(self):
        df = pd.DataFrame({
            "File name": ["tricky"],
            "English": ["A | B title"],
            "French": ["Titre A | B"],
            "Spanish": [""],
            "Arabic": [""],
        })
        content = regenerate_skill.generate_article_titles_file(df)
        assert r"A \| B title" in content

    def test_generate_reference_files_routes_article_titles(self, tmp_path):
        sheets = {"Article titles": self._make_df()}
        files = regenerate_skill.generate_reference_files(sheets)
        assert "article-titles.md" in files
        assert "getting-started" in files["article-titles.md"]

    def test_article_titles_not_routed_to_other_files(self, tmp_path):
        sheets = {"Article titles": self._make_df()}
        files = regenerate_skill.generate_reference_files(sheets)
        # Should not appear in brand or ui files
        assert "brand-terminology.md" not in files
        assert "ui-terminology.md" not in files


# ---------------------------------------------------------------------------
# regenerate_skill tests — full end-to-end generation
# ---------------------------------------------------------------------------

class TestFullRegeneration:
    def test_article_titles_file_written_to_disk(self, tmp_path):
        xlsx_path = make_minimal_xlsx(tmp_path)
        refs_dir = tmp_path / "references"

        with mock.patch.object(regenerate_skill, "SOURCES_DIR", tmp_path):
            with mock.patch.object(regenerate_skill, "REFERENCES_DIR", refs_dir):
                with mock.patch.object(regenerate_skill, "SKILL_ROOT", tmp_path):
                    regenerate_skill.main()

        article_titles = refs_dir / "article-titles.md"
        assert article_titles.exists(), "article-titles.md was not generated"
        content = article_titles.read_text()
        assert "OFFICIAL" in content
        assert "getting-started" in content

    def test_standard_reference_files_still_generated(self, tmp_path):
        xlsx_path = make_minimal_xlsx(tmp_path)
        refs_dir = tmp_path / "references"

        with mock.patch.object(regenerate_skill, "SOURCES_DIR", tmp_path):
            with mock.patch.object(regenerate_skill, "REFERENCES_DIR", refs_dir):
                with mock.patch.object(regenerate_skill, "SKILL_ROOT", tmp_path):
                    regenerate_skill.main()

        assert (refs_dir / "brand-terminology.md").exists()
        assert (refs_dir / "ui-terminology.md").exists()

    def test_skill_md_references_article_titles(self, tmp_path):
        xlsx_path = make_minimal_xlsx(tmp_path)
        refs_dir = tmp_path / "references"

        with mock.patch.object(regenerate_skill, "SOURCES_DIR", tmp_path):
            with mock.patch.object(regenerate_skill, "REFERENCES_DIR", refs_dir):
                with mock.patch.object(regenerate_skill, "SKILL_ROOT", tmp_path):
                    regenerate_skill.main()

        skill_md = (tmp_path / "SKILL.md").read_text()
        assert "article-titles.md" in skill_md

    def test_skill_md_article_title_checklist_item(self, tmp_path):
        xlsx_path = make_minimal_xlsx(tmp_path)
        refs_dir = tmp_path / "references"

        with mock.patch.object(regenerate_skill, "SOURCES_DIR", tmp_path):
            with mock.patch.object(regenerate_skill, "REFERENCES_DIR", refs_dir):
                with mock.patch.object(regenerate_skill, "SKILL_ROOT", tmp_path):
                    regenerate_skill.main()

        skill_md = (tmp_path / "SKILL.md").read_text()
        assert "article-titles.md" in skill_md
        # Quality checklist item
        assert "article" in skill_md.lower() and "title" in skill_md.lower()


# ---------------------------------------------------------------------------
# validate_sources tests
# ---------------------------------------------------------------------------

class TestValidateSources:
    def test_article_titles_in_expected_sheets(self):
        assert "Article titles" in validate_sources.EXPECTED_SHEETS

    def test_article_titles_columns_defined(self):
        for col in ("File name", "English", "French", "Spanish", "Arabic"):
            assert col in validate_sources.ARTICLE_TITLES_COLUMNS

    def test_valid_glossary_passes(self, tmp_path):
        xlsx_path = make_minimal_xlsx(tmp_path)
        errors = validate_sources.validate_glossary(xlsx_path)
        assert errors == [], f"Unexpected errors: {errors}"

    def test_missing_article_titles_sheet_is_error(self, tmp_path):
        dest = tmp_path / "glossary.xlsx"
        sheets_without_article_titles = [s for s in GLOSSARY_SHEETS if s != "Article titles"]
        with pd.ExcelWriter(dest, engine="openpyxl") as writer:
            for sheet in sheets_without_article_titles:
                df = pd.DataFrame({
                    "English": ["Global KoboToolbox Server"],
                    "French": ["Le serveur KoboToolbox mondial"],
                    "Spanish": ["Servidor Global"],
                })
                df.to_excel(writer, sheet_name=sheet, index=False)

        errors = validate_sources.validate_glossary(dest)
        assert any("Article titles" in e for e in errors), f"Expected missing-sheet error, got: {errors}"

    def test_article_titles_missing_column_is_error(self, tmp_path):
        dest = tmp_path / "glossary.xlsx"
        with pd.ExcelWriter(dest, engine="openpyxl") as writer:
            for sheet in GLOSSARY_SHEETS:
                if sheet == "Article titles":
                    # Missing "Arabic" column
                    df = pd.DataFrame({
                        "File name": ["getting-started"],
                        "English": ["Getting Started"],
                        "French": ["Premiers pas"],
                        "Spanish": ["Primeros pasos"],
                    })
                else:
                    df = pd.DataFrame({
                        "English": ["Global KoboToolbox Server"],
                        "French": ["Le serveur KoboToolbox mondial"],
                        "Spanish": ["Servidor Global"],
                    })
                df.to_excel(writer, sheet_name=sheet, index=False)

        errors = validate_sources.validate_glossary(dest)
        assert any("Article titles" in e and "Arabic" in e for e in errors), (
            f"Expected missing-column error for Article titles, got: {errors}"
        )

    def test_missing_glossary_file_is_error(self, tmp_path):
        errors = validate_sources.validate_glossary(tmp_path / "nonexistent.xlsx")
        assert len(errors) > 0

    def test_missing_critical_terms_reported(self, tmp_path):
        dest = tmp_path / "glossary.xlsx"
        with pd.ExcelWriter(dest, engine="openpyxl") as writer:
            for sheet in GLOSSARY_SHEETS:
                if sheet == "Proper & Kobo specific":
                    # Omit all critical terms
                    df = pd.DataFrame({
                        "English": ["Some Other Term"],
                        "French": ["Autre terme"],
                        "Spanish": ["Otro término"],
                    })
                elif sheet == "Article titles":
                    df = pd.DataFrame({
                        "File name": ["x"], "English": ["X"], "French": ["X"],
                        "Spanish": ["X"], "Arabic": ["X"],
                    })
                else:
                    df = pd.DataFrame({"English": ["x"], "French": ["x"], "Spanish": ["x"]})
                df.to_excel(writer, sheet_name=sheet, index=False)

        errors = validate_sources.validate_glossary(dest)
        assert any("critical" in e.lower() or "Missing critical" in e for e in errors), (
            f"Expected critical-terms error, got: {errors}"
        )
