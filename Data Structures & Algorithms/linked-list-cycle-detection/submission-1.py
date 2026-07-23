# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        if not temp.next:
            return False
        temp2 = temp.next
        while temp and temp2:
            if temp == temp2:
                return True
            temp = temp.next;
            temp2 = temp2.next
            if temp2:
                temp2 = temp2.next
            else:
                return False
        return False
        

            