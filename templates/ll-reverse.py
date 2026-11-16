"""
ll-reverse — in-place link rewiring

Trigger: you are *rewriting* the links of a list you already have — reverse the whole thing, reverse a segment, reverse in groups, or reverse half of it to compare. You walk one pointer forward and leave a trail of back-pointers behind it. The whole list needs no dummy; a stretch inside the list needs a dummy and a pointer on the node before it, then a reconnect. Complexity: O(n) / O(1)
"""

def reverse_list(head):
      prev, cur = None, head
      while cur:
              nxt = cur.next      # save it FIRST -- the next line destroys this link
              cur.next = prev     # the reversal itself
              prev = cur          # then walk both forward, in this order
              cur = nxt
      return prev             # cur is None here; prev is the new head


def reverse_stretch(before, after):
      # a stretch inside the list: the nodes strictly between before and after
      start = before.next         # the stretch's front now, its back once reversed
      prev, cur = after, start    # start prev at after, so the new back links on to the rest
      while cur is not after:
              nxt = cur.next
              cur.next = prev
              prev = cur
              cur = nxt
      before.next = prev          # reconnect: before -> the stretch's new front
      return start                # the new back: the "before" of the next stretch

# dummy = ListNode(0, head); before = dummy   (a dummy, in case the stretch starts at the head)
# before = reverse_stretch(before, after)     (move before to the new back after each stretch)
# return dummy.next
