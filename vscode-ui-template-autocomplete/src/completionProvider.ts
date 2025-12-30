import * as vscode from 'vscode';
import { UIString } from './poParser';

/**
 * Completion provider for {{ui:KEY}} templates in markdown files
 */
export class UITemplateCompletionProvider implements vscode.CompletionItemProvider {
    private uiStrings: UIString[] = [];

    constructor(uiStrings: UIString[]) {
        this.uiStrings = uiStrings;
    }

    /**
     * Update the UI strings (when PO file is reloaded)
     */
    public updateUIStrings(uiStrings: UIString[]): void {
        this.uiStrings = uiStrings;
    }

    /**
     * Provide completion items
     */
    public provideCompletionItems(
        document: vscode.TextDocument,
        position: vscode.Position,
        token: vscode.CancellationToken,
        context: vscode.CompletionContext
    ): vscode.CompletionItem[] | undefined {
        // Get the text before the cursor on the current line
        const linePrefix = document.lineAt(position).text.substring(0, position.character);

        // Check if we're inside a {{ui: template
        const templateMatch = linePrefix.match(/\{\{ui:([^}|]*)$/);
        if (!templateMatch) {
            return undefined;
        }

        const searchTerm = templateMatch[1];

        // Fuzzy search UI strings
        const matches = this.searchUIStrings(searchTerm);

        // Create completion items
        return matches.map(uiString => {
            const item = new vscode.CompletionItem(
                uiString.key,
                vscode.CompletionItemKind.Value
            );

            // The text to insert (just the key, without the template syntax)
            item.insertText = uiString.key;

            // Detail shown in the completion list
            item.detail = 'UI Template String';

            // Documentation/preview
            item.documentation = new vscode.MarkdownString(
                `**Template:** \`{{ui:${uiString.key}}}\`\n\n` +
                `**With formatting:** \`{{ui:${uiString.key}|bold}}\``
            );

            // Sort text for ordering
            item.sortText = uiString.key;

            return item;
        });
    }

    /**
     * Fuzzy search UI strings
     */
    private searchUIStrings(query: string, limit: number = 50): UIString[] {
        if (!query || query.trim() === '') {
            // Return top matches if no query
            return this.uiStrings.slice(0, limit);
        }

        const normalizedQuery = query.toLowerCase().trim();

        // Find matches
        const matches = this.uiStrings.filter(s =>
            s.normalizedKey.includes(normalizedQuery)
        );

        // Sort by relevance
        matches.sort((a, b) => {
            const aStarts = a.normalizedKey.startsWith(normalizedQuery);
            const bStarts = b.normalizedKey.startsWith(normalizedQuery);

            if (aStarts && !bStarts) return -1;
            if (!aStarts && bStarts) return 1;

            return a.key.length - b.key.length;
        });

        return matches.slice(0, limit);
    }
}

/**
 * Completion provider for formatting options (bold, italic, code, etc.)
 * Triggers after the pipe character: {{ui:Deploy|
 */
export class FormattingCompletionProvider implements vscode.CompletionItemProvider {
    private formattingOptions = [
        { label: 'bold', description: 'Bold text: **text**' },
        { label: 'italic', description: 'Italic text: *text*' },
        { label: 'code', description: 'Code text: `text`' },
        { label: 'upper', description: 'UPPERCASE' },
        { label: 'lower', description: 'lowercase' },
        { label: 'upper,bold', description: 'UPPERCASE and bold' },
        { label: 'upper,code', description: 'UPPERCASE and code' }
    ];

    public provideCompletionItems(
        document: vscode.TextDocument,
        position: vscode.Position,
        token: vscode.CancellationToken,
        context: vscode.CompletionContext
    ): vscode.CompletionItem[] | undefined {
        const linePrefix = document.lineAt(position).text.substring(0, position.character);

        // Check if we're after a pipe in a {{ui: template
        const formatMatch = linePrefix.match(/\{\{ui:[^}|]+\|([^}]*)$/);
        if (!formatMatch) {
            return undefined;
        }

        // Create completion items for formatting options
        return this.formattingOptions.map(option => {
            const item = new vscode.CompletionItem(
                option.label,
                vscode.CompletionItemKind.Property
            );

            item.insertText = option.label;
            item.detail = 'Formatting option';
            item.documentation = option.description;

            return item;
        });
    }
}
