"""
344. Reverse String · https://leetcode.com/problems/reverse-string/
2026-11-03 · 4m · skeleton: tp-opposite
O(n) time / O(1) space — Traversing input only maintaining pointers
"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        left, right = 0, len(s)-1

        while left < right:

            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            
            left+=1
            right-=1

        return s