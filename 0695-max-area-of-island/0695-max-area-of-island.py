class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        MaxArea = 0
        visited = set()
        
        def search(gr, gc):
            area = 1
            q = collections.deque()
            q.append((gr, gc))
            visited.add((gr, gc))
            
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                     r = row + dr
                     c = col + dc
                     if (r in range(rows) 
                         and c in range(cols) 
                         and grid[r][c] == 1 
                         and (r, c) not in visited):
                        area += 1
                        q.append((r, c))
                        visited.add((r, c))
            return area
                     
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = search(i, j)
                    MaxArea = max(area, MaxArea)
                    
                
        return MaxArea