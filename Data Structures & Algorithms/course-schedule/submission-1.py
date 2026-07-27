class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for crs, req in prerequisites:
            adjList[crs].append(req) # represents the list of courses crs depends on
            indegree[req] += 1 # represents the number of courses this depends on
        
        que = deque()
        for index, indeg in enumerate(indegree):
            if indeg == 0:
                que.append(index)
        finished = 0
        while que:
            curr = que.popleft()
            finished+=1
            for nei in adjList[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    que.append(nei)
        return finished == numCourses