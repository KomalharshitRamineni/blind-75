"""
881. Boats To Save People · http://leetcode.com/problems/boats-to-save-people/
2026-10-23 · clean · 15m · skeleton: tp-opposite
O(nlog(n)) time / O(1) space - Two pointers, give only two people per boat (Important constraint)
"""

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        
        people.sort()

        left, right = 0, len(people)-1
        count = 0

        while left <= right:

            if people[left] + people[right] > limit:
                right-=1
            else:
                left+=1
                right -=1

            count+=1

        return count
            
