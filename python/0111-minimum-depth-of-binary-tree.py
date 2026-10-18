"""
111. Minimum Depth Of Binary Tree · https://leetcode.com/problems/minimum-depth-of-binary-tree/
2026-10-18 · tfail · 12m · skeleton: tree-bfs-levels
O(n) time / O(w) space — Traverse whole tree, worst case is the max width of the binary tree
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        

        queue = collections.deque()
        queue.append((root,1))

        res = float("inf")

        while queue:

            cur,level = queue.popleft()
            if cur:
                queue.append((cur.left,level+1))
                queue.append((cur.right,level+1))

                if not(cur.left or cur.right):
                    res = min(res,level)

        return res if root else 0




    

