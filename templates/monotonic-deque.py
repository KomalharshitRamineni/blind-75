"""
monotonic-deque 

Trigger: max or min of every sliding window · the best of the last k values, needed at every step. Complexity: O(n) / O(k)
"""


from collections import deque

def monotonic_deque(nums):

    def foo(j, i):
        return False

    queue = deque()     # monotonically decreasing, [value, index]
    res = []

    for i in range(len(nums)):

        while queue and queue[-1][0] < nums[i]:
            queue.pop()

        queue.append([nums[i], i])

        # front's index j no longer valid for whatever condition
        while queue and foo(queue[0][1], i):
            queue.popleft()

        res.append(queue[0][0])     # front = max of the window

    return res
