class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # CARIT: clarify, approach, runtime, implement, test

        # union find and the result is the number of components (different parents)
        parent = [x for x in range(n)]
        size = [1] * n

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a] # base case where parents[a] =
        def union(x, y):
            parentX = find(x)
            parentY = find(y)

            if parentX == parentY:
                return False # same parent already
            
            if size[parentX] > size[parentY]:
                parent[parentY] = parentX
                size[parentX] += size[parentY]
            else:
                parent[parentX] = parentY
                size[parentY] += size[parentX]
            return True
        
        for n1, n2 in edges:
            union(n1, n2)
        res = set()
        for i in range(n):
            res.add(find(i))
        return len(res)