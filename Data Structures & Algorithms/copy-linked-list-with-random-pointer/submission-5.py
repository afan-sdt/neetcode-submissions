"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        orig = head
        mappi = {None: None}
        while orig:
            mappi[orig] = Node(orig.val, None, None)
            orig = orig.next
        orig = head
        while orig:
            tmp = mappi[orig]
            tmp.next = mappi[orig.next]
            tmp.random = mappi[orig.random]
            orig = orig.next
        return mappi[head]
            

            
