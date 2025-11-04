# Testing Prompt Caching

## Quick Test Guide

### Test 1: SRT Translation with Caching

Run a multi-chunk SRT translation:

```bash
python scripts/translate_srt.py \
  examples/sample_transcript_en.srt \
  --language es \
  --chunk-size 10 \
  --output test_output_es.srt
```

**Expected Output:**
```
Chunk 1:
  ✓ Tokens: 50 in, 200 out
  💾 Cache: 0 read, 15000 write

Chunk 2:
  ✓ Tokens: 50 in, 200 out
  💾 Cache: 15000 read, 0 write

Chunk 3:
  ✓ Tokens: 50 in, 200 out
  💾 Cache: 15000 read, 0 write

📊 Translation Statistics
============================================================
Total input tokens: 150
Total output tokens: 600
💾 Cache read tokens: 30,000
💾 Cache write tokens: 15,000
💰 Cache savings: $0.0810
💰 Estimated cost: $0.0731
   (Input: $0.0005, Cache Write: $0.0563, Cache Read: $0.0090, Output: $0.0090)
============================================================
```

### Test 2: Documentation Translation with Caching

Translate multiple files in sequence:

```bash
# First file - creates cache
python scripts/translation_agent.py \
  --file docs/en/test_simple.md \
  --language es \
  --save \
  --test

# Second file - uses cache
python scripts/translation_agent.py \
  --file docs/en/another_file.md \
  --language es \
  --save \
  --test
```

**Expected Output:**

File 1:
```
📊 Tokens used: 100 input, 500 output
💾 Cache: 0 read, 12000 write
💰 Estimated cost: $0.0525
```

File 2:
```
📊 Tokens used: 100 input, 500 output
💾 Cache: 12000 read, 0 write
💰 Estimated cost: $0.0111
```

**Savings**: 78% reduction on second file!

### Test 3: Verify Cache Metrics in GitHub Actions

Run the workflow and check the logs:

1. Go to Actions → Run workflow
2. Check job logs for cache metrics
3. Look for lines with 💾 emoji

Example from workflow:
```
  💾 Cache: 14,523 read, 0 write
  💰 Cache savings: $0.3920
```

## Interpreting Results

### Cache Write (First API Call)
- Shows up as `cache_creation_input_tokens`
- Costs 25% more than regular tokens ($3.75 vs $3.00)
- Only happens once per language/session

### Cache Read (Subsequent Calls)
- Shows up as `cache_read_input_tokens`
- Costs 90% less than regular tokens ($0.30 vs $3.00)
- Happens on all chunks/files after the first

### Break-Even Point
Cache write premium is recovered after just **2 API calls**:
- Call 1: Pay extra $0.75 per million tokens
- Call 2: Save $2.70 per million tokens
- Net: $1.95 saved per million tokens from call 2 onwards

## Troubleshooting

### If You Don't See Cache Metrics

**Possible reasons:**
1. Skill files are too small (< 1,024 tokens for Sonnet 4.5)
   - Check: Count tokens in skill files
   - Solution: Should not be an issue with our large skill files

2. Content is being modified between calls
   - Check: Ensure skill context is identical
   - Solution: Verify skill files aren't changing

3. Calls are > 5 minutes apart
   - Check: Timing between chunks
   - Solution: Should not be an issue (chunks process in seconds)

### Verify Cache Implementation

Check the message structure includes cache_control:

```python
message_content = [
    {
        "type": "text",
        "text": skill_context,
        "cache_control": {"type": "ephemeral"}  # ← Must be present
    },
    {
        "type": "text",
        "text": variable_content
        # ← No cache_control here
    }
]
```

## Cost Comparison Examples

### Example 1: 20-minute SRT file (6 chunks)

**Without caching:**
```
Skill: 15,000 tokens × 6 chunks = 90,000 tokens
Cost: 90,000 × $3.00/MTok = $0.27
```

**With caching:**
```
Chunk 1: 15,000 write = $0.056
Chunks 2-6: 75,000 read = $0.023
Total: $0.079 (71% savings!)
```

### Example 2: Bulk docs translation (20 files, 3 languages)

**Without caching:**
```
Skill: 12,000 tokens × 60 translations = 720,000 tokens
Cost: 720,000 × $3.00/MTok = $2.16
```

**With caching:**
```
First file per lang: 36,000 write = $0.135
Remaining 57 files: 684,000 read = $0.205
Total: $0.340 (84% savings!)
```

## Success Metrics

After implementing caching, you should see:

✅ Cache read tokens > 0 on chunks 2+
✅ Cache write tokens only on first chunk per language
✅ Cost reduction of 60-80% on input tokens
✅ "Cache savings" line in statistics
✅ Faster processing time (reduced latency)

## Next Steps

1. Run a test translation with multiple chunks
2. Verify cache metrics appear in logs
3. Compare costs before/after
4. Monitor cache hit rates in production workflows
5. Celebrate the savings! 🎉
