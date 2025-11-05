# Quick Start: Translation Guide Maintenance

**TL;DR**: Expand Arabic guide and maintain all language guides efficiently

## ⚡ 3-Minute Setup

### 1. Set API Key
```bash
export ANTHROPIC_API_KEY='your-key-here'
```

### 2. Generate Comprehensive Arabic Guide
```bash
python scripts/generate_arabic_guide.py
```

### 3. Validate All Guides
```bash
python scripts/validate_guides.py
```

**Done!** You now have:
- ✅ Complete Arabic guide (600+ lines)
- ✅ All reference files populated
- ✅ Quality validation report

## 🎯 Common Tasks

### Task: Add New Term to All Languages

**Edit**: `terminology/master_terminology.yaml`
```yaml
brand_terms:
  - english: "New Feature"
    category: "OFFICIAL"
    translations:
      fr: "Nouvelle fonctionnalité"
      es: "Nueva funcionalidad"
      ar: "ميزة جديدة"
```

**Sync**:
```bash
python scripts/sync_terminology.py
```

**Time**: 2 minutes vs 30+ minutes manually

### Task: Check Translation Quality

```bash
# All languages
python scripts/validate_guides.py

# Specific language
python scripts/validate_guides.py --language ar

# See errors and suggestions
```

### Task: Auto-Generate Missing Translations

```bash
# Find gaps
python scripts/sync_terminology.py --validate-only

# Fill automatically
python scripts/sync_terminology.py --auto-generate
```

## 📁 File Structure

```
terminology/master_terminology.yaml   ← Add terms here
scripts/generate_arabic_guide.py      ← Generate content
scripts/sync_terminology.py           ← Sync to all languages
scripts/validate_guides.py            ← Check quality
```

## 🔄 Typical Workflow

```bash
# 1. Add terms to master database
vim terminology/master_terminology.yaml

# 2. Sync to all guides
python scripts/sync_terminology.py --auto-generate

# 3. Validate
python scripts/validate_guides.py

# 4. Review and commit
git diff
git add .
git commit -m "Add new terminology: X, Y, Z"
```

## 🚨 Important Notes

**Generated content needs review!**
- Have native speakers validate
- Test with real translations
- Iterate based on feedback

**Master terminology is the source of truth**
- Always edit there first
- Then sync to guides
- Not the other way around

## 📚 Full Documentation

See `TRANSLATION_GUIDE_MAINTENANCE.md` for:
- Complete architecture
- All workflows
- Scaling to new languages
- Troubleshooting
- Best practices

## 🆘 Quick Help

```bash
# See all options
python scripts/generate_arabic_guide.py --help
python scripts/sync_terminology.py --help
python scripts/validate_guides.py --help

# Dry run (preview without saving)
python scripts/generate_arabic_guide.py --dry-run

# Validate only
python scripts/sync_terminology.py --validate-only
```

## ✨ Benefits

**Before** (manual approach):
- 😓 Update 3+ files per term
- 😰 Risk of inconsistencies
- ⏰ Hours to add new language
- 🐛 Hard to find errors

**After** (automated approach):
- ⚡ One YAML edit = all languages updated
- ✅ Guaranteed consistency
- 🚀 Minutes to add new language
- 🤖 Automatic validation

## 🎓 What You Built

1. **Meta-Skill Generator** (`generate_arabic_guide.py`)
   - Uses French + Spanish to create Arabic guide
   - Fills in all gaps automatically
   - Adds language-specific guidance

2. **Master Database** (`master_terminology.yaml`)
   - Single source of truth
   - Version controlled
   - Easy to update

3. **Sync System** (`sync_terminology.py`)
   - Propagates changes to all languages
   - Auto-generates missing translations
   - Validates completeness

4. **Validation System** (`validate_guides.py`)
   - Checks structure
   - Verifies terminology
   - Ensures quality

## 🎉 Success!

You now have a **scalable, maintainable system** for managing multilingual translation guides.

**Next**: Scale to Portuguese, German, Swahili, or any language!
