# Blind 75 — solutions

Python solutions to the NeetCode Blind 75, worked through with a spaced-repetition
system: one skeleton per pattern, drilled from memory, with failed problems re-tested
on an expanding schedule against *neighbour* problems that share the skeleton.

Conventions: [CONTRIBUTING.md](CONTRIBUTING.md) · Pattern templates: [templates/](templates/)

**7 / 75 Blind 75 solved** · **1 neighbour problem** solved on the review ladder.

| # | Problem | List | Solved | First pass | Skeleton | Complexity |
|---|---|---|---|---|---|---|
| 1 | [3. Longest Substring Without Repeating Characters](python/0003-longest-substring-without-repeating-characters.py) | Blind 75 | 2026-09-07 | fail | `sliding-window` | O(n) time / O(n) space — Sliding window makes sense for contiguous problems, follow through with pointer implementation as opposed to half half with for loops, can use any to store seen here for constant check up time |
| 2 | [11. Container With Most Water](python/0011-container-with-most-water.py) | Blind 75 | 2026-09-05 | fail | `tp-opposite` | O(n) time / O(1) space — Adjusting pointers to elimnate search space as adjusting means we computed best in the given space/ |
| 3 | [15. 3Sum](python/0015-3sum.py) | Blind 75 | 2026-09-04 | fail | `tp-opposite` | O(n^2) time / O(1) space — Fix one value and doing two pointers opposite, while avoiding recomputes. |
| 4 | [121. Best Time To Buy and Sell Stock](python/0121-best-time-to-buy-and-sell-stock.py) | Blind 75 | 2026-09-06 | fail | `sliding-window` | O(n) time / O(1) space — since we need to preserve order we use sliding window and update pointers to fit solution requirments |
| 5 | [125. Valid Palindrome](python/0125-valid-palindrome.py) | Blind 75 | 2026-09-01 | fail | `tp-opposite` | O(n) time / O(1) space — single pass, two pointers converge from the ends |
| 6 | [153. Find Minimum in Rotated Sorted Array](python/0153-find-minimum-in-rotated-sorted-array.py) | Blind 75 | 2026-09-10 | fail | `bs-lower-bound` | O(log(n)) time / O(1) space — binary search, find how to divide and conqure search space, based of mid point check |
| 7 | [424. Longest Repeating Character Replacement](python/0424-longest-repeating-character-replacement.py) | Blind 75 | 2026-09-08 | fail | `sliding-window` | O(n) time / O(1) space — Sliding window useful when we have a condition and we want to search contiguious values to satisfiy said condition |
| 8 | [567. Permutation In String](python/0567-permutation-in-string.py) | neighbour | 2026-09-23 | fail | `sliding-window` | O(n) time / O(1) space — Sliding window to to find continguous substring to satisfy value but over a fixed window |
