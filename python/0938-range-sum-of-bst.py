"""
938. Range Sum Of BST · https://leetcode.com/problems/range-sum-of-bst/
2026-10-20 · pass · 12m · skeleton: tree-dfs
O(n)) time / O(h) space - Dfs, worst case whole tree is in range of serach space
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:

        total = 0

        stack = [root]

        while stack:
            
            cur = stack.pop()
            if cur:

                if cur.val>= low and cur.val <= high:
                    total+=cur.val

                stack.append(cur.right)
                stack.append(cur.left)

        return total