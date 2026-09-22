class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #CARIT
        # clarify, approach, runtime, implement, test
        # which of the pair is the prerequisite? which happens second?
        # for the indegrees, we want to know dependencies. How many dependencies does x have
        
        #approach: 
        # 1) count number of indegrees (how many dependencies does this course have) and create adjacency list
        # 2) add all things with a 0 to queue of "eligible" courses. This means all of its prereqs have been fulfilled
        # 3) while there are elements in the que:
            # add them to result array, go through all of its courses that depend on it, decrement the indegree, if indegree is 0, add to que
        # if res array = numCourses, return res, else []
        
        # QUESTION: how does indegrees approach handle cycles? there will still be elements not added to res bc they will have unfulfilled dependencies. this will be the circular dependency
        # are there circular dependencies? shouldn't be because we add everything to the array once

        indegrees = [0] * numCourses
        adjList = {i: [] for i in range(numCourses)}
        res = []
        q = deque()
        for post, pre in prerequisites:
            indegrees[post] += 1
            adjList[pre].append(post)
        
        for i, v in enumerate(indegrees):
            if v == 0:
                q.append(i)
        while q:
            curr = q.popleft()
            res.append(curr)
            for dep in adjList[curr]:
                indegrees[dep] -=1
                if indegrees[dep] == 0:
                    q.append(dep)
        return res if len(res) == numCourses else []

