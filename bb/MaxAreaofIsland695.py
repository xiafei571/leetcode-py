class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def inArea(grid, i ,j):
            return i>=0 and j>=0 and i<len(grid) and j<len(grid[0])

        def dfs(grid, i, j):
            if inArea(grid, i, j) and grid[i][j] == 1:
                grid[i][j] = 0
                curArea=1

                curArea += dfs(grid, i-1, j)
                curArea += dfs(grid, i+1, j)
                curArea += dfs(grid, i, j-1)
                curArea += dfs(grid, i, j+1)
                return curArea
            return 0

        # begin
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curArea = 0
                    curArea = dfs(grid, i, j)
                    maxArea = max(maxArea, curArea)
        return maxArea
        # end
                