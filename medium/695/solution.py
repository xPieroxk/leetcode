class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0

        def dfs(i, j):
            if (i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0):
                return 0

            grid[i][j] = 0
            area = 1
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                area += dfs(i + di, j + dj)
            return area

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(dfs(i, j), ans)
        return ans
