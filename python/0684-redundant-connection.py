"""
684. Redundant Connection · https://leetcode.com/problems/redundant-connection/
2026-11-07 · 30m · skeleton: union-find
O(E+V) time / O(V) space — find operation amortised is constant and we are looping through all edges performing union
"""



class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:

   
        
        parents = [0] + [i+1 for i in range(len(edges))]
        rank = [0] + [1 for i in range(len(edges))]



        def find(a):
            #We find the parent of give node
            cur = a

            while parents[cur] != cur:
                #Then we move on and look for parents paernt
                #This way we essentially compress the path as we go along
                parents[cur] = parents[parents[cur]]
                cur = parents[cur]
            
            return cur

        res = []

        def union(a,b):
            A, B = find(a), find(b)

            if A == B:
                #Already connected
                res.append([a,b])
                return 

            #Otherwise lets connect these

            if rank[A] <= rank[B]:
                #We want to connect the smaller one to the bigger one
                parents[A] = B
                rank[B] += rank[A]
            else:
                parents[B] = A
                rank[A] += rank[B]

            return 

        for a, b in edges:
            union(a,b)
 
        return res[-1]

