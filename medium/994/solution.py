from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruits = minute = 0
        d = deque()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_fruits += 1
                elif grid[i][j] == 2:
                    d.append((i, j))

        if not fresh_fruits: return 0

        while d and fresh_fruits:
            minute += 1

            for count in range(len(d)):
                i, j = d.popleft()

                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1):
                        fresh_fruits -= 1
                        grid[ni][nj] = 2
                        d.append((ni, nj))

        return minute if fresh_fruits == 0 else -1