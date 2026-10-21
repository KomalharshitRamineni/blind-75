"""
topo-sort — Kahn's algorithm with indegree

Trigger: directed graphs — ordering under prerequisites · "can you finish all courses" · cycle detection in a directed graph, where `union-find` gives false positives. The three-colour variant of `graph-dfs-visited` also answers "is there a cycle?"; this one also gives the order. Complexity: O(V + E)
"""



from collections import deque

class Solution:
    def topo_sort(V,E):
        
        graph = {}

        for i in range(V):
            graph[i] = []

        for a, b in E:
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

        if len(order) != V:
            return False

        return True
