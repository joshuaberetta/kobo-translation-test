# Bulk Retranslation Workflows

## Two Ways to Bulk Retranslate

### 🌐 GitHub Actions (Team-Friendly)
```
┌─────────────────────────────────────────┐
│   GitHub Repository                     │
│                                         │
│   1. Click "Actions" tab                │
│   2. Select "Bulk Retranslate"          │
│   3. Click "Run workflow"               │
│                                         │
│   ┌───────────────────────────────┐     │
│   │ Mode:        [test ▾]         │     │
│   │ Languages:   [es,fr,ar]       │     │
│   │ Files:       [optional]       │     │
│   │ ☑ Confirm    (for all mode)   │     │
│   └───────────────────────────────┘     │
│                                         │
│   4. Click "Run workflow"               │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│   Automatic Processing                  │
│                                         │
│   • Validates inputs                    │
│   • Runs bulk_retranslate.py            │
│   • Creates PR automatically            │
│   • Adds cost summary                   │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│   Pull Request Created                  │
│                                         │
│   🔄 Bulk Retranslation (test) #123     │
│                                         │
│   📊 Summary:                            │
│   - Mode: test                          │
│   - Languages: es, fr, ar               │
│   - Files: 2                            │
│   - Cost: ~$2.50                        │
│                                         │
│   [Review Changes] [Merge]              │
└─────────────────────────────────────────┘
```

**✅ Best for:**
- Team members without technical setup
- Consistent, reproducible results
- Automatic PR creation
- Cost tracking in PR

---

### 💻 Local Scripts (Developer-Friendly)
```
┌─────────────────────────────────────────┐
│   Terminal / Command Line               │
│                                         │
│   $ ./scripts/retranslate.sh test-es    │
│                                         │
│   OR                                    │
│                                         │
│   $ python scripts/bulk_retranslate.py \│
│       --language es \                   │
│       --files test_simple.md            │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│   Direct Translation                    │
│                                         │
│   [1/2] test_simple.md                  │
│     → ES ✅                              │
│   [2/2] test_complex.md                 │
│     → ES ✅                              │
│                                         │
│   📊 Summary                             │
│   ✅ Successful: 2                       │
│   💰 Cost: $1.20                         │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│   Manual Git Workflow                   │
│                                         │
│   $ git status                          │
│   $ git diff docs/es/test_simple.md     │
│   $ git add docs/es/                    │
│   $ git commit -m "Retranslate"         │
│   $ git push                            │
└─────────────────────────────────────────┘
```

**✅ Best for:**
- Quick local testing
- Development and debugging
- Custom file selection
- Immediate feedback

---

## Mode Comparison

| Mode | Files Translated | Use Case | Cost (est.) |
|------|------------------|----------|-------------|
| `test` | 2-3 test files | Safe testing | $0.50-$1 |
| `specific` | Files you list | Targeted updates | Varies |
| `all` | ALL ~100 files | Major refresh | $15-30/lang |

---

## Workflow Comparison

| Feature | GitHub Actions | Local Scripts |
|---------|---------------|---------------|
| **Setup Required** | None | Python + deps |
| **Best For** | Teams | Developers |
| **PR Creation** | Automatic | Manual |
| **Cost Tracking** | In PR | Terminal only |
| **Confirmation** | UI checkbox | Shell prompt |
| **Speed** | Cloud runner | Local machine |
| **Logs** | GitHub Actions | Terminal |
| **Access** | Anyone with repo access | Local clone |

---

## Decision Tree

```
Do you have local Python environment set up?
│
├─ NO  → Use GitHub Actions
│        (No setup required, click buttons in browser)
│
└─ YES → Choose based on need:
         │
         ├─ Quick test/development
         │  → Use local scripts (faster feedback)
         │
         └─ Team collaboration/documentation
            → Use GitHub Actions (automatic PR)
```

---

## Example: Testing Skill Updates

### Method 1: GitHub Actions
1. Update skills → commit → push
2. Actions → Bulk Retranslate → test mode
3. Review PR with before/after comparison
4. If good → Actions → all mode

### Method 2: Local Scripts
1. Update skills locally
2. `python3 scripts/split_skill_by_language.py`
3. `./scripts/retranslate.sh test-es`
4. `git diff docs/es/test_simple.md`
5. If good → `./scripts/retranslate.sh all-es`
6. Commit and push

---

## Security Note

Both methods require:
- `ANTHROPIC_API_KEY` (for Claude API)
- `TRANSLATION_BOT_TOKEN` (for GitHub PR creation - Actions only)

Store these as:
- **GitHub Actions:** Repository Secrets
- **Local:** `.env` file (git-ignored)
