"""
15. 3Sum · https://leetcode.com/problems/3sum/
2026-09-04 · fail · 30m · skeleton: tp-opposite
O(n^2) time / O(1) space — Fix one value and doing two pointers opposite, while avoiding recomputes.
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums)-2):

            if nums[i] == nums[i-1] and i > 0:
                continue

            j = i+1
            k = len(nums)-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k-=1
                elif total < 0:
                    j+=1
                else:
                    res.append([nums[i],nums[j], nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1

        return res