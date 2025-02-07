# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None: return None
        d = ListNode(-1, head)
        a = d
        cur = head
        for i in range(n):
            cur = cur.next
        temp = head
        while cur:
            cur = cur.next
            temp = temp.next
            a = a.next
        a.next = temp.next
        return d.next