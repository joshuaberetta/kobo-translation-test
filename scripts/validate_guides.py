#!/usr/bin/env python3
"""
Translation Guide Validation System

Validates translation guides for:
- Structural completeness (all sections present)
- Terminology consistency with master database
- Cross-references and links
- Language-specific patterns
- Common errors and pitfalls

Usage:
    python scripts/validate_guides.py [--language LANG] [--strict] [--fix]
"""

import os
import sys
import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
SKILLS_DIR = PROJECT_ROOT / 'skills'
TERMINOLOGY_DIR = PROJECT_ROOT / 'terminology'


@dataclass
class ValidationIssue:
    """Represents a validation issue found in a guide."""
    severity: str  # ERROR, WARNING, INFO
    category: str  # structure, terminology, cross-ref, etc.
    language: str
    file: str
    line: int
    message: str
    suggestion: str = ""


class GuideValidator:
    """Validates translation guides for completeness and consistency."""

    def __init__(self, strict: bool = False):
        self.strict = strict
        self.issues: List[ValidationIssue] = []
        self.master_terminology = self.load_master_terminology()

    def load_master_terminology(self) -> Dict:
        """Load master terminology if available."""
        master_file = TERMINOLOGY_DIR / 'master_terminology.yaml'
        if master_file.exists():
            with open(master_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        return {}

    def validate_guide_structure(self, lang: str, content: str) -> None:
        """Validate that guide has all required sections."""
        required_sections = [
            "# KoboToolbox Translation & Localization",
            "## Overview",
            "## 🚨 CRITICAL: Pre-Translation Checklist",
            "## Quick Reference",
            "## Common Translation Pitfalls",
            "## Translation Workflow",
            "## Core Translation Principles",
            "## Common Translation Patterns",
            "## Terminology References",
            "## Translation Decision Tree",
            "## Enhanced Quality Checklist",
            "## Translation Error Examples",
        ]

        for section in required_sections:
            if section not in content:
                self.issues.append(ValidationIssue(
                    severity="ERROR" if self.strict else "WARNING",
                    category="structure",
                    language=lang,
                    file="SKILL.md",
                    line=0,
                    message=f"Missing required section: {section}",
                    suggestion="Add this section following the French/Spanish guide structure"
                ))

    def validate_tables_completeness(self, lang: str, content: str) -> None:
        """Check that all tables have content (no empty cells in critical columns)."""

        # Find all markdown tables
        table_pattern = r'\|.*\|.*\n\|[-:| ]+\|.*\n((?:\|.*\|.*\n)+)'
        tables = re.finditer(table_pattern, content)

        line_num = 0
        for match in tables:
            table_text = match.group(0)
            table_start = content[:match.start()].count('\n') + 1

            # Check for empty cells in tables (except Notes column)
            lines = table_text.strip().split('\n')
            if len(lines) > 2:  # Has data rows
                for i, line in enumerate(lines[2:], start=2):  # Skip header and separator
                    cells = [cell.strip() for cell in line.split('|')[1:-1]]  # Remove outer empty cells

                    # Check if important columns are empty (not the last column which is often Notes)
                    for j, cell in enumerate(cells[:-1]):  # Check all but Notes
                        if not cell or cell == '':
                            self.issues.append(ValidationIssue(
                                severity="WARNING",
                                category="completeness",
                                language=lang,
                                file="SKILL.md",
                                line=table_start + i,
                                message=f"Empty cell in table column {j+1}",
                                suggestion="Fill in all critical table cells with appropriate content"
                            ))

    def validate_language_specific_content(self, lang: str, content: str) -> None:
        """Validate that language-specific sections have appropriate content."""

        if lang == 'ar':
            # Arabic-specific checks
            if 'RTL' not in content and 'right-to-left' not in content.lower():
                self.issues.append(ValidationIssue(
                    severity="WARNING",
                    category="language-specific",
                    language=lang,
                    file="SKILL.md",
                    line=0,
                    message="Arabic guide should include RTL (right-to-left) text handling guidance",
                    suggestion="Add section on RTL text, dir='rtl' attributes, and Arabic text layout"
                ))

            if 'dir="rtl"' not in content:
                self.issues.append(ValidationIssue(
                    severity="INFO",
                    category="language-specific",
                    language=lang,
                    file="SKILL.md",
                    line=0,
                    message="No examples of dir='rtl' usage found",
                    suggestion="Include examples showing <section dir='rtl'> wrapper usage"
                ))

        if lang == 'fr':
            # French-specific checks
            if 'vous' not in content:
                self.issues.append(ValidationIssue(
                    severity="ERROR",
                    category="language-specific",
                    language=lang,
                    file="SKILL.md",
                    line=0,
                    message="French guide must specify 'vous' vs 'tu' usage",
                ))

        if lang == 'es':
            # Spanish-specific checks
            if 'tú' not in content and 'usted' not in content:
                self.issues.append(ValidationIssue(
                    severity="ERROR",
                    category="language-specific",
                    language=lang,
                    file="SKILL.md",
                    line=0,
                    message="Spanish guide must specify 'tú' vs 'usted' usage",
                ))

    def validate_cross_references(self, lang: str, content: str, skill_dir: Path) -> None:
        """Validate that cross-references to other files exist."""

        # Find all markdown links
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        links = re.finditer(link_pattern, content)

        for match in links:
            link_text = match.group(1)
            link_path = match.group(2)

            # Skip external links
            if link_path.startswith('http://') or link_path.startswith('https://'):
                continue

            # Skip anchor links
            if link_path.startswith('#'):
                continue

            # Check if file exists
            if link_path.startswith('references/'):
                full_path = skill_dir / link_path
            elif link_path.startswith('../'):
                # Cross-language link
                full_path = SKILLS_DIR / link_path.replace('../', '')
            else:
                full_path = skill_dir / link_path

            if not full_path.exists():
                line_num = content[:match.start()].count('\n') + 1
                self.issues.append(ValidationIssue(
                    severity="WARNING",
                    category="cross-reference",
                    language=lang,
                    file="SKILL.md",
                    line=line_num,
                    message=f"Broken link: {link_path}",
                    suggestion=f"Create missing file or update link"
                ))

    def validate_terminology_consistency(self, lang: str, content: str) -> None:
        """Check terminology usage against master database."""
        if not self.master_terminology:
            return

        # Check for common brand term errors
        brand_terms = self.master_terminology.get('brand_terms', [])

        for term_data in brand_terms:
            english = term_data['english']
            pitfalls = term_data.get('pitfalls', {})

            # Check for wrong translations
            wrong_key = f'{lang}_wrong'
            if wrong_key in pitfalls:
                wrong_translation = pitfalls[wrong_key]
                if wrong_translation in content:
                    reason = pitfalls.get(f'{lang}_reason', 'Incorrect translation')
                    correct = term_data['translations'].get(lang, '')

                    self.issues.append(ValidationIssue(
                        severity="ERROR",
                        category="terminology",
                        language=lang,
                        file="SKILL.md",
                        line=0,
                        message=f"Found incorrect translation: '{wrong_translation}' for '{english}'",
                        suggestion=f"Use correct translation: '{correct}'. Reason: {reason}"
                    ))

    def validate_reference_file(self, lang: str, ref_file: Path) -> None:
        """Validate a reference terminology file."""
        if not ref_file.exists():
            self.issues.append(ValidationIssue(
                severity="WARNING",
                category="missing-file",
                language=lang,
                file=ref_file.name,
                line=0,
                message=f"Reference file missing: {ref_file.name}",
                suggestion="Create this file following the French/Spanish template"
            ))
            return

        content = ref_file.read_text(encoding='utf-8')

        # Check for OFFICIAL vs PREFERRED designation
        if 'OFFICIAL' not in content and 'PREFERRED' not in content:
            self.issues.append(ValidationIssue(
                severity="INFO",
                category="terminology",
                language=lang,
                file=ref_file.name,
                line=0,
                message="File should specify OFFICIAL vs PREFERRED terminology",
                suggestion="Add note about translation requirements"
            ))

    def validate_all(self, languages: List[str] = None) -> bool:
        """Run all validations for specified languages."""
        if languages is None:
            languages = ['fr', 'es', 'ar']

        print("🔍 Validating Translation Guides\n")

        for lang in languages:
            print(f"Validating {lang.upper()}...")
            skill_dir = SKILLS_DIR / f'kobo-translation-{lang}'

            if not skill_dir.exists():
                self.issues.append(ValidationIssue(
                    severity="ERROR",
                    category="missing-file",
                    language=lang,
                    file="",
                    line=0,
                    message=f"Language directory missing: {skill_dir}",
                ))
                continue

            # Validate SKILL.md
            skill_file = skill_dir / 'SKILL.md'
            if skill_file.exists():
                content = skill_file.read_text(encoding='utf-8')

                self.validate_guide_structure(lang, content)
                self.validate_tables_completeness(lang, content)
                self.validate_language_specific_content(lang, content)
                self.validate_cross_references(lang, content, skill_dir)
                self.validate_terminology_consistency(lang, content)
            else:
                self.issues.append(ValidationIssue(
                    severity="ERROR",
                    category="missing-file",
                    language=lang,
                    file="SKILL.md",
                    line=0,
                    message="Main skill file missing",
                ))

            # Validate reference files
            ref_files = [
                'brand-terminology.md',
                'ui-terminology.md',
                'form-building-terms.md',
                'question-types.md',
                'data-collection-terms.md',
                'course-terminology.md'
            ]

            for ref in ref_files:
                ref_path = skill_dir / 'references' / ref
                self.validate_reference_file(lang, ref_path)

        return len([i for i in self.issues if i.severity == "ERROR"]) == 0

    def print_report(self) -> None:
        """Print validation report."""
        if not self.issues:
            print("\n✅ All validations passed!")
            return

        # Group by severity
        by_severity = defaultdict(list)
        for issue in self.issues:
            by_severity[issue.severity].append(issue)

        # Print summary
        print(f"\n📊 Validation Summary:")
        print(f"   ERRORS:   {len(by_severity['ERROR'])}")
        print(f"   WARNINGS: {len(by_severity['WARNING'])}")
        print(f"   INFO:     {len(by_severity['INFO'])}")

        # Print details
        for severity in ['ERROR', 'WARNING', 'INFO']:
            issues = by_severity[severity]
            if not issues:
                continue

            icon = {'ERROR': '❌', 'WARNING': '⚠️', 'INFO': 'ℹ️'}[severity]
            print(f"\n{icon} {severity}S:")

            for issue in issues:
                location = f"{issue.language.upper()}:{issue.file}"
                if issue.line:
                    location += f":{issue.line}"

                print(f"\n   [{location}]")
                print(f"   {issue.message}")
                if issue.suggestion:
                    print(f"   💡 {issue.suggestion}")


def main():
    parser = argparse.ArgumentParser(description='Validate translation guides')
    parser.add_argument('--language', '-l', type=str,
                       help='Validate specific language only (fr, es, ar)')
    parser.add_argument('--strict', '-s', action='store_true',
                       help='Strict mode: treat warnings as errors')
    parser.add_argument('--fix', '-f', action='store_true',
                       help='Auto-fix issues where possible')

    args = parser.parse_args()

    validator = GuideValidator(strict=args.strict)

    languages = [args.language] if args.language else ['fr', 'es', 'ar']
    success = validator.validate_all(languages)

    validator.print_report()

    if args.fix:
        print("\n🔧 Auto-fix is not yet implemented")
        print("   Consider using: python scripts/sync_terminology.py --auto-generate")

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    import argparse
    main()
