class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        island = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r, c):
            nonlocal rows, cols
            if (r < 0 or r == rows 
               or c < 0 or c == cols
               or grid[r][c] == '0'
               or (r, c) in visited):
                return 
            
            visited.add((r, c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    island += 1
        
        return island
        
        
        
        
#         if not grid:
#             return 0
        
#         rows = len(grid)
#         cols = len(grid[0])
#         island = 0
#         visited = set()
        
#         def search(gr, gc):
#             q = collections.deque()
#             q.append((gr, gc))
#             visited.add((gr, gc))
            
#             while q:
#                 row, col = q.popleft()
#                 directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#                 for dr, dc in directions:
#                      r = row + dr
#                      c = col + dc
#                      if (r in range(rows) 
#                          and c in range(cols) 
#                          and grid[r][c] == "1" 
#                          and (r, c) not in visited):
#                         q.append((r, c))
#                         visited.add((r, c))
                     
        
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == "1" and (i, j) not in visited:
#                     search(i, j)
#                     island += 1
                
#         return island
                    
        
        