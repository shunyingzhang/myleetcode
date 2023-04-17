class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        pre0 = grid[0].copy()
        pre1 = grid[1].copy()
        
        for i in range(1, N):
            pre0[i] += pre0[i - 1]
            pre1[i] += pre1[i - 1]
            
        res = float(inf)
        for i in range(N):
            row0 = pre0[-1] - pre0[i]
            row1 = pre1[i - 1] if i > 0 else 0
            
            secondRobot = max(row0, row1)
            
            res = min(res, secondRobot)
            
        return res
        