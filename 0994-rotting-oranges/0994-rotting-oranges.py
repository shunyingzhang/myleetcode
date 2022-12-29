class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = collections.deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])
        
        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while fresh and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    
                    if (r + dr >= 0 and r + dr < rows
                        and c + dc >= 0 and c + dc < cols
                        and grid[r + dr][c + dc] == 1):
                        grid[r + dr][c + dc] = 2
                        q.append([r + dr, c + dc])
                        fresh -= 1
            time += 1
        
        if fresh:
            return -1
        return time
        
        
        
#         rows = len(grid)
#         cols = len(grid[0])
#         fresh = 0
#         time = 0
#         q = collections.deque()
        
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1:
#                     fresh += 1
#                 if grid[r][c] == 2:
#                     q.append([r, c])
        
#         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
#         while fresh > 0 and q:
#             time += 1
            
#             for i in range(len(q)):
#                 qr, qc = q.popleft()
#                 for dr, dc in directions:
#                     r = qr + dr
#                     c = qc + dc
                 
#                     if (r >= 0 and r < rows 
#                         and c >= 0 and c <  cols
#                         and grid[r][c] == 1):
#                         grid[r][c] = 2
#                         q.append([r, c])
#                         fresh -= 1
        
#         return -1 if fresh else time 