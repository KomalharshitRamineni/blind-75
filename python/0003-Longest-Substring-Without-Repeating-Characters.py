"""
11. Longest Substring Without Repeating Characters · https://leetcode.com/problems/longest-substring-without-repeating-characters/
2026-09-07 · fail · 30m · skeleton: sliding-window
O(n) time / O(n) space — Sliding window makes sense for contiguous problems, follow through with pointer implementation as opposed to half half with for loops, can use any to store seen here for constant check up time
"""




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        l = 0
        r = 0
        max_length = 0

        while r<len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            seen.add(s[r])
            r+=1
            max_length = max(max_length, len(seen))

        return max_length            

        