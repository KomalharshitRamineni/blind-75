"""
239. Sliding Window Maximum · https://leetcode.com/problems/sliding-window-maximum/
2026-10-12 · fail · 30m · skeleton: sliding-window
O(n) time / O(k+n) space — Using a montonic queue to keep track off the current max indicies and avoiding recomputations by popping small added values
"""

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        

        res = []

        queue = collections.deque()

        left, right = 0, 0

        while right < len(nums):

            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            if left > queue[0]:
                queue.popleft()

            if right + 1 >= k:
                res.append(nums[queue[0]])
                left += 1

            right += 1 

        return res