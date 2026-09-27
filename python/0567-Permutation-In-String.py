"""
567 · Permutation In String · https://leetcode.com/problems/permutation-in-string/
2026-09-23 · fail · 30m · skeleton: sliding-window
O(n) time / O(1) space — Sliding window to to find continguous substring to satisfy value but over a fixed window
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        s2_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)

        if s1_count == s2_count:
            return True

        left = 0
        right = len(s1)

        while right<len(s2):

            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1
            s2_count[s2[left]] -= 1

            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]

            if s1_count == s2_count:
                return True

            left += 1
            right += 1


        return False