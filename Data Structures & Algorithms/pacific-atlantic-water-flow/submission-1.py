class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = {}, {}
        res = []
        def isPacific(row: int, col: int) -> bool:
            # TODO
            print("pacific" + str(row) + str(col))
            if (row, col) in pacific:
                return pacific[(row,col)]
            else:
                pacific[(row, col)] = False
            if row == 0 or col == 0:
                pacific[(row, col)] = True
                return True
            for c, d in [(-1,0), (0,-1), (1,0), (0,1)]:
                newRow = row + c
                newCol = col + d
                if newRow >=0 and newRow < len(heights) and newCol >= 0 and newCol < len(heights[0]) and heights[newRow][newCol] <= heights[row][col]:
                    if isPacific(newRow, newCol):
                        pacific[row,col] = True
                        return True
            pacific[(row, col)] = False
            return False
        def isAtlantic(row: int, col: int) -> bool:
            # TODO
            print("atlantic" + str(row) + str(col))
            if (row, col) in atlantic:
                return atlantic[row,col]
            else:
                atlantic[(row,col)]= False
            if row == (len(heights) - 1) or col == (len(heights[0])-1):
                atlantic[(row, col)] = True
                return True
            for c, d in [(1,0), (0,1), (-1,0), (0,-1)]:
                newRow = row + c
                newCol = col + d
                if newRow >= 0 and newRow < len(heights) and newCol >= 0 and newCol < len(heights[0]) and heights[newRow][newCol] <= heights[row][col]:
                    if isAtlantic(newRow, newCol):
                        atlantic[(row, col)] = True
                        return True
            atlantic[(row, col)] = False
            return False

        for i in range(len(heights)):
            for j in range(len(heights[i])):
                print(f"outer call i: {i} j: {j}")
                if isPacific(i, j) and isAtlantic(i, j):
                    res.append([i,j])
        return res