"""
325. Lowest Common Ancestor of a Binary Search Tree · https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
2026-10-07 · fail ·30m · skeleton: tree-dfs
O(log(n)) time / O(1) space — Eliminating Half the search space at each point, resulting in logaritmic time complexity
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        cur = root

        while cur:

            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur