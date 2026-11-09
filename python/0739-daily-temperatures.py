"""
739. Daily Temperatures · https://leetcode.com/problems/daily-temperatures/
2026-11-09 · 30m · skeleton: montonic-stack
O(n) time / O(n) space - Searching through n items and worst case popping n items = 2n -> O(n) space is res and stack = O(n)
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                colderDay = stack.pop()
                res[colderDay] = i-colderDay
            stack.append(i)

        return res
