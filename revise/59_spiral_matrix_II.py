class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for i in range(n)]
        return self.dfs(0, 0, matrix, False, 1)

    def dfs(self, i, j, matrix, goUp, num):

        if self.is_valid(i, j, matrix):
            matrix[i][j] = num
            if goUp:
                self.dfs(i - 1, j, matrix, True, num + 1)
            self.dfs(i, j + 1, matrix, False, num + 1)
            self.dfs(i + 1, j, matrix, False, num + 1)
            self.dfs(i, j - 1, matrix, False, num + 1)
            self.dfs(i - 1, j, matrix, True, num + 1)

            return matrix

    def is_valid(self, i, j, matrix):
        return not (i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] > 0)