"""
graph-bfs-grid — queue over cells with a visited set

Trigger: a grid where each cell connects to its 4 neighbours. Count or fill regions (islands, flood fill), or find the fewest steps / minutes for something to spread. BFS reaches cells in order of distance, so it's the one to use when the answer *is* a distance. Multi-source = seed every source before the loop. Complexity: O(rows × cols) / O(rows × cols)
"""


def graphBfsGrid(grid):

	ROWS = len(grid)
	COLS = len(grid[0])
	
	visited = set()

	def bfs(row, col):
	
		queue = collections.deque()
		queue.append((row,col))
		visited.add((row,col))
		
		
		def invalid(r,c):
		
			return ((r < 0 or c < 0) or
				(r >= ROWS or c >= COLS) or
				((r, c) in visited) or
				(grid[r][c] == "Not Target"))

		while queue:
	
			curR, curC = queue.popleft()
			directions = [(0,1), (0,-1), (1,0), (-1,0)]

			for direction in directions:
			
				r, c = direction
				
				if not invalid(curR + r, curC + c):
				
					queue.append((curR + r, curC + c))
					visited.add((curR + r,curC + c))
			
	
	for row in range(ROWS):
		for col in range(COLS):
			if ((row,col) not in visited) and grid[row][col] == "Target":
				bfs(row,col)

	return
