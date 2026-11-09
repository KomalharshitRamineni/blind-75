"""
901. Online Stock Span · https://leetcode.com/problems/online-stock-span/
2026-11-09 · 30m · skeleton: monotonic-stack
O(n) time / O(n) space - We add and pop at most n inputs, without popping or adding same input again
"""


class StockSpanner:

    def __init__(self):
        self.prices = []
        self.day = 0

    def next(self, price: int) -> int:
        
        self.day+=1

        while self.prices and self.prices[-1][0] <= price:
            self.prices.pop()

        if not self.prices:
            self.prices.append([price,self.day])
            return self.day
        else:
            res = self.day - self.prices[-1][1]
            self.prices.append([price,self.day])
            return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)