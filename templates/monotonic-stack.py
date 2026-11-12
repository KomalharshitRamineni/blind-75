"""
monotonic-stack 

Trigger: "next greater / next smaller element" · how far until a larger value · histogram area · anything needing the nearest unresolved earlier element. Complexity: O(n) / O(n)
"""


def monotonic_stack(nums):

    stack = []
    res = [0] * len(nums)       # default for items never popped (0 or -1)

    for i in range(len(nums)):

       #If adding current element would violate the montonic inc/dec property
        while stack and stack[-1][0] < nums[i]:
            _, idx = stack.pop()    #Item popped wasn't violated till now
            res[idx] = nums[i]      # store element or index in the result

        stack.append([nums[i], i])

    return res
