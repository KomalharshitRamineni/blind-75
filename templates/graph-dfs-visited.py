"""
graph-dfs-visited — DFS over an adjacency list

Trigger: connected components · island counting · clone graph · cycle detection in a directed graph (three-colour variant). Complexity: O(V + E)
"""


def graphDfsVisited(edges):
    adj = {}
    for a, b in edges:
        if a not in adj: adj[a] = []
        if b not in adj: adj[b] = []
        adj[a].append(b)
        adj[b].append(a)            # undirected: both ways. Directed: drop this line

    visited = set()                 # dict if each node needs a value (clone graph: node -> copy)

    def dfs(node):
        if node in visited:
            return
        visited.add(node)           # mark BEFORE the loop, or a cycle recurses forever
        for nei in adj[node]:
            dfs(nei)

    for node in adj:                # one known start (clone graph, path exists) -> just dfs(start)
        if node not in visited:
            dfs(node)

    return
