"""
bs-lower-bound — boundary / first-true

Trigger: first index satisfying a monotone predicate · "minimum X such that feasible(X)", i.e. binary search over the *answer* rather than over the array. This is the variant that actually shows up. Complexity: O(log range × cost of feasible)
"""


def bs_lower_bound(arr):
    left, right = 0, len(arr) - 1

    def foo():
        return None

    while left <= right:
        mid = (left + right) // 2

        if foo():
            right = mid - 1
        else:
            left = mid + 1

    return left
