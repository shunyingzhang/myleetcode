class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        alt = set()        
        
        def dfs(r, c, prev, ocean):
            if (r < 0 or r == rows
               or c < 0 or c == cols
               or (r, c) in ocean
               or heights[r][c] < prev):
                return
            
            ocean.add((r, c))
            dfs(r + 1, c, heights[r][c], ocean)
            dfs(r - 1, c, heights[r][c], ocean)
            dfs(r, c + 1, heights[r][c], ocean)
            dfs(r, c - 1, heights[r][c], ocean)            
        
        for i in range(rows):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, cols - 1, heights[i][cols - 1], alt) 
        
        for i in range(cols):
            dfs(0, i,  heights[0][i], pac)
            dfs(rows - 1, i, heights[rows - 1][i], alt) 
        
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in alt:
                    res.append([i, j])
        
        return res
        
#         rows = len(heights)
#         cols = len(heights[0])
#         pac = set()
#         alt = set()
        
#         def dfs(dr, dc, preH, ocean):
#             if (dr < 0 or dr == rows
#                or dc < 0 or dc == cols
#                or (dr, dc) in ocean 
#                or heights[dr][dc] < preH):
#                 return
#             ocean.add((dr, dc))
#             dfs(dr + 1, dc, heights[dr][dc], ocean)
#             dfs(dr - 1, dc, heights[dr][dc], ocean)
#             dfs(dr, dc + 1, heights[dr][dc], ocean)
#             dfs(dr, dc - 1, heights[dr][dc], ocean)
            
        
#         for c in range(cols):
#             dfs(0, c, heights[0][c], pac)
#             dfs(rows - 1, c, heights[rows - 1][c], alt)
        
        
#         for r in range(rows):
#             dfs(r, 0, heights[r][0], pac)
#             dfs(r, cols - 1, heights[r][cols - 1], alt)
        
#         res = []
#         for c in range(cols):
#             for r in range(rows):
#                 if (r, c) in pac and (r, c) in alt:
#                     res.append([r, c])
        
#         return res
            