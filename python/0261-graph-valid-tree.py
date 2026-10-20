"""
261. Graph Valid Tree · https://neetcode.io/problems/valid-tree/question
2026-10-20 · fail · 30m · skeleton: union-find
O(V + (E * α(V))) time / O(V) space — Iterating through edges and for each edge, we are doing a union operation (α(V)) then building parents and rank is + O(V) and that is also only space.
"""



class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False


        parents = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(node):

            cur = node

            while parents[cur] != cur:
                parents[cur] = parents[parents[cur]]
                cur = parents[cur]

            return cur

        def union(a,b):

            
            A = find(a)
            B = find(b)

            if A == B:
                return False

            if rank[A] > rank[B]:
                parents[B] = A
                rank[A] += rank[B]
            else:
                parents[A] = B
                rank[B] += rank[A]

            return True

        res = True
        for a, b in edges:
            res = res and union(a,b)
        return res

        