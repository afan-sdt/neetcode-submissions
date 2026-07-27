class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = [[] for _ in range(numCourses)]
        for crs, req in prerequisites:
            prereqs[crs].append(req)
        
        cycle, visited = set(), set()
        output = []

        def dfs(crs):
            # base cases
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for i in prereqs[crs]:
                if not dfs(i):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output