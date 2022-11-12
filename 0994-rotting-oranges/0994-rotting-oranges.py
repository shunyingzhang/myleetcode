class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        time = 0
        q = collections.deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while fresh > 0 and q:
            time += 1
            # if time == 1:
            #     return q
            
            for i in range(len(q)):
                qr, qc = q.popleft()
                # if time == 1 and i == 0:
                #     return r, c
                for dr, dc in directions:
                    r = qr + dr
                    c = qc + dc
                 
                    if (r >= 0 and r < rows 
                        and c >= 0 and c <  cols
                        and grid[r][c] == 1):
                        grid[r][c] = 2
                        q.append([r, c])
                        fresh -= 1
                        # if time == 1 and i == 0:
                        #      return fresh
        
        return -1 if fresh else time 