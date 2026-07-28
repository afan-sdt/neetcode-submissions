class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges) +1
        parent = [i for i in range(N)]
        rank = [1] * N
        def find(node):
            if node == parent[node]:
                return parent[node]
            parent[node] = parent[parent[node]]
            return find(parent[node])
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False # cycle detected
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1,e2]
        return []