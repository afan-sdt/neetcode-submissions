class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #we iterate through the grid
        #once we hit the first letter, we start a dfs at that location
        # the dfs needs the current position and letter index
        # if one of the neighbors is the next character, we recurse
        def dfs(x, y, index):
            if index == len(word):
                return True
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                if x + dx >= 0 and x + dx < len(board) and y + dy >= 0 and y + dy < len(board[0]):
                    if board[x + dx][y+dy] == word[index]:
                        board[x+dx][y+dy] = '/'
                        if dfs(x+dx, y+dy, index + 1):
                            return True
                        board[x+dx][y+dy] = word[index]
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = '/'
                    if dfs(i, j, 1):
                        return True
                    board[i][j] = word[0]
        return False 