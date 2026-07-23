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
        oldToCopy = {}
        oldToCopy[None] = None
        orig = head
        while orig:
            oldToCopy[orig] = Node(orig.val, None, None)
            orig = orig.next
        orig = head
        while orig:
            oldToCopy[orig].next = oldToCopy[orig.next]
            oldToCopy[orig].random = oldToCopy[orig.random]
            orig = orig.next
        return oldToCopy[head]
            

            
