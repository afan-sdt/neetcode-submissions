# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        res = dummy
        carry = False
        while l1 or l2:
            val = 0
            if carry:
                val +=1
            if l1:
                val+=l1.val
                l1 = l1.next
            if l2:
                val+=l2.val
                l2 = l2.next
            if val > 9:
                val-=10
                carry = True
            else:
                carry = False
            dummy.next = ListNode(val, None)
            dummy = dummy.next
        if carry:
            dummy.next = ListNode(1, None)
        return res.next

            
