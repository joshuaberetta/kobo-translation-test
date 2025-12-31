import * as fs from 'fs';
import * as path from 'path';

export interface UIString {
    key: string;           // Original string
    normalizedKey: string; // Lowercase version for matching
    label: string;         // Display label for autocomplete
}

/**
 * Simple JSON loader for UI strings extracted from PO files.
 * Much faster and more reliable than parsing PO files directly.
 */
export class UIStringLoader {
    private uiStrings: UIString[] = [];

    /**
     * Load UI strings from a JSON file
     */
    public loadFromJSON(filePath: string): UIString[] {
        if (!fs.existsSync(filePath)) {
            throw new Error(`JSON file not found: ${filePath}`);
        }

        const content = fs.readFileSync(filePath, 'utf-8');
        const data = JSON.parse(content);

        if (!data.strings || !Array.isArray(data.strings)) {
            throw new Error(`Invalid JSON format: expected 'strings' array`);
        }

        this.uiStrings = data.strings.map((str: string) => ({
            key: str,
            normalizedKey: this.normalizeKey(str),
            label: str
        }));

        // Sort by key length (shorter first) for better autocomplete ordering
        this.uiStrings.sort((a, b) => a.key.length - b.key.length);

        return this.uiStrings;
    }

    /**
     * Normalize a key for case-insensitive matching
     */
    private normalizeKey(key: string): string {
        return key.toLowerCase().trim();
    }

    /**
     * Get all loaded UI strings
     */
    public getUIStrings(): UIString[] {
        return this.uiStrings;
    }

    /**
     * Fuzzy search UI strings
     * Returns strings that contain the search term (case-insensitive)
     */
    public search(query: string, limit: number = 50): UIString[] {
        if (!query || query.trim() === '') {
            return this.uiStrings.slice(0, limit);
        }

        const normalizedQuery = query.toLowerCase().trim();

        // Find matches
        const matches = this.uiStrings.filter(s =>
            s.normalizedKey.includes(normalizedQuery)
        );

        // Sort by relevance:
        // 1. Starts with query (highest priority)
        // 2. Word boundary match
        // 3. Contains query (lowest priority)
        matches.sort((a, b) => {
            const aStarts = a.normalizedKey.startsWith(normalizedQuery);
            const bStarts = b.normalizedKey.startsWith(normalizedQuery);

            if (aStarts && !bStarts) return -1;
            if (!aStarts && bStarts) return 1;

            // If both start or both don't start, sort by length
            return a.key.length - b.key.length;
        });

        return matches.slice(0, limit);
    }
}
