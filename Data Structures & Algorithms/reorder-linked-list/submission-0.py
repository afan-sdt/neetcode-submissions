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
        n = len(stck)
        curr = head
        while len(stck) > n//2:
            p = stck.pop()
            p.next = curr.next
            curr.next = p
            curr = p.next
        curr.next = None