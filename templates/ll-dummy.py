"""
ll-dummy — dummy head, building a list you return

Trigger: you are *producing* a list — merging, partitioning, splitting, deleting nodes. Reach for a dummy whenever the head itself might change, so "attach the first node" and "attach the tenth" become the same line and head-handling stops being a special case. Complexity: O(n) / O(1)
"""


def build_list(list1, list2):
      dummy = tail = ListNode()       # sentinel: now "attach the first" == "attach the nth"
      while list1 and list2:
              if foo(list1, list2):       # which source wins this step
                      tail.next = list1
                      list1 = list1.next
              else:
                      tail.next = list2
                      list2 = list2.next
              tail = tail.next            # advance the tail every iteration
      tail.next = list1 or list2      # one list is non-empty -- attach the remainder
      return dummy.next               # dummy.next, NOT dummy
