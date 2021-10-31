class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.set_zeroes(i, j, matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == None:
                    matrix[i][j] = 0

    def set_zeroes(self, i, j, matrix):
        for ix in range(len(matrix[0])):
            if matrix[i][ix] != 0:
                matrix[i][ix] = None

        for jx in range(len(matrix)):
            if matrix[jx][j] != 0:
                matrix[jx][j] = None
