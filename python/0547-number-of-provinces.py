"""
547. Number Of Provinces · https://leetcode.com/problems/number-of-provinces/
2026-11-03 · 30m · skeleton: union-find
O(n) time O(n) / O(graph) space — union-find is constant amortised and we traverse all of input worst case, space is graph we buikld
"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = {}

        for city in range(len(isConnected)):
            graph[city] = []


        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    graph[i].append(j)


        parents = [i for i in range(len(isConnected))]
        rank = [1] * len(isConnected)

        def find(a):
            
            #We are trying to find the parent of a given city
            cur = a
            while parents[cur] != cur:
                #We want to keep travesring that until we find the parent
                parents[cur] = parents[parents[cur]]
                cur = parents[cur]

            return cur

        def union(a,b):

            A, B = find(a), find(b)
            if A == B:
                return

            if rank[A] <= rank[B]:
                parents[A] = B
                rank[B] += rank[A]
            else:
                parents[B] = A
                rank[A] += rank[B]

            return

        for key, values in graph.items():
            for val in values:
                union(key,val)

        #Then at the end, we can just count the nubmer of parents
        seen = set()
        count = 0

        for city in range(len(isConnected)):
            province = find(city)
            if province not in seen:
                seen.add(province)
                count+=1

        return count            


            
        #Lets see we are buildihgn up a graph, so len(number of cities)
        #We are traversing through all of is conneccted
        #Then for union find operations
        #Becuase ofd the optimastiosn of mertging by rnak and the path compression
        # find is essentially constant, amotrtised
        # union is just finding and combining so its also constant amortised

        #Then we end up unioning on all the cities and  connections so time complexity is O(n) where n is is connected
        #Space is O(cities + edges)