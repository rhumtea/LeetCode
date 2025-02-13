# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        # let c = distance from intersection node to end
        # a moves = skipA + c + skipB 
        # b moves = skipB + c + skipA
        # a meets b at intersection => a moves == b moves 
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
            
