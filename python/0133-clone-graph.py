"""
133. Clone Graph · https://leetcode.com/problems/clone-graph/
2026-10-14 · fail · 30m · skeleton: graph-dfs-visited
O(n) time / O(n) space — Visiting whole graph, storing clone mapping
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        graphMap = {}

        def dfs(node):
            if node in graphMap:
                return graphMap[node]
            
            clone = Node(node.val)
            graphMap[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        
        return dfs(node) if node else None
