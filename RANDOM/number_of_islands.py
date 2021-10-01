class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        colLen = len(grid[0])
        rowLen = len(grid)

        def dfs(i, j, visited, grid):
            if i < 0 or j < 0 or i >= rowLen or j >= colLen or visited[i][j] == 1 or grid[i][j] == "0":
                return
            visited[i][j] = 1
            dfs(i + 1, j, visited, grid)
            dfs(i - 1, j, visited, grid)
            dfs(i, j + 1, visited, grid)
            dfs(i, j - 1, visited, grid)

        visited = [[0] * colLen for i in range(rowLen)]
        c = 0
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == "1":
                    if not visited[i][j]:
                        c += 1
                        dfs(i, j, visited, grid)

        return c
