"""
21. Merge Two Sorted Lists · https://leetcode.com/problems/merge-two-sorted-lists/
2026-10-03 · clean · 20m · skeleton: ll-dummy
O(n+m) time / O(1) space — Only one node is ever held at one time in memory, therefore making it O(1) space complexity
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        

        dummy = ListNode()
        dummyHead = dummy

        while list1 and list2:

            if list1.val <= list2.val:

                dummy.next = list1
                list1 = list1.next

            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next

        if list1:
            dummy.next = list1
        else:
            dummy.next = list2
       
       
        return dummyHead.next
