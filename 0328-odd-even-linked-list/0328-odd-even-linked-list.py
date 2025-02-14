# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        a1 = a2 = head
        b1 = b2 = t = head.next
        while b1 and b1.next:
            a2 = a2.next.next
            b2 = b2.next.next
            a1.next = a2
            a1 = a2
            b1.next = b2
            b1 = b2
        a1.next = t
        return head