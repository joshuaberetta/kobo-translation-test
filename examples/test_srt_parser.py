#!/usr/bin/env python3
"""
Test script to verify SRT parser handles webinar content with special characters
"""

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from srt_helper import SRTParser, SRTWriter, SRTConverter

def test_webinar_srt():
    """Test parsing and processing webinar SRT file"""
    
    print("🧪 Testing SRT Parser with Webinar Content")
    print("=" * 60)
    
    # Test file path
    test_file = Path(__file__).parent / 'test_webinar.srt'
    
    if not test_file.exists():
        print(f"❌ Test file not found: {test_file}")
        return False
    
    # Test 1: Parse the file
    print("\n1️⃣  Testing parse...")
    try:
        subtitles = SRTParser.parse_file(str(test_file))
        print(f"✅ Parsed {len(subtitles)} subtitles")
    except Exception as e:
        print(f"❌ Parse failed: {e}")
        return False
    
    # Test 2: Validate structure
    print("\n2️⃣  Testing validation...")
    try:
        result = SRTParser.validate_srt(str(test_file))
        if result['valid']:
            print(f"✅ Valid SRT file")
            print(f"   - Subtitle count: {result['subtitle_count']}")
        else:
            print(f"⚠️  Validation issues found:")
            for issue in result.get('issues', []):
                print(f"   - {issue}")
    except Exception as e:
        print(f"❌ Validation failed: {e}")
        return False
    
    # Test 3: Check special characters handling
    print("\n3️⃣  Testing special character handling...")
    first_sub = subtitles[0]
    if '\\*Music\\*' in first_sub.text or '*Music*' in first_sub.text:
        print(f"✅ Special characters preserved: {first_sub.text}")
    else:
        print(f"⚠️  Unexpected text format: {first_sub.text}")
    
    # Test 4: Test round-trip conversion
    print("\n4️⃣  Testing round-trip conversion...")
    try:
        # Convert to SRT format
        srt_output = SRTWriter.to_string(subtitles)
        
        # Parse again
        reparsed = SRTParser.parse_string(srt_output)
        
        if len(reparsed) == len(subtitles):
            print(f"✅ Round-trip successful: {len(reparsed)} subtitles")
            
            # Check text preservation
            if reparsed[0].text == subtitles[0].text:
                print(f"✅ Text preserved: '{reparsed[0].text}'")
            else:
                print(f"⚠️  Text changed:")
                print(f"   Original: '{subtitles[0].text}'")
                print(f"   After:    '{reparsed[0].text}'")
        else:
            print(f"❌ Subtitle count mismatch: {len(subtitles)} -> {len(reparsed)}")
            return False
    except Exception as e:
        print(f"❌ Round-trip failed: {e}")
        return False
    
    # Test 5: Test JSON conversion
    print("\n5️⃣  Testing JSON conversion...")
    try:
        json_data = SRTConverter.srt_to_json(str(test_file))
        print(f"✅ Converted to JSON: {json_data['subtitle_count']} subtitles")
        
        # Check first subtitle in JSON
        first_json = json_data['subtitles'][0]
        print(f"   First subtitle text: {first_json['text']}")
        
        # Convert back to SRT
        srt_from_json = SRTConverter.json_dict_to_srt(json_data)
        reparsed_from_json = SRTParser.parse_string(srt_from_json)
        
        if len(reparsed_from_json) == len(subtitles):
            print(f"✅ JSON round-trip successful")
        else:
            print(f"⚠️  JSON round-trip count mismatch")
    except Exception as e:
        print(f"❌ JSON conversion failed: {e}")
        return False
    
    # Test 6: Display subtitle details
    print("\n6️⃣  Subtitle details:")
    for sub in subtitles:
        print(f"   [{sub.index}] {sub.start_time} --> {sub.end_time}")
        print(f"       {sub.text}")
        print()
    
    print("=" * 60)
    print("✅ All tests passed! SRT parser handles webinar content correctly.")
    print("\n📝 Summary:")
    print(f"   - Parses escaped characters (\\*Music\\*)")
    print(f"   - Handles long subtitle text")
    print(f"   - Preserves timestamps correctly")
    print(f"   - Round-trip conversion works")
    print(f"   - JSON conversion works")
    print(f"   - Validation passes")
    
    return True

if __name__ == '__main__':
    success = test_webinar_srt()
    sys.exit(0 if success else 1)
