# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stck = []
        curr = head
        while curr:
            stck.append(curr)
            curr = curr.next
        temp = None
        curr = head
        for i in range(len(stck)//2):
            temp = curr.next
            curr.next = stck.pop()
            curr = curr.next
            curr.next = temp
            curr = curr.next
        curr.next = None