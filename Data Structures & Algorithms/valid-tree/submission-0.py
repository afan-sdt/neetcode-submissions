class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #connected and no cycles,  do a DFS from a node and see if you can reach every node
        # how do we check if connected? keep track of visited, if all nodes visited, connected
        # for cycle, dfs + parent tracking, if it's visited and not parent, cycle
        
        if len(edges) != n-1 : # if more, cycle. if less, not connected
            return False
        adj = {i:[] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = set()
        
        def dfs(node: int, parent: int) -> bool:
            # if node in visited and node != parent:
            #     print(f"cycle detected {node} + {parent}")
            #     print(f"visited arr:{visited}")
            #     return False # cycle detected
            if node in visited and node == parent:
                return True
            visited.add(node)
            for i in adj[node]:
                if i in visited and i == parent:
                    continue
                if i in visited and i!= parent:
                    return False
                if not dfs(i, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        print(visited)
        return len(visited) == n

