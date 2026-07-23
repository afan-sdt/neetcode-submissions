# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        speed1 = head
        speed2 = head.next
        while speed1 and speed2:
            if speed1 == speed2:
                return True
            speed1 = speed1.next
            if not speed1:
                return False
            speed2 = speed2.next
            if not speed2:
                return False
            speed2 = speed2.next
        return False