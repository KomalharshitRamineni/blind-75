"""
417. Pacific Atlantic Water Flow · https://leetcode.com/problems/pacific-atlantic-water-flow/
2026-10-16 · fail · 30m · skeleton: graph-bfs-grid
O(m * n) time / O(m * n) space — Think of working towards a point instead of working out, avoids recomputed work
"""

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:

        ROWS = len(heights)
        COLS = len(heights[0])

        pacific, atlantic = set(), set()


        def outOfBounds(row,col):
            
            return ((row < 0 or col < 0) or 
                    (row >= ROWS or col >=COLS))


        def bfs(row, col, visited):

            queue = collections.deque()
            queue.append((row,col))
            visited.add((row,col))

            while queue:

                curR, curC = queue.popleft()

                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dirr in directions:
                    r, c = dirr

                    if ((not outOfBounds(curR + r, curC + c)) and 
                        (heights[curR][curC] <= heights[curR + r][curC + c]) and
                        (curR + r, curC + c) not in visited):

                         queue.append((curR + r, curC + c))
                         visited.add((curR + r, curC + c))



        for row in range(ROWS):
            bfs(row,0,pacific)
            bfs(row,COLS-1,atlantic)
        for col in range(COLS):
            bfs(0,col,pacific)
            bfs(ROWS-1,col,atlantic)

        #Now we have two sets of nodes that reach from pacifc, node sthat reach from atlantic

        res = []

        for row,col in pacific.intersection(atlantic):
            res.append([row,col])

        return res



        # ROWS = len(heights)
        # COLS = len(heights[0])

        # res = []


        # def outOfBounds(row,col):
            
        #     return ((row < 0 or col < 0) or 
        #             (row >= ROWS or col >=COLS))

        # def bfs(row,col):

        #     queue = collections.deque()
        #     queue.append((row,col))

        #     visited = set()
        #     visited.add((row,col))

        #     reachPacific = False
        #     reachAtlantic = False

        #     while queue:

        #         curR, curC = queue.popleft()

        #         if [curR,curC] in res:
        #             return True
        #         if curR == 0 or curC == 0:
        #             reachPacific = True
        #         if curR == ROWS-1 or curC == COLS-1:
        #             reachAtlantic = True
        #         if (reachAtlantic and reachPacific):
        #             return True

        #         directions = [(1,0),(-1,0),(0,1),(0,-1)]
        #         for dirr in directions:
        #             r, c = dirr

        #             if ((not outOfBounds(curR + r, curC + c)) and 
        #                 (heights[curR][curC] >= heights[curR + r][curC + c]) and
        #                 (curR + r, curC + c) not in visited):

        #                  queue.append((curR + r, curC + c))
        #                  visited.add((curR + r, curC + c))

        #     return reachAtlantic and reachPacific

        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if bfs(row,col):
        #             res.append([row,col])
                    
        # return res




        
