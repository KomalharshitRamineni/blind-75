"""
376. Wiggle Subsequence · https://leetcode.com/problems/wiggle-subsequence/
2026-11-13 · 30m · skeleton: none, greedy (count the turning points)
O(n) time / O(n) space — Create diff array and iterate through that.
"""


class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:


        diffarr = []
        count = 2

        for i in range (1, len(nums)):
            diff = nums[i]-nums[i-1]
            if diff != 0:
                diffarr.append(nums[i]-nums[i-1])

        if not diffarr:
            return 1

        for i in range(1, len(diffarr)):

            if ((diffarr[i] > 0 and diffarr[i-1] < 0) or
                (diffarr[i] < 0 and diffarr[i-1] > 0)):
                count+=1

        return count
