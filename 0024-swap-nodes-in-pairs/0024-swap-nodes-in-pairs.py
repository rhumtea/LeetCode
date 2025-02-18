# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        d = ListNode(-1, head)
        c, t = d, head
        while t and t.next:
            t1 = t.next
            c.next = t1
            t.next = t1.next
            t1.next = t
            c = t
            t = c.next
        return d.next