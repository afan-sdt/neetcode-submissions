class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # traverse through array until you hit the first letter of the word
        # res = False
        def search(y: int, x: int, rest: str) -> bool:
            print("searching", rest)
            if rest == "":
                return True
            if y+1 < len(board) and board[y+1][x] == rest[0]:
                #need to flip that letter to # and revert it back after traversal
                board[y+1][x] = '#'
                if search(y+1, x, rest[1:]):
                    return True
                board[y+1][x] = rest[0]
            if y-1 >= 0 and board[y-1][x] == rest[0]:
                board[y-1][x] = '#'
                if search(y-1, x, rest[1:]):
                    return True
                board[y-1][x] = rest[0]
            if x+1 < len(board[y]) and board[y][x+1]== rest[0]:
                board[y][x+1] = '#'
                if search(y, x+1, rest[1:]):
                    return True
                board[y][x+1] = rest[0]
            if x-1 >= 0 and board[y][x-1]== rest[0]:
                board[y][x-1] = '#'
                if search(y, x-1, rest[1:]):
                    return True
                board[y][x-1] = rest[0]
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    board[i][j] = '#'
                    if search(i, j, word[1:]):
                        return True
                    board[i][j] = word[0]
        return False