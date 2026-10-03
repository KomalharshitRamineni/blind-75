"""
209. Minimum Size Subarray Sum · https://leetcode.com/problems/minimum-size-subarray-sum/
2026-09-30 · fail · 30m · skeleton: sliding-window
O(n) time / O(1) space — grow and shrink window based on our condition
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        

        left = 0

        minLength = None

        total = 0

        for right in range(len(nums)):

            total+=nums[right]

            while total >= target:
                if minLength:
                    minLength = min(minLength, right-left + 1)
                else:
                    minLength = right - left + 1

                total-=nums[left]
                left+=1

        return minLength if minLength else 0