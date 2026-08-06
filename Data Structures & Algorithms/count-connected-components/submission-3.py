class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)] # each node is a parent of itself
        self.groups = n
        self.size = [1] * n
    
    def find(self, x) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) #compresses path to point directly to parent
            return self.parent[x]
        return x
    def union(self, a, b):
        aRoot = self.find(a)
        bRoot = self.find(b)
        if aRoot == bRoot:
            return
        aSize = self.size[aRoot]
        bSize = self.size[bRoot]
        if aSize > bSize:
            self.parent[bRoot] = aRoot
            self.size[aRoot] += bSize
        else:
            self.parent[aRoot] = bRoot
            self.size[bRoot] += aSize
        self.groups -= 1
    

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjointSet = DSU(n)
        for i, j in edges:
            disjointSet.union(i, j)
        return disjointSet.groups
        