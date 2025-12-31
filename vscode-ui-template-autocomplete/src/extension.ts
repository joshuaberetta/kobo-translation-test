import * as vscode from 'vscode';
import * as path from 'path';
import { UIStringLoader } from './jsonLoader';
import { UITemplateCompletionProvider, FormattingCompletionProvider } from './completionProvider';

let uiTemplateProvider: UITemplateCompletionProvider | undefined;
let formattingProvider: FormattingCompletionProvider | undefined;

/**
 * Extension activation
 */
export function activate(context: vscode.ExtensionContext) {
    console.log('Kobo UI Template Autocomplete extension is now active');

    // Load UI strings from PO file
    const uiStrings = loadUIStrings();

    if (!uiStrings || uiStrings.length === 0) {
        vscode.window.showWarningMessage(
            'Kobo UI Template Autocomplete: No UI strings loaded. ' +
            'Please check the PO file path in settings.'
        );
    } else {
        vscode.window.showInformationMessage(
            `Kobo UI Template Autocomplete: Loaded ${uiStrings.length} UI strings`
        );
    }

    // Register completion provider for UI template keys
    uiTemplateProvider = new UITemplateCompletionProvider(uiStrings);
    const uiCompletionDisposable = vscode.languages.registerCompletionItemProvider(
        { language: 'markdown', scheme: 'file' },
        uiTemplateProvider,
        ':' // Trigger on colon after {{ui
    );

    // Register completion provider for formatting options
    formattingProvider = new FormattingCompletionProvider();
    const formattingCompletionDisposable = vscode.languages.registerCompletionItemProvider(
        { language: 'markdown', scheme: 'file' },
        formattingProvider,
        '|' // Trigger on pipe for formatting
    );

    // Register reload command
    const reloadCommand = vscode.commands.registerCommand(
        'koboUITemplate.reload',
        () => {
            const newUIStrings = loadUIStrings();
            if (uiTemplateProvider && newUIStrings) {
                uiTemplateProvider.updateUIStrings(newUIStrings);
                vscode.window.showInformationMessage(
                    `Reloaded ${newUIStrings.length} UI strings`
                );
            }
        }
    );

    // Add to subscriptions
    context.subscriptions.push(
        uiCompletionDisposable,
        formattingCompletionDisposable,
        reloadCommand
    );
}

/**
 * Load UI strings from JSON file
 */
function loadUIStrings() {
    try {
        // Get workspace folder
        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders || workspaceFolders.length === 0) {
            vscode.window.showErrorMessage(
                'Kobo UI Template Autocomplete: No workspace folder open'
            );
            return [];
        }

        const workspaceRoot = workspaceFolders[0].uri.fsPath;

        // Get JSON file path from configuration
        const config = vscode.workspace.getConfiguration('koboUITemplate');
        const relativeJsonPath = config.get<string>('jsonFilePath') ||
            'external/form-builder-translations/ui-strings.json';

        const jsonFilePath = path.join(workspaceRoot, relativeJsonPath);

        // Load from JSON file
        const loader = new UIStringLoader();
        const uiStrings = loader.loadFromJSON(jsonFilePath);

        console.log(`Loaded ${uiStrings.length} UI strings from ${jsonFilePath}`);
        return uiStrings;

    } catch (error) {
        const errorMessage = error instanceof Error ? error.message : String(error);
        vscode.window.showErrorMessage(
            `Kobo UI Template Autocomplete: Failed to load UI strings: ${errorMessage}`
        );
        console.error('Error loading UI strings:', error);
        return [];
    }
}

/**
 * Extension deactivation
 */
export function deactivate() {
    console.log('Kobo UI Template Autocomplete extension is now deactivated');
}
