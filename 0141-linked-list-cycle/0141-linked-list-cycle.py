# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c = t = head
        while t and t.next:
            c = c.next
            t = t.next.next
            if c == t:
                return True
        return False