"""
515. Find Largest Value In Each Tree Row · https://leetcode.com/problems/find-largest-value-in-each-tree-row/
2026-11-17 · 5m · skeleton: tree-bfs-levels
O(n) time / O(max(w, h)) space — We explore the whole tree and worst case we store the width of the tree and the height of the tree, whichever is greater
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []

        while queue:

            rowLength = len(queue)
            curMax = float("-inf")

            for _ in range(rowLength):
                cur = queue.popleft()
                curMax = max(curMax, cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            res.append(curMax)
