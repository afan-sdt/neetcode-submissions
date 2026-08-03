class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adjList = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            indegree[b] +=1 # a has indegree[a] prerequisites
            adjList[a].append(b) # represents the courses depending on b, indegree of those goes down when this is removed
            print("hello")

        que = deque()
        print(indegree)
        #populate with all nodes with no dependents
        for i, v in enumerate(indegree):
            if v == 0:
                que.append(i)
        res = []
        print("test")
        while que:
            curr = que.popleft()
            res.append(curr)
            for i in adjList[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    que.append(i)
        if len(res) != numCourses:
            return []
        return res[::-1]