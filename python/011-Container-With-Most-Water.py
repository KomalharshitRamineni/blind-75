"""
11. Container With Most Water · https://leetcode.com/problems/container-with-most-water/
2026-09-05 · fail · 30m · skeleton: tp-opposite
O(n) time / O(1) space — Adjusting pointers to elimnate search space as adjusting means we computed best in the given space/
"""



class Solution:
    def maxArea(self, height: List[int]) -> int:
        

        l, r = 0, len(height)-1
        max_capacity = 0
        
        def get_area(l,r):
            area = (r-l) * min(height[l],height[r])
            return area


        if len(height) == 2:
            return min(height[0],height[1]) * min(height[0],height[1])

        while l < r:
            max_capacity = max(max_capacity, get_area(l,r))

            if height[l] > height[r]:
                r-=1

            elif height[r] > height[l]:
                l+=1

            else:
                l+=1



        return max_capacity
