"""
1046. Last Stone Weight · https://leetcode.com/problems/last-stone-weight/
2026-10-21 · clean · 10m · skeleton: heap-topk
O(nlog(n)) time / O(n) space - Maintain maxHeap and then pop as required
"""

import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        res  = []
        for stone in stones:
            heapq.heappush(res,-stone)

        while len(res)>1:

            x = -heapq.heappop(res)
            y = -heapq.heappop(res)
            diff = abs(x-y)

            if diff != 0:
                heapq.heappush(res,-diff)

        return -res[0] if res else 0
