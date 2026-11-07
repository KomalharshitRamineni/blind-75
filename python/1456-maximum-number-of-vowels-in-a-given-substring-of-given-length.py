"""
1456. Maximum Number of Vowels In a Given Substring of Given Length · https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
2026-11-07 · 10m · skeleton: sliding-window
O(n) time / O(1) space - Going through input size n and maintaining a count and using set for checks to keep time complexity constant
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        

        vowels = set(['a','e','i','o','u'])
        curWindow = 0


        #Lets also go up to k first
        for i in range(k):
            if s[i] in vowels:
                curWindow+=1

        res = curWindow
        left = 0

        for right in range(k,len(s)):

            #First lets check our left
            if s[left] in vowels:
                curWindow-=1

            left+=1

            #Now we check our right
            if s[right] in vowels:
                curWindow+=1

            #Lets compare this to the max we ahve seen
            res = max(res,curWindow)

        return res

        #Time complexity for this is O(n) space is constant