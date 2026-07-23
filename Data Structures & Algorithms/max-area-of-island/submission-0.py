class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def bfs(yIndex: int, xIndex: int)->int:
            count = 0
            que = deque()
            que.append((yIndex, xIndex))
            while que:
                y, x = que.pop()
                count += 1
                #check above
                if y+1 < len(grid) and grid[y+1][x] == 1:
                    grid[y+1][x] = 0
                    que.append((y+1,x))
                #check below
                if y-1 >= 0 and grid[y-1][x] == 1:
                    grid[y-1][x] = 0
                    que.append((y-1,x))
                #check right
                if x+1 < len(grid[y]) and grid[y][x+1] == 1:
                    grid[y][x+1] = 0
                    que.append((y,x+1))
                #check left
                if x-1 >= 0 and grid[y][x-1] == 1:
                    grid[y][x-1] = 0
                    que.append((y,x-1))
            return count
        #iterate through matrix
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    grid[y][x] = 0
                    maxArea = max(bfs(y,x), maxArea)
        return maxArea