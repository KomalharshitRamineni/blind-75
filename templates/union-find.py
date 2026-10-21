"""
union-find — path compression + union by size

Trigger: undirected graphs only — connectivity queries as edges arrive · counting components · cycle detection / the redundant edge · Kruskal's MST. Never for a directed graph: `union` ignores direction, so a→b, c→b, a→c reads as a cycle when it isn't one (→ `topo-sort`). Complexity: ~O(E · α(V)), effectively linear
"""



def union_find(n,edges):
    
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
            return #No union was done, components already connected

        if rank[pA] > rank[pB]:
            parents[pB] = pA
            rank[pA] += rank[pB]
        else:
            parents[pA] = pB
            rank[pB] += rank[pA]

        return #Union was done, we connected a,b
