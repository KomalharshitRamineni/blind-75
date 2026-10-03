"""
219. Contains Duplicate II · https://leetcode.com/problems/contains-duplicate-ii/
2026-09-30 · clean · 28m · skeleton: sliding-window
O(n) time / O(n) space — grow and shrink window based on our condition
"""

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        seen = {}

        for index, elm in enumerate(nums):
            if seen.get(elm):
                seen[elm].append(index)
            else:
                seen[elm] = [index]
            

        for values in seen.values():
            
            if len(values) >=2:

                left = 0
                for right in range(1,len(values)):

                    res = abs(values[left]-values[right])
                    if res <= k:
                        return True
                    else:
                        left+=1
                    
        return False








                
