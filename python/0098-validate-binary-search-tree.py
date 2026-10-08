"""
98. Validate Binary Search Tree · https://leetcode.com/problems/validate-binary-search-tree/
2026-10-06 · fail ·30m · skeleton: tree-dfs
O(n) time / O(h) space — Every node in tree is visited and call stack for deepest node is stored in memory
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:


        def valid(node, left, right):

            if not node:
                return True

            if left >= node.val or right <= node.val:
                return False

            return valid(node.left,left,node.val) and valid(node.right,node.val,right)

        return valid(root,float("-inf"),float("inf"))