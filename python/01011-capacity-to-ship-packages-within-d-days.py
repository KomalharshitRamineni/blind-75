"""
1011. Capacity To Ship Packages Within D Days · https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
2026-11-08 · 30m · skeleton: bs-lower-bound
O(nlog(n)) time / O(1) space - Binary serach trying to find the minimum capcaity that satisfies our condition
"""



class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        def helper(capacity):
            #We check if this capcaity works
            total = 0
            totalDays = 1
            
            for w in weights:

                if totalDays > days:
                    return False

                if (total+w) > capacity:
                    totalDays+=1
                    total = 0

                total += w
        
            return days >= totalDays


        #lets find the min and max for our binary search
        lower = max(weights)
        upper = sum(weights)

        #Now we are going to converge on a wight that is minimum that satisfies oru condition
        while lower <= upper:
            mid = (lower+upper)//2
            #Now lets try this capcaity
            if helper(mid):
                #Meaning this works, however we want to find minim
                upper = mid-1
            else:
                #Meaning this doesn't work we need more cpacity
                lower = mid+1

        #We should return lower
        return lower