"""
658. Find K Closest Elements · https://leetcode.com/problems/find-k-closest-elements/
2026-10-10 · fail · 20m · skeleton: tp-opposite
O(n) time / O(1) space — Searching through input with fixed window
"""



class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        left, right = 0, len(arr)-1

        #right-left != window size, just distance between them!!!!!
        while right-left > k - 1:
            leftDiff = abs(arr[left]-x)
            rightDiff = abs(arr[right]-x)

            if leftDiff <= rightDiff:
                right-=1
            else:
                left+=1

        return arr[left:right+1]












###First attempt

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        #We want to find closest

        closest = len(arr)-1

        for cur in reversed(range(len(arr))):
            diff = abs(x-arr[cur])
            if diff <= abs(x-arr[closest]):
                #Then this is the new closest
                closest = cur

        #Now from here we wnat ot build k elemnst

        left = right = closest

        for i in range(k-1):

            lower = left - 1
            upper = right + 1

            if lower < 0:
                right += 1

            elif upper > len(arr)-1:
                left -=1

            else:

                diffLower = abs(arr[lower]-x)
                diffUpper = abs(arr[upper]-x)

                if diffLower <= diffUpper:
                    left -=1
                else:
                    right+=1

        return arr[left:right+1]


