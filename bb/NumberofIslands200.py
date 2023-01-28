class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def inArea(grid, i, j):
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

        def dfs(grid, i, j):
            if inArea(grid, i, j) and grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(grid, i-1, j)
                dfs(grid, i+1, j)
                dfs(grid, i, j-1)
                dfs(grid, i, j+1)

        num_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_of_islands += 1
                    dfs(grid, i, j)
        return num_of_islands
    