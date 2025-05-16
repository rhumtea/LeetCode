# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            d = ListNode(-1, None)
            c1, c2 = list1, list2
            t = d
            while c1 and c2:
                if c1.val <= c2.val:
                    t.next = c1
                    t = c1
                    c1 = c1.next
                else:
                    t.next = c2
                    t = c2
                    c2 = c2.next
            if c1: t.next = c1
            elif c2: t.next = c2
        return d.next