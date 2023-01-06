class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxlen = 0
        for i in range(len(matrix[0]) - 1, -1, -1):
            if matrix[len(matrix) - 1][i] == '1':
                maxlen = 1
                break
        for i in range(len(matrix) - 1, -1, -1):
            if matrix[i][len(matrix[0]) - 1] == '1':
                maxlen = 1
                break
        for i in range(len(matrix) -2, -1, -1):
            for j in range(len(matrix[0]) - 2, -1, -1):
                if matrix[i][j] == '1':
                    matrix[i][j] = str(int(matrix[i][j]) + 
                                      min(int(matrix[i][j + 1]), int(matrix[i + 1][j]), 
                                          int(matrix[i + 1][j + 1])))
                    maxlen = max(maxlen, int(matrix[i][j]))
        return maxlen ** 2
        