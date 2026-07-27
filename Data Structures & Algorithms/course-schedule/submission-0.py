class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize prereq dictionary to empty arrays
        preMap = {i:[] for i in range(numCourses)}
        for i, j in prerequisites:
            preMap[i].append(j) #course i needs course j
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if len(preMap[crs]) == 0:
                return True
            visited.add(crs)
            for i in preMap[crs]:
                if not dfs(i):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True