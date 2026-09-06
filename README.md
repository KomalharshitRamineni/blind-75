# Blind 75 — solutions

Python solutions to the NeetCode Blind 75, worked through with a spaced-repetition
system: one skeleton per pattern, drilled from memory, with failed problems re-tested
on an expanding schedule against *neighbour* problems that share the skeleton.

Conventions: [CONTRIBUTING.md](CONTRIBUTING.md) · Pattern templates: [templates/](templates/)

**4 / 75 solved.**

| # | Problem | Solved | First pass | Skeleton | Complexity |
|---|---|---|---|---|---|
| 1 | [11. Container With Most Water](python/0011-Container-With-Most-Water.py) | 2026-09-05 | fail | `tp-opposite` | O(n) time / O(1) space — Adjusting pointers to elimnate search space as adjusting means we computed best in the given space/ |
| 2 | [15. 3Sum](python/0015-3Sum.py) | 2026-09-04 | fail | `tp-opposite` | O(n^2) time / O(1) space — Fix one value and doing two pointers opposite, while avoiding recomputes. |
| 3 | [121. Best Time To Buy and Sell Stock](python/0121-Best-Time-To-Buy-and-Sell-Stock.py) | 2026-09-06 | fail | `sliding-window` | O(n) time / O(1) space — since we need to preserve order we use sliding window and update pointers to fit solution requirments |
| 4 | [125. Valid Palindrome](python/0125-valid-palindrome.py) | 2026-09-01 | fail | `tp-opposite` | O(n) time / O(1) space — single pass, two pointers converge from the ends |
