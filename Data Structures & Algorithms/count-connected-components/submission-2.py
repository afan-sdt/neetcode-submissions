class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # two arrays needed: parent and rank
        parent = [i for i in range(n)] # each node is originally parent of itself
        rank = [1] * n # each one has no children, is a component of size 1

        def find(node): # finds parent of a node:
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]] #path compression, otherwise does nothing
                res = parent[res]
            return res # this means this node is the parent of itself, i.e a root node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2: # share a parent , no union done
                return 0
            if rank[p2] > rank[p1]: #whichever has higher rank
                parent[p1] = p2
                rank[p1] += rank[p2]
            else:
                parent[p2] = p1
                rank[p2] += rank[p1]
            return 1
        res = n
        for a, b in edges:
            res -= union(a,b)
        return res
        
            


