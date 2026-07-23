# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        temp = res
        p1, p2, = list1, list2
        while p1 != None or p2 != None:
            if p1 != None and p2 != None and p1.val <= p2.val:
                temp.next = p1
                p1 = p1.next
            elif p1 != None and p2 != None:
                temp.next = p2
                p2 = p2.next
            elif p1 != None:
                temp.next = p1
                p1 = p1.next
            elif p2 != None:
                temp.next = p2
                p2 = p2.next
            temp = temp.next
        return res.next