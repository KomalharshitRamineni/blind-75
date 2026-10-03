"""
978. Longest Turbulent Subarray · https://leetcode.com/problems/longest-turbulent-subarray/
2026-10-03 · fail · 30m · skeleton: sliding-window
O(n) time / O(1) space - Sliding window moving pointers when subarray no longer valid
"""


class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        

        left, right = 0, 1

        res, prev = 1, ""


        while right < len(arr):

            if arr[right-1] > arr[right] and prev != ">":
                res = max(res, (right - left) + 1)
                right += 1
                prev = ">"
            elif arr[right-1] < arr[right] and prev != "<":
                res = max(res, (right - left) + 1)
                right += 1
                prev = "<"
            else:
                if arr[right-1] == arr[right]:
                    left = right
                else:
                    left = right - 1

                right +=1
        return res