class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m00 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        m00 = 0
                    else:
                        matrix[i][0] = 0
        
        
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                 for j in range(1, len(matrix)):
                    matrix[j][i] = 0

        if m00 == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
                