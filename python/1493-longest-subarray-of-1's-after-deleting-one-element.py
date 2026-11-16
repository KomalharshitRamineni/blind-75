"""
1493. Longest Subarray of 1's After Deleting One Element · https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
2026-11-16 · 17m · skeleton: sliding-window
O(n) time / O(1) space - Going through the input and maintaining a flag of whether we deleted an elent or not and shrinking to the index after we gain back that operation
"""




class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        

        deleteUsed = False
        left = 0
        longest = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                if not deleteUsed:
                    deleteUsed = True
                else:

                    while left <= right and nums[left] != 0:
                        left += 1

                    left += 1

            longest = max(longest, (right-left) + 1)

        return longest - 1
