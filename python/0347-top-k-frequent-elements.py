"""
347. Top K Frequent Elements · https://leetcode.com/problems/top-k-frequent-elements/
2026-10-11 · fail · 30m · skeleton: heap-topk
O(nlogk) time / O(n) space — heapify is linear and pushing and popping is log(n) so worst case, hashMap is n, for n items we do log(k)
"""



import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:



        hashMap = {}

        for num in nums:
            hashMap[num] = 1 + hashMap.get(num,0)

        maxHeap = []

        for num, freq in hashMap.items():
            heapq.heappush(maxHeap, (freq,num))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])

        return res






"""
Linear time and constant space

"""

        # hashMap = {}

        # for x in nums:
        #     if hashMap.get(x):
        #         hashMap[x] = hashMap.get(x) + 1
        #     else:
        #         hashMap[x] = 1
        
        # bucket = [[] for num in range(len(nums)+1)]
    
        # for num, frequency in hashMap.items():
        #     bucket[frequency].append(num)

        # res = []

        # for i in range(len(bucket)-1,0,-1):
        #     if bucket[i]:
        #         for num in bucket[i]:
        #             if len(res) == k:
        #                 break
        #             res.append(num)

        # return res