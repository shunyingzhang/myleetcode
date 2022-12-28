class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
        rows = len(grid)
        cols = len(grid[0])
        
        MaxIsl = 0
        visited = set()
        
        def dfs(r, c):
            island = 0
            nonlocal rows, cols
            if (r < 0 or r == rows 
               or c < 0 or c == cols
               or grid[r][c] == 0
               or (r, c) in visited):
                return 0
            
            visited.add((r, c))
            island += 1
            return island + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = dfs(i, j)
                    MaxIsl = max(MaxIsl, area)
        
        return MaxIsl
        
        
        
#         if not grid:
#             return 0
        
#         rows = len(grid)
#         cols = len(grid[0])
#         MaxArea = 0
#         visited = set()
        
#         def search(gr, gc):
#             area = 1
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
#                          and grid[r][c] == 1 
#                          and (r, c) not in visited):
#                         area += 1
#                         q.append((r, c))
#                         visited.add((r, c))
#             return area
                     
        
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == 1 and (i, j) not in visited:
#                     area = search(i, j)
#                     MaxArea = max(area, MaxArea)
                    
                
#         return MaxArea