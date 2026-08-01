class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # we want to iterate until we hit a treasure chest (curr = 0)
        # when we hit a chest we start a BFS 
        # each neighbor we mark is as min(this + 1, current value)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    #start a BFS
                    que = deque()
                    que.append((i,j))
                    currDist = 0
                    while que:
                        lev = []
                        while que:
                            lev.append(que.popleft())
                        for x, y in lev:
                            for c, d in [(1,0),(0,1), (-1, 0), (0,-1)]:
                                if x + c < len(grid) and x + c >= 0 and y+d < len(grid[i]) and y+d >= 0 and grid[x+c][y+d] > (currDist + 1):
                                    grid[x+c][y+d] = min(grid[x+c][y+d], currDist + 1)
                                    que.append((x+c, y+d))
                        currDist+=1