class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        visited = set()

        
        def dfs2(r, c):
            nonlocal rows, cols
            if (r < 0 or r == rows
               or c < 0 or c == cols
               or (r, c) in visited
               or grid2[r][c] == 0):
                return True
            
            if grid1[r][c] != 1:
                return False
            
            visited.add((r, c))
            res = True
            res = dfs2(r + 1, c) and res
            res = dfs2(r - 1, c) and res
            res = dfs2(r, c + 1) and res
            res = dfs2(r, c - 1) and res
            return res
         
        
        sub = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid1[i][j] == 1 and (i, j) not in visited:
                    if dfs2(i, j):
                        sub += 1
        
        return sub
                        
            
        