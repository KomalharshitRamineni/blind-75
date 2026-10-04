"""
tp-fast-slow — fast/slow pointers

Trigger: cycle detection in a linked list · find the middle · find a duplicate by treating the array as a linked list. Complexity: O(n) / O(1)
"""

  

def tp_fast_slow(head):

	fast, slow = head, head
	
	while fast and fast.next:
		
		fast = fast.next.next
		slow = slow.next
	
		if fast == slow:
			return True
	
	return False
