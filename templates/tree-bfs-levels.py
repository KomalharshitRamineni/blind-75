"""
tree-bfs-levels — level-order with a size-snapshot loop

Trigger: the word "level" · right side view · minimum depth · shortest path in a tree. The `for _ in range(len(queue))` snapshot is what makes levels work. Complexity: O(n) / O(w)
"""


def tree_bfs_levels(root):

	queue = collections.deque()
	queue.append(root)
	

	while queue:
		
		levels = len(queue)
	
		for i in range(levels):
		
			node = queue.pop()
			
			if node:
			
				#Do something with this node
				#We are visting every node level by level
				queue.append(node.left)
				queue.append(node.right)
