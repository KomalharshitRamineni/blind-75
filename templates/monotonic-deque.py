"""
monotonic-deque 

Trigger: max or min of every sliding window · the best of the last k values, needed at every step. Complexity: O(n) / O(k)
"""


from collections import deque

def monotonic_deque(arr):

    def foo(j, i):
        return False

    queue = deque()     # indices, values decreasing front to back

    res = []

    for i in range(len(arr)):

        # front's index j no longer valid for whatever condition
        while queue and foo(queue[0], i):
            queue.popleft()

        while queue and arr[i] > arr[queue[-1]]:
            queue.pop()

        queue.append(i)

        res.append(arr[queue[0]])     # front = max of the window

    return res
