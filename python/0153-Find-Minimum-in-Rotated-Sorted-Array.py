"""
153. Find Minimum in Rotated Sorted Array · https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
2026-09-10 · fail · 30m · skeleton: bs-lower-bound
O(log(n)) time / O(1) space — binary search, find how to divide and conqure search space, based of mid point check
"""



class Solution:
    def findMin(self, nums: List[int]) -> int:


        l, r  = 0 , len(nums)-1
        res = nums[0]

        while l<=r:

            if nums[l] < nums[r]:
                res = min(nums[l],res)
                #This means that whole search space is sorted
        
            mid = (l+r)//2
            res = min(res,nums[mid])
            if nums[l] <= nums[mid]:
                #Then  check the right
                l = mid +1
            else:
                r = mid - 1

        return res