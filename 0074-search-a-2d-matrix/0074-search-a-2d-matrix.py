class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u = 0
        d = len(matrix) - 1
        
        while u <= d:
            row = (u + d) // 2
            if matrix[row][len(matrix[row]) - 1] < target:
                u = row + 1
            elif matrix[row][0] > target:
                d = row - 1
            else:
                break
                
        row = (u + d) // 2
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            m = (l +  r) // 2
            if matrix[row][m] > target:
                r = m -1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        
        return False
        
        
        
        
        
        
#         u = 0
#         d = len(matrix) - 1
        
#         while u < d:
#             m = (u + d) // 2
#             if target > matrix[m][len(matrix[m]) - 1]:
#                 u = m + 1
#             elif target < matrix[m][0]:
#                 d = m -1
#             else:
#                 break
                
#         row = (u + d) // 2
#         l = 0
#         r = len(matrix[row]) - 1
#         while l <= r:
#             m = (r + l) // 2
#             if target > matrix[row][m]:
#                 l = m + 1
#             elif target < matrix[row][m]:
#                 r = m - 1
#             else:
#                 return True
        
#         return False
                
        
        