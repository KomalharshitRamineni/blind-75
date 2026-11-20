"""
110. Balanced Binary Tree · https://leetcode.com/problems/balanced-binary-tree/
2026-11-19 · 30m · skeleton: tree-dfs
O(n) time / O(h) space — Traversing whole tree, worst case space is height of call stack which is height of tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:


        def dfs(node):
            if not node:
                return (0, True)

            left, leftBalanced = dfs(node.left)
            right, rightBalanced = dfs(node.right)

            isBalanced = (
                abs(left - right) <= 1
                and leftBalanced
                and rightBalanced
            )

            return (max(left, right) + 1, isBalanced)

        return dfs(root)[1]
        