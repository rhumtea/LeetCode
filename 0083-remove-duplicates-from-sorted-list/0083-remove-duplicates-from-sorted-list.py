# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        c = head
        while c.next.next:
            if c.val == c.next.val:
                t = c.next.next
                c.next = t
            else:
                c = c.next
        if c.val == c.next.val:
            c.next = None
        return head
