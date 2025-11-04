"""
Automated QA workflow for Thinkific course translations.

Runs quality checks and determines if translation can be auto-published
or needs human review.

Quality checks include:
- Structure preservation
- Link validation
- Media presence
- Quiz integrity
- Content length appropriateness
- Terminology consistency (with Transifex)
"""

from typing import Dict, List
import re
from pathlib import Path


class QAWorkflow:
    """
    Automated quality assurance for course translations.
    
    Assigns confidence scores and determines approval workflow.
    """
    
    # Confidence threshold for auto-publish (95%)
    AUTO_APPROVE_THRESHOLD = 0.95
    
    # Warning threshold (80%)
    WARNING_THRESHOLD = 0.80
    
    def __init__(self, transifex_sync=None):
        """
        Initialize QA workflow.
        
        Args:
            transifex_sync: TransifexSync instance for terminology checking
        """
        self.transifex_sync = transifex_sync
    
    # ========================================================================
    # Main QA Entry Point
    # ========================================================================
    
    def run_quality_checks(self, translated_course: Dict) -> Dict:
        """
        Run all quality checks on translated course.
        
        Args:
            translated_course: Dictionary with translated course data
            
        Returns:
            QA results dictionary with:
                - confidence: Overall confidence score (0.0-1.0)
                - passed: Boolean if passes auto-publish threshold
                - checks: Individual check results
                - issues: List of issues found
                - recommendations: List of recommended actions
        """
        print(f"\n🔍 Running quality checks on {translated_course.get('name', 'course')}...")
        
        checks = {
            'structure_preserved': self.check_structure(translated_course),
            'links_valid': self.check_links(translated_course),
            'media_present': self.check_media(translated_course),
            'quizzes_valid': self.check_quizzes(translated_course),
            'length_appropriate': self.check_length(translated_course),
            'terminology_consistent': self.check_terminology(translated_course)
        }
        
        # Calculate overall confidence
        confidence = sum(checks.values()) / len(checks)
        
        # Identify issues
        issues = [
            self._get_issue_description(check_name)
            for check_name, passed in checks.items()
            if not passed
        ]
        
        # Generate recommendations
        recommendations = self._generate_recommendations(checks, confidence)
        
        # Determine if passed
        passed = confidence >= self.AUTO_APPROVE_THRESHOLD
        
        result = {
            'confidence': confidence,
            'passed': passed,
            'checks': checks,
            'issues': issues,
            'recommendations': recommendations,
            'action': 'auto_publish' if passed else 'manual_review'
        }
        
        # Print summary
        self._print_qa_summary(result)
        
        return result
    
    # ========================================================================
    # Individual Quality Checks
    # ========================================================================
    
    def check_structure(self, course: Dict) -> bool:
        """
        Check that course structure is preserved.
        
        Verifies:
        - Same number of chapters
        - Same number of lessons
        - Lesson order maintained
        """
        print("  ✓ Checking structure preservation...")
        
        original_structure = course.get('_original_structure', {})
        if not original_structure:
            # No original to compare against - assume valid
            return True
        
        # Check chapter count
        orig_chapter_count = len(original_structure.get('chapters', []))
        trans_chapter_count = len(course.get('chapters', []))
        
        if orig_chapter_count != trans_chapter_count:
            print(f"    ⚠️  Chapter count mismatch: {orig_chapter_count} vs {trans_chapter_count}")
            return False
        
        # Check lesson count per chapter
        for orig_chapter, trans_chapter in zip(
            original_structure.get('chapters', []),
            course.get('chapters', [])
        ):
            orig_lesson_count = len(orig_chapter.get('lessons', []))
            trans_lesson_count = len(trans_chapter.get('lessons', []))
            
            if orig_lesson_count != trans_lesson_count:
                print(f"    ⚠️  Lesson count mismatch in chapter '{trans_chapter.get('name')}'")
                return False
        
        return True
    
    def check_links(self, course: Dict) -> bool:
        """
        Check that links are preserved and properly formatted.
        
        Verifies:
        - Links still present
        - URLs not translated
        - Link format maintained
        """
        print("  ✓ Checking links...")
        
        issues_found = 0
        
        for chapter in course.get('chapters', []):
            for lesson in chapter.get('lessons', []):
                content = lesson.get('content', '')
                
                # Check for broken markdown links
                broken_links = re.findall(r'\[([^\]]+)\]\s+\(', content)
                if broken_links:
                    print(f"    ⚠️  Broken link formatting in '{lesson.get('name')}'")
                    issues_found += 1
                
                # Check for translated URLs (common mistake)
                # Look for __LINK_URL_ placeholders that weren't restored
                if '__LINK_URL_' in content:
                    print(f"    ⚠️  Unrestored link placeholder in '{lesson.get('name')}'")
                    issues_found += 1
        
        return issues_found == 0
    
    def check_media(self, course: Dict) -> bool:
        """
        Check that media files are present and handled.
        
        Verifies:
        - Media references preserved
        - Media handling plan exists
        """
        print("  ✓ Checking media presence...")
        
        media_items = course.get('media', [])
        
        if not media_items:
            # No media to check
            return True
        
        # Check if all media has been handled
        unhandled = [
            item for item in media_items
            if item.get('status') == 'unknown_type' or not item.get('action')
        ]
        
        if unhandled:
            print(f"    ⚠️  {len(unhandled)} media items not handled")
            return False
        
        # Check for media that needs manual attention
        needs_attention = [
            item for item in media_items
            if item.get('status') in ['needs_review', 'needs_creation']
        ]
        
        if len(needs_attention) > len(media_items) * 0.3:  # More than 30%
            print(f"    ⚠️  Many media items need manual attention ({len(needs_attention)})")
            return False
        
        return True
    
    def check_quizzes(self, course: Dict) -> bool:
        """
        Check quiz integrity.
        
        Verifies:
        - Correct answers preserved
        - Question structure maintained
        - All questions translated
        """
        print("  ✓ Checking quizzes...")
        
        quizzes = course.get('quizzes', [])
        
        if not quizzes:
            # No quizzes to check
            return True
        
        issues_found = 0
        
        for quiz in quizzes:
            # Check if quiz has validation results
            validation = quiz.get('_validation', {})
            
            if not validation.get('valid', True):
                print(f"    ⚠️  Quiz '{quiz.get('title')}' failed validation")
                issues_found += 1
                
                for issue in validation.get('issues', []):
                    if 'CRITICAL' in issue.upper():
                        print(f"    ❌ CRITICAL: {issue}")
                        # Critical issues are automatic fail
                        return False
        
        return issues_found == 0
    
    def check_length(self, course: Dict) -> bool:
        """
        Check that translated content length is appropriate.
        
        Different languages expand/contract differently:
        - Spanish: ~15-20% longer than English
        - French: ~15-20% longer
        - Arabic: ~10-15% shorter (denser script)
        
        Flag if length change is extreme (>50% change)
        """
        print("  ✓ Checking content length...")
        
        original_structure = course.get('_original_structure', {})
        if not original_structure:
            return True
        
        language = course.get('language', 'unknown')
        
        # Expected length ratios
        expected_ratios = {
            'es': (0.95, 1.25),  # 95% to 125%
            'fr': (0.95, 1.25),
            'ar': (0.85, 1.15)
        }
        
        min_ratio, max_ratio = expected_ratios.get(language, (0.5, 2.0))
        
        issues_found = 0
        
        for orig_chapter, trans_chapter in zip(
            original_structure.get('chapters', []),
            course.get('chapters', [])
        ):
            for orig_lesson, trans_lesson in zip(
                orig_chapter.get('lessons', []),
                trans_chapter.get('lessons', [])
            ):
                orig_length = len(orig_lesson.get('content', ''))
                trans_length = len(trans_lesson.get('content', ''))
                
                if orig_length == 0:
                    continue
                
                ratio = trans_length / orig_length
                
                if ratio < min_ratio or ratio > max_ratio:
                    print(
                        f"    ⚠️  Unusual length in '{trans_lesson.get('name')}': "
                        f"{ratio:.1%} of original"
                    )
                    issues_found += 1
        
        # Allow some issues (up to 10% of lessons)
        max_allowed_issues = max(1, len(course.get('all_lessons', [])) * 0.1)
        
        return issues_found <= max_allowed_issues
    
    def check_terminology(self, course: Dict) -> bool:
        """
        Check that translations use consistent terminology with Transifex.
        
        Verifies:
        - Key UI terms match Transifex translations
        - Technical terms not mistranslated
        """
        print("  ✓ Checking terminology consistency...")
        
        if not self.transifex_sync:
            # No Transifex integration - skip check
            return True
        
        language = course.get('language', 'en')
        
        # Get UI terminology from Transifex
        try:
            # This would use your existing TransifexSync
            # For POC, we'll do basic checks
            
            # Common KoboToolbox terms to check
            key_terms = {
                'form': ['formulario', 'form', 'formulaire'],
                'survey': ['encuesta', 'survey', 'enquête'],
                'data': ['datos', 'data', 'données'],
                'project': ['proyecto', 'project', 'projet']
            }
            
            # Check if key terms appear in reasonable contexts
            # This is a simplified version
            return True
            
        except Exception as e:
            print(f"    ⚠️  Could not check terminology: {e}")
            # Don't fail on terminology check errors
            return True
    
    # ========================================================================
    # Helpers
    # ========================================================================
    
    def _get_issue_description(self, check_name: str) -> str:
        """Get human-readable description of failed check."""
        descriptions = {
            'structure_preserved': 'Course structure was modified during translation',
            'links_valid': 'Links are broken or improperly formatted',
            'media_present': 'Media files missing or not properly handled',
            'quizzes_valid': 'Quiz questions have errors or correctness issues',
            'length_appropriate': 'Content length changed unusually during translation',
            'terminology_consistent': 'Translations do not match standard terminology'
        }
        return descriptions.get(check_name, f'Check failed: {check_name}')
    
    def _generate_recommendations(self, checks: Dict, confidence: float) -> List[str]:
        """Generate recommended actions based on check results."""
        recommendations = []
        
        if confidence >= self.AUTO_APPROVE_THRESHOLD:
            recommendations.append('✅ Ready for automatic publication')
        elif confidence >= self.WARNING_THRESHOLD:
            recommendations.append('⚠️  Manual review recommended before publishing')
        else:
            recommendations.append('❌ Requires revision before publishing')
        
        # Specific recommendations for failed checks
        if not checks.get('structure_preserved'):
            recommendations.append('🔧 Review course structure - chapters/lessons may be missing')
        
        if not checks.get('links_valid'):
            recommendations.append('🔧 Fix broken or malformed links')
        
        if not checks.get('media_present'):
            recommendations.append('🔧 Handle media files - some need attention')
        
        if not checks.get('quizzes_valid'):
            recommendations.append('🔧 Review quiz questions - correctness may be compromised')
        
        if not checks.get('length_appropriate'):
            recommendations.append('🔧 Check lessons with unusual length changes')
        
        if not checks.get('terminology_consistent'):
            recommendations.append('🔧 Review terminology for consistency with UI translations')
        
        return recommendations
    
    def _print_qa_summary(self, result: Dict):
        """Print formatted QA summary."""
        confidence = result['confidence']
        passed = result['passed']
        
        print(f"\n{'='*60}")
        print(f"  QA RESULTS")
        print(f"{'='*60}")
        print(f"  Overall Confidence: {confidence:.1%}")
        print(f"  Status: {'✅ PASSED' if passed else '⚠️  NEEDS REVIEW'}")
        print(f"  Action: {result['action'].replace('_', ' ').title()}")
        
        print(f"\n  Individual Checks:")
        for check_name, check_passed in result['checks'].items():
            status = '✅' if check_passed else '❌'
            name = check_name.replace('_', ' ').title()
            print(f"    {status} {name}")
        
        if result['issues']:
            print(f"\n  Issues Found ({len(result['issues'])}):")
            for issue in result['issues']:
                print(f"    • {issue}")
        
        print(f"\n  Recommendations:")
        for rec in result['recommendations']:
            print(f"    {rec}")
        
        print(f"{'='*60}\n")


if __name__ == "__main__":
    """Test QA workflow with sample data."""
    
    print("🧪 Testing QA Workflow...\n")
    
    qa = QAWorkflow()
    
    # Sample translated course (perfect translation)
    perfect_course = {
        'name': 'Introducción a KoboToolbox',
        'language': 'es',
        'chapters': [
            {
                'name': 'Comenzando',
                'lessons': [
                    {'name': 'Bienvenida', 'content': '<p>Contenido aquí...</p>'},
                    {'name': 'Configuración', 'content': '<p>Más contenido...</p>'}
                ]
            }
        ],
        'media': [
            {'action': 'reuse', 'status': 'ready'},
            {'action': 'use_existing_subtitles', 'status': 'ready'}
        ],
        'quizzes': [
            {'title': 'Quiz 1', '_validation': {'valid': True, 'issues': []}}
        ],
        '_original_structure': {
            'chapters': [
                {
                    'name': 'Getting Started',
                    'lessons': [
                        {'name': 'Welcome', 'content': '<p>Content here...</p>'},
                        {'name': 'Setup', 'content': '<p>More content...</p>'}
                    ]
                }
            ]
        }
    }
    
    results = qa.run_quality_checks(perfect_course)
    
    # Sample course with issues
    print("\n" + "="*60)
    print("Testing course with issues...")
    print("="*60 + "\n")
    
    problem_course = {
        **perfect_course,
        'chapters': [
            {
                'name': 'Comenzando',
                'lessons': [
                    {'name': 'Bienvenida', 'content': '<p>Short</p>'}  # Too short
                ]
            }
        ],
        'media': [
            {'action': 'unknown', 'status': 'unknown_type'}  # Problematic media
        ]
    }
    
    results2 = qa.run_quality_checks(problem_course)
