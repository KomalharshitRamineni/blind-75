"""
206. Reverese Linked List · https://leetcode.com/problems/reverse-linked-list/description/
O(n) time / O(1/n) space — Depending on recursive or iterative approach, careful of what links are adjusted recursively (what is present in call stack) iteratively what we store and change
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:


        cur, prev = head, None


        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev



class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        
        if head:
            if not head.next:
                return head
        else:
            return None

        nxt = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return nxt
