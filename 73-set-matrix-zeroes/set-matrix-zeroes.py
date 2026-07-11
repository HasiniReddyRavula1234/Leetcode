class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 00 01 02
        # 10 11 12 
        # 20 21 22
        r = [False] * len(matrix)
        c = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r[i] = True
                    c[j] = True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if r[i] or c[j]:
                    matrix[i][j] = 0