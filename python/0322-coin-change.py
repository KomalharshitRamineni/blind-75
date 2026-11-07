"""
322. Coin Change · https://leetcode.com/problems/coin-change/
2026-10-31 · 30m · skeleton: dp-topdown
O(n*t) time / O(t) space — Complexity for a memoised dp-topdown is number of states x work per state
"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        def coinChoose(total,cache):

            if total in cache:
                return cache[total]

            if total == 0:
                return 0

            if total < 0:
                return float("inf")

            result = float("inf")

            for coin in coins:
                result = min(result,1 + coinChoose(total-coin,cache))

            cache[total] = result

            return cache[total]

        res = coinChoose(amount,{})
        if res == float("inf"):
            return -1
        else:
            return res