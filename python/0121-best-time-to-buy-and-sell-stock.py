"""
121. Best Time To Buy and Sell Stock · https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
2026-09-06 · fail · 30m · skeleton: sliding-window
O(n) time / O(1) space — since we need to preserve order we use sliding window and update pointers to fit solution requirments
"""



class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        max_profit = 0

        l = 0
        r = 1

        while r <= len(prices)-1:

            max_profit = max(max_profit,prices[r]-prices[l])

            if prices[r] < prices[l]:
                l=r
                r+=1
            else:
                r+=1

        return max_profit