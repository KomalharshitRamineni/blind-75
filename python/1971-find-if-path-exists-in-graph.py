"""
1971. Find If Path Exists In Graph · https://leetcode.com/problems/find-if-path-exists-in-graph/
2026-10-27 · clean · 10m · skeleton: graph-dfs-visited
O(V + E) time / O(V + E) space - Worst case we are traversing whole graph and we store the whole graph in memory so that gives us V + E space complexity
"""


from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        graph = {}
        for v in range(n):
            graph[v] = []
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        #So we have our graph built up, so now lets explre and see if we can visit our destination

        #Lets explore this graph
        visited = set()
        queue = deque()
        queue.append(source)
    

        while queue:

            cur = queue.popleft()
            #So what we going to do is go through its neighbours and add it to our visited
            if cur in visited:
                continue
            else:
                visited.add(cur)
                #First we check if this is our destination
                if cur == destination:
                    return True
                else:
                    for nei in graph[cur]:
                        queue.append(nei)
                
        return False

        #So this should work if the path exists
        #The time complexity of this would be V + E, as we iterate through V and E to create graph and then worst case we
        # Explore the whole graph to find a path that exists.

