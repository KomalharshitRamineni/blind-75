"""
104. Maximum Depth Of Binary Tree · https://leetcode.com/problems/maximum-depth-of-binary-tree/
2026-10-04 · fail · 30m · skeleton: tree-dfs
O(n) time / O(h) space — Every node in tree is visited and call stack for deepest node is stored in memory 
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        if not root:
            return 0

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left,right)




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        stack = [[root,1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(depth,res)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])

            
        return res
            


            

