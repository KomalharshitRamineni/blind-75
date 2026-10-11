"""
230. Kth Smallest Element In A BST · https://leetcode.com/problems/kth-smallest-element-in-a-bst/
2026-10-10 · hint · 30m · skeleton: tree-inorder-iterative
O(n) time / O(h) space — Traversing tree in order
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        
        stack = []

        cur = root

        while cur or stack:

            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            
            k-=1
            if k == 0:
                return cur.val

            cur = cur.right

        
#First solution, traversese WHOLE tree

# Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        
#         res = []

#         def dfs(node):

#             if not node:
#                 return node

#             dfs(node.left)
#             res.append(node.val)
#             dfs(node.right)

#         dfs(root)


#         return res[k-1]