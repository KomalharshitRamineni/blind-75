"""
100. Same Tree · https://leetcode.com/problems/same-tree/
2026-10-04 · clean ·25m · skeleton: tree-dfs
O(n) time / O(h) space — Every node in tree is visited and call stack for deepest node is stored in memory
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        
        if not p and not q:
            return True

        if p and not q:
            return False

        if q and not p:
            return False

        if p.val!=q.val:
            return False
    
        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)


        return left and right




class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        
        stackq = [q]
        stackp = [p]

        while stackq:

            qnode = stackq.pop()
            pnode = stackp.pop()

            if qnode and pnode:
                if qnode.val!= pnode.val:
                    return False

                else:
                    stackq.append(qnode.left)
                    stackq.append(qnode.right)

                    stackp.append(pnode.left)
                    stackp.append(pnode.right)

            elif not qnode and pnode:
                return False
            elif not pnode and qnode:
                return False
            else:
                continue

        return True