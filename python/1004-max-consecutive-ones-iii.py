"""
1004. Max Consecutive Ones III · https://leetcode.com/problems/max-consecutive-ones-iii/
2026-10-27 · fail · 30m · skeleton: sliding-window
O(n) time / O(1) space - Sliding window - ALWAYS KEEP ONE POINTER MOVING AT A FIXED RATE AND DON'T MOVE BOTH CONDITIONALY.
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        left = 0
        longest = 0
        for right in range(len(nums)):

            if nums[right] == 0:
                k-=1

            if k < 0:
                #We need the left to recover
                while left <= right and nums[left] == 1:
                    left+=1

                #So now we got to first 0, now we want to look past that
                left+=1
                k+=1

            #So now we comput the longest window of 1s we have seen
            longest = max(longest,right-left+1)

        return longest