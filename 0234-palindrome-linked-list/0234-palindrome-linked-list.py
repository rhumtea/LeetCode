# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = f = head
        d = ListNode(-1, head)
        t = d
        while f and f.next:
            s, f = s.next, f.next.next
            head.next = d
            d = head
            head = s
        if f: s = s.next
        a, b = d, s
        while a and b:
            if a.val == b.val: a, b = a.next, b.next
            else: return False
        return True
        