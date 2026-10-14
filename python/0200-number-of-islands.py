"""
200. Number Of Islands · https://leetcode.com/problems/number-of-islands/
2026-10-14 · clean · 12m · skeleton: graph-bfs-grid
O(n * m) time / O(n * m) space — visiting every node in grid and worst case island size of grid
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        islandCount = 0


        def bfs(row, col):

            queue = collections.deque()
            queue.append((row,col))
            visited.add((row,col))

            def outOfBounds(r,c):
                return ((r < 0 or c < 0) or (r >= ROWS or c >= COLS) or ((r, c) in visited) or (grid[r][c] == "0"))

            while queue:

                curR, curC = queue.popleft()

                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for direction in directions:

                    r, c = direction
                    
                    if not outOfBounds(curR + r, curC + c):
                        queue.append((curR + r, curC + c))
                        visited.add((curR + r,curC + c))


        for row in range(ROWS):
            for col in range(COLS):
                if ((row,col) not in visited) and grid[row][col] == "1":
                    bfs(row,col)
                    islandCount += 1

        return islandCount
    








        # def dfs(row, col):

        #     if ((row < 0 or col < 0) or
        #         (row >= ROWS or col >= COLS) or
        #         ((row, col) in visited) or
        #         (grid[row][col] == "0")):
        #             return 

        #     visited.add((row,col))

        #     dfs(row+1,col)
        #     dfs(row-1,col)
        #     dfs(row,col+1)
        #     dfs(row,col-1)

