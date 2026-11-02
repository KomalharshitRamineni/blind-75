"""
92. Reverse Linked List II · https://leetcode.com/problems/reverse-linked-list-ii/
2026-11-02 · fail · 30m · skeleton: ll-dummy
O(n) time / O(1) space — Traversing through list splitting and reversing, maintaining pointers
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        def reverse(head):

            #Lets cut off the right 

            node = head
            for _ in range(right-left):
                node = node.next

            afterNode = node.next
            node.next = None
            node = afterNode


            prev, cur = None, head

            while cur:

                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            return [prev,node]

        #Reverse function is sound, how do we want therest of this funtion to work?

        dummy = ListNode()
        dummy.next = cur = head
        #So lets work with this
        prev = dummy

        #Lets just traverse this linked list
        index = 1

        while cur:

            if index == left:

                newCur,afterCur = reverse(cur)

                prev.next = newCur
                cur.next = afterCur

                prev = newCur
                cur = afterCur
                index = right + 1

            else:

                prev = cur
                cur = cur.next
                index+=1


        return dummy.next




        