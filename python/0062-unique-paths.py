"""
62. Unique Paths · https://leetcode.com/problems/unique-paths/
2026-11-07 · 30m · skeleton: dp-2d-grid
O(n*m) time / O(n) space — Only a row needed to be held in memory at a time
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        def move(r,c,cache):
            state = (r,c)

            if state in cache:
                return cache[state]

            if r == m or c == n:
                return 0

            if r==m-1 and c==n-1:
                return 1

            down = move(r+1,c,cache)
            right = move(r,c+1,cache)

            cache[state] = down + right
            return cache[state]


        def bottom_up():

            memo = []
            for r in range(m):
                memo.append([])
                for c in range(n):
                    memo[-1].append(0)
                    

            for r in range(m):
                for c in range(n):
                    if r == 0 and c == 0:
                        memo[r][c] = 0
                    elif r == 0:
                        memo[r][c] = 1
                    elif c == 0:
                        memo[r][c] = 1
                    else:
                        memo[r][c] = memo[r-1][c] + memo[r][c-1]

            return memo[m-1][n-1]

        def bottom_up_space_optimised(m,n):

            memo = [1 for _ in range(n)]

            for r in range(m-1):
                newMemo = [1 for _ in range(n)]
                for c in range(1,n):
                    newMemo[c] = newMemo[c-1] + memo[c]

                memo = newMemo

            return memo[-1]


        return bottom_up_space_optimised(m,n)
        return bottom_up()
        return move(0,0,{})