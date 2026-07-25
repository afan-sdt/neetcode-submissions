class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate through the map 
        #if you hit a 1, increment islandCount and start a BFS
        # iterate through the 4 directions, 
        # if its within the bounds and = 1:
        #   flip the 1 to 0 , add to queue, continue
        # go until queue is empty.
        islandCount = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    #start BFS
                    islandCount += 1
                    que = deque()
                    que.append((i,j))
                    grid[i][j] = '0'
                    while que:
                        currX, currY = que.popleft()
                        if currX + 1 < len(grid) and grid[currX+1][currY] == '1':
                            grid[currX+1][currY] = 0
                            que.append((currX+1, currY))
                        if currX - 1 >= 0 and grid[currX-1][currY] == '1':
                            grid[currX-1][currY] = 0
                            que.append((currX-1, currY))
                        if currY + 1 < len(grid[0]) and grid[currX][currY+1] == '1':
                            grid[currX][currY+1] = 0
                            que.append((currX, currY+1))
                        if currY - 1 >= 0 and grid[currX][currY-1] == '1':
                            grid[currX][currY-1] = 0
                            que.append((currX, currY-1))
        return islandCount
                        