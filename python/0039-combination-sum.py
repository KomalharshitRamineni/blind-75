"""
39. Combination Sum · https://leetcode.com/problems/combination-sum/
2026-10-13 · fail · 30m · skeleton: backtracking
O(2^{n}) time / O(n) space — Backtracking along a decision tree pruning branches
"""



class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        res = []

        def dfs(i, cur, total):

            if i >= len(candidates) or total > target:
                return


            if total == target:
                res.append(cur.copy())
                return

            cur.append(candidates[i])
            dfs(i,cur,total+candidates[i])
            cur.pop()
            i+=1
            dfs(i,cur,total)

        dfs(0,[],0)

        return res




        # res = []
        # candidates.sort()


        # stack = [([],0,0)]

        # while stack:

        #     combination, index, total = stack.pop()

        #     if index >= len(candidates) or total > target:
        #         continue

        #     if total == target:
        #         res.append(combination)
        #         continue

        #     for i in range(index,len(candidates)):
        #         if (total+candidates[i]) > target:
        #             continue
        #         else:
        #             stack.append((combination + [candidates[i]], i, total+candidates[i]))

        # return res
            


