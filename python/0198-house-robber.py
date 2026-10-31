"""
198. House Robber · https://leetcode.com/problems/house-robber/
2026-09-31 · fail · 30m · skeleton: dp-topdown
O(n) time / O(n) space — Solves each subproblem once and worst case call stack is length n
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        

        def backtracking(index, cache):

            if index in cache:
                return cache[index]

            if index >= len(nums):
                return 0
 
            robHouse = nums[index] + backtracking(index+2,cache)
            skipHouse = backtracking(index+1,cache)

            cache[index] = max(robHouse,skipHouse)

            return cache[index]


        return backtracking(0,{})
            




