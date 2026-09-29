"""
680. Valid Palindrome II · https://leetcode.com/problems/valid-palindrome-ii/
2026-09-29 · hint · 30m · skeleton: tp-opposite
O(n) time / O(1) space — one pass plus at most one rescan of the inner range
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def checkPalindrome(lo, hi):

            while lo < hi:
                if s[lo] == s[hi]:
                    lo += 1
                    hi -= 1
                else:
                    return False

            return True


        left, right = 0, len(s) - 1

        while left < right:

            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # everything outside [left, right] already mirrors, so only the
                # inner range needs rechecking — skip the left char, or the right
                return checkPalindrome(left + 1, right) or checkPalindrome(left, right - 1)

        return True
