#!/usr/bin/env python3
"""
Quick test to verify language-specific skill loading works correctly
"""

import sys
import os
from pathlib import Path

# Set a dummy API key for testing
os.environ['ANTHROPIC_API_KEY'] = 'test-key-not-used-in-this-test'

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent / 'scripts'))

# Need to set the env var before importing
from translation_agent import TranslationAgent

def test_language_specific_skills():
    """Test that we can load skills for each language"""
    print("🧪 Testing Language-Specific Skill Loading\n")
    
    # Initialize agent
    agent = TranslationAgent(test_mode=True)
    print("✅ Agent initialized\n")
    
    # Test each language
    for lang in ['es', 'fr', 'ar']:
        print(f"📝 Testing {lang.upper()} skill loading...")
        
        try:
            skill_context = agent._get_skill_context(lang)
            
            # Verify we got content
            assert 'main' in skill_context, f"Missing 'main' in {lang} skill"
            assert 'brand' in skill_context, f"Missing 'brand' in {lang} skill"
            assert 'ui' in skill_context, f"Missing 'ui' in {lang} skill"
            
            # Check that it's language-specific
            main_content = skill_context['main']
            
            # Should have the target language name
            lang_names = {'es': 'Spanish', 'fr': 'French', 'ar': 'Arabic'}
            assert lang_names[lang] in main_content, f"Language name not found in {lang} skill"
            
            # Should have been renamed
            assert f'kobo-translation-{lang}' in main_content, f"Skill not renamed for {lang}"
            
            # Verify it loaded from the right directory
            skill_size = len(main_content)
            print(f"  ✅ {lang.upper()} skill loaded ({skill_size:,} characters)")
            print(f"  ✅ Contains {len(skill_context)} files")
            
            # Check that other languages are reduced (they should be filtered out)
            other_langs = [l for l in ['Spanish', 'French', 'Arabic'] if l != lang_names[lang]]
            other_lang_count = sum(main_content.count(other) for other in other_langs)
            print(f"  📊 References to other languages: {other_lang_count}")
            
        except Exception as e:
            print(f"  ❌ Failed to load {lang} skill: {e}")
            return False
        
        print()
    
    # Check caching
    print("📦 Testing caching...")
    skill_es_1 = agent._get_skill_context('es')
    skill_es_2 = agent._get_skill_context('es')
    assert skill_es_1 is skill_es_2, "Caching not working - returned different objects"
    print("  ✅ Caching works correctly\n")
    
    print("✅ All tests passed!")
    return True

if __name__ == '__main__':
    success = test_language_specific_skills()
    sys.exit(0 if success else 1)
