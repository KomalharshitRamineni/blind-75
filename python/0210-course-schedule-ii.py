"""
210. Course Schedule II · https://leetcode.com/problems/course-schedule-ii/
2026-11-08 · 30m · skeleton: topo-sort
O(V + E) time / O(V + E) space — Traverse whole graph worst case and storing graph
"""

from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        graph = {i:[] for i in range(numCourses)}
        indegree = [0 for _ in range(numCourses)]
        order = []

        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)

        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            cur = queue.popleft()
            order.append(cur)
            for nei in graph[cur]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    queue.append(nei)


        return order if len(order) == numCourses else []


