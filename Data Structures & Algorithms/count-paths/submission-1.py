class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def paths(x, y):
            if x >= m or y >=n:
                return 0
            if (x,y) in memo:
                return memo[(x,y)]
            if x == m-1 and y == n-1:
                return 1
            
            memo[(x,y)] = paths(x+1, y) + paths(x, y+1)
            return memo[(x,y)]
        return paths(0,0)
        