"""
Thinkific API integration for course content management.

This module provides a client for interacting with Thinkific's API to:
- Fetch course content and structure
- Create translated course copies
- Update lessons and chapters
- Publish courses

API Documentation: https://developers.thinkific.com/api/api-documentation/
"""

import os
import requests
import time
from typing import Dict, List, Optional, Any
from datetime import datetime


class ThinkificAPIError(Exception):
    """Custom exception for Thinkific API errors."""
    pass


class ThinkificSync:
    """
    Client for syncing course content with Thinkific API.
    
    Handles rate limiting, error handling, and provides methods for
    reading and writing course content.
    """
    
    # Thinkific rate limits: 500 requests per 10 minutes per IP
    API_CALLS_PER_PERIOD = 450  # Leave buffer for safety
    PERIOD_SECONDS = 600
    
    def __init__(self, api_key: Optional[str] = None, subdomain: Optional[str] = None):
        """
        Initialize Thinkific API client.
        
        Args:
            api_key: Thinkific API key (or reads from THINKIFIC_API_KEY env var)
            subdomain: Thinkific subdomain (or reads from THINKIFIC_SUBDOMAIN env var)
        """
        self.api_key = api_key or os.getenv('THINKIFIC_API_KEY')
        self.subdomain = subdomain or os.getenv('THINKIFIC_SUBDOMAIN')
        
        if not self.api_key:
            raise ThinkificAPIError("THINKIFIC_API_KEY not found in environment or parameters")
        
        if not self.subdomain:
            raise ThinkificAPIError("THINKIFIC_SUBDOMAIN not found in environment or parameters")
        
        self.base_url = "https://api.thinkific.com/api/public/v1"
        self.headers = {
            'X-Auth-API-Key': self.api_key,
            'X-Auth-Subdomain': self.subdomain,
            'Content-Type': 'application/json'
        }
        
        # Track API calls for rate limiting
        self._api_calls = []
    
    def _check_rate_limit(self):
        """Check and enforce rate limiting."""
        now = time.time()
        
        # Remove calls older than the period
        self._api_calls = [
            call_time for call_time in self._api_calls 
            if now - call_time < self.PERIOD_SECONDS
        ]
        
        # If we're at the limit, wait
        if len(self._api_calls) >= self.API_CALLS_PER_PERIOD:
            oldest_call = self._api_calls[0]
            wait_time = self.PERIOD_SECONDS - (now - oldest_call) + 1
            print(f"⏳ Rate limit reached. Waiting {wait_time:.0f} seconds...")
            time.sleep(wait_time)
            self._api_calls = []
        
        # Record this call
        self._api_calls.append(now)
    
    def _make_request(
        self, 
        endpoint: str, 
        method: str = 'GET', 
        data: Optional[Dict] = None,
        params: Optional[Dict] = None
    ) -> Dict:
        """
        Make a rate-limited API request to Thinkific.
        
        Args:
            endpoint: API endpoint (e.g., '/courses')
            method: HTTP method (GET, POST, PUT, DELETE)
            data: Request body for POST/PUT
            params: Query parameters
            
        Returns:
            JSON response as dictionary
            
        Raises:
            ThinkificAPIError: If request fails
        """
        self._check_rate_limit()
        
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data,
                params=params,
                timeout=30
            )
            
            response.raise_for_status()
            
            # Return empty dict for 204 No Content
            if response.status_code == 204:
                return {}
            
            return response.json()
            
        except requests.exceptions.HTTPError as e:
            error_msg = f"Thinkific API error: {e.response.status_code}"
            try:
                error_detail = e.response.json()
                error_msg += f" - {error_detail}"
            except:
                error_msg += f" - {e.response.text}"
            raise ThinkificAPIError(error_msg)
        except requests.exceptions.RequestException as e:
            raise ThinkificAPIError(f"Request failed: {str(e)}")
    
    # ========================================================================
    # Course Operations
    # ========================================================================
    
    def list_courses(self, page: int = 1, limit: int = 25) -> Dict:
        """
        List all courses in the Thinkific account.
        
        Args:
            page: Page number for pagination
            limit: Number of courses per page (max 100)
            
        Returns:
            Dictionary with 'items' list and pagination metadata
        """
        params = {'page': page, 'limit': min(limit, 100)}
        return self._make_request('/courses', params=params)
    
    def get_course(self, course_id: int) -> Dict:
        """
        Get detailed information about a specific course.
        
        Args:
            course_id: Thinkific course ID
            
        Returns:
            Course data including name, description, etc.
        """
        return self._make_request(f'/courses/{course_id}')
    
    def get_course_with_full_content(self, course_id: int) -> Dict:
        """
        Fetch course with all chapters, lessons, and content.
        
        This makes multiple API calls to build a complete picture:
        - Course details
        - Chapters
        - Lessons with content
        
        Args:
            course_id: Thinkific course ID
            
        Returns:
            Complete course data structure
        """
        print(f"📥 Fetching course {course_id} with full content...")
        
        # Get base course info
        course = self.get_course(course_id)
        
        # Get chapters
        chapters = self.get_chapters(course_id)
        course['chapters'] = chapters
        
        # Get lessons for each chapter
        all_lessons = []
        for chapter in chapters:
            lessons = self.get_lessons(chapter['id'])
            
            # Get full content for each lesson
            for lesson in lessons:
                lesson_detail = self.get_lesson(lesson['id'])
                lesson.update(lesson_detail)
            
            chapter['lessons'] = lessons
            all_lessons.extend(lessons)
        
        course['all_lessons'] = all_lessons
        
        print(f"  ✅ Fetched {len(chapters)} chapters, {len(all_lessons)} lessons")
        
        return course
    
    def create_course(self, course_data: Dict) -> Dict:
        """
        Create a new course.
        
        Args:
            course_data: Dictionary with course properties:
                - name: Course title (required)
                - description: Course description
                - user_id: Instructor user ID (required)
                - card_image_url: Cover image URL
                
        Returns:
            Created course data with ID
        """
        return self._make_request('/courses', method='POST', data=course_data)
    
    def update_course(self, course_id: int, course_data: Dict) -> Dict:
        """
        Update an existing course.
        
        Args:
            course_id: Thinkific course ID
            course_data: Dictionary with course properties to update
            
        Returns:
            Updated course data
        """
        return self._make_request(
            f'/courses/{course_id}', 
            method='PUT', 
            data=course_data
        )
    
    # ========================================================================
    # Chapter Operations
    # ========================================================================
    
    def get_chapters(self, course_id: int) -> List[Dict]:
        """
        Get all chapters for a course.
        
        Args:
            course_id: Thinkific course ID
            
        Returns:
            List of chapter dictionaries
        """
        response = self._make_request(f'/courses/{course_id}/chapters')
        return response.get('items', [])
    
    def create_chapter(self, course_id: int, chapter_data: Dict) -> Dict:
        """
        Create a new chapter in a course.
        
        Args:
            course_id: Thinkific course ID
            chapter_data: Dictionary with:
                - name: Chapter title (required)
                - position: Chapter order (optional)
                
        Returns:
            Created chapter data with ID
        """
        data = {**chapter_data, 'course_id': course_id}
        return self._make_request('/chapters', method='POST', data=data)
    
    def update_chapter(self, chapter_id: int, chapter_data: Dict) -> Dict:
        """
        Update an existing chapter.
        
        Args:
            chapter_id: Thinkific chapter ID
            chapter_data: Dictionary with chapter properties to update
            
        Returns:
            Updated chapter data
        """
        return self._make_request(
            f'/chapters/{chapter_id}', 
            method='PUT', 
            data=chapter_data
        )
    
    # ========================================================================
    # Lesson Operations
    # ========================================================================
    
    def get_lessons(self, chapter_id: int) -> List[Dict]:
        """
        Get all lessons in a chapter.
        
        Args:
            chapter_id: Thinkific chapter ID
            
        Returns:
            List of lesson dictionaries (basic info only)
        """
        response = self._make_request(f'/chapters/{chapter_id}/lessons')
        return response.get('items', [])
    
    def get_lesson(self, lesson_id: int) -> Dict:
        """
        Get detailed information about a specific lesson.
        
        Args:
            lesson_id: Thinkific lesson ID
            
        Returns:
            Full lesson data including content
        """
        return self._make_request(f'/lessons/{lesson_id}')
    
    def create_lesson(self, chapter_id: int, lesson_data: Dict) -> Dict:
        """
        Create a new lesson in a chapter.
        
        Args:
            chapter_id: Thinkific chapter ID
            lesson_data: Dictionary with:
                - name: Lesson title (required)
                - lesson_type: Type (video, text, download, etc.)
                - content: Lesson content (HTML/text)
                - position: Lesson order (optional)
                
        Returns:
            Created lesson data with ID
        """
        data = {**lesson_data, 'chapter_id': chapter_id}
        return self._make_request('/lessons', method='POST', data=data)
    
    def update_lesson(self, lesson_id: int, lesson_data: Dict) -> Dict:
        """
        Update an existing lesson.
        
        Args:
            lesson_id: Thinkific lesson ID
            lesson_data: Dictionary with lesson properties to update
            
        Returns:
            Updated lesson data
        """
        return self._make_request(
            f'/lessons/{lesson_id}', 
            method='PUT', 
            data=lesson_data
        )
    
    # ========================================================================
    # Bulk Operations for Translation
    # ========================================================================
    
    def create_translated_course(
        self, 
        source_course_id: int, 
        target_language: str,
        translated_content: Dict,
        instructor_id: int
    ) -> Dict:
        """
        Create a complete translated copy of a course.
        
        This orchestrates multiple API calls to:
        1. Create new course with translated title/description
        2. Create chapters with translated names
        3. Create lessons with translated content
        
        Args:
            source_course_id: Original course ID
            target_language: Target language code (e.g., 'es', 'fr', 'ar')
            translated_content: Dictionary with all translated content
            instructor_id: User ID for course instructor
            
        Returns:
            Created course data with full structure
        """
        print(f"\n🚀 Creating translated course ({target_language.upper()})...")
        
        # Create course
        course_data = {
            'name': f"{translated_content['name']} ({target_language.upper()})",
            'description': translated_content.get('description', ''),
            'user_id': instructor_id
        }
        
        if 'card_image_url' in translated_content:
            course_data['card_image_url'] = translated_content['card_image_url']
        
        new_course = self.create_course(course_data)
        print(f"  ✅ Created course: {new_course['id']}")
        
        # Create chapters and lessons
        for chapter_data in translated_content.get('chapters', []):
            chapter = self.create_chapter(new_course['id'], {
                'name': chapter_data['name'],
                'position': chapter_data.get('position')
            })
            print(f"    ✅ Created chapter: {chapter_data['name']}")
            
            for lesson_data in chapter_data.get('lessons', []):
                lesson = self.create_lesson(chapter['id'], lesson_data)
                print(f"      ✅ Created lesson: {lesson_data['name']}")
        
        print(f"\n🎉 Successfully created translated course: {new_course['id']}")
        
        return new_course
    
    def create_draft_course(
        self, 
        source_course_id: int,
        target_language: str,
        translated_content: Dict,
        instructor_id: int
    ) -> Dict:
        """
        Create a draft course for review before publishing.
        
        Same as create_translated_course but marks as draft/unpublished.
        
        Args:
            source_course_id: Original course ID
            target_language: Target language code
            translated_content: Dictionary with all translated content
            instructor_id: User ID for course instructor
            
        Returns:
            Created draft course data
        """
        # Create course (courses are draft by default in Thinkific)
        new_course = self.create_translated_course(
            source_course_id,
            target_language,
            translated_content,
            instructor_id
        )
        
        # Add [DRAFT] prefix to make it clear
        self.update_course(new_course['id'], {
            'name': f"[DRAFT] {new_course['name']}"
        })
        
        print(f"📝 Course created as draft for review")
        
        return new_course
    
    # ========================================================================
    # Utility Methods
    # ========================================================================
    
    def test_connection(self) -> bool:
        """
        Test API connection and credentials.
        
        Returns:
            True if connection successful, False otherwise
        """
        try:
            courses = self.list_courses(limit=1)
            print("✅ Thinkific API connection successful")
            return True
        except ThinkificAPIError as e:
            print(f"❌ Thinkific API connection failed: {e}")
            return False
    
    def get_course_summary(self, course_id: int) -> str:
        """
        Get a human-readable summary of a course.
        
        Args:
            course_id: Thinkific course ID
            
        Returns:
            Formatted string with course overview
        """
        course = self.get_course_with_full_content(course_id)
        
        summary = f"""
Course: {course['name']}
ID: {course['id']}
Chapters: {len(course.get('chapters', []))}
Lessons: {len(course.get('all_lessons', []))}

Chapter Structure:
"""
        
        for i, chapter in enumerate(course.get('chapters', []), 1):
            summary += f"  {i}. {chapter['name']} ({len(chapter.get('lessons', []))} lessons)\n"
            for j, lesson in enumerate(chapter.get('lessons', []), 1):
                lesson_type = lesson.get('lesson_type', 'unknown')
                summary += f"     {i}.{j}. {lesson['name']} [{lesson_type}]\n"
        
        return summary


if __name__ == "__main__":
    """Quick test of Thinkific API connection."""
    
    print("🧪 Testing Thinkific API connection...\n")
    
    try:
        client = ThinkificSync()
        
        if client.test_connection():
            print("\nℹ️  Fetching courses...")
            courses = client.list_courses(limit=5)
            
            if courses.get('items'):
                print(f"\nFound {len(courses['items'])} course(s):\n")
                for course in courses['items']:
                    print(f"  • {course['name']} (ID: {course['id']})")
            else:
                print("\nNo courses found in this account.")
        
    except ThinkificAPIError as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you have set:")
        print("  - THINKIFIC_API_KEY in .env")
        print("  - THINKIFIC_SUBDOMAIN in .env")
