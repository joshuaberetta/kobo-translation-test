import * as fs from 'fs';
import * as path from 'path';

export interface UIString {
    key: string;           // Original msgid
    normalizedKey: string; // Lowercase version for matching
    label: string;         // Display label for autocomplete
}

/**
 * Simple PO file parser that extracts msgid entries.
 * Handles multi-line msgid strings and basic PO format.
 */
export class POParser {
    private uiStrings: UIString[] = [];

    /**
     * Parse a PO file and extract all msgid entries
     */
    public parse(filePath: string): UIString[] {
        if (!fs.existsSync(filePath)) {
            throw new Error(`PO file not found: ${filePath}`);
        }

        const content = fs.readFileSync(filePath, 'utf-8');
        const lines = content.split('\n');

        this.uiStrings = [];
        let currentMsgId = '';
        let inMsgId = false;

        for (let i = 0; i < lines.length; i++) {
            const line = lines[i].trim();

            // Start of msgid
            if (line.startsWith('msgid "')) {
                inMsgId = true;
                // Extract text between quotes
                const match = line.match(/msgid\s+"(.*)"/);
                if (match) {
                    currentMsgId = match[1];
                }
            }
            // Continuation of multi-line msgid
            else if (inMsgId && line.startsWith('"') && !line.startsWith('msgstr')) {
                const match = line.match(/"(.*)"/);
                if (match) {
                    currentMsgId += match[1];
                }
            }
            // End of msgid (when we hit msgstr)
            else if (line.startsWith('msgstr')) {
                inMsgId = false;

                // Only add non-empty msgids
                if (currentMsgId && currentMsgId.trim() !== '') {
                    this.addUIString(currentMsgId);
                }

                currentMsgId = '';
            }
        }

        // Sort by key length (shorter first) for better autocomplete ordering
        this.uiStrings.sort((a, b) => a.key.length - b.key.length);

        return this.uiStrings;
    }

    /**
     * Add a UI string with both original and normalized versions
     */
    private addUIString(msgId: string): void {
        // Decode common escape sequences
        const decoded = msgId
            .replace(/\\n/g, '\n')
            .replace(/\\t/g, '\t')
            .replace(/\\"/g, '"')
            .replace(/\\\\/g, '\\');

        const uiString: UIString = {
            key: decoded,
            normalizedKey: this.normalizeKey(decoded),
            label: decoded
        };

        this.uiStrings.push(uiString);
    }

    /**
     * Normalize a key for case-insensitive matching
     */
    private normalizeKey(key: string): string {
        return key.toLowerCase().trim();
    }

    /**
     * Get all parsed UI strings
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
