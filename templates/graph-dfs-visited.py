"""
graph-dfs-visited — DFS over an adjacency list

Trigger: visit every node reachable over an adjacency list, once each — components · clone graph · does a path exist · cycle in a directed graph. The body is the directed three-colour version: `path` holds the nodes on the current DFS path, and reaching one again is a cycle. Undirected: add `adj[b].append(a)` and delete every `path` line, since both-way edges make a→b→a look like a cycle. For an undirected cycle check use `union-find`. Complexity: O(V + E)
"""



def graphDfsVisited(edges):
    adj = {}
    for a, b in edges:
        if a not in adj: adj[a] = []
        if b not in adj: adj[b] = []
        adj[a].append(b)            

    visited = set()
    path = set()                    # Current DFS path

    def dfs(node):
        if node in path:
            return True             # Cycle in this path

        if node in visited:         # visited and not on path = finished 
            return False
        
        visited.add(node)
        path.add(node)     

        for nei in adj[node]:
            if dfs(nei):            # pass a found cycle straight up, stop
                return True
            
        path.remove(node)           #  like path.pop()
        return False

    for node in adj:
        if node not in visited:
            if dfs(node):
                return True

    return False
