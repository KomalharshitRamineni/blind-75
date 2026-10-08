"""
102. Binary Tree Level Order Traversal · https://leetcode.com/problems/binary-tree-level-order-traversal/
2026-10-05 · fail · 30m · skeleton: tree-bfs-levels
O(n) time / O(n) space — Visiting every node in input and space at worst will be height of tree n/2 == o(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        queue = collections.deque()
        queue.append(root)

        res = []

        while queue:

            queueLength = len(queue)
            level = []

            for i in range(queueLength):

                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
        
            if level:
                res.append(level)
        
        return res


