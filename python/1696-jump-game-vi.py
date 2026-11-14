"""
1696. Jump Game VI · https://leetcode.com/problems/jump-game-vi/
2026-11-14 · 30m · skeleton: dp, monotonic-deque
O(n) time / O(n + k) space - Coming up with the dp solution and then understanding that we only care about max seen in window k.
"""


from collections import deque

class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n

        # Base case
        dp[n - 1] = nums[n - 1]

        q = deque([n - 1])

        for i in range(n - 2, -1, -1):

            # Remove indices outside jump range
            while q and q[0] > i + k:
                q.popleft()

            # Best score from reachable next positions
            dp[i] = nums[i] + dp[q[0]]

            # Maintain decreasing dp values
            while q and dp[q[-1]] <= dp[i]:
                q.pop()

            q.append(i)

        return dp[0]