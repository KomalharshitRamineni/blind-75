"""
bs-exact — classic exact match

Trigger: sorted array, find an exact target. Complexity: O(log n) / O(1)
"""


def bs_exact(arr, target):

	left, right = 0, len(arr) - 1

	while left <= right:

		mid = (left + right) // 2

		if arr[mid] > target:
			right = mid - 1        # mid - 1, NOT mid -- that pairing is bs-lower-bound
		elif arr[mid] < target:
			left = mid + 1
		else:
			return mid

	# loop exits when left > right: the target is absent
	return -1
