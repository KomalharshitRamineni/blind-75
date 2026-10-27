"""
78. Subsets · https://leetcode.com/problems/subsets/description/
2026-10-27 · clean · 12m · skeleton: backtracking
O(2^{n}) time / O(n) space — 2^{n} being the size of the whole tree we are exploring and O(n) as the deepest node will be of length n
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        res = []
        current = []

        def dfs(index):

            #So our base case, if we run out of elements to add
            if index == len(nums):
                #we want to add current subset to res
                res.append(current.copy())
                return

            #So if not then we keep on tracking
            #So what are our two decisions, we either keep choose nums[index] or keep path same
            #Note that on each we add to index
            current.append(nums[index])
            dfs(index+1)
            current.pop()
            dfs(index+1)

        dfs(0)
        return res

        #This ends up being a 2^length(nums) time and space is goingto be lengh nums worst caset tahts the deepest