# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Find 1st meet which is in cycle
        s = f = res = head
        while f and f.next:
            s, f = s.next, f.next.next
            if s == f:
                # Find 2nd meet which is result
                while s != res:
                    s, res = s.next, res.next
                return res
        