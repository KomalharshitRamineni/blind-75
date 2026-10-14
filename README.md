# Blind 75 — solutions

Python solutions to the NeetCode Blind 75, worked through with a spaced-repetition
system: one skeleton per pattern, drilled from memory, with failed problems re-tested
on an expanding schedule against *neighbour* problems that share the skeleton.

Conventions: [CONTRIBUTING.md](CONTRIBUTING.md) · Pattern templates: [templates/](templates/)

**26 / 75 Blind 75 solved** · **9 neighbour problems** solved on the review ladder.

| # | Problem | List | Solved | First pass | Skeleton | Complexity |
|---|---|---|---|---|---|---|
| 1 | [3. Longest Substring Without Repeating Characters](python/0003-longest-substring-without-repeating-characters.py) | Blind 75 | 2026-09-07 | fail | `sliding-window` | O(n) time / O(n) space — Sliding window makes sense for contiguous problems, follow through with pointer implementation as opposed to half half with for loops, can use any to store seen here for constant check up time |
| 2 | [11. Container With Most Water](python/0011-container-with-most-water.py) | Blind 75 | 2026-09-05 | fail | `tp-opposite` | O(n) time / O(1) space — Adjusting pointers to elimnate search space as adjusting means we computed best in the given space/ |
| 3 | [15. 3Sum](python/0015-3sum.py) | Blind 75 | 2026-09-04 | fail | `tp-opposite` | O(n^2) time / O(1) space — Fix one value and doing two pointers opposite, while avoiding recomputes. |
| 4 | [20. Valid Parentheses](python/0020-valid-parentheses.py) | Blind 75 | 2026-09-08 | clean | `plain matching stack` | O(n) time / O(n) space — one pass; the stack holds up to n when the input is all openers |
| 5 | [21. Merge Two Sorted Lists](python/0021-merge-two-sorted-lists.py) | Blind 75 | 2026-10-03 | clean | `ll-dummy` | O(n+m) time / O(1) space — Only one node is ever held at one time in memory, therefore making it O(1) space complexity |
| 6 | [33. Search in Rotated Sorted Array](python/0033-search-in-rotated-sorted-array.py) | Blind 75 | 2026-09-29 | clean | `bs-exact` | O(log n) time / O(1) space — one halving per iteration, no extra storage |
| 7 | [39. Combination Sum](python/0039-combination-sum.py) | Blind 75 | 2026-10-13 | fail | `backtracking` | O(2^{n}) time / O(n) space — Backtracking along a decision tree pruning branches |
| 8 | [79. Word Search](python/0079-word-search.py) | Blind 75 | 2026-10-14 | fail | `backtracking` | O(m * n * 4^{n}) time / O(n) space — Matrix backtracking, dfs has complexity of decisions ^ {depth of call stack} |
| 9 | [98. Validate Binary Search Tree](python/0098-validate-binary-search-tree.py) | Blind 75 | 2026-10-06 | fail | `tree-dfs` | O(n) time / O(h) space — Every node in tree is visited and call stack for deepest node is stored in memory |
| 10 | [100. Same Tree](python/0100-same-tree.py) | Blind 75 | 2026-10-04 | clean | `tree-dfs` | O(n) time / O(h) space — Every node in tree is visited and call stack for deepest node is stored in memory |
| 11 | [102. Binary Tree Level Order Traversal](python/0102-binary-tree-level-order-traversal.py) | Blind 75 | 2026-10-05 | fail | `tree-bfs-levels` | O(n) time / O(n) space — Visiting every node in input and space at worst will be height of tree n/2 == o(n) |
| 12 | [104. Maximum Depth Of Binary Tree](python/0104-maximum-depth-of-binary-tree.py) | Blind 75 | 2026-10-04 | fail | `tree-dfs` | O(n) time / O(h) space — Every node in tree is visited and call stack for deepest node is stored in memory |
| 13 | [121. Best Time To Buy and Sell Stock](python/0121-best-time-to-buy-and-sell-stock.py) | Blind 75 | 2026-09-06 | fail | `sliding-window` | O(n) time / O(1) space — since we need to preserve order we use sliding window and update pointers to fit solution requirments |
| 14 | [125. Valid Palindrome](python/0125-valid-palindrome.py) | Blind 75 | 2026-09-01 | fail | `tp-opposite` | O(n) time / O(1) space — single pass, two pointers converge from the ends |
| 15 | [133. Clone Graph](python/0133-clone-graph.py) | Blind 75 | 2026-10-14 | fail | `graph-dfs-visited` | O(n) time / O(n) space — Visiting whole graph, storing clone mapping |
| 16 | [141. Linked List Cycle](python/0141-linked-list-cycle.py) | Blind 75 | 2026-10-04 | clean | `tp-fast-slow` | O(n) time / O(1) space — At any arbitrary point, gap between fast and slow is always closed by -1, resulting in O(n) time complexity |
| 17 | [153. Find Minimum in Rotated Sorted Array](python/0153-find-minimum-in-rotated-sorted-array.py) | Blind 75 | 2026-09-10 | fail | `bs-lower-bound` | O(log(n)) time / O(1) space — binary search, find how to divide and conqure search space, based of mid point check |
| 18 | [167. Two Sum II Input Array Is Sorted](python/0167-two-sum-ii-input-array-is-sorted.py) | neighbour | 2026-09-18 | clean | `tp-opposite` | O(n) time / O(1) space — one pass, pointers only ever converge |
| 19 | [200. Number Of Islands](python/0200-number-of-islands.py) | Blind 75 | 2026-10-14 | clean | `graph-bfs-grid` | O(n * m) time / O(n * m) space — visiting every node in grid and worst case island size of grid |
| 20 | [206. Reverse Linked List](python/0206-reverse-linked-list.py) | Blind 75 | 2026-10-02 | hint | `ll-reverse` | O(n) time / O(1/n) space — Depending on recursive or iterative approach, careful of what links are adjusted recursively (what is present in call stack) iteratively what we store and change |
| 21 | [208. Implement Trie](python/0208-implement-trie.py) | Blind 75 | 2026-10-10 | clean | `trie` | O(n) time / O(t) space — O(n) per function call and o(t) meaning the total number of trie nodes created. |
| 22 | [209. Minimum Size Subarray Sum](python/0209-minimum-size-subarray-sum.py) | neighbour | 2026-09-30 | fail | `sliding-window` | O(n) time / O(1) space — grow and shrink window based on our condition |
| 23 | [211. Design Add and Search Words Data Structure](python/0211-design-add-and-search-words-data-structure.py) | Blind 75 | 2026-10-11 | clean | `trie` | O(n) time / O(n) space — For Add, we are searching through n at worst case where n is size of trie, for search, worstcase all of trie serached |
| 24 | [219. Contains Duplicate II](python/0219-contains-duplicate-ii.py) | neighbour | 2026-09-30 | clean | `sliding-window` | O(n) time / O(n) space — grow and shrink window based on our condition |
| 25 | [226. Invert Binary Tree](python/0226-invert-binary-tree.py) | Blind 75 | 2026-10-04 | clean | `tree-dfs` | O(n) time / O(h) space — Every node in tree is visited and call stack for deepest node is stored in memory |
| 26 | [230. Kth Smallest Element In A BST](python/0230-kth-smallest-element-in-a-bst.py) | Blind 75 | 2026-10-10 | hint | `tree-inorder-iterative` | O(n) time / O(h) space — Traversing tree in order |
| 27 | [235. Lowest Common Ancestor of a Binary Search Tree](python/0235-lowest-common-ancestor-of-a-bst.py) | Blind 75 | 2026-10-07 | fail | `tree-dfs` | O(log(n)) time / O(1) space — Eliminating Half the search space at each point, resulting in logaritmic time complexity |
| 28 | [239. Sliding Window Maximum](python/0239-sliding-window-maximum.py) | neighbour | 2026-10-12 | fail | `sliding-window` | O(n) time / O(k+n) space — Using a montonic queue to keep track off the current max indicies and avoiding recomputations by popping small added values |
| 29 | [347. Top K Frequent Elements](python/0347-top-k-frequent-elements.py) | Blind 75 | 2026-10-11 | fail | `heap-topk` | O(nlogk) time / O(n) space — heapify is linear and pushing and popping is log(n) so worst case, hashMap is n, for n items we do log(k) |
| 30 | [424. Longest Repeating Character Replacement](python/0424-longest-repeating-character-replacement.py) | Blind 75 | 2026-09-08 | fail | `sliding-window` | O(n) time / O(1) space — Sliding window useful when we have a condition and we want to search contiguious values to satisfiy said condition |
| 31 | [567. Permutation In String](python/0567-permutation-in-string.py) | neighbour | 2026-09-23 | fail | `sliding-window` | O(n) time / O(1) space — Sliding window to to find continguous substring to satisfy value but over a fixed window |
| 32 | [658. Find K Closest Elements](python/0658-find-k-closest-elements.py) | neighbour | 2026-10-10 | fail | `tp-opposite` | O(n) time / O(1) space — Searching through input with fixed window |
| 33 | [680. Valid Palindrome II](python/0680-valid-palindrome-ii.py) | neighbour | 2026-09-29 | hint | `tp-opposite` | O(n) time / O(1) space — one pass plus at most one rescan of the inner range |
| 34 | [875. Koko Eating Bananas](python/0875-koko-eating-bananas.py) | neighbour | 2026-10-02 | fail | `bs-lower-bound` | O(piles * log(max(piles))) time / O(1) space - Binary search based off of known maximum that works |
| 35 | [978. Longest Turbulent Subarray](python/0978-longest-turbulent-subarray.py) | neighbour | 2026-10-03 | fail | `sliding-window` | O(n) time / O(1) space - Sliding window moving pointers when subarray no longer valid |
