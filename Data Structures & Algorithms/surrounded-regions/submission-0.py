class Solution:
    def solve(self, board: List[List[str]]) -> None:

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    # begin BFS
                    que = deque()
                    que.append((i,j))
                    indices = []
                    enclosed = True #enclosed until it hits the end
                    while que:
                        x, y = que.popleft()
                        indices.append((x,y))
                        if x == (len(board) -1) or x == 0 or y ==(len(board[0])-1) or y == 0:
                            enclosed = False 
                        #check neighbors
                        for c, d in [(1,0), (0,1), (-1,0), (0, -1)]:
                            if x+c >= 0 and x+c < len(board) and y+d >=0 and y+d < len(board[0]) and board[x+c][y+d] == 'O':
                                board[x+c][y+d] = 'T'
                                que.append((x+c, y+d))
                    if enclosed:
                        for a, b in indices:
                            board[a][b] = 'X'
                    else:
                        for a, b in indices:
                            board[a][b] = 'O'
