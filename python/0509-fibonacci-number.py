"""
509. Fibonacci Number · https://leetcode.com/problems/fibonacci-number/
2026-11-07 · 30m · skeleton: dp
O(n) time / O(1) space — Looping through values up to N re using comptued values
"""


class Solution:
    def fib(self, n: int) -> int:
        
        fx0 = 0
        fx1 = 1

        if n == 0:
            return 0

        if n == 1:
            return 1

        for i in range(1,n):
            fx2 = fx1 + fx0
            fx0 = fx1
            fx1 = fx2

        return fx1


        def dp(n,cache):

            if n in cache:
                return cache[n]

            if n == 0:
                return 0
            if n == 1:
                return 1

            return dp(n-1,cache) + dp(n-2,cache)

        return dp(n,{})
        