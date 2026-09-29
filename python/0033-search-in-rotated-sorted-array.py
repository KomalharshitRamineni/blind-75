"""
33. Search in Rotated Sorted Array · https://leetcode.com/problems/search-in-rotated-sorted-array/
2026-09-29 · clean · 23m · skeleton: bs-exact
O(log n) time / O(1) space — one halving per iteration, no extra storage
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left, right = 0, len(nums)-1

        while left <= right:


            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < nums[right]:
                #right side is sorted
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                #left side is sorted
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left= mid + 1

        return -1
