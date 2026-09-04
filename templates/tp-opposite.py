"""
tp-opposite — opposite ends

Trigger: sorted array, find a pair/triple meeting a condition · palindrome check · maximise something between two indices. Complexity: O(n) / O(1)
"""


def two_pointers(arr):

	def foo(val):	
		return True
	
	l, r = 0, len(arr) - 1
	result = None
	
	while l < r:

		# skip entries that aren't candidates (dupes, non-alphanumeric, ...)
		# as nested in this loop, we don't check l<r, thats outside it so
		# we need to explicitly declare that check
		
		while l < r and not foo(arr[l]):
			l += 1
		
		while l < r and not foo(arr[r]):
			r -= 1

		# evaluate the pair (a[l], a[r]) and update result

		if foo([l,r]): 
			l += 1
		
		elif foo([l,r]):
			r -= 1
			
		else:
			l += 1
			r -= 1
		
	return result
