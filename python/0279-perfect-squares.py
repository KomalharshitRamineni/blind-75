"""
279. Perfect Squares · https://leetcode.com/problems/perfect-squares/
2026-11-14 · 30m · skeleton: dp
O(n*sqrt(n)) time / O(n) space — Going through each state, building up solution bottom up, worst case for each element loop sqrt(n)
"""


class Solution:
    def numSquares(self, n: int) -> int:



        memo = [0] * (n + 1)
        memo[1] = 1

        for i in range(1, n+1):

            minimum = float("inf")
            for j in range(1, i+1):

                psquare = j*j
                if psquare > i:
                    break
                else:
                    minimum = min(memo[i-psquare], minimum)

            memo[i] = minimum + 1

        
        return memo[-1]
