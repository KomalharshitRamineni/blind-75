"""
46. Permutations · https://leetcode.com/problems/permutations/
2026-11-01 · fail · 30m · skeleton: backtracking
O(n!*n) time / O(n!*n) space — Storing the recursive callstack, memory is same as time complexity
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        res = []
        visited = set()

        def bf(path):

            #We want to brute force the path
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                if num not in visited:
                    visited.add(num)
                    path.append(num)
                    bf(path)

                    visited.remove(num)
                    path.pop()

        bf([])


        return res
            







# class Solution:
#     def permute(self, nums: list[int]) -> list[list[int]]:


#         res = []
#         visited = set()

#         def bf(path):

#             #We want to brute force the path
#             if len(path) == len(nums):
#                 res.append(path)
#                 return

#             for num in nums:
#                 if num not in path:
#                     bf(path + [num])

#         bf([])


#         return res
            
