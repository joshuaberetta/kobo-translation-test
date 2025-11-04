#!/usr/bin/env python3
"""
Test Transifex Integration

Quick test to verify Transifex API connection and fetch sample terminology
"""

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent / 'scripts'))

from transifex_sync import TransifexSync


def test_transifex_connection():
    """Test basic Transifex API connection"""
    print("🧪 Testing Transifex Integration")
    print("=" * 60)
    
    try:
        # Initialize sync
        print("\n1. Initializing TransifexSync...")
        sync = TransifexSync()
        print("   ✅ Connected successfully")
        
        # List resources
        print("\n2. Fetching available resources...")
        resources = sync.get_project_resources('kobotoolbox', 'kobotoolbox')
        
        if resources:
            print(f"   ✅ Found {len(resources)} resources:")
            for r in resources[:5]:  # Show first 5
                print(f"      - {r['slug']}: {r['name']} ({r['string_count']} strings)")
            if len(resources) > 5:
                print(f"      ... and {len(resources) - 5} more")
        else:
            print("   ⚠️  No resources found")
        
        # Test fetching translations for Spanish
        print("\n3. Fetching sample Spanish translations...")
        translations = sync.sync_language_terminology('es')
        
        if translations:
            print(f"   ✅ Retrieved {len(translations)} Spanish UI terms")
            print("\n   Sample terms:")
            for i, (english, spanish) in enumerate(list(translations.items())[:10]):
                print(f"      {english} → {spanish}")
                if i >= 9:
                    break
            
            if len(translations) > 10:
                print(f"      ... and {len(translations) - 10} more")
            
            # Save to file
            print("\n4. Saving to skill reference file...")
            output_path = sync.save_terminology_file(translations, 'es')
            print(f"   ✅ Saved to: {output_path}")
            
            print("\n" + "=" * 60)
            print("✨ Test complete! Transifex integration is working.")
            print("\nNext steps:")
            print("  1. Review the saved file:", output_path)
            print("  2. Run a translation with: python scripts/translate_srt.py ...")
            print("  3. The Transifex terminology will be automatically included!")
            
        else:
            print("   ⚠️  No translations retrieved")
            print("\nPossible issues:")
            print("  - Wrong organization/project name")
            print("  - Resource doesn't have Spanish translations")
            print("  - API token lacks permissions")
        
    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        print("\nMake sure you have set TRANSIFEX_API_TOKEN in your .env file")
        print("Get your token at: https://app.transifex.com/user/settings/api/")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    test_transifex_connection()
