class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #kahns algorithm for bfs using indegrees
        indegrees = [0] * numCourses
        adjList = {i:[] for i in range(numCourses)}
        res = []
        for post, pre in prerequisites:
            indegrees[post] += 1
            adjList[pre].append(post) #when you remove this from the stack, all of the classes dependent lose this as dependency
        que = deque()
        for ind, val in enumerate(indegrees):
            if val == 0:
                que.append(ind)
        while que:
            curr = que.popleft()
            res.append(curr)
            for dependent in adjList[curr]:
                indegrees[dependent] -= 1
                if indegrees[dependent] == 0:
                    que.append(dependent)
        
        if len(res) != numCourses:
            return []
        return res