class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.visited = [[False for x in range(len(matrix[0]))] for y in range(len(matrix))]
        self.res = []
        self.dfs(matrix, 0, 0, False)
        return self.res

    def dfs(self, matrix, i, j, goUp):
        if self.is_valid(i, j, matrix):
            self.res.append(matrix[i][j])
            self.visited[i][j] = True
            if goUp:
                self.dfs(matrix, i - 1, j, True)
            self.dfs(matrix, i, j + 1, False)
            self.dfs(matrix, i + 1, j, False)
            self.dfs(matrix, i, j - 1, False)
            self.dfs(matrix, i - 1, j, True)

    def is_valid(self, i, j, matrix):
        return not (i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or self.visited[i][j])