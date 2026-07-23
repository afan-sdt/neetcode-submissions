class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #traverse each row
        for i in range(len(board)): #iterate through rows
            arr = [False]*10
            for j in range(len(board[i])):
                ch = board[i][j]
                if ch == '.':
                    continue
                if arr[int(ch)]:
                    return False
                arr[int(ch)] = True
        
        #traverse each column
        for j in range(len(board[0])):
            arr = [False] * 10
            for i in range(len(board)):
                ch = board[i][j]
                if ch == '.':
                    continue
                if arr[int(ch)]:
                    return False
                arr[int(ch)] = True
        #traverse each box individually
        for i in range(0,9,3):
            for j in range(0,9,3):
                arr=[False]*10
                for k in range(0,3,1):
                    for l in range(0,3,1):
                        ch = board[i+k][j+l]
                        if ch == '.':
                            continue
                        if arr[int(ch)]:
                            return False
                        arr[int(ch)] = True
        return True


        