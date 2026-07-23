# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        res = ListNode()
        curr = res
        while temp1 or temp2:
            if temp1 and temp2:
                if temp1.val < temp2.val:
                    curr.next = temp1
                    curr = temp1
                    temp1 = temp1.next
                else:
                    curr.next = temp2
                    curr = temp2
                    temp2 = temp2.next
            elif temp1:
                curr.next = temp1
                curr = temp1
                temp1 = temp1.next
            elif temp2:
                curr.next = temp2
                curr = temp2
                temp2 = temp2.next
        return res.next


                
