"""
79. Word Search · https://leetcode.com/problems/word-search/
2026-10-14 · fail · 30m · skeleton: backtracking
O(m * n * 4^{n}) time / O(n) space — Matrix backtracking, dfs has complexity of decisions ^ {depth of call stack}
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])
        
        path = set()

        def dfs(row, col ,index):

            if index == len(word):return True

            if ((row < 0 or col < 0) or 
                (row >= ROWS or col >= COLS) or
                (board[row][col]!= word[index]) or 
                ((row,col) in path)):

                return False

            path.add((row,col))

            res = (dfs(row+1,col,index+1) or
                    dfs(row-1,col,index+1) or
                    dfs(row,col+1,index+1) or
                    dfs(row,col-1,index+1))
            
            path.remove((row,col))

            return res


        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if dfs(row,col,0): return True

        return False




