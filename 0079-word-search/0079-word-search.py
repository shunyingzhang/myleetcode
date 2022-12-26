class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        path = set()
        
        def dfs(i, j, k):
            if k == len(word):
                return True
            
            if (i < 0 or i >= rows 
               or j < 0 or j >= cols
                or board[i][j] != word[k]
               or (i, j) in path):
                return False
            
            path.add((i, j))
            
            res = (dfs(i + 1, j, k + 1)
                  or dfs(i - 1, j, k + 1)
                  or dfs(i, j + 1, k + 1)
                  or dfs(i, j - 1, k + 1))
            path.remove((i, j))
            
            return res
        
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
        
        
        
        
        
#         rows = len(board)
#         cols = len(board[0])
#         path = set()
        
#         def dfs(r, c, k):
#             if k == len(word):
#                 return True
#             if (r < 0 or c< 0 
#                 or r >= rows or c >= cols 
#                 or board[r][c] != word[k] 
#                 or (r, c) in path):
#                 return False
            
#             path.add((r, c))
#             res = (dfs(r + 1, c, k + 1) or 
#             dfs(r - 1, c, k + 1) or
#             dfs(r, c + 1, k + 1) or
#             dfs(r, c - 1, k + 1))
#             path.remove((r, c))
            
#             return res
        
        
#         for i in range(rows):
#             for j in range(cols):
#                 if dfs(i, j, 0):
#                     return True
        
#         return False
        
        
        
        