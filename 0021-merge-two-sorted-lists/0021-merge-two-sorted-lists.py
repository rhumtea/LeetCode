# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = list1, list2
        if list1 == None: return list2
        elif list2 == None: return list1
        if c1.val <= c2.val: d = ListNode(-1, list1)
        else: d = ListNode(-1, list2)
        temp = d
        while c1 and c2:
            if c1.val <= c2.val:
                temp.next = c1
                temp = c1
                c1 = c1.next
            else:
                temp.next = c2
                temp = c2
                c2 = c2.next
        if c1: temp.next = c1
        elif c2: temp.next = c2
        return d.next