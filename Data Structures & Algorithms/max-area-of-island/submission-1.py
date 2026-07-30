class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        #iterate through
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # found land, do a BFS
                if grid[i][j] == 1: 
                    area = 0
                    que = deque()
                    que.append((i,j))
                    grid[i][j] = 0
                    while que:
                        # check all directions
                        x, y = que.pop()
                        area += 1
                        for c, d in [(1,0), (0,1), (-1, 0), (0,-1)]:
                            if x + c < len(grid) and x + c >= 0 and y + d < len(grid[i]) and y+d >=0 and grid[x+c][y+d] == 1:
                                grid[x+c][y+d] = 0
                                que.append((x+c, y+d))
                    maxArea = max(maxArea, area)
        return maxArea
                    