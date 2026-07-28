class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # need to create a union find structure
        # honestly for this, all we need is to see if they all have the same root
        # we can create a hashmap of size n
        # each entry corresponds to its root/head node
        # in the beginning, each node points to itself.
        #when an edge is found, we take the minimum of the two and make it the root
        # to find the root we dfs into the list until root[x] = x this makes it the root node
        # at the end, we return how many elements in the array have a root of themselves
        adjList = {i: [] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in adjList[node]:
                dfs(i)
        res = 0
        for i in range(n):
            # for each element, we want to dfs, marking visited nodes as visited
            if i not in visited:
                res += 1
                dfs(i)
        return res