class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if (r < 0 or r == n
               or c < 0 or c == n
               or (r, c) in visited
               or grid[r][c] == 0):
                return
            visited.add((r, c))
            for d in directions:
                dfs(r + d[0], c + d[1])
                
        def bfs():   
            q = deque(visited)
            bridge = 0
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for d in directions:
                        dr = r + d[0]
                        dc = c + d[1]
                        if (0 <= dr <n
                           and 0 <= dc < n
                           and (dr, dc) not in visited
                           and grid[dr][dc] == 0):
                            q.append([dr, dc])
                            visited.add((dr, dc))
 
                        elif (0 <= dr <n
                           and 0 <= dc < n
                           and (dr, dc) not in visited
                           and grid[dr][dc] == 1):
                            return bridge
                bridge += 1
            
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs()
        
        
        