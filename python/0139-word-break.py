"""
139. Word Break · https://leetcode.com/problems/word-break
2026-11-03 · fail · 30m · skeleton: dp-1d-topdown
O(n * w * t) time / O(n) space — Traversing string, looping through each word in dict, slicing string
"""



class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:


            dp = [False] * (len(s) + 1)
            dp[-1] = True

            for i in range(len(s)-1,-1,-1):
                
                for word in wordDict:
                    if i + len(word) > len(s):
                        continue

                    if s[i: i + len(word)] == word:
                        dp[i] = dp[i + len(word)]

                    if dp[i]:
                        break


            return dp[0]





        # def foo(string, cache):

        #     if string in cache:
        #         return cache[string]

        #     if not string:
        #         return True

        #     for word in wordDict:
        #         if string.startswith(word):
        #             removed = string[len(word):]
        #             cache[string] = foo(removed, cache)
        #             if cache[string]:
        #                 return True

        #     cache[string] = False
        #     return cache[string]

        # return foo(s,{})

