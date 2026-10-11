"""
tree-inorder-iterative — explicit stack

Trigger: kth smallest in a BST · validating a BST by ordering · needing to pause mid-traversal. Lower priority. Complexity: O(n) / O(h)
"""


def tree_inorder_iterative(root):

	stack = []
	cur = root
	
	while stack or cur:
	
		while cur:
		
			stack.append(cur.left)
			cur = cur.left
		
		cur = stack.pop() 
		
		#Do something, we are in order there
		
		cur = cur.right
