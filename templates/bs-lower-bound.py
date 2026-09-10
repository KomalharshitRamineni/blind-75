"""
bs-lower-bound — boundary / first-true

Trigger: first index satisfying a monotone predicate · "minimum X such that feasible(X)", i.e. binary search over the *answer* rather than over the array. This is the variant that actually shows up. Complexity: O(log range × cost of feasible)
"""


def bs_lower_bound(arr):

	l, r = 0, len(arr)-1
	res = arr[0]

	def foo():
		return None

	while l < r:
	
		mid = (l+r) // 2
		res = min(arr[mid], res)

		if foo():
			r = mid
		
		else:
			l = mid + 1
	
	return res
