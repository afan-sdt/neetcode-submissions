class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we want to iterate through the entire grid until there's no more moves left
        # two approaches: 
        # 1 - every minute we iterate through the whole grid
        # 2 - every minute we iterate through a list of rotting fruit
        # the time complexity is kind of the same as time goes on because 
        # the number of rotting fruit grows with time

        # i like keeping track of new rots

        #algo:
        # initialize a list with all the indexes rotten oranges 
        # loop through the list, checking all 4 directions for fresh fruits to rot
        # if there's no new rots, that means the fruits are done expanding
        #check if there's any fresh fruits left in the array
        rotted = []
        mins = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotted.append((i,j))
        
        while rotted:
            # print('minute')
            # print("rotted Count" + str((rotted)))
            # mins+=1
            newRots = []
            for x,y in rotted:
                for c,d in [(1,0), (-1, 0), (0,1), (0,-1)]:
                    if (x + c < len(grid)
                        and x + c >=0 
                        and y + d < len(grid[0])
                        and y + d >=0 
                        and grid[x+c][y+d] == 1):
                        grid[x+c][y+d] = 2
                        newRots.append((x+c, y+d))
            if newRots:
                mins+=1
            rotted = newRots
        for i in grid:
            if 1 in i:
                return -1
        return mins
                