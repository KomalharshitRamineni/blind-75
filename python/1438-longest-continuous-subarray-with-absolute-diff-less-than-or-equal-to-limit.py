"""
1438. Longest Continuous Subarray With Absolute Diff Less Than Or Equal To Limit · https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
2026-11-13 · 30m · skeleton: monotonic-deque
O(n) time / O(n) space - each element popped and pushed at most once twice so 2n -> O(n)
"""

from collections import deque

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:

        lowest = deque()
        highest = deque()
        res = 1

        left = 0

        for i in range(len(nums)):

            while lowest and nums[i] < lowest[-1][0]:
                lowest.pop()

            while highest and nums[i] > highest[-1][0]:
                highest.pop()

            lowest.append([nums[i],i])
            highest.append([nums[i],i])

            while highest[0][0] - lowest[0][0] > limit:
                if nums[left] == highest[0][0]:
                    highest.popleft()
                if nums[left] == lowest[0][0]:
                    lowest.popleft()
                left += 1
            res = max(res, i - left + 1)


        return res