# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# dummy node -> prev
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        prev = ListNode(-1, head)
        cur = head
        while cur:
            ne = cur.next
            cur.next = prev
            prev = cur
            cur = ne
        head.next = None
        return prev    