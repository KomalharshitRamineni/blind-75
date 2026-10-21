"""
207. Course Schedule · https://leetcode.com/problems/course-schedule/
2026-10-21 · fail · 30m · skeleton: topo-sort
O(V + E) time / O(V + E) space — We are looking at nodes that have no arrows pointed to them, then starting with those, iterating through graph to see if we can also bring every other node's in-degree down to 0 by removing the arrows of finished nodes.
"""



from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for a, b in prerequisites:
            graph.get(a).append(b)

        indegree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        queue = deque(n for n in graph if indegree[n] == 0)
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1          # "remove" the edge
                if indegree[neighbor] == 0:      # all prerequisites met
                    queue.append(neighbor)

        if len(order) != numCourses:
            return False

        return True









        # #Check if there are cycles in this graph
        # path = set()
        # visited = set()

        # def dfs(node):
        #     if node in path:
        #         return True
        #     if node in visited:
        #         return False

        #     visited.add(node)
        #     path.add(node)

        #     for neigh in graph[node]:
        #         if dfs(neigh):
        #             return True

        #     path.remove(node)
        #     return False


        # for i in range(numCourses):
        #     if dfs(i):
        #         return False

        # return True





