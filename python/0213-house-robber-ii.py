"""
213. House Robber II · https://leetcode.com/problems/house-robber-ii/
2026-11-03 · fail · 30m · skeleton: dp-1d-bottomup
O(n) time / O(n/1) space — We go through our input and maintain a state space which can be optimised for constant memory
"""

class Solution:
    def rob(self, nums: list[int]) -> int:


        def helper(nums):

            if not nums:
                return 0

            if len(nums) <=2:
                return max(nums)

            state = [0] * len(nums)

            state[0] = nums[0]
            state[1] = max(state[0],nums[1])

            for i in range(2,len(nums)):
                state[i] = max(state[i-1],state[i-2] + nums[i])

            return state[-1]

        return max(nums[0],helper(nums[1:]),helper(nums[:-1]))


        #Then we can further space optmise this by seeing what sates we actually need