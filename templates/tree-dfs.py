"""
tree-dfs — recursive DFS returning info upward

Trigger: any per-subtree computation — depth, diameter, validity, path sums, balance. The default tree template. Complexity: O(n) / O(h)
"""


def tree_dfs_recursive(root):
	
	if not root:
		return root
	
	left = tree_dfs_recursive(root.left)
	right = tree_dfs_recursive(root.right)
	
	#Do our fucntion wth these lefts and righrts

	return root

  

def tree_dfs_iterative(root):

	stack = []

	while stack:
	
		node = stack.pop()
	
		if node:
		
			#Do something
			stack.append(node.left)
			stack.append(node.right)
