"""
125. Valid Palindrome · https://leetcode.com/problems/valid-palindrome/
2026-09-01 · fail · 30m · skeleton: tp-opposite
O(n) time / O(1) space — single pass, two pointers converge from the ends
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isAlpha(c):
            return (ord('a') <= ord(c) and ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))

        l = 0
        r = len(s) - 1

        s = s.lower()
        while r > l:
            while r > l and not(isAlpha(s[l])):
                l += 1
            while r > l and not(isAlpha(s[r])):
                r -= 1

            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True