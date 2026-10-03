"""
ll-reverse — in-place pointer reversal

Trigger: you are *rewriting* the links of a list you already have — reverse the whole thing, reverse a segment, reverse in groups, or reverse half of it to compare. No dummy: you walk one pointer forward and leave a trail of back-pointers behind it. Complexity: O(n) / O(1)
"""

def reverse_list(head):
      prev, cur = None, head
      while cur:
              nxt = cur.next      # save it FIRST -- the next line destroys this link
              cur.next = prev     # the reversal itself
              prev = cur          # then walk both forward, in this order
              cur = nxt
      return prev             # cur is None here; prev is the new head
