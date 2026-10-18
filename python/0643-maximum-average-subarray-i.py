"""
643. Maximum Average Subarray I · https://leetcode.com/problems/maximum-average-subarray-i/
2026-10-17 · fail · 15m · skeleton: sliding-window
O(n) time / O(1) space — Sliding window, returning max of a function applied to a window
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        left, right = 0, k-1

        total = 0

        for i in range(k):
            total+=nums[i] 

        maxAvg = total

        right+=1

        while right < len(nums):

            total-=nums[left]
            total+=nums[right]

            maxAvg = max(total,maxAvg)

            right+=1
            left+=1

        return maxAvg/k
