# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # reverse from mid to end
        if not head or not head.next: return head
        def reverse(head):
            d = ListNode(-1, head)
            c = head
            while head:
                t = head
                head = head.next
                t.next = d
                d = t
            head = t
            c.next = None
            return head
        # Find middle node
        s = f = a = head
        while f and f.next:
            if s != head: a = a.next
            s, f = s.next, f.next.next
        a.next = None
        s = reverse(s)
        # # Reorder list node
        c = head
        while s:
            t = c.next
            c.next = s
            c = s
            s = t