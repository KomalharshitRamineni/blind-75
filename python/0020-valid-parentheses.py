"""
20. Valid Parentheses · https://leetcode.com/problems/valid-parentheses/
2026-09-08 · clean · 20m · skeleton: plain matching stack
O(n) time / O(n) space — one pass; the stack holds up to n when the input is all openers
"""


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {'}' : '{',
                  ')':'(',
                  ']':'['}


        for a in s:

            if not stack:
                stack.append(a)
                continue
            elif pairs.get(a) == stack[-1]:
                stack.pop()
            else:
                stack.append(a)

        return len(stack)==0
