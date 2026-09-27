"""
424. Longest Repeating Character Replacement · https://leetcode.com/problems/longest-repeating-character-replacement/
2026-09-08 · fail · 30m · skeleton: sliding-window
O(n) time / O(1) space — Sliding window useful when we have a condition and we want to search contiguious values to satisfiy said condition
"""




class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        l,r = 0, 0
        freq = {}
        longest = 0

        def check_valid():
            max_freq = 0
            for value in freq.values():
                max_freq = max(max_freq, value)

            if k + max_freq >= (r-l+1):
                return True
            else:
                return False

        while r < len(s):

            if freq.get(s[r]):
                freq[s[r]] = freq.get(s[r]) + 1
            else:
                freq[s[r]] = 1

            if check_valid():
                longest = max(longest,r-l+1)

            else:
                while not check_valid():
                    freq[s[l]] -=1
                    l+=1
            r+=1
            
        return longest
