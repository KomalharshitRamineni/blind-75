"""
77. Combinations · https://leetcode.com/problems/combinations/
2026-11-12 · 30m · skeleton: backtracking
O(2^{n} + k*(nCk)) time / O(k(nCk)) space — copy operations are done nCk times and copy costs k, whole tree time complexity is 2^n plus copy time complexity
"""

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        

        res = []
        path = []


        def backtracking(index):


            if len(path) == k:
                res.append(path.copy())
                return

            if index == n+1:
                return

            path.append(index)
            backtracking(index+1)
            path.pop()
            backtracking(index+1)

        backtracking(1)

        return res



            