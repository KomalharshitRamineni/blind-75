# Blind 75 — solutions

Python solutions to the NeetCode Blind 75, worked through with a spaced-repetition
system: one skeleton per pattern, drilled from memory, with failed problems re-tested
on an expanding schedule against *neighbour* problems that share the skeleton.

Conventions: [CONTRIBUTING.md](CONTRIBUTING.md) · Pattern templates: [templates/](templates/)

**18 / 75 Blind 75 solved** · **7 neighbour problems** solved on the review ladder.

| # | Problem | List | Solved | First pass | Skeleton | Complexity |
|---|---|---|---|---|---|---|
| 1 | [3. Longest Substring Without Repeating Characters](python/0003-longest-substring-without-repeating-characters.py) | Blind 75 | 2026-09-07 | fail | `sliding-window` | O(n) time / O(n) space — Sliding window makes sense for contiguous problems, follow through with pointer implementation as opposed to half half with for loops, can use any to store seen here for constant check up time |
| 2 | [11. Container With Most Water](python/0011-container-with-most-water.py) | Blind 75 | 2026-09-05 | fail | `tp-opposite` | O(n) time / O(1) space — Adjusting pointers to elimnate search space as adjusting means we computed best in the given space/ |
| 3 | [15. 3Sum](python/0015-3sum.py) | Blind 75 | 2026-09-04 | fail | `tp-opposite` | O(n^2) time / O(1) space — Fix one value and doing two pointers opposite, while avoiding recomputes. |
| 4 | [20. Valid Parentheses](python/0020-valid-parentheses.py) | Blind 75 | 2026-09-08 | clean | `plain matching stack` | O(n) time / O(n) space — one pass; the stack holds up to n when the input is all openers |
| 5 | [21. Merge Two Sorted Lists](python/0021-merge-two-sorted-lists.py) | Blind 75 | 2026-10-03 | clean | `ll-dummy` | O(n+m) time / O(1) space — Only one node is ever held at one time in memory, therefore making it O(1) space complexity |
| 6 | [33. Search in Rotated Sorted Array](python/0033-search-in-rotated-sorted-array.py) | Blind 75 | 2026-09-29 | clean | `bs-exact` | O(log n) time / O(1) space — one halving per iteration, no extra storage |
| 7 | [98. Validate Binary Search Tree](python/0098-validate-binary-search-tree.py) | Blind 75 | 2026-10-06 | fail | `tree-dfs` | O(n) time / O(h) space — Every node in tree is visited and call stack for deepest node is stored in memory |
| 8 | [100. Same Tree](python/0100-same-tree.py) | Blind 75 | 2026-10-04 | clean | `tree-dfs` | O(n) time / O(h) space — Every node in tree is visited and call stack for deepest node is stored in memory |
| 9 | [102. Binary Tree Level Order Traversal](python/0102-binary-tree-level-order-traversal.py) | Blind 75 | 2026-10-04 | fail | `tree-bfs-levels` | O(n) time / O(n) space — Visiting every node in input and space at worst will be height of tree n/2 == o(n) |
| 10 | [104. Maximum Depth Of Binary Tree](python/0104-maximum-depth-of-binary-tree.py) | Blind 75 | 2026-10-04 | fail | `tree-dfs` | O(n) time / O(h) space — Every node in tree is visited and call stack for deepest node is stored in memory |
| 11 | [121. Best Time To Buy and Sell Stock](python/0121-best-time-to-buy-and-sell-stock.py) | Blind 75 | 2026-09-06 | fail | `sliding-window` | O(n) time / O(1) space — since we need to preserve order we use sliding window and update pointers to fit solution requirments |
| 12 | [125. Valid Palindrome](python/0125-valid-palindrome.py) | Blind 75 | 2026-09-01 | fail | `tp-opposite` | O(n) time / O(1) space — single pass, two pointers converge from the ends |
| 13 | [141. Linked List Cycle](python/0141-linked-list-cycle.py) | Blind 75 | 2026-10-04 | clean | `tp-fast-slow` | O(n) time / O(1) space — At any arbitrary point, gap between fast and slow is always closed by -1, resulting in O(n) time complexity |
| 14 | [153. Find Minimum in Rotated Sorted Array](python/0153-find-minimum-in-rotated-sorted-array.py) | Blind 75 | 2026-09-10 | fail | `bs-lower-bound` | O(log(n)) time / O(1) space — binary search, find how to divide and conqure search space, based of mid point check |
| 15 | [167. Two Sum II Input Array Is Sorted](python/0167-two-sum-ii-input-array-is-sorted.py) | neighbour | 2026-09-18 | clean | `tp-opposite` | O(n) time / O(1) space — one pass, pointers only ever converge |
| 16 | [206. Reverse Linked List](python/0206-reverse-linked-list.py) | Blind 75 | 2026-10-02 | hint | `ll-reverse` | O(n) time / O(1/n) space — Depending on recursive or iterative approach, careful of what links are adjusted recursively (what is present in call stack) iteratively what we store and change |
| 17 | [209. Minimum Size Subarray Sum](python/0209-minimum-size-subarray-sum.py) | neighbour | 2026-09-30 | fail | `sliding-window` | O(n) time / O(1) space — grow and shrink window based on our condition |
| 18 | [219. Contains Duplicate II](python/0219-contains-duplicate-ii.py) | neighbour | 2026-09-30 | clean | `sliding-window` | O(n) time / O(n) space — grow and shrink window based on our condition |
| 19 | [226. Invert Binary Tree](python/0226-invert-binary-tree.py) | Blind 75 | 2026-10-04 | clean | `tree-dfs` | O(n) time / O(h) space — Every node in tree is visited and call stack for deepest node is stored in memory |
| 20 | [235. Lowest Common Ancestor of a Binary Search Tree](python/0235-lowest-common-ancestor-of-a-bst.py) | Blind 75 | 2026-10-07 | fail | `tree-dfs` | O(log(n)) time / O(1) space — Eliminating Half the search space at each point, resulting in logaritmic time complexity |
| 21 | [424. Longest Repeating Character Replacement](python/0424-longest-repeating-character-replacement.py) | Blind 75 | 2026-09-08 | fail | `sliding-window` | O(n) time / O(1) space — Sliding window useful when we have a condition and we want to search contiguious values to satisfiy said condition |
| 22 | [567. Permutation In String](python/0567-permutation-in-string.py) | neighbour | 2026-09-23 | fail | `sliding-window` | O(n) time / O(1) space — Sliding window to to find continguous substring to satisfy value but over a fixed window |
| 23 | [680. Valid Palindrome II](python/0680-valid-palindrome-ii.py) | neighbour | 2026-09-29 | hint | `tp-opposite` | O(n) time / O(1) space — one pass plus at most one rescan of the inner range |
| 24 | [875. Koko Eating Bananas](python/0875-koko-eating-bananas.py) | neighbour | 2026-10-02 | fail | `bs-lower-bound` | O(piles * log(max(piles))) time / O(1) space - Binary search based off of known maximum that works |
| 25 | [978. Longest Turbulent Subarray](python/0978-longest-turbulent-subarray.py) | neighbour | 2026-10-03 | fail | `sliding-window` | O(n) time / O(1) space - Sliding window moving pointers when subarray no longer valid |
