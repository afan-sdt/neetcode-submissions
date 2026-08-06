class DSU:
    def __init__(self, n: int):
        self.groups = n
        self.parent = [i for i in range(n)] #initialize each parent to be itself
        self.size = [1] * n #each node initializes to size 1

    def find(self, x: int) -> int: #takes in a node number and returns its parent
        if self.parent[x] != x:
           self.parent[x] = self.find(self.parent[x]) # path compression
           return self.parent[x]
        return x
    
    def union(self, a: int, b: int) -> bool: # takes in two nodes and makes them part of the same group
        aRoot = self.find(a)
        bRoot = self.find(b)
        if aRoot == bRoot:
            return False
        if self.size[aRoot] > self.size[bRoot]:
            self.parent[bRoot] = aRoot
            self.size[aRoot] += self.size[bRoot]
        else:
            self.parent[aRoot] = bRoot
            self.size[bRoot] += self.size[aRoot]
        self.groups -= 1
        return True
    def numGroups():
        return self.groups
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            print("not right num of edges")
            return False
        disjointSet = DSU(n)
        for i, j in edges:
            if not disjointSet.union(i,j):
                print(f"union failed {i} and {j}")
                return False
        print(disjointSet.groups)
        return disjointSet.groups == 1
