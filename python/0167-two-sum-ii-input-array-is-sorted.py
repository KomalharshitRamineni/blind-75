"""
167. Two Sum II Input Array Is Sorted · https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
2026-09-18 · clean · 10m · skeleton: tp-opposite
O(n) time / O(1) space — one pass, pointers only ever converge
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        

        l, r = 0, len(numbers)-1

        while l < r:

            cur = numbers[l] + numbers[r]

            if cur > target:
                r-=1
            elif cur < target:
                l+=1
            else:
                return [l+1,r+1]
