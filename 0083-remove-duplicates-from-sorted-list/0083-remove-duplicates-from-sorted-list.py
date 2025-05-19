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
        t = c.next
        while t:
            if c.val == t.val:
                t = t.next
                c.next = t
            else:
                c = c.next
                t = t.next
        return head