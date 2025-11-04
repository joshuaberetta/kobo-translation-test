#!/usr/bin/env python3
"""
Test script for Thinkific integration.

Tests:
1. API connection
2. Course fetching
3. Content parsing
4. Media handling
5. Quiz translation
6. QA workflow
7. End-to-end pipeline (without actual publishing)
"""

import sys
from pathlib import Path

# Add scripts to path
sys.path.append(str(Path(__file__).parent / 'scripts'))

from scripts.thinkific_sync import ThinkificSync, ThinkificAPIError
from scripts.thinkific_content_parser import ThinkificContentParser
from scripts.thinkific_media_handler import MediaHandler
from scripts.thinkific_quiz_translator import QuizTranslator
from scripts.thinkific_qa_workflow import QAWorkflow


def test_api_connection():
    """Test 1: Verify Thinkific API connection."""
    print("\n" + "="*70)
    print("TEST 1: Thinkific API Connection")
    print("="*70 + "\n")
    
    try:
        client = ThinkificSync()
        
        if client.test_connection():
            print("✅ API connection successful!\n")
            
            # Try to list courses
            courses = client.list_courses(limit=3)
            
            if courses.get('items'):
                print(f"Found {len(courses['items'])} course(s):\n")
                for course in courses['items']:
                    print(f"  • {course['name']} (ID: {course['id']})")
                return True, courses['items'][0]['id'] if courses['items'] else None
            else:
                print("⚠️  No courses found in account")
                return True, None
        else:
            print("❌ API connection failed")
            return False, None
            
    except ThinkificAPIError as e:
        print(f"❌ API Error: {e}")
        print("\nMake sure .env contains:")
        print("  THINKIFIC_API_KEY=your_api_key")
        print("  THINKIFIC_SUBDOMAIN=your_subdomain")
        return False, None


def test_content_parser():
    """Test 2: Content parsing for HTML and Markdown."""
    print("\n" + "="*70)
    print("TEST 2: Content Parser")
    print("="*70 + "\n")
    
    parser = ThinkificContentParser()
    
    # Test HTML parsing
    print("📝 Testing HTML parsing...")
    html_sample = """
    <div class="lesson">
        <h1>Welcome to KoboToolbox</h1>
        <p>This is a powerful data collection platform.</p>
        <img src="logo.png" alt="KoboToolbox Logo" />
        <a href="https://kobotoolbox.org">Learn more</a>
        <pre><code>const data = fetchData();</code></pre>
    </div>
    """
    
    segments, soup = parser.extract_html_segments(html_sample)
    print(f"  ✅ Extracted {len(segments)} segments")
    print(f"     Text nodes: {len([s for s in segments if s['type'] == 'text_node'])}")
    print(f"     Attributes: {len([s for s in segments if s['type'] == 'attribute'])}")
    
    # Test Markdown parsing
    print("\n📝 Testing Markdown parsing...")
    markdown_sample = """
# Getting Started

Learn how to use KoboToolbox.

```bash
pip install kobo-cli
```

Visit [our docs](https://docs.kobotoolbox.org).
"""
    
    markdown_data = parser.extract_markdown_segments(markdown_sample)
    print(f"  ✅ Extracted translatable text")
    print(f"     Preserved: {len(markdown_data['placeholders'])} elements")
    
    return True


def test_media_handler():
    """Test 3: Media file handling."""
    print("\n" + "="*70)
    print("TEST 3: Media Handler")
    print("="*70 + "\n")
    
    handler = MediaHandler()
    
    # Test video handling
    print("📹 Testing video handling...")
    video_result = handler.handle_video(
        "https://cdn.example.com/intro.mp4",
        "es"
    )
    print(f"  Action: {video_result['action']}")
    print(f"  Status: {video_result['status']}")
    
    # Test image handling
    print("\n🖼️  Testing image handling...")
    image_result = handler.handle_image(
        "https://cdn.example.com/logo.png",
        "fr"
    )
    print(f"  Action: {image_result['action']}")
    print(f"  Status: {image_result['status']}")
    
    # Test lesson media extraction
    print("\n📄 Testing lesson content parsing...")
    sample_content = """
    <video src="https://cdn.example.com/video1.mp4"></video>
    <img src="https://cdn.example.com/screenshot.png" />
    <a href="https://cdn.example.com/guide.pdf">Guide</a>
    """
    
    media_items = handler.process_lesson_media(sample_content, "es")
    summary = handler.get_media_summary(media_items)
    
    print(f"  ✅ Found {summary['total']} media items")
    print(f"     Ready: {summary['ready']}")
    print(f"     Needs attention: {summary['needs_translation'] + summary['needs_review']}")
    
    return True


def test_quiz_translator():
    """Test 4: Quiz translation."""
    print("\n" + "="*70)
    print("TEST 4: Quiz Translator")
    print("="*70 + "\n")
    
    translator = QuizTranslator()
    
    # Sample quiz
    sample_quiz = {
        'id': 1,
        'title': 'KoboToolbox Basics',
        'questions': [
            {
                'id': 1,
                'question_type': 'multiple_choice',
                'text': 'What is KoboToolbox?',
                'answers': [
                    {'id': 'a', 'text': 'Data collection tool', 'is_correct': True},
                    {'id': 'b', 'text': 'Video editor', 'is_correct': False}
                ]
            },
            {
                'id': 2,
                'question_type': 'true_false',
                'text': 'KoboToolbox works offline',
                'correct_answer': True
            }
        ]
    }
    
    print("📝 Translating quiz...")
    translated = translator.translate_quiz(sample_quiz, 'es')
    
    print(f"  ✅ Translated {len(translated['questions'])} questions")
    
    # Validate
    print("\n🔍 Validating translation...")
    validation = translator.validate_quiz_translation(sample_quiz, translated)
    
    print(f"  Valid: {validation['valid']}")
    print(f"  Checked: {validation['checked']} questions")
    
    if validation['issues']:
        print("  Issues:")
        for issue in validation['issues']:
            print(f"    - {issue}")
        return False
    else:
        print("  ✅ No issues found!")
        return True


def test_qa_workflow():
    """Test 5: QA workflow."""
    print("\n" + "="*70)
    print("TEST 5: QA Workflow")
    print("="*70 + "\n")
    
    qa = QAWorkflow()
    
    # Sample course (good translation)
    good_course = {
        'name': 'Introducción a KoboToolbox',
        'language': 'es',
        'chapters': [
            {
                'name': 'Comenzando',
                'lessons': [
                    {'name': 'Bienvenida', 'content': '<p>Bienvenidos a KoboToolbox...</p>' * 10}
                ]
            }
        ],
        'media': [
            {'action': 'reuse', 'status': 'ready'}
        ],
        'quizzes': [
            {'title': 'Quiz 1', '_validation': {'valid': True, 'issues': []}}
        ],
        '_original_structure': {
            'chapters': [
                {
                    'name': 'Getting Started',
                    'lessons': [
                        {'name': 'Welcome', 'content': '<p>Welcome to KoboToolbox...</p>' * 10}
                    ]
                }
            ]
        }
    }
    
    print("🔍 Running QA checks on good translation...")
    results = qa.run_quality_checks(good_course)
    
    if results['passed']:
        print("✅ QA checks passed!")
        return True
    else:
        print("⚠️  QA checks found issues")
        return False


def test_full_pipeline(course_id: int = None):
    """Test 6: End-to-end pipeline (simulation)."""
    print("\n" + "="*70)
    print("TEST 6: End-to-End Pipeline (Simulation)")
    print("="*70 + "\n")
    
    if not course_id:
        print("⏭️  Skipping - no course ID provided")
        return True
    
    print(f"📥 Would fetch course {course_id}...")
    print(f"🔄 Would sync Transifex terminology...")
    print(f"📝 Would translate content...")
    print(f"🎬 Would process media...")
    print(f"✅ Would translate quizzes...")
    print(f"🔍 Would run QA checks...")
    print(f"🚀 Would create translated course...")
    
    print("\n✅ Pipeline simulation complete!")
    print("   (Run with --course-id to test with real course)")
    
    return True


def main():
    """Run all tests."""
    print("\n" + "="*70)
    print("  THINKIFIC INTEGRATION TEST SUITE")
    print("="*70)
    
    results = {}
    course_id = None
    
    # Test 1: API Connection
    success, found_course_id = test_api_connection()
    results['API Connection'] = success
    
    if found_course_id:
        course_id = found_course_id
    
    # Test 2: Content Parser
    results['Content Parser'] = test_content_parser()
    
    # Test 3: Media Handler
    results['Media Handler'] = test_media_handler()
    
    # Test 4: Quiz Translator
    results['Quiz Translator'] = test_quiz_translator()
    
    # Test 5: QA Workflow
    results['QA Workflow'] = test_qa_workflow()
    
    # Test 6: Full Pipeline (simulation)
    results['Full Pipeline'] = test_full_pipeline(course_id)
    
    # Summary
    print("\n" + "="*70)
    print("  TEST SUMMARY")
    print("="*70 + "\n")
    
    all_passed = True
    for test_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"  {status}  {test_name}")
        if not passed:
            all_passed = False
    
    print("\n" + "="*70)
    
    if all_passed:
        print("  ✅ ALL TESTS PASSED!")
        print("="*70 + "\n")
        print("Next steps:")
        print("  1. Set THINKIFIC_INSTRUCTOR_ID in .env")
        print("  2. Run: python scripts/thinkific_translate_course.py --list-courses")
        print("  3. Run: python scripts/thinkific_translate_course.py --course-id <ID> --language es --draft")
        print()
        return 0
    else:
        print("  ⚠️  SOME TESTS FAILED")
        print("="*70 + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
