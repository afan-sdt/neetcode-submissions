"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create a dictionary that maps each node index to its neighbors indices
        # indexNeighbor {index: [neighbors indices]}
        # we create this by traversing the node tree using DFS and visited
        # visited = set() i think we don't need this bc indexMapping will serve as our visited
        if not node:
            return None
        indexMapping = {}
        stck = [] # stck contains nodes that need to be visited
        stck.append(node)
        while stck:
            curr = stck.pop()
            indexMapping[curr.val] = []
            if curr.neighbors:
                for neigh in curr.neighbors:
                    if neigh.val not in indexMapping:
                        stck.append(neigh)
                    indexMapping[curr.val].append(neigh.val)
        print(indexMapping)

        
        #then create an array of new nodes of size of prev dictionary
        #iterate through the array and assign the neighbors of each node to the appropriate node in this dictionary
        # for i in range(newNodesArray):
        # newNodes[i].neighbors.append(newNodes[indexNeighbor[i][j]])
        #return newNodes[node.val]
        newNodes = {}
        for i in range(1, len(indexMapping)+1):
            newNodes[i] = Node(i)
        for i in range(1, len(indexMapping)+ 1):
            for n in indexMapping[i]:
                newNodes[i].neighbors.append(newNodes[n])
        return newNodes[node.val]

        