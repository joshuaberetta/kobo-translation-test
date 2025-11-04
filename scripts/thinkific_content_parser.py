"""
Content parser for Thinkific course materials.

Extracts translatable text from HTML and Markdown while preserving:
- HTML structure and tags
- Markdown formatting
- Code blocks
- Links and media references
- Special formatting

This ensures translations maintain the original structure and formatting.
"""

from bs4 import BeautifulSoup, NavigableString
import re
from typing import Dict, List, Tuple, Any


class ThinkificContentParser:
    """
    Parser for extracting and reconstructing translatable content.
    
    Handles both HTML (Thinkific lesson content) and Markdown formats.
    Preserves structure while isolating translatable text segments.
    """
    
    # HTML tags that should NOT have their content translated
    PRESERVE_TAGS = ['code', 'pre', 'script', 'style', 'iframe']
    
    # HTML tags that contain translatable attributes
    TRANSLATABLE_ATTRS = {
        'img': ['alt', 'title'],
        'a': ['title'],
        'input': ['placeholder', 'value'],
        'button': ['aria-label'],
    }
    
    def __init__(self):
        self.placeholder_counter = 0
    
    # ========================================================================
    # HTML Content Processing
    # ========================================================================
    
    def extract_html_segments(self, html: str) -> Tuple[List[Dict], BeautifulSoup]:
        """
        Extract translatable text segments from HTML.
        
        Args:
            html: HTML content string
            
        Returns:
            Tuple of:
                - List of translatable segments with metadata
                - BeautifulSoup object for reconstruction
        """
        if not html or not html.strip():
            return [], None
        
        soup = BeautifulSoup(html, 'html.parser')
        segments = []
        
        # Extract text content
        text_segments = self._extract_text_nodes(soup)
        segments.extend(text_segments)
        
        # Extract translatable attributes
        attr_segments = self._extract_translatable_attributes(soup)
        segments.extend(attr_segments)
        
        return segments, soup
    
    def _extract_text_nodes(self, soup: BeautifulSoup) -> List[Dict]:
        """Extract translatable text from HTML nodes."""
        segments = []
        segment_id = 0
        
        for element in soup.find_all(text=True):
            # Skip if empty or whitespace-only
            text = str(element).strip()
            if not text:
                continue
            
            # Skip if inside a preserved tag
            if self._is_in_preserved_tag(element):
                continue
            
            # Skip if it's a script or style content
            if element.parent.name in ['script', 'style']:
                continue
            
            segments.append({
                'id': segment_id,
                'type': 'text_node',
                'text': text,
                'original_text': str(element),  # Preserve original whitespace
                'parent_tag': element.parent.name if element.parent else None,
                'element': element  # Store reference for reconstruction
            })
            
            segment_id += 1
        
        return segments
    
    def _extract_translatable_attributes(self, soup: BeautifulSoup) -> List[Dict]:
        """Extract translatable attributes from HTML tags."""
        segments = []
        segment_id = 1000  # Start from 1000 to avoid conflicts
        
        for tag_name, attr_names in self.TRANSLATABLE_ATTRS.items():
            for element in soup.find_all(tag_name):
                for attr_name in attr_names:
                    attr_value = element.get(attr_name)
                    if attr_value and attr_value.strip():
                        segments.append({
                            'id': segment_id,
                            'type': 'attribute',
                            'text': attr_value.strip(),
                            'tag_name': tag_name,
                            'attr_name': attr_name,
                            'element': element
                        })
                        segment_id += 1
        
        return segments
    
    def _is_in_preserved_tag(self, element) -> bool:
        """Check if element is inside a tag that should be preserved."""
        current = element.parent
        while current:
            if current.name in self.PRESERVE_TAGS:
                return True
            current = current.parent
        return False
    
    def reconstruct_html(
        self, 
        soup: BeautifulSoup, 
        translated_segments: List[Dict]
    ) -> str:
        """
        Reconstruct HTML with translated text.
        
        Args:
            soup: Original BeautifulSoup object
            translated_segments: List of segments with translated_text field
            
        Returns:
            HTML string with translations applied
        """
        if not soup:
            return ""
        
        # Apply text node translations
        text_segments = [s for s in translated_segments if s['type'] == 'text_node']
        for segment in text_segments:
            element = segment['element']
            translated_text = segment.get('translated_text', segment['text'])
            
            # Preserve original whitespace pattern
            original = segment['original_text']
            if original.startswith(' ') or original.startswith('\n'):
                translated_text = original[0] + translated_text
            if original.endswith(' ') or original.endswith('\n'):
                translated_text = translated_text + original[-1]
            
            element.replace_with(translated_text)
        
        # Apply attribute translations
        attr_segments = [s for s in translated_segments if s['type'] == 'attribute']
        for segment in attr_segments:
            element = segment['element']
            attr_name = segment['attr_name']
            translated_text = segment.get('translated_text', segment['text'])
            element[attr_name] = translated_text
        
        return str(soup)
    
    # ========================================================================
    # Markdown Content Processing
    # ========================================================================
    
    def extract_markdown_segments(self, markdown: str) -> Dict:
        """
        Extract translatable content from Markdown.
        
        Preserves:
        - Code blocks (```code```)
        - Inline code (`code`)
        - Links ([text](url))
        - Images (![alt](url))
        - HTML tags
        
        Args:
            markdown: Markdown content string
            
        Returns:
            Dictionary with:
                - translatable_text: Text ready for translation
                - placeholders: Mapping of placeholders to preserved content
        """
        self.placeholder_counter = 0
        placeholders = {}
        text = markdown
        
        # Extract code blocks first (highest priority)
        text, code_blocks = self._extract_code_blocks(text)
        placeholders.update(code_blocks)
        
        # Extract inline code
        text, inline_code = self._extract_inline_code(text)
        placeholders.update(inline_code)
        
        # Extract images (preserve entirely)
        text, images = self._extract_images(text)
        placeholders.update(images)
        
        # Extract links (preserve URL, keep text translatable)
        text, links = self._extract_links(text)
        placeholders.update(links)
        
        # Extract HTML tags
        text, html_tags = self._extract_html_tags(text)
        placeholders.update(html_tags)
        
        return {
            'translatable_text': text,
            'placeholders': placeholders
        }
    
    def _extract_code_blocks(self, text: str) -> Tuple[str, Dict]:
        """Extract fenced code blocks."""
        placeholders = {}
        
        def replace_code_block(match):
            placeholder = f"__CODE_BLOCK_{self.placeholder_counter}__"
            self.placeholder_counter += 1
            placeholders[placeholder] = match.group(0)
            return placeholder
        
        # Match ```language\ncode\n```
        text = re.sub(
            r'```[\s\S]*?```',
            replace_code_block,
            text
        )
        
        return text, placeholders
    
    def _extract_inline_code(self, text: str) -> Tuple[str, Dict]:
        """Extract inline code spans."""
        placeholders = {}
        
        def replace_inline_code(match):
            placeholder = f"__INLINE_CODE_{self.placeholder_counter}__"
            self.placeholder_counter += 1
            placeholders[placeholder] = match.group(0)
            return placeholder
        
        # Match `code`
        text = re.sub(
            r'`[^`]+`',
            replace_inline_code,
            text
        )
        
        return text, placeholders
    
    def _extract_images(self, text: str) -> Tuple[str, Dict]:
        """Extract image references."""
        placeholders = {}
        
        def replace_image(match):
            placeholder = f"__IMAGE_{self.placeholder_counter}__"
            self.placeholder_counter += 1
            placeholders[placeholder] = match.group(0)
            return placeholder
        
        # Match ![alt](url)
        text = re.sub(
            r'!\[[^\]]*\]\([^)]+\)',
            replace_image,
            text
        )
        
        return text, placeholders
    
    def _extract_links(self, text: str) -> Tuple[str, Dict]:
        """Extract links, keeping text translatable but preserving URL."""
        placeholders = {}
        
        def replace_link(match):
            link_text = match.group(1)
            url = match.group(2)
            
            # Store the URL
            url_placeholder = f"__LINK_URL_{self.placeholder_counter}__"
            self.placeholder_counter += 1
            placeholders[url_placeholder] = url
            
            # Return translatable format
            return f"[{link_text}]({url_placeholder})"
        
        # Match [text](url)
        text = re.sub(
            r'\[([^\]]+)\]\(([^)]+)\)',
            replace_link,
            text
        )
        
        return text, placeholders
    
    def _extract_html_tags(self, text: str) -> Tuple[str, Dict]:
        """Extract HTML tags embedded in markdown."""
        placeholders = {}
        
        def replace_html(match):
            placeholder = f"__HTML_{self.placeholder_counter}__"
            self.placeholder_counter += 1
            placeholders[placeholder] = match.group(0)
            return placeholder
        
        # Match <tag> or <tag /> or </tag>
        text = re.sub(
            r'<[^>]+>',
            replace_html,
            text
        )
        
        return text, placeholders
    
    def restore_markdown(self, translated_text: str, placeholders: Dict) -> str:
        """
        Restore preserved content into translated markdown.
        
        Args:
            translated_text: Translated text with placeholders
            placeholders: Mapping of placeholders to original content
            
        Returns:
            Complete markdown with translations and preserved content
        """
        result = translated_text
        
        # Replace all placeholders
        for placeholder, original_content in placeholders.items():
            result = result.replace(placeholder, original_content)
        
        return result
    
    # ========================================================================
    # Utility Methods
    # ========================================================================
    
    def is_html(self, content: str) -> bool:
        """Check if content is HTML (vs plain text or markdown)."""
        if not content:
            return False
        
        # Simple heuristic: contains HTML tags
        return bool(re.search(r'<[^>]+>', content))
    
    def extract_translatable_content(self, content: str) -> Tuple[List[Dict], Any]:
        """
        Auto-detect format and extract translatable content.
        
        Args:
            content: Content string (HTML or Markdown)
            
        Returns:
            Tuple appropriate for the detected format:
                - HTML: (segments list, BeautifulSoup object)
                - Markdown: (metadata dict, None)
        """
        if self.is_html(content):
            return self.extract_html_segments(content)
        else:
            markdown_data = self.extract_markdown_segments(content)
            # Return in similar format for consistency
            return [{'text': markdown_data['translatable_text']}], markdown_data
    
    def reconstruct_content(
        self, 
        translations: Any, 
        metadata: Any,
        content_type: str = 'auto'
    ) -> str:
        """
        Reconstruct content with translations.
        
        Args:
            translations: Translation data (format depends on content_type)
            metadata: Metadata from extraction (BeautifulSoup or placeholders dict)
            content_type: 'html', 'markdown', or 'auto'
            
        Returns:
            Reconstructed content string
        """
        if content_type == 'html' or isinstance(metadata, BeautifulSoup):
            return self.reconstruct_html(metadata, translations)
        else:
            # Markdown
            if isinstance(translations, list) and len(translations) > 0:
                translated_text = translations[0].get('translated_text', '')
            else:
                translated_text = translations
            
            placeholders = metadata.get('placeholders', {})
            return self.restore_markdown(translated_text, placeholders)


if __name__ == "__main__":
    """Test the content parser with sample HTML and Markdown."""
    
    parser = ThinkificContentParser()
    
    print("🧪 Testing HTML parsing...\n")
    
    html_sample = """
    <div class="lesson-content">
        <h1>Welcome to KoboToolbox</h1>
        <p>This is a <strong>powerful</strong> data collection platform.</p>
        <img src="logo.png" alt="KoboToolbox Logo" />
        <pre><code>
        // This code should not be translated
        const data = fetchData();
        </code></pre>
        <a href="https://kobotoolbox.org" title="Visit our site">Learn more</a>
    </div>
    """
    
    segments, soup = parser.extract_html_segments(html_sample)
    
    print(f"Extracted {len(segments)} translatable segments:\n")
    for seg in segments[:5]:  # Show first 5
        print(f"  [{seg['type']}] {seg['text'][:60]}...")
    
    print("\n🧪 Testing Markdown parsing...\n")
    
    markdown_sample = """
# Getting Started with KoboToolbox

Learn how to create surveys and collect data.

## Installation

```bash
pip install kobo-cli
```

Visit our [documentation](https://docs.kobotoolbox.org) for more info.

![Dashboard Screenshot](screenshot.png)

Use the `create-form` command to start.
"""
    
    markdown_data = parser.extract_markdown_segments(markdown_sample)
    
    print("Translatable text:")
    print(markdown_data['translatable_text'][:200])
    print(f"\n\nPreserved {len(markdown_data['placeholders'])} elements")
    print("\nPlaceholders:")
    for placeholder, content in list(markdown_data['placeholders'].items())[:5]:
        print(f"  {placeholder}: {content[:50]}...")
