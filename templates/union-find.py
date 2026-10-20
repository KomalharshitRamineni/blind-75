"""
union-find — path compression + union by size

Trigger: connectivity queries as edges arrive · counting components · detecting the redundant edge · Kruskal's MST. Complexity: ~O(E · α(V)), effectively linear
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
