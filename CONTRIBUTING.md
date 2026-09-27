# File conventions

**Naming:** `python/NNNN-kebab-case-title.py` — the LeetCode problem number zero-padded to
four digits, so the directory sorts in problem order. **All lowercase**, words joined by
single hyphens: `0011-container-with-most-water.py`, never `0011-Container-With-Most-Water.py`.

**Header:** every file opens with this docstring and nothing else above it. `sync` parses it
to regenerate `README.md`, so keep the field order.

```python
"""
125. Valid Palindrome · https://leetcode.com/problems/valid-palindrome/
2026-09-01 · clean · 14m · skeleton: tp-opposite
O(n) time / O(1) space — bottleneck is the single two-pointer pass
"""
```

Line 1: `<number>. <title> · <url>`
Line 2: `<date> · clean|hint|fail · <mins> · skeleton: <template-name>`
Line 3: the complexity line, copied from the `log.md` write-up.

**Two lists live here.** Most files are Blind 75. The rest are *neighbours* — problems from
the wider NeetCode 250 that share a pattern with a Blind 75 problem and are used to re-test it
later. `README.md` tags which is which and counts them separately.

**Do not paste the problem statement.** Your code and your own complexity note only.

**Do not commit solutions to a live online assessment or take-home** until that process is
over — regardless of repo visibility.

The full write-up (Cue / Key insight / What broke / Complexity / Template) lives in the
private vault's `log.md`, not here.
