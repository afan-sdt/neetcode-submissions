"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        #map value to Node object
        mapping = {} 
        stax = []
        stax.append(node)
        res = []
        while stax:
            curr = stax.pop()
            mapping[curr.val] = curr
            for i in curr.neighbors:
                if i.val not in mapping:
                    stax.append(i)
        print(len(mapping))

        for i in range(len(mapping)):
            res.append(Node())
        for i in range(len(mapping)):
            res[i].val = mapping[i+1].val
            for j in mapping[i+1].neighbors:
                res[i].neighbors.append(res[j.val-1])
        return res[0]