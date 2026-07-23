class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # this has to do with game state and maintaining valid game state
        # for every row, there is a 9 sized array
        rows = [[ 0 for _ in range(9)] for _ in range(9)]
        cols = [[0 for _ in range(9)] for _ in range(9) ]
        sqrs = [[0 for _ in range(9)] for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]
                if val == '.':
                    continue
                val = int(val) - 1
                if rows[i][val] == 1:
                    print("break row")
                    return False
                else:
                    rows[i][val] = 1
                if cols[j][val] == 1:
                    print("break col")
                    return False
                else:
                    cols[j][val] = 1
                currSquare = i//3 + ((j//3) * 3)
                if sqrs[currSquare] [val] == 1:
                    print("break squares i:" + str(i) + ' j:' + str(j) + ' square:' + str(currSquare))
                    return False
                else:
                    sqrs[currSquare][val] = 1
        return True

