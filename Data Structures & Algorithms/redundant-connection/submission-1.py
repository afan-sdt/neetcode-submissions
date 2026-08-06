class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # if we do union find and find the first union that doesn't join two groups, we have our edge
        # in a fully connected graph, edges = n-1 where n is nodes. in this case the number
        # of edges is n because there's a redundant edge
        parent = [i for i in range(len(edges))]
        size = [1] * len(edges)

        def find(x) -> int: # finds the parent/representative of a node
            if parent[x] != x:
                parent[x] = find(parent[x])
                return parent[x]
            return x
        def union(a, b) -> bool:
            aRoot = find(a)
            bRoot = find(b)
            if aRoot == bRoot:
                return False
            
            if size[aRoot] > size[bRoot]:
                parent[bRoot] = aRoot
                size[aRoot] += size[bRoot]
            else:
                parent[aRoot] = bRoot
                size[bRoot] += size[aRoot]
            return True
        
        for i, j in edges:
            if not union(i-1,j-1):
                return [i,j]
        return []
        
