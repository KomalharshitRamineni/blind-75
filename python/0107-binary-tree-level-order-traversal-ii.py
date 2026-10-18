"""
107. Binary Tree Level Order Traversal II · https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
2026-10-18 · clean · 15m · skeleton: tree-bfs-levels
O(n) time / O(n) space — Traversing whole tree and reversing level order traversal, worst case node wise, width of tree stored, all node.val stored in memory for output
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:

        res, queue = deque(), deque()
        queue.append(root)

        while queue:
            
            levels =  len(queue)
            level = []
            for _ in range(levels):
                cur = queue.popleft()
                if cur:
                    level.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)

            res.appendleft(level)

        out = []

        for level in res:
            if level:
                out.append(level)

        return out

        
        