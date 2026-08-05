class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #dfs algorithm with visited
        #start a DFS at each unvisited node, if it has dependendency, go into that until you reach a node with no dependency
        #the adj list here has each course and list of things that need to come first. so it's more like adj[post] -> [pre, pre]
        # if you see something twice in the recursive path, you've hit a cycle
        # if you get through all the nodes without a cycle, you're good

        # diff between visited and in path: visited means all of its dependencies are clear, you can ignore, cycle means it's in the current path and you're seeing it again. cycle means still processing, visited means fully processed

        adjList = {i: [] for i in range(numCourses)}
        visited = set()
        cycle = set()
        res = []
        for post, pre in prerequisites:
            adjList[post].append(pre)
        
        def dfs(course: int) -> bool:
            if course in visited:
                return True
            if course in cycle:
                return False
            cycle.add(course)
            for dep in adjList[course]:
                if not dfs(dep):
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        
