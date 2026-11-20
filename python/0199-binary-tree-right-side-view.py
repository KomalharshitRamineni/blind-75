"""
199. Binary Tree Right Side View · https://leetcode.com/problems/binary-tree-right-side-view/
2026-11-17 · 8m · skeleton: tree-bfs-levels
O(n) time / O(max(w, h)) space — Traversing Whole tree worst case queue is max width and res is height, whichever is higher
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:

        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        res = []

        while queue:

            length = len(queue)
            res.append(queue[-1].val)
            for _ in range(length):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return res