class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        def dfs(i,j):
            if (i<0 or i==n or j<0 or j==m
                or grid[i][j] != '1'):
                return

            grid[i][j] = '#'
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                dfs(i+di,j+dj)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans+=1
                    dfs(i,j)

        return ans