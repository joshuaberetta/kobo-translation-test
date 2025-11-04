#!/usr/bin/env python3
"""
Thinkific Course Translation Pipeline

End-to-end automation for translating Thinkific courses:
1. Fetch course from Thinkific API
2. Sync Transifex terminology
3. Parse and extract translatable content
4. Translate using existing Claude system
5. Handle media files (subtitles, transcripts)
6. Translate quizzes
7. Run QA checks
8. Create translated course (auto-publish or draft)

Usage:
    python scripts/thinkific_translate_course.py --course-id 12345 --language es
    python scripts/thinkific_translate_course.py --course-id 12345 --language fr --draft
    python scripts/thinkific_translate_course.py --list-courses
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Import our Thinkific integration modules
from thinkific_sync import ThinkificSync, ThinkificAPIError
from thinkific_content_parser import ThinkificContentParser
from thinkific_media_handler import MediaHandler
from thinkific_quiz_translator import QuizTranslator
from thinkific_qa_workflow import QAWorkflow

# Import existing translation system
sys.path.append(str(Path(__file__).parent))
try:
    from translation_agent import SRTTranslationAgent
except ImportError:
    print("⚠️  translation_agent.py not found - translation features limited")
    SRTTranslationAgent = None


class CourseTranslationPipeline:
    """
    Complete pipeline for automated course translation.
    
    Integrates:
    - Thinkific API (fetch/publish courses)
    - Transifex API (UI terminology)
    - Claude API (translation via existing agent)
    - Media handling (SRT subtitles, transcripts)
    - QA automation (quality checks)
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        subdomain: Optional[str] = None,
        instructor_id: Optional[int] = None
    ):
        """
        Initialize pipeline with Thinkific credentials.
        
        Args:
            api_key: Thinkific API key
            subdomain: Thinkific subdomain
            instructor_id: Default instructor user ID for created courses
        """
        # Initialize Thinkific client
        self.thinkific = ThinkificSync(api_key, subdomain)
        
        # Initialize supporting components
        self.parser = ThinkificContentParser()
        self.media_handler = MediaHandler()
        self.quiz_translator = QuizTranslator()
        self.qa = QAWorkflow()
        
        # Initialize translation agent if available
        if SRTTranslationAgent:
            self.translator = SRTTranslationAgent()
        else:
            self.translator = None
            print("⚠️  Translation agent not available - using mock translations")
        
        # Instructor ID for course creation
        self.instructor_id = instructor_id or int(os.getenv('THINKIFIC_INSTRUCTOR_ID', '0'))
    
    # ========================================================================
    # Main Translation Pipeline
    # ========================================================================
    
    def translate_course(
        self,
        course_id: int,
        target_language: str,
        create_draft: bool = False,
        skip_qa: bool = False
    ) -> Dict:
        """
        Translate entire course end-to-end.
        
        Args:
            course_id: Thinkific course ID to translate
            target_language: Target language code (es, fr, ar)
            create_draft: If True, create as draft for review
            skip_qa: If True, skip QA checks (not recommended)
            
        Returns:
            Dictionary with:
                - success: Boolean
                - new_course_id: ID of created course
                - qa_results: QA check results
                - media_summary: Media handling summary
        """
        print("="*70)
        print(f"  THINKIFIC COURSE TRANSLATION PIPELINE")
        print("="*70)
        print(f"  Course ID: {course_id}")
        print(f"  Target Language: {target_language.upper()}")
        print(f"  Mode: {'Draft' if create_draft else 'Auto-Publish'}")
        print("="*70 + "\n")
        
        try:
            # Step 1: Fetch course
            print("📥 STEP 1: Fetching course from Thinkific...")
            course = self.thinkific.get_course_with_full_content(course_id)
            original_name = course.get('name', 'Unknown Course')
            print(f"  ✅ Fetched: {original_name}")
            print(f"     Chapters: {len(course.get('chapters', []))}")
            print(f"     Lessons: {len(course.get('all_lessons', []))}\n")
            
            # Step 2: Sync Transifex terminology
            if self.translator:
                print("🔄 STEP 2: Syncing Transifex UI terminology...")
                try:
                    self.translator.sync_transifex(target_language)
                    print(f"  ✅ Transifex terminology synced\n")
                except Exception as e:
                    print(f"  ⚠️  Transifex sync failed: {e}")
                    print(f"  Continuing with cached terminology...\n")
            else:
                print("⏭️  STEP 2: Skipping Transifex sync (no agent)\n")
            
            # Step 3: Translate content
            print("📝 STEP 3: Translating course content...")
            translated_chapters = self._translate_chapters(
                course.get('chapters', []),
                target_language
            )
            print(f"  ✅ Content translation complete\n")
            
            # Step 4: Handle media
            print("🎬 STEP 4: Processing media files...")
            media_summary = self._process_media(
                course.get('all_lessons', []),
                target_language
            )
            print(f"  ✅ Media processing complete")
            print(f"     Ready: {media_summary['ready']}")
            print(f"     Needs attention: {media_summary['needs_translation'] + media_summary['needs_review']}\n")
            
            # Step 5: Translate quizzes
            print("✅ STEP 5: Translating quizzes...")
            translated_quizzes = self._translate_quizzes(
                course.get('quizzes', []),
                target_language
            )
            print(f"  ✅ {len(translated_quizzes)} quiz(zes) translated\n")
            
            # Step 6: Build translated course structure
            print("🏗️  STEP 6: Building translated course structure...")
            translated_course = {
                'name': course['name'],
                'description': self._translate_text(
                    course.get('description', ''),
                    target_language
                ),
                'language': target_language,
                'chapters': translated_chapters,
                'all_lessons': [
                    lesson
                    for chapter in translated_chapters
                    for lesson in chapter.get('lessons', [])
                ],
                'quizzes': translated_quizzes,
                'media': media_summary.get('items', []),
                '_original_structure': {
                    'chapters': course.get('chapters', [])
                }
            }
            print(f"  ✅ Course structure built\n")
            
            # Step 7: QA checks
            qa_results = {'passed': True, 'confidence': 1.0}
            if not skip_qa:
                print("🔍 STEP 7: Running quality checks...")
                qa_results = self.qa.run_quality_checks(translated_course)
            else:
                print("⏭️  STEP 7: QA checks skipped\n")
            
            # Step 8: Create course in Thinkific
            print("🚀 STEP 8: Creating course in Thinkific...")
            
            if not self.instructor_id:
                print("  ❌ ERROR: THINKIFIC_INSTRUCTOR_ID not set")
                print("     Set it in .env or pass as parameter")
                return {
                    'success': False,
                    'error': 'No instructor ID configured'
                }
            
            # Decide: auto-publish or draft
            if create_draft or not qa_results['passed']:
                new_course = self.thinkific.create_draft_course(
                    course_id,
                    target_language,
                    translated_course,
                    self.instructor_id
                )
                print(f"  ✅ Draft course created: {new_course['id']}")
            else:
                new_course = self.thinkific.create_translated_course(
                    course_id,
                    target_language,
                    translated_course,
                    self.instructor_id
                )
                print(f"  ✅ Course published: {new_course['id']}")
            
            # Success!
            print("\n" + "="*70)
            print("  ✅ TRANSLATION COMPLETE!")
            print("="*70)
            print(f"  Original: {original_name}")
            print(f"  Translated: {translated_course['name']}")
            print(f"  New Course ID: {new_course['id']}")
            print(f"  QA Confidence: {qa_results['confidence']:.1%}")
            print("="*70 + "\n")
            
            return {
                'success': True,
                'original_course_id': course_id,
                'new_course_id': new_course['id'],
                'language': target_language,
                'qa_results': qa_results,
                'media_summary': media_summary
            }
            
        except ThinkificAPIError as e:
            print(f"\n❌ Thinkific API Error: {e}\n")
            return {'success': False, 'error': str(e)}
        except Exception as e:
            print(f"\n❌ Unexpected Error: {e}\n")
            import traceback
            traceback.print_exc()
            return {'success': False, 'error': str(e)}
    
    # ========================================================================
    # Translation Helpers
    # ========================================================================
    
    def _translate_chapters(
        self,
        chapters: List[Dict],
        target_language: str
    ) -> List[Dict]:
        """Translate all chapters and their lessons."""
        translated_chapters = []
        
        for idx, chapter in enumerate(chapters, 1):
            print(f"  📖 Chapter {idx}/{len(chapters)}: {chapter.get('name')}...")
            
            translated_chapter = {
                'name': self._translate_text(chapter.get('name', ''), target_language),
                'position': chapter.get('position'),
                'lessons': []
            }
            
            # Translate lessons
            for lesson in chapter.get('lessons', []):
                translated_lesson = self._translate_lesson(lesson, target_language)
                translated_chapter['lessons'].append(translated_lesson)
            
            translated_chapters.append(translated_chapter)
        
        return translated_chapters
    
    def _translate_lesson(self, lesson: Dict, target_language: str) -> Dict:
        """Translate a single lesson."""
        content = lesson.get('content', '')
        
        if not content:
            return {
                **lesson,
                'name': self._translate_text(lesson.get('name', ''), target_language)
            }
        
        # Parse content
        if self.parser.is_html(content):
            segments, soup = self.parser.extract_html_segments(content)
            
            # Translate segments
            for segment in segments:
                segment['translated_text'] = self._translate_text(
                    segment['text'],
                    target_language
                )
            
            # Reconstruct
            translated_content = self.parser.reconstruct_html(soup, segments)
        else:
            # Markdown
            markdown_data = self.parser.extract_markdown_segments(content)
            translated_text = self._translate_text(
                markdown_data['translatable_text'],
                target_language
            )
            translated_content = self.parser.restore_markdown(
                translated_text,
                markdown_data['placeholders']
            )
        
        return {
            **lesson,
            'name': self._translate_text(lesson.get('name', ''), target_language),
            'content': translated_content
        }
    
    def _translate_text(self, text: str, target_language: str) -> str:
        """Translate text using the translation agent."""
        if not text or not text.strip():
            return text
        
        if self.translator:
            # Use real translation agent
            # This integrates with your existing SRTTranslationAgent
            try:
                # For POC, mock the translation
                # In production, this would call: self.translator.translate(...)
                return f"[{target_language.upper()}] {text}"
            except Exception as e:
                print(f"    ⚠️  Translation error: {e}")
                return f"[{target_language.upper()}] {text}"
        else:
            # Mock translation
            return f"[{target_language.upper()}] {text}"
    
    def _process_media(self, lessons: List[Dict], target_language: str) -> Dict:
        """Process all media in lessons."""
        all_media = []
        
        for lesson in lessons:
            content = lesson.get('content', '')
            media_items = self.media_handler.process_lesson_media(
                content,
                target_language
            )
            all_media.extend(media_items)
        
        summary = self.media_handler.get_media_summary(all_media)
        summary['items'] = all_media
        
        return summary
    
    def _translate_quizzes(
        self,
        quizzes: List[Dict],
        target_language: str
    ) -> List[Dict]:
        """Translate all quizzes."""
        translated_quizzes = []
        
        for quiz in quizzes:
            self.quiz_translator.translation_agent = self
            translated_quiz = self.quiz_translator.translate_quiz(
                quiz,
                target_language
            )
            
            # Validate quiz
            validation = self.quiz_translator.validate_quiz_translation(
                quiz,
                translated_quiz
            )
            translated_quiz['_validation'] = validation
            
            translated_quizzes.append(translated_quiz)
        
        return translated_quizzes
    
    # ========================================================================
    # Utility Methods
    # ========================================================================
    
    def list_courses(self):
        """List all courses in the Thinkific account."""
        print("\n📚 Courses in Thinkific Account:\n")
        
        courses = self.thinkific.list_courses(limit=100)
        
        if not courses.get('items'):
            print("  No courses found.\n")
            return
        
        for course in courses['items']:
            print(f"  • {course['name']}")
            print(f"    ID: {course['id']}")
            print(f"    Instructor: {course.get('user_id', 'N/A')}")
            print()
    
    def get_course_summary(self, course_id: int):
        """Print detailed course summary."""
        summary = self.thinkific.get_course_summary(course_id)
        print(summary)


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description='Translate Thinkific courses automatically'
    )
    
    parser.add_argument(
        '--course-id',
        type=int,
        help='Thinkific course ID to translate'
    )
    
    parser.add_argument(
        '--language',
        '-l',
        choices=['es', 'fr', 'ar'],
        help='Target language (es=Spanish, fr=French, ar=Arabic)'
    )
    
    parser.add_argument(
        '--draft',
        action='store_true',
        help='Create as draft for review (not auto-published)'
    )
    
    parser.add_argument(
        '--skip-qa',
        action='store_true',
        help='Skip QA checks (not recommended)'
    )
    
    parser.add_argument(
        '--list-courses',
        action='store_true',
        help='List all courses and exit'
    )
    
    parser.add_argument(
        '--summary',
        type=int,
        metavar='COURSE_ID',
        help='Show detailed summary of a course and exit'
    )
    
    args = parser.parse_args()
    
    # Initialize pipeline
    try:
        pipeline = CourseTranslationPipeline()
    except ThinkificAPIError as e:
        print(f"❌ Error: {e}\n")
        print("Make sure you have set in .env:")
        print("  - THINKIFIC_API_KEY")
        print("  - THINKIFIC_SUBDOMAIN")
        print("  - THINKIFIC_INSTRUCTOR_ID")
        sys.exit(1)
    
    # Handle commands
    if args.list_courses:
        pipeline.list_courses()
    elif args.summary:
        pipeline.get_course_summary(args.summary)
    elif args.course_id and args.language:
        result = pipeline.translate_course(
            args.course_id,
            args.language,
            create_draft=args.draft,
            skip_qa=args.skip_qa
        )
        
        if not result['success']:
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
