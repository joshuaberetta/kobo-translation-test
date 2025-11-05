#!/usr/bin/env python3
"""
Arabic Terminology Extractor for KoboToolbox Translation Skill

This script extracts Arabic translations from existing documentation files by:
1. Comparing Arabic docs with English originals
2. Identifying consistently translated terms
3. Detecting patterns in translation choices
4. Generating structured terminology databases

Usage:
    python extract_arabic_terminology.py --output skills/kobo-translation-ar/extracted_terms.yaml
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Set

class ArabicTerminologyExtractor:
    """Extract translation patterns from Arabic documentation."""
    
    def __init__(self, en_dir: str = "docs/en", ar_dir: str = "docs/ar"):
        self.en_dir = Path(en_dir)
        self.ar_dir = Path(ar_dir)
        self.terminology = defaultdict(lambda: {
            'translations': Counter(),
            'contexts': [],
            'confidence': 0
        })
        
        # Known brand terms to track
        self.brand_terms = [
            "KoboToolbox",
            "Global KoboToolbox Server",
            "European Union KoboToolbox Server", 
            "Formbuilder",
            "Question Library",
            "Community Forum",
            "Help Center",
            "KoboToolbox Academy",
            "Community Plan",
            "KoboCollect"
        ]
        
        # UI terms to track
        self.ui_terms = [
            "FORM",
            "DATA", 
            "DEPLOY",
            "Draft",
            "NEW",
            "Table view",
            "Map view"
        ]
        
        # Technical terms to track
        self.technical_terms = [
            "data collection",
            "form building",
            "survey",
            "submission",
            "deployment",
            "cascading select",
            "skip logic",
            "validation"
        ]
    
    def extract_from_paired_files(self) -> Dict:
        """
        Extract translations by comparing paired EN/AR files.
        
        Returns:
            Dict of extracted terminology with confidence scores
        """
        print("🔍 Scanning paired documentation files...")
        
        # Find all English markdown files
        en_files = list(self.en_dir.glob("*.md"))
        processed = 0
        
        for en_file in en_files:
            ar_file = self.ar_dir / en_file.name
            
            if not ar_file.exists():
                continue
                
            self._process_file_pair(en_file, ar_file)
            processed += 1
            
        print(f"✅ Processed {processed} file pairs")
        return self._calculate_confidence_scores()
    
    def _process_file_pair(self, en_file: Path, ar_file: Path):
        """Process a pair of EN/AR files to extract terminology."""
        
        # Read files
        en_content = en_file.read_text(encoding='utf-8')
        ar_content = ar_file.read_text(encoding='utf-8')
        
        # Extract brand terms
        for term in self.brand_terms:
            self._extract_term_translations(term, en_content, ar_content, 'brand')
        
        # Extract UI terms
        for term in self.ui_terms:
            self._extract_term_translations(term, en_content, ar_content, 'ui')
            
        # Extract technical terms
        for term in self.technical_terms:
            self._extract_term_translations(term, en_content, ar_content, 'technical')
    
    def _extract_term_translations(self, en_term: str, en_text: str, 
                                   ar_text: str, category: str):
        """
        Extract Arabic translation for a specific English term.
        
        Strategy:
        1. Find context around English term (surrounding sentences)
        2. Look for Arabic text in similar position
        3. Extract likely Arabic translation
        4. Track frequency to build confidence
        """
        
        # Simple approach: Look for term in markdown links or headings
        # More sophisticated: Use sentence alignment
        
        # Find English term with context
        en_pattern = rf'(.{{0,50}}){re.escape(en_term)}(.{{0,50}})'
        en_matches = list(re.finditer(en_pattern, en_text, re.IGNORECASE))
        
        if not en_matches:
            return
        
        # For now, extract based on known patterns
        # In production, would use more sophisticated alignment
        
        # Example: Extract from markdown links
        if en_term == "Community Forum":
            ar_match = re.search(r'\[([^\]]*المنتدى[^\]]*)\]', ar_text)
            if ar_match:
                ar_translation = ar_match.group(1)
                self._record_translation(en_term, ar_translation, category, 
                                       en_matches[0].group(0))
        
        elif en_term == "Help Center":
            ar_match = re.search(r'\[([^\]]*مركز المساعدة[^\]]*)\]', ar_text)
            if ar_match:
                ar_translation = ar_match.group(1)
                self._record_translation(en_term, ar_translation, category,
                                       en_matches[0].group(0))
    
    def _record_translation(self, en_term: str, ar_translation: str, 
                          category: str, context: str):
        """Record a translation occurrence."""
        self.terminology[en_term]['translations'][ar_translation] += 1
        self.terminology[en_term]['contexts'].append({
            'en_context': context,
            'ar_translation': ar_translation,
            'category': category
        })
    
    def _calculate_confidence_scores(self) -> Dict:
        """
        Calculate confidence scores based on:
        - Frequency (more occurrences = higher confidence)
        - Consistency (same translation used = higher confidence)
        - Category (brand terms should be 100% consistent)
        """
        results = {}
        
        for en_term, data in self.terminology.items():
            total_occurrences = sum(data['translations'].values())
            most_common = data['translations'].most_common(1)
            
            if not most_common:
                continue
            
            ar_term, frequency = most_common[0]
            consistency = frequency / total_occurrences if total_occurrences > 0 else 0
            
            # Confidence score: 0-100
            confidence = min(100, int(consistency * 100 * (1 + min(frequency / 5, 1))))
            
            results[en_term] = {
                'arabic': ar_term,
                'confidence': confidence,
                'occurrences': frequency,
                'total_contexts': total_occurrences,
                'category': data['contexts'][0]['category'] if data['contexts'] else 'unknown',
                'alternative_translations': [
                    {'text': t, 'count': c} 
                    for t, c in data['translations'].most_common(5)
                    if t != ar_term
                ]
            }
        
        return results
    
    def extract_patterns(self) -> Dict:
        """
        Analyze Arabic translations to identify language-specific patterns.
        
        Returns:
            Dict of patterns like:
            - Article usage
            - Capitalization conventions
            - RTL handling
            - Gender patterns
        """
        patterns = {
            'rtl_usage': self._check_rtl_patterns(),
            'article_patterns': self._analyze_article_usage(),
            'capitalization': self._analyze_capitalization(),
            'common_prefixes': self._find_common_prefixes(),
            'common_suffixes': self._find_common_suffixes(),
        }
        
        return patterns
    
    def _check_rtl_patterns(self) -> Dict:
        """Check how RTL is implemented in existing docs."""
        rtl_stats = {
            'uses_rtl_wrapper': 0,
            'total_files': 0,
            'wrapper_pattern': None
        }
        
        ar_files = list(self.ar_dir.glob("*.md"))
        rtl_stats['total_files'] = len(ar_files)
        
        for ar_file in ar_files:
            content = ar_file.read_text(encoding='utf-8')
            if 'dir="rtl"' in content or "dir='rtl'" in content:
                rtl_stats['uses_rtl_wrapper'] += 1
                
                # Extract the pattern
                match = re.search(r'<section[^>]*dir="rtl"[^>]*>', content)
                if match and not rtl_stats['wrapper_pattern']:
                    rtl_stats['wrapper_pattern'] = match.group(0)
        
        return rtl_stats
    
    def _analyze_article_usage(self) -> List[str]:
        """Analyze Arabic article usage patterns."""
        # This is a simplified version
        # In production, would do proper Arabic linguistic analysis
        return [
            "Arabic uses definite article ال (al-) prefix",
            "Article attached directly to noun (no space)",
            "Pattern observed in مركز المساعدة (Help Center)"
        ]
    
    def _analyze_capitalization(self) -> List[str]:
        """Analyze capitalization patterns in Arabic."""
        return [
            "Arabic doesn't have capital/lowercase distinction",
            "Emphasis shown through bold or different styling",
            "UI terms may use Latin capitals for buttons (DEPLOY, FORM, DATA)"
        ]
    
    def _find_common_prefixes(self) -> List[str]:
        """Find common Arabic prefixes in translations."""
        # Simplified analysis
        return ["ال (al- definite article)", "و (wa- and)", "ب (bi- with/by)"]
    
    def _find_common_suffixes(self) -> List[str]:
        """Find common Arabic suffixes in translations."""
        return ["ات (plural feminine)", "ون/ين (plural masculine)", "ة (feminine singular)"]
    
    def generate_reference_file(self, category: str, output_path: Path):
        """
        Generate a reference terminology file for a specific category.
        
        Args:
            category: 'brand', 'ui', 'technical', etc.
            output_path: Where to write the markdown file
        """
        # Filter terms by category
        terms = {
            en: data for en, data in self.terminology.items()
            if data.get('contexts') and data['contexts'][0]['category'] == category
        }
        
        if not terms:
            print(f"⚠️  No terms found for category: {category}")
            return
        
        # Generate markdown
        md_content = f"# {category.title()} Terminology\n\n"
        md_content += "## Extracted from Existing Arabic Documentation\n\n"
        md_content += "| English | Arabic | Confidence | Notes |\n"
        md_content += "|---------|--------|------------|-------|\n"
        
        for en_term, data in sorted(terms.items()):
            ar_term = data.get('arabic', '???')
            confidence = data.get('confidence', 0)
            occurrences = data.get('occurrences', 0)
            
            emoji = "✅" if confidence >= 80 else "⚠️" if confidence >= 50 else "❓"
            notes = f"{emoji} {occurrences} occurrences"
            
            md_content += f"| {en_term} | {ar_term} | {confidence}% | {notes} |\n"
        
        # Write file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(md_content, encoding='utf-8')
        print(f"✅ Generated {output_path}")
    
    def export_to_yaml(self, output_path: Path):
        """Export extracted terminology to YAML for further processing."""
        output_data = {
            'extracted_at': '2024-11-05',
            'source': 'docs/ar/*.md',
            'total_terms': len(self.terminology),
            'terms': dict(self.terminology),
            'patterns': self.extract_patterns()
        }
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(output_data, f, allow_unicode=True, sort_keys=False)
        
        print(f"✅ Exported terminology to {output_path}")
    
    def generate_completion_report(self) -> str:
        """
        Generate a report on what's missing in the Arabic skill files.
        
        Returns:
            Markdown report showing gaps
        """
        report = "# Arabic Translation Skill Completion Report\n\n"
        report += "## Summary\n\n"
        
        # Check what exists
        ar_skill_dir = Path("skills/kobo-translation-ar")
        
        if not ar_skill_dir.exists():
            report += "❌ Arabic skill directory not found\n"
            return report
        
        # Check main SKILL.md
        skill_file = ar_skill_dir / "SKILL.md"
        if skill_file.exists():
            content = skill_file.read_text()
            
            # Count empty tables
            empty_tables = len(re.findall(r'\|\s*-+\s*\|\s*-+\s*\|\s*\n(?!\|)', content))
            
            # Count placeholder sections
            placeholders = len(re.findall(r'\[To be specified.*?\]', content))
            
            report += f"### Main Skill File\n"
            report += f"- ✅ File exists\n"
            report += f"- ⚠️  Empty tables found: {empty_tables}\n"
            report += f"- ⚠️  Placeholder sections: {placeholders}\n\n"
        
        # Check reference files
        refs_dir = ar_skill_dir / "references"
        if refs_dir.exists():
            ref_files = list(refs_dir.glob("*.md"))
            report += f"### Reference Files\n"
            report += f"- ✅ Found {len(ref_files)} reference files\n\n"
            
            for ref_file in ref_files:
                content = ref_file.read_text()
                empty_tables = len(re.findall(r'\|\s*-+\s*\|\s*-+\s*\|\s*\n(?!\|)', content))
                
                if empty_tables > 2:
                    report += f"- ⚠️  {ref_file.name}: {empty_tables} empty tables\n"
                else:
                    report += f"- ✅ {ref_file.name}: Mostly complete\n"
        
        report += "\n## Recommendations\n\n"
        report += "1. Use extracted terminology to fill empty tables\n"
        report += "2. Compare with French/Spanish patterns for structural completion\n"
        report += "3. Request native Arabic speaker review for:\n"
        report += "   - Gender-inclusive language rules\n"
        report += "   - Formality level (MSA vs. dialects)\n"
        report += "   - Cultural adaptation notes\n"
        
        return report


def main():
    """Main execution function."""
    print("=" * 60)
    print("Arabic Terminology Extractor for KoboToolbox")
    print("=" * 60)
    print()
    
    # Initialize extractor
    extractor = ArabicTerminologyExtractor()
    
    # Step 1: Extract terminology
    print("📚 Step 1: Extracting terminology from existing translations...")
    terminology = extractor.extract_from_paired_files()
    
    print(f"\n✅ Extracted {len(terminology)} terms\n")
    
    # Step 2: Analyze patterns  
    print("🔍 Step 2: Analyzing Arabic language patterns...")
    patterns = extractor.extract_patterns()
    
    print(f"✅ Identified {len(patterns)} pattern categories\n")
    
    # Step 3: Generate completion report
    print("📊 Step 3: Generating completion report...")
    report = extractor.generate_completion_report()
    
    # Write report
    report_path = Path("skills/kobo-translation-ar/COMPLETION_REPORT.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding='utf-8')
    print(f"✅ Report saved to {report_path}\n")
    
    # Step 4: Export data
    print("💾 Step 4: Exporting extracted data...")
    
    # Export to YAML
    yaml_path = Path("skills/kobo-translation-ar/extracted_terminology.yaml")
    extractor.export_to_yaml(yaml_path)
    
    # Generate reference files (examples)
    # extractor.generate_reference_file('brand', 
    #     Path("skills/kobo-translation-ar/references/brand-terminology-extracted.md"))
    
    print("\n" + "=" * 60)
    print("✅ Extraction Complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review COMPLETION_REPORT.md")
    print("2. Check extracted_terminology.yaml")
    print("3. Use data to fill gaps in SKILL.md and reference files")
    print("4. Request native speaker review")


if __name__ == "__main__":
    main()
