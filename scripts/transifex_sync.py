#!/usr/bin/env python3
"""
Transifex Sync - Fetch KoboToolbox UI translations from Transifex
Keeps docs and SRT translations aligned with official UI terminology
"""

import os
import sys
import json
import requests
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class TransifexSync:
    """
    Sync KoboToolbox UI terminology from Transifex to local translation skills
    """
    
    TRANSIFEX_API = "https://rest.api.transifex.com"
    
    # KoboToolbox project configuration
    DEFAULT_ORG = "kobotoolbox"
    DEFAULT_PROJECT = "kobotoolbox"
    
    def __init__(self, api_token: str = None):
        """
        Initialize Transifex sync
        
        Args:
            api_token: Transifex API token (or uses TRANSIFEX_API_TOKEN env var)
        """
        self.api_token = api_token or os.getenv('TRANSIFEX_API_TOKEN')
        if not self.api_token:
            raise ValueError(
                "TRANSIFEX_API_TOKEN environment variable not set.\n"
                "Get your token from: https://app.transifex.com/user/settings/api/"
            )
        
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/vnd.api+json"
        }
        
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def get_project_resources(self, organization: str, project: str) -> List[Dict]:
        """
        Get all resources (translation files) in a Transifex project
        
        Args:
            organization: Organization slug
            project: Project slug
        
        Returns:
            List of resource dictionaries
        """
        print(f"📋 Fetching resources from {organization}/{project}...", file=sys.stderr)
        
        url = f"{self.TRANSIFEX_API}/resources"
        params = {
            "filter[project]": f"o:{organization}:p:{project}"
        }
        
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            resources = []
            
            for item in data.get('data', []):
                resource = {
                    'id': item['id'],
                    'slug': item['attributes']['slug'],
                    'name': item['attributes']['name'],
                    'string_count': item['attributes'].get('string_count', 0)
                }
                resources.append(resource)
            
            print(f"✅ Found {len(resources)} resources", file=sys.stderr)
            return resources
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to fetch resources: {e}", file=sys.stderr)
            raise
    
    def get_resource_translations(self, 
                                 organization: str,
                                 project: str,
                                 resource: str,
                                 language: str) -> Dict[str, str]:
        """
        Fetch UI translations for a specific language and resource
        
        Args:
            organization: Organization slug
            project: Project slug  
            resource: Resource slug
            language: Language code (e.g., 'es', 'fr', 'ar')
        
        Returns:
            Dictionary mapping English source strings to translations
        """
        print(f"  📥 Fetching {language.upper()} translations for resource '{resource}'...", 
              file=sys.stderr)
        
        # Build resource filter
        resource_filter = f"o:{organization}:p:{project}:r:{resource}"
        
        url = f"{self.TRANSIFEX_API}/resource_translations"
        params = {
            "filter[resource]": resource_filter,
            "filter[language]": f"l:{language}"
        }
        
        try:
            response = self.session.get(url, params=params, timeout=60)
            response.raise_for_status()
            
            data = response.json()
            translations = {}
            
            for item in data.get('data', []):
                attrs = item.get('attributes', {})
                source = attrs.get('strings', {}).get('other', '')
                translation = attrs.get('strings', {}).get('other', '')
                
                # Only include if both source and translation exist
                if source and translation and source != translation:
                    translations[source] = translation
            
            print(f"    ✓ Retrieved {len(translations)} translations", file=sys.stderr)
            return translations
            
        except requests.exceptions.RequestException as e:
            print(f"    ⚠️  Failed to fetch translations: {e}", file=sys.stderr)
            return {}
    
    def sync_language_terminology(self, 
                                 language: str,
                                 organization: str = None,
                                 project: str = None,
                                 resources: List[str] = None) -> Dict[str, str]:
        """
        Sync all UI terminology for a specific language
        
        Args:
            language: Target language code
            organization: Transifex organization (default: kobotoolbox)
            project: Transifex project (default: kobotoolbox)
            resources: List of resource slugs to sync (default: all)
        
        Returns:
            Combined dictionary of all translations
        """
        org = organization or self.DEFAULT_ORG
        proj = project or self.DEFAULT_PROJECT
        
        print(f"\n🔄 Syncing {language.upper()} terminology from Transifex...", file=sys.stderr)
        print(f"   Organization: {org}", file=sys.stderr)
        print(f"   Project: {proj}", file=sys.stderr)
        
        all_translations = {}
        
        # Get available resources if not specified
        if not resources:
            available_resources = self.get_project_resources(org, proj)
            # Focus on main UI resources (you can customize this)
            resources = [r['slug'] for r in available_resources 
                        if any(keyword in r['slug'].lower() 
                              for keyword in ['interface', 'ui', 'main', 'core'])]
            
            if not resources and available_resources:
                # Fallback: use first resource
                resources = [available_resources[0]['slug']]
        
        # Fetch translations for each resource
        for resource in resources:
            translations = self.get_resource_translations(org, proj, resource, language)
            all_translations.update(translations)
        
        print(f"\n✅ Total translations retrieved: {len(all_translations)}", file=sys.stderr)
        return all_translations
    
    def format_terminology_markdown(self, 
                                    translations: Dict[str, str],
                                    language: str) -> str:
        """
        Format translations as markdown reference file
        
        Args:
            translations: Dictionary of source -> translation
            language: Target language code
        
        Returns:
            Formatted markdown content
        """
        lines = [
            "# Official UI Terminology (from Transifex)",
            "",
            "**⚠️ AUTO-GENERATED FILE - DO NOT EDIT MANUALLY**",
            "",
            f"This file contains official UI translations from the KoboToolbox Transifex project.",
            f"Last synced: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}",
            f"Language: {language.upper()}",
            "",
            "Use these translations for UI elements, buttons, and interface terms.",
            "",
            "## Terminology",
            "",
            "| English Term | Translation | Notes |",
            "|--------------|-------------|-------|"
        ]
        
        # Sort by English term for consistency
        for english, translation in sorted(translations.items()):
            # Escape pipe characters in content
            english_safe = english.replace('|', '\\|')
            translation_safe = translation.replace('|', '\\|')
            lines.append(f"| {english_safe} | {translation_safe} | UI |")
        
        return '\n'.join(lines)
    
    def save_terminology_file(self, 
                             translations: Dict[str, str],
                             language: str,
                             base_skill_path: Path = None) -> Path:
        """
        Save terminology to skill reference file
        
        Args:
            translations: Dictionary of translations
            language: Target language code
            base_skill_path: Base path to skill directory (default: skills/kobo-translation-{lang})
        
        Returns:
            Path to saved file
        """
        if not base_skill_path:
            base_skill_path = Path(f'skills/kobo-translation-{language}')
        
        # Create directories if they don't exist
        refs_dir = base_skill_path / 'references'
        refs_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate markdown content
        content = self.format_terminology_markdown(translations, language)
        
        # Save to file
        output_path = refs_dir / 'transifex-ui-terminology.md'
        output_path.write_text(content, encoding='utf-8')
        
        print(f"💾 Saved to: {output_path}", file=sys.stderr)
        return output_path
    
    def sync_all_languages(self, 
                          languages: List[str] = None,
                          organization: str = None,
                          project: str = None) -> Dict[str, Path]:
        """
        Sync terminology for multiple languages
        
        Args:
            languages: List of language codes (default: ['es', 'fr', 'ar'])
            organization: Transifex organization
            project: Transifex project
        
        Returns:
            Dictionary mapping language codes to saved file paths
        """
        if not languages:
            languages = ['es', 'fr', 'ar']
        
        print(f"\n🌐 Syncing terminology for {len(languages)} languages...", file=sys.stderr)
        print(f"=" * 60, file=sys.stderr)
        
        results = {}
        
        for lang in languages:
            try:
                # Fetch translations
                translations = self.sync_language_terminology(
                    lang, 
                    organization, 
                    project
                )
                
                if translations:
                    # Save to file
                    output_path = self.save_terminology_file(translations, lang)
                    results[lang] = output_path
                else:
                    print(f"⚠️  No translations found for {lang.upper()}", file=sys.stderr)
                
            except Exception as e:
                print(f"❌ Failed to sync {lang.upper()}: {e}", file=sys.stderr)
                continue
        
        print(f"\n" + "=" * 60, file=sys.stderr)
        print(f"✅ Synced {len(results)}/{len(languages)} languages successfully", file=sys.stderr)
        
        return results


def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Sync KoboToolbox UI terminology from Transifex'
    )
    
    parser.add_argument(
        '--language', '-l',
        action='append',
        choices=['es', 'fr', 'ar'],
        help='Target language(s) to sync (can specify multiple times, default: all)'
    )
    parser.add_argument(
        '--organization', '-o',
        default='kobotoolbox',
        help='Transifex organization slug (default: kobotoolbox)'
    )
    parser.add_argument(
        '--project', '-p',
        default='kobotoolbox',
        help='Transifex project slug (default: kobotoolbox)'
    )
    parser.add_argument(
        '--api-token',
        help='Transifex API token (or use TRANSIFEX_API_TOKEN env var)'
    )
    parser.add_argument(
        '--list-resources',
        action='store_true',
        help='List available resources and exit'
    )
    
    args = parser.parse_args()
    
    try:
        # Initialize sync
        sync = TransifexSync(api_token=args.api_token)
        
        # List resources if requested
        if args.list_resources:
            resources = sync.get_project_resources(args.organization, args.project)
            print("\nAvailable resources:")
            for r in resources:
                print(f"  - {r['slug']}: {r['name']} ({r['string_count']} strings)")
            return
        
        # Sync languages
        languages = args.language or ['es', 'fr', 'ar']
        results = sync.sync_all_languages(
            languages=languages,
            organization=args.organization,
            project=args.project
        )
        
        if results:
            print(f"\n✨ Sync complete! Updated files:")
            for lang, path in results.items():
                print(f"  {lang.upper()}: {path}")
        else:
            print(f"\n⚠️  No files were updated", file=sys.stderr)
            sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
