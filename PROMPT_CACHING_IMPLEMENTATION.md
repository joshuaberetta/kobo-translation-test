# Prompt Caching Implementation

## Overview

Prompt caching has been implemented in both translation workflows to significantly reduce costs and improve performance.

## What Changed

### 1. SRT Translation (`scripts/translate_srt.py`)

**Before:**
- Skill context sent as plain text in every chunk
- Full cost for all input tokens on every API call

**After:**
- Skill context marked with `cache_control` for caching
- First chunk: Creates cache (25% premium: $3.75/MTok)
- Subsequent chunks: Read from cache (90% discount: $0.30/MTok)
- Added cache metrics tracking and reporting

### 2. Documentation Translation (`scripts/translation_agent.py`)

**Before:**
- Skill context sent as plain text for every translation
- Full cost for terminology references

**After:**
- Skill context marked with `cache_control` for caching
- First translation per language: Creates cache
- Subsequent files in same language: Read from cache
- Added cache metrics tracking and reporting

## Benefits

### Cost Savings

**Example: 30-minute video (~8 chunks)**

**Without caching:**
```
Skill context: 15,000 tokens × 8 chunks = 120,000 tokens
Cost: 120,000 × $3.00/MTok = $0.36
```

**With caching:**
```
First chunk:  15,000 cache write = $0.056
Next 7 chunks: 105,000 cache read = $0.031
Total: $0.087 (76% savings!)
```

### Performance Improvements

- Faster time-to-first-token (cached content skips processing)
- Reduced latency for sequential translations
- Better rate limit utilization (cache reads don't count toward limits)

## How It Works

### Cache Structure

```python
message_content = [
    {
        "type": "text",
        "text": skill_context,  # All terminology, guidelines, examples
        "cache_control": {"type": "ephemeral"}  # ← This marks it for caching
    },
    {
        "type": "text",
        "text": content_to_translate  # Changes per chunk/file
        # No cache_control - this varies
    }
]
```

### Cache Lifetime

- **Default TTL**: 5 minutes (free refresh on each use)
- **Typical workflow**: Chunks/files processed within seconds
- **Perfect fit**: Our sequential processing pattern

### Cache Metrics

The scripts now track and report:
- `cache_read_input_tokens`: Tokens read from cache
- `cache_creation_input_tokens`: Tokens written to cache
- Cache savings in dollars

Example output:
```
💾 Cache: 14,523 read, 0 write
💰 Cache savings: $0.3920
```

## Implementation Details

### SRT Translation

1. **Skill context cached**: 
   - Base translation skill (SKILL.md)
   - All reference files (brand-terminology, UI, data-collection, etc.)
   - SRT-specific skill extension

2. **Per-chunk content (not cached)**:
   - Target language
   - Translation guidelines
   - Previous/next context
   - Actual subtitles to translate

3. **Typical flow**:
   - Chunk 1: Creates cache + translates
   - Chunks 2-N: Use cached skills + translate new subtitles

### Documentation Translation

1. **Skill context cached**:
   - Main translation skill
   - Brand terminology
   - UI terminology
   - Data collection terms
   - Form building terms
   - Question types
   - Course terminology

2. **Per-file content (not cached)**:
   - Target language
   - Source document
   - Translation instructions

3. **Typical flow**:
   - First file in language: Creates cache
   - Subsequent files: Use cached skills
   - Each language has its own cache

## Cost Breakdown

### Pricing (Claude Sonnet 4.5)

| Token Type | Cost per MTok | Notes |
|------------|---------------|-------|
| Regular input | $3.00 | Non-cached tokens |
| Cache write | $3.75 | 25% premium, but only once |
| Cache read | $0.30 | 90% discount! |
| Output | $15.00 | Unchanged |

### Break-Even Analysis

Cache write premium pays off after just **2 chunks/files**:
- Chunk 1: Pay $3.75/MTok (write)
- Chunk 2: Save $2.70/MTok (vs $3.00)
- Net after 2: Already $0.45/MTok cheaper
- Chunks 3+: Pure $2.70/MTok savings each

## Testing

No changes to workflow files needed - the caching is handled automatically by the Python scripts.

To verify:
1. Run any translation workflow
2. Check logs for cache metrics:
   ```
   💾 Cache: X read, Y write
   ```
3. First chunk/file will show cache writes
4. Subsequent chunks/files will show cache reads

## Monitoring

Track effectiveness:
- Watch for `cache_read_input_tokens` in logs
- Compare costs before/after (shown in statistics)
- Cache savings explicitly reported in final summary

## Limitations

- Minimum cacheable content: 1,024 tokens (Sonnet 4.5)
  - Our skill files easily exceed this
- Cache invalidated if skill content changes
  - Expected: We only update skills occasionally
- 5-minute lifetime
  - Perfect for our sequential processing

## Future Optimizations

Potential improvements:
- Use 1-hour cache for very large batch jobs
- Implement cache warming for parallel workflows
- Add cache hit rate metrics to CI/CD

## References

- [Claude Prompt Caching Documentation](https://docs.claude.com/en/docs/build-with-claude/prompt-caching)
- [Pricing Details](https://www.anthropic.com/pricing)
