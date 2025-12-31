# Test UI Template Autocomplete

This file is for testing the `{{ui:KEY}}` autocomplete functionality.

## Test Cases

Try typing the following to test autocomplete:

{{ui:could}}

### Basic Autocomplete
- `{{ui:` (should show top suggestions)
- `{{ui:dep` (should show "Deployed", "Deploying...", etc.)
- `{{ui:data` (should show "Data", related strings)
- `{{ui:save` (should show "Save", "Save Changes", etc.)
- `{{ui:form` (should show "Form", form-related strings)
- `{{ui:delete` (should show "Delete", "Delete Project", etc.)

### Exact Matches
- `{{ui:Deploy}}` - Testing exact key
- `{{ui:Data}}` - Testing exact key
- `{{ui:Save}}` - Testing exact key

### With Formatting
- `{{ui:Deploy|bold}}` - Should format as **Deploy**
- `{{ui:Data|code}}` - Should format as `Data`
- `{{ui:Form|upper}}` - Should format as FORM
- `{{ui:Save Changes|upper,bold}}` - Should format as **SAVE CHANGES**

## Expected Behavior

1. **Trigger**: Autocomplete should trigger automatically after typing `{{ui:`
2. **Filtering**: As you type more characters, suggestions should filter down
3. **Relevance**: Matches starting with your query should appear first
4. **Formatting**: After the pipe `|`, formatting options should appear

## Common UI Strings to Try

From the extracted 843 strings, here are some commonly used ones:

- Deploy
- Data
- Form
- Save
- Delete
- Edit
- Settings
- Projects
- Library
- Upload
- Download
- Export
- Import
- Share
- Archive
- Unarchive
- Submit
- Question
- Group
- Validation
- Required

## Debugging

If autocomplete isn't working:

1. Check the status bar message when opening a markdown file
2. Should see: "Loaded 843 UI strings"
3. Press `Ctrl+Space` (or `Cmd+Space` on Mac) to manually trigger
4. Check Output panel: View → Output → "Kobo UI Template Autocomplete"
