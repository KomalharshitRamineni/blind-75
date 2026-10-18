"""
404. Sum Of Left Leaves · https://leetcode.com/problems/sum-of-left-leaves/
2026-10-18 · clean · 15m · skeleton: tree-dfs
O(n) time / O(h) space — Traversing whole tree, worst case the height of the tree is stored in stack
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        

        stack = [(root,None)]
        total = 0

        while stack:

            cur, direction = stack.pop()
            if cur:

                stack.append((cur.right,0))
                stack.append((cur.left,1))

                if not cur.left and not cur.right and direction == 1:
                    total += cur.val


        return total