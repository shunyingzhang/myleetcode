class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1):
            tmp = row
            for j in range(n - 2, -1, -1):
                tmp[j] = row[j] + tmp[j + 1]
            row = tmp
        return row[0]
        
        
        
        
        
#         row = [1] * n
        
#         for i in range (m - 1):
#             newRow = [1] * n
#             for j in range(n - 2, -1, -1):
#                 newRow[j] = row[j] + newRow[j + 1]
            
#             row = newRow
        
#         return row[0]
        