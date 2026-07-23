class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #count of islands
        count = 0

        def bfs(yIndex:int, xIndex: int):
            que = deque()
            que.append((yIndex, xIndex))
            # print(grid)
            while que:
                y, x = que.pop()
                print(x,y)
                #check all 4 sides
                if y+1 < len(grid) and grid[y+1][x] == '1':
                    grid[y+1][x] = '0'
                    que.append((y+1, x))
                if y-1 >= 0 and grid[y-1][x] == '1':
                    grid[y-1][x] = '0'
                    que.append((y-1, x))
                if x+1 < len(grid[y]) and grid[y][x+1] == '1':
                    grid[y][x+1] = '0'
                    que.append((y, x+1))
                if x-1 >= 0 and grid[y][x-1] == '1':
                    grid[y][x-1] = '0'
                    que.append((y, x-1))
            # print(grid)
        # print(grid)
        #iterate through matrix
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                # print("indices:",y,x)
                # print("value", grid[y][x])
                # if grid[y][x] == '0':
                #     # print("no island at ", y, x)
                #     continue
                if grid[y][x] == '1':
                    # print("hit island at index:", y, x)
                    count +=1
                    grid[y][x] = 0
                    bfs(y, x)
        return count
