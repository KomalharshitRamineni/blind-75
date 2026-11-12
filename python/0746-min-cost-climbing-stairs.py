"""
746. Min Cost Climbing Stairs · https://leetcode.com/problems/min-cost-climbing-stairs/
2026-11-11 · 25m · skeleton: dp-1d
O(n) time / O(1) space - Building up from previous states, visit n states, constant space complexity
"""

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:


        fx0 = cost[0]
        fx1 = min(cost[1],cost[1] + fx0)

        for n in range(2,len(cost)):
            fx2 = cost[n] + min(fx1,fx0)
            fx0 = fx1
            fx1 = fx2

        return min(fx1,fx0)        



        # def dp(index,cache):

        #     if index in cache:
        #         return cache[index]

        #     if index >= len(cost):
        #         return 0

        #     D1 = cost[index] + dp(index+1, cache)
        #     D2 = cost[index] + dp(index+2, cache)

        #     cache[index] = min(D1, D2)

        #     return cache[index]

        # return min(dp(0,{}),dp(1,{}))
