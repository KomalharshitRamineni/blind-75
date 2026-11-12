"""
239. Sliding Window Maximum · https://leetcode.com/problems/sliding-window-maximum/
2026-10-12 · 30m · skeleton: sliding-window
O(n) time / O(k+n) space — Using a montonic queue to keep track off the max seen so far to avoid computing max sum for each window
"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        
        queue = deque()
        res = []

        for i in range(k-1):

            while queue and nums[i] > queue[-1][0]:
                queue.pop()

            queue.append([nums[i], i])


        for i in range(k-1,len(nums)):

            if queue and queue[0][1] <= i-k:
                queue.popleft()

            while queue and nums[i] > queue[-1][0]:
                queue.pop()

            queue.append([nums[i], i])
            res.append(queue[0][0])

        return res
