"""
875. Koko Eating Bananas · https://leetcode.com/problems/koko-eating-bananas/
2026-10-02 · fail · 30m · skeleton: bs-lower-bound
O(piles * log(max(piles))) time / O(1) space - Binary search based off of known maximum that works
"""

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:


        def check(k):

            hours = 0
    
            for bananas in piles:
                hours += math.ceil(bananas / k)
                if hours > h:
                    return False
                    
            return True

        k = max(piles)

        left, right = 1, k

        while left <= right:

            mid = (left+right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left