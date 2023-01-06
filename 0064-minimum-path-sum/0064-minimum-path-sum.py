class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = [[float('inf')] * (cols + 1) for r in range(rows + 1)]
        res[rows - 1][cols] = 0
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                res[i][j] = grid[i][j] + min(res[i + 1][j], res[i][j + 1])
        return res[0][0]
        
  
        # dp = {}
        # def dfs(i, j, t):
        #     if (i, j, t) in dp:
        #         return dp[(i, j, t)]
        #     if ((i < rows - 1 and j == cols)
        #        or (i == rows and j < cols - 1)):
        #         return float('inf')
        #     if ((i == rows - 1 and j == cols)
        #        or (i == rows and j == cols - 1)):
        #         return t
        #     t += grid[i][j]
        #     dp[(i, j, t)] = min(dfs(i + 1, j, t), dfs(i, j + 1, t))
        #     return dp[(i, j, t)]
        # return dfs(0, 0, 0)