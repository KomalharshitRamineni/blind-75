"""
323. Number Of Connected Components · https://neetcode.io/problems/count-connected-components/question
2026-10-20 · fail · 30m · skeleton: union-find
O(V + (E * α(V))) time / O(V) space — Iterating through edges and for each edge, we are doing a union operation (α(V)) then building parents and rank is + O(V) and that is also only space
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parents = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(a):

            cur = a

            while cur != parents[a]:
                parents[cur] = parents[parents[cur]]
                cur = parents[cur]

            return cur



        def union(a,b):

            pA, pB = find(a), find(b)

            if pA == pB:
                return 0

            if rank[pA] > rank[pB]:
                parents[pB] = pA
                rank[pA] += rank[pB]
            else:
                parents[pA] = pB
                rank[pB] += rank[pA]


            return 1

        components = n
        for a,b in edges:
            components-=union(a,b)

        return components

        # graph = {}
        # visited = set()
        # for i in range(n):
        #     graph[i] = []

        # for start, end in edges:
        #     graph[start].append(end)
        #     graph[end].append(start)

        
        # def dfs(node):
            
        #     if node in visited:
        #         return

        #     visited.add(node)

        #     for neigh in graph[node]:
        #         dfs(neigh)

        # components = 0
        # for node in range(n):
        #     if node not in visited:
        #         dfs(node)
        #         components+=1

        # return components