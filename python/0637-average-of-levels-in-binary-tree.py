"""
637. Average Of Levels In Binary Tree · https://leetcode.com/problems/average-of-levels-in-binary-tree/
2026-10-18 · clean · 10m · skeleton: tree-bfs-levels
O(n) time / O(w) space — Traversing whole tree, worst case the width of the tree is stored in queue
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:

            levels = len(queue)

            total = 0
            count = 0

            for level in range(levels):

                cur = queue.popleft()
                if cur:
                    total+=cur.val
                    count+=1
                    queue.append(cur.left)
                    queue.append(cur.right)
            
            if count!=0:
                res.append(total/count)

        return res
