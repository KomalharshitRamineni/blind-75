"""
1137. N-th Tribonacci Number · https://leetcode.com/problems/n-th-tribonacci-number/
2026-11-10 · 10m · skeleton: dp-1d-bottomup
O(n) time / O(1) space - Looping up to n, fixed extra memory
"""

class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        if n<3:
            return 1

        fx0 = 0
        fx1 = 1
        fx2 = 1

        for i in range(3, n+1):

            fx3 = fx2 + fx1 + fx0
            fx0 = fx1
            fx1 = fx2
            fx2 = fx3
        
        return fx2


        # def dp(n, cache):

        #     if n in cache:
        #         return cache[n]

        #     if n == 0:
        #         return 0

        #     if n < 3:
        #         return 1

        #     cache[n] = dp(n-1,cache) + dp(n-2, cache) + dp(n-3, cache)
        #     return cache[n]

        # return dp(n, {})
            



