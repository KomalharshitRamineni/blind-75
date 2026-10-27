"""
70. Climbing Stairs · https://leetcode.com/problems/climbing-stairs/
2026-10-23 · fail · 30m · skeleton: dp-topdown
O(n) time / O(n) space — We are only every solving a sub problem once, caching every solved sub problem
"""

class Solution:
    def climbStairs(self, n: int) -> int:


        def backtracking(steps, cache):

            if steps in cache:
                return cache[steps]
            
            if steps == 0:
                return 1

            if steps < 0:
                return 0

            cache[steps] = backtracking(steps-1, cache) + backtracking(steps-2, cache)
        
            return cache[steps]
        
        return backtracking(n,{})



