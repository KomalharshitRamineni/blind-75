"""
18. 4Sum · https://leetcode.com/problems/4sum/
2026-10-19 · clean · 30m · skeleton: tp-opposite
O(n^3) time / O(m) space — fix values and sort to reduce to two sum, avoid recomputing duplicates
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        nums.sort()
        cur,res = [],[]


        def kSum(k,start,target):

            if k == 2:
                
                left, right = start, len(nums)-1

                while left  < right:
                    if nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        res.append(cur + [nums[left]] + [nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left-1]:
                            left +=1

                        while left < right and nums[right] == nums[right+1]:
                            right-=1
                

            else:

                for i in range(start,len(nums)-k+1):
                    if i > start and nums[i-1] == nums[i]:
                        continue
                    cur.append(nums[i])
                    kSum(k-1,i+1,target-nums[i])
                    cur.pop()

        kSum(4,0,target)
        return res






        # nums.sort()
        # res = []
        # seen = set()

        # for a in range(len(nums)-3):
        #     targetB = target-nums[a]

        #     for b in range(a+1,len(nums)-2):

        #         targetC = targetB - nums[b]

        #         left, right = b+1,len(nums)-1

        #         while left < right:
        #             if nums[left] + nums[right] > targetC:
        #                 right -= 1
        #             elif nums[left] + nums[right] < targetC:
        #                 left  +=1
        #             else:
        #                 sol = (nums[a],nums[b],nums[left],nums[right])
        #                 if sol not in seen:

        #                     res.append([nums[a],nums[b],nums[left],nums[right]])
        #                     seen.add(sol)

        #                 left +=1
        #                 right -=1
        # return res





            



