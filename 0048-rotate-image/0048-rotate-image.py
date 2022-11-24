class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                r = i
                c = j
                tmp = matrix[r][c]
                for k in range(4):
                    tmpr = r
                    r = c
                    c = n - 1 - tmpr
                    tmpNext = matrix[r][c]
                    matrix[r][c] = tmp
                    tmp = tmpNext
                    
                    
                
        
        
            
        