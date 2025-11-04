"""
Media file handler for Thinkific course translations.

Handles different media types in course content:
- Videos: Add translated subtitles (SRT files)
- Audio: Provide translated transcripts
- Images: Flag for review if text present, reuse if no text
- PDFs: Trigger document translation workflow

Integrates with existing SRT translation system.
"""

import os
import re
from typing import Dict, List, Optional
from pathlib import Path
from urllib.parse import urlparse


class MediaHandler:
    """
    Handle media files during course translation.
    
    Strategy: Maximize automation while minimizing re-uploads.
    - Videos: Use subtitle files (already have SRT workflow)
    - Audio: Provide transcripts (text-based)
    - Images: Reuse unless text detected
    - PDFs: Use existing doc translation workflow
    """
    
    # Supported media types
    VIDEO_EXTENSIONS = ['.mp4', '.mov', '.avi', '.webm', '.mkv', '.m4v']
    AUDIO_EXTENSIONS = ['.mp3', '.wav', '.m4a', '.ogg', '.aac']
    IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp']
    DOCUMENT_EXTENSIONS = ['.pdf', '.doc', '.docx']
    
    def __init__(self, srt_dir: Optional[str] = None):
        """
        Initialize media handler.
        
        Args:
            srt_dir: Directory containing SRT files (default: transcripts/)
        """
        self.srt_dir = Path(srt_dir or 'transcripts')
    
    def handle_media(self, media_url: str, media_type: str, language: str) -> Dict:
        """
        Process media file for translation.
        
        Args:
            media_url: URL or path to media file
            media_type: Type of media (video, audio, image, document)
            language: Target language code
            
        Returns:
            Dictionary with handling instructions:
                - action: What to do with this media
                - original_url: Original media URL
                - additional fields based on action
        """
        handlers = {
            'video': self.handle_video,
            'audio': self.handle_audio,
            'image': self.handle_image,
            'document': self.handle_document,
            'pdf': self.handle_document
        }
        
        handler = handlers.get(media_type.lower(), self.handle_unknown)
        return handler(media_url, language)
    
    # ========================================================================
    # Video Handling
    # ========================================================================
    
    def handle_video(self, video_url: str, language: str) -> Dict:
        """
        Handle video translation via subtitles.
        
        Strategy:
        1. Check if SRT file exists for this video
        2. If yes, use translated SRT
        3. If no, flag for SRT creation
        4. Keep original video URL (no re-upload needed!)
        
        Args:
            video_url: URL to video file
            language: Target language code
            
        Returns:
            Action dict with subtitle information
        """
        video_name = self._extract_filename(video_url)
        
        # Check for existing SRT files
        en_srt = self.srt_dir / 'en' / f"{video_name}.srt"
        translated_srt = self.srt_dir / language / f"{video_name}.srt"
        
        if translated_srt.exists():
            # We have a translated SRT!
            return {
                'action': 'use_existing_subtitles',
                'original_url': video_url,
                'subtitle_file': str(translated_srt),
                'language': language,
                'status': 'ready',
                'note': 'Translated subtitles available'
            }
        
        elif en_srt.exists():
            # We have English SRT, need to translate it
            return {
                'action': 'translate_subtitles',
                'original_url': video_url,
                'source_srt': str(en_srt),
                'target_language': language,
                'status': 'needs_translation',
                'note': 'English SRT available - run translate_srt.py',
                'command': f"python scripts/translate_srt.py {en_srt} --language {language}"
            }
        
        else:
            # No SRT exists yet
            return {
                'action': 'create_subtitles',
                'original_url': video_url,
                'target_language': language,
                'status': 'needs_srt_creation',
                'note': 'No SRT file found - create English SRT first',
                'steps': [
                    '1. Extract/create English SRT file',
                    f'2. Save to: {en_srt}',
                    f'3. Run: python scripts/translate_srt.py {en_srt} --language {language}'
                ]
            }
    
    def get_video_with_subtitles(self, video_url: str, subtitle_file: str) -> Dict:
        """
        Get video configuration with subtitle track.
        
        For Thinkific, this might involve:
        - Uploading SRT to CDN
        - Configuring video player with subtitle URL
        
        Args:
            video_url: Original video URL
            subtitle_file: Path to SRT file
            
        Returns:
            Video configuration dict
        """
        return {
            'video_url': video_url,
            'subtitles': [
                {
                    'file': subtitle_file,
                    'language': self._extract_language_from_path(subtitle_file),
                    'label': self._get_language_label(subtitle_file)
                }
            ]
        }
    
    # ========================================================================
    # Audio Handling
    # ========================================================================
    
    def handle_audio(self, audio_url: str, language: str) -> Dict:
        """
        Handle audio translation via transcript.
        
        Strategy:
        - Provide translated transcript as text
        - Keep original audio (no re-recording needed)
        - Transcript can be added as lesson text
        
        Args:
            audio_url: URL to audio file
            language: Target language code
            
        Returns:
            Action dict with transcript information
        """
        audio_name = self._extract_filename(audio_url)
        
        # Check for transcript (could be SRT or text file)
        transcript_srt = self.srt_dir / language / f"{audio_name}.srt"
        transcript_txt = self.srt_dir / language / f"{audio_name}.txt"
        
        if transcript_srt.exists() or transcript_txt.exists():
            transcript_file = transcript_srt if transcript_srt.exists() else transcript_txt
            
            return {
                'action': 'use_existing_transcript',
                'original_url': audio_url,
                'transcript_file': str(transcript_file),
                'language': language,
                'status': 'ready',
                'note': 'Translated transcript available'
            }
        
        else:
            return {
                'action': 'create_transcript',
                'original_url': audio_url,
                'target_language': language,
                'status': 'needs_transcript',
                'note': 'Create and translate transcript for audio',
                'steps': [
                    '1. Transcribe audio to English text/SRT',
                    f'2. Translate using translate_srt.py',
                    '3. Add as supplementary lesson text'
                ]
            }
    
    # ========================================================================
    # Image Handling
    # ========================================================================
    
    def handle_image(self, image_url: str, language: str) -> Dict:
        """
        Handle image translation.
        
        Strategy:
        - Reuse image if it's purely visual (no text)
        - Flag for manual replacement if text detected
        - In POC: assume images are reusable (no OCR yet)
        
        Args:
            image_url: URL to image file
            language: Target language code
            
        Returns:
            Action dict
        """
        # For POC: simple heuristic - check filename for hints
        filename = self._extract_filename(image_url).lower()
        
        # Common patterns suggesting text in images
        text_indicators = [
            'screenshot', 'diagram', 'chart', 'graph',
            'interface', 'ui', 'menu', 'button'
        ]
        
        likely_has_text = any(indicator in filename for indicator in text_indicators)
        
        if likely_has_text:
            return {
                'action': 'flag_for_review',
                'original_url': image_url,
                'language': language,
                'status': 'needs_review',
                'note': 'Image likely contains text - may need localized version',
                'suggestion': 'Create language-specific versions or use language-neutral images'
            }
        else:
            return {
                'action': 'reuse',
                'original_url': image_url,
                'translated_url': image_url,  # Same URL
                'language': language,
                'status': 'ready',
                'note': 'Image is language-neutral - reusing original'
            }
    
    def detect_text_in_image(self, image_url: str) -> bool:
        """
        Detect if image contains text (placeholder for future OCR).
        
        Future enhancement: Integrate with AWS Rekognition or Google Vision API
        
        Args:
            image_url: URL to image
            
        Returns:
            True if text detected (currently always False - POC)
        """
        # TODO: Implement OCR detection
        # For now, return False (assume images are text-free)
        return False
    
    # ========================================================================
    # Document Handling
    # ========================================================================
    
    def handle_document(self, document_url: str, language: str) -> Dict:
        """
        Handle document translation.
        
        Strategy:
        - Download document
        - Convert to markdown if needed
        - Use existing translation workflow
        - Upload translated version
        
        Args:
            document_url: URL to document
            language: Target language code
            
        Returns:
            Action dict with translation workflow
        """
        doc_name = self._extract_filename(document_url)
        doc_ext = Path(document_url).suffix.lower()
        
        return {
            'action': 'translate_document',
            'original_url': document_url,
            'document_name': doc_name,
            'document_type': doc_ext,
            'target_language': language,
            'status': 'needs_translation',
            'note': 'Document needs translation using existing workflow',
            'steps': [
                f'1. Download: {document_url}',
                '2. Convert to markdown if PDF',
                f'3. Translate: python scripts/translation_agent.py document.md --language {language}',
                '4. Convert back to original format',
                '5. Upload to CDN',
                '6. Update lesson with new URL'
            ]
        }
    
    # ========================================================================
    # Unknown Media
    # ========================================================================
    
    def handle_unknown(self, media_url: str, language: str) -> Dict:
        """Handle unknown media type."""
        return {
            'action': 'manual_review',
            'original_url': media_url,
            'language': language,
            'status': 'unknown_type',
            'note': 'Unknown media type - manual review needed'
        }
    
    # ========================================================================
    # Batch Processing
    # ========================================================================
    
    def process_lesson_media(
        self, 
        lesson_content: str, 
        language: str
    ) -> List[Dict]:
        """
        Extract and process all media from lesson content.
        
        Args:
            lesson_content: HTML content of lesson
            language: Target language code
            
        Returns:
            List of media handling actions
        """
        media_items = []
        
        # Extract video URLs
        videos = re.findall(
            r'<video[^>]+src=["\']([^"\']+)["\']',
            lesson_content,
            re.IGNORECASE
        )
        for video_url in videos:
            media_items.append(self.handle_video(video_url, language))
        
        # Extract audio URLs
        audios = re.findall(
            r'<audio[^>]+src=["\']([^"\']+)["\']',
            lesson_content,
            re.IGNORECASE
        )
        for audio_url in audios:
            media_items.append(self.handle_audio(audio_url, language))
        
        # Extract image URLs
        images = re.findall(
            r'<img[^>]+src=["\']([^"\']+)["\']',
            lesson_content,
            re.IGNORECASE
        )
        for image_url in images:
            media_items.append(self.handle_image(image_url, language))
        
        # Extract document links
        docs = re.findall(
            r'<a[^>]+href=["\']([^"\']+\.(?:pdf|doc|docx))["\']',
            lesson_content,
            re.IGNORECASE
        )
        for doc_url in docs:
            media_items.append(self.handle_document(doc_url, language))
        
        return media_items
    
    def get_media_summary(self, media_items: List[Dict]) -> Dict:
        """
        Generate summary of media processing status.
        
        Args:
            media_items: List of media handling results
            
        Returns:
            Summary statistics
        """
        summary = {
            'total': len(media_items),
            'ready': 0,
            'needs_translation': 0,
            'needs_review': 0,
            'needs_creation': 0,
            'by_action': {}
        }
        
        for item in media_items:
            action = item.get('action', 'unknown')
            status = item.get('status', 'unknown')
            
            # Count by status
            if status == 'ready':
                summary['ready'] += 1
            elif 'needs' in status:
                if 'translation' in status:
                    summary['needs_translation'] += 1
                elif 'review' in status:
                    summary['needs_review'] += 1
                elif 'creation' in status or 'srt' in status:
                    summary['needs_creation'] += 1
            
            # Count by action
            summary['by_action'][action] = summary['by_action'].get(action, 0) + 1
        
        return summary
    
    # ========================================================================
    # Utility Methods
    # ========================================================================
    
    def _extract_filename(self, url: str) -> str:
        """Extract filename without extension from URL."""
        parsed = urlparse(url)
        path = Path(parsed.path)
        return path.stem
    
    def _extract_language_from_path(self, filepath: str) -> str:
        """Extract language code from file path."""
        path = Path(filepath)
        # Assume format: transcripts/LANG/filename.srt
        parts = path.parts
        if len(parts) >= 2:
            return parts[-2]
        return 'en'
    
    def _get_language_label(self, filepath: str) -> str:
        """Get human-readable language label."""
        lang_code = self._extract_language_from_path(filepath)
        labels = {
            'en': 'English',
            'es': 'Spanish',
            'fr': 'French',
            'ar': 'Arabic'
        }
        return labels.get(lang_code, lang_code.upper())
    
    def get_media_type(self, url: str) -> str:
        """Determine media type from URL."""
        ext = Path(urlparse(url).path).suffix.lower()
        
        if ext in self.VIDEO_EXTENSIONS:
            return 'video'
        elif ext in self.AUDIO_EXTENSIONS:
            return 'audio'
        elif ext in self.IMAGE_EXTENSIONS:
            return 'image'
        elif ext in self.DOCUMENT_EXTENSIONS:
            return 'document'
        else:
            return 'unknown'


if __name__ == "__main__":
    """Test media handler with sample content."""
    
    print("🧪 Testing Media Handler...\n")
    
    handler = MediaHandler()
    
    # Test video handling
    print("📹 Testing video handling:")
    video_result = handler.handle_video(
        "https://cdn.example.com/videos/intro-to-kobo.mp4",
        "es"
    )
    print(f"  Action: {video_result['action']}")
    print(f"  Status: {video_result['status']}")
    print(f"  Note: {video_result['note']}\n")
    
    # Test image handling
    print("🖼️  Testing image handling:")
    image_result = handler.handle_image(
        "https://cdn.example.com/images/logo.png",
        "fr"
    )
    print(f"  Action: {image_result['action']}")
    print(f"  Status: {image_result['status']}\n")
    
    # Test lesson media processing
    print("📄 Testing lesson content parsing:")
    sample_content = """
    <div class="lesson">
        <video src="https://cdn.example.com/video1.mp4"></video>
        <img src="https://cdn.example.com/screenshot.png" />
        <img src="https://cdn.example.com/logo.png" />
        <a href="https://cdn.example.com/guide.pdf">Download Guide</a>
    </div>
    """
    
    media_items = handler.process_lesson_media(sample_content, "es")
    print(f"  Found {len(media_items)} media items")
    
    summary = handler.get_media_summary(media_items)
    print(f"\n  Summary:")
    print(f"    Ready: {summary['ready']}")
    print(f"    Needs translation: {summary['needs_translation']}")
    print(f"    Needs review: {summary['needs_review']}")
    print(f"    Needs creation: {summary['needs_creation']}")
