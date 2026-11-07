"""
733. Flood Fill · https://leetcode.com/problems/flood-fill/
2026-11-02 · 13m · skeleton: graph-bfs-grid
O(mxn) time / O(mxn) space — Worst case traversing the whole board and storing in queue
"""



from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        ROWS, COLS = len(image), len(image[0])
        visited = set()

        def bfs(row, col):
            target = image[row][col]
            queue = deque()
            queue.append((row,col))
            visited.add((row,col))
            image[row][col] = color
            
            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            while queue:

                curR, curC = queue.popleft()
                for dirr in directions:
                    r, c = dirr
                    nextR, nextC = curR + r, curC + c
                    #Now we want to check if this is in bounds, and not in visited
                    if ((not ((nextR < 0 or nextR >= ROWS) or 
                        (nextC < 0 or nextC >= COLS) or
                        ((nextR,nextC) in visited))) and
                        image[nextR][nextC] == target):

                        #Then we add to our queue
                        queue.append((nextR,nextC))
                        visited.add((nextR,nextC))
                        image[nextR][nextC] = color


        bfs(sr,sc)
        return image

    #Time complexity for this would be traversing whlole grid at worst case so O(mxn) space being worst case
    # The whole board can be in the queue

                
                