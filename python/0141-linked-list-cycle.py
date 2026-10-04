"""
141. Linked List Cycle · https://leetcode.com/problems/linked-list-cycle/
2026-10-04 · clean · 13 · skeleton: tp-fast-slow
O(n) time / O(1) space — At any arbitrary point, gap between fast and slow is always closed by -1, resulting in O(n) time complexity
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


            fast, slow = head, head

            while fast and fast.next:

                fast = fast.next.next
                slow = slow.next

                if fast == slow:
                    return True

            return False


