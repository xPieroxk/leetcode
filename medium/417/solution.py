from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        d = deque()
        atlantic = []
        pacific = []

        n, m = len(heights), len(heights[0])
        for i in range(n):
            pacific.append((i, 0))
            atlantic.append((i, m - 1))
        for j in range(m):
            pacific.append((0, j))
            atlantic.append((n - 1, j))

        def bfs(ocean):
            d = deque(ocean)
            ocean = set(ocean)
            while d:
                i, j = d.popleft()
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < n and 0 <= nj < m and (ni, nj) not in ocean
                            and heights[ni][nj] >= heights[i][j]):
                        d.append((ni, nj))
                        ocean.add((ni, nj))
            return ocean

        return list(bfs(pacific).intersection(bfs(atlantic)))
