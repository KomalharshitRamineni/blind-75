"""
503. Next Greater Element · https://leetcode.com/problems/next-greater-element-ii/
2026-11-10 · 30m · skeleton: monotonic-stack
O(n) time / O(n) space — Iterate through array twice maintaining the same stack
"""

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:

        n = len(nums)
        stack = []
        res = [-1] * n

        for i in range(n*2):
            i = i % n

            #Otherwise our montoinc stack check and loop
            while stack and stack[-1][0] < nums[i]:

                candidate = stack.pop()[1]
                nextGreater = nums[i]
                res[candidate] = nextGreater

            stack.append([nums[i],i])

        return res

