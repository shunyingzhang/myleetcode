class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = set()
        
        def dfs(r, c):
            if (r < 0 or r == rows
               or c < 0 or c == cols
               or (r, c) in visited
               or board[r][c] == 'X'):
                return
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)
        
        for i in range(1, cols - 1):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[rows - 1][i] == 'O':
                dfs(rows - 1, i)
        
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = "X"
                
        
        
#         rows = len(board)
#         cols = len(board[0])
#         visited = set()
        
#         def dfs(dr, dc):
#             if (dr < 0 or dr == rows
#                or dc < 0 or dc == cols
#                or (dr, dc) in visited
#                or board[dr][dc] == 'X'):
#                 return
#             visited.add((dr, dc))
#             dfs(dr + 1, dc)
#             dfs(dr - 1, dc)
#             dfs(dr, dc + 1)
#             dfs(dr, dc - 1)
        
#         for c in range(cols):
#             if board[0][c] == 'O' and (0, c) not in visited:
#                 dfs(0, c)
#             if board[rows - 1][c] == 'O' and (rows - 1, c) not in visited:
#                 dfs(rows - 1, c)
        
#         for r in range(1, rows - 1):
#             if board[r][0] == 'O' and (r, 0) not in visited:
#                 dfs(r, 0)
#             if board[r][cols - 1] == 'O' and (r, cols - 1) not in visited:
#                 dfs(r, cols - 1)
        
#         for r in range(1, rows -1):
#             for c in range(1, cols - 1):
#                 if (r, c) not in visited:
#                     board[r][c] = 'X'
        
#         return
        