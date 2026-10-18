"""
24. Swap Nodes In Pairs · https://leetcode.com/problems/swap-nodes-in-pairs/
2026-10-15 · fail · 30m · skeleton: ll-reverse
O(n) time / O(1) space — Only one node is ever held at one time in memory, therefore making it O(1) space complexity
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        
        if not head or not head.next:
            return head

        dummy = node = ListNode()
        prev, cur = node, head


        while cur and cur.next:

            first = cur.next
            second = cur.next.next

            first.next = cur
            cur.next = second
            prev.next = first

            prev = cur
            cur = second

        return dummy.next

