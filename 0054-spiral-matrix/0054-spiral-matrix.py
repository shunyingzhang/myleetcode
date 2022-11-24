class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bott = len(matrix)
        res = []

        while left < right and top < bott:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bott):
                res.append(matrix[i][right - 1])
            right -= 1
                
            if top >= bott or left >= right:
                break
    
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bott - 1][i])
            bott -= 1
            
            for i in range(bott - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res
    
       
        
        
            
            
        
        