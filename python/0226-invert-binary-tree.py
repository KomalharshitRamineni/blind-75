"""
226. Invert Binary Tree · https://leetcode.com/problems/invert-binary-tree/
2026-10-04 · clean · 10m · skeleton: tree-dfs
O(n) time / O(h) space — Every node in tree is visited and call stack for deepest node is stored in memory
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        if not root:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        left = root.left
        right = root.right

        root.right = left
        root.left = right

        return root



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        

        stack = [root]

        while stack:
            node = stack.pop()
            if node:

                left = node.left
                right = node.right

                stack.append(node.left)
                stack.append(node.right)
                
                node.left = right
                node.right = left


        return root


