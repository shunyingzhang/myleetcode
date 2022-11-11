class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        alt = set()
        
        def dfs(dr, dc, preH, ocean):
            if (dr < 0 or dr == rows
               or dc < 0 or dc == cols
               or (dr, dc) in ocean 
               or heights[dr][dc] < preH):
                return
            ocean.add((dr, dc))
            dfs(dr + 1, dc, heights[dr][dc], ocean)
            dfs(dr - 1, dc, heights[dr][dc], ocean)
            dfs(dr, dc + 1, heights[dr][dc], ocean)
            dfs(dr, dc - 1, heights[dr][dc], ocean)
            
        
        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows - 1][c], alt)
        
        
        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols - 1], alt)
        
        res = []
        for c in range(cols):
            for r in range(rows):
                if (r, c) in pac and (r, c) in alt:
                    res.append([r, c])
        
        return res
            