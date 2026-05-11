from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])

        d= deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    d.append((i,j))

        while d:
            i,j = d.popleft()
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                r,c =i+di,j+dj
                if 0<=r<n and 0<=c<m and grid[r][c]==2147483647:
                    grid[r][c] = grid[i][j]+1
                    d.append((r,c))
