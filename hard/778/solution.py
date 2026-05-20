from collections import defaultdict
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        h = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        while h:
            w, r, c, = heapq.heappop(h)
            if r == (n - 1) and c == (n - 1): return w

            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni, nj = r + di, c + dj
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                    heapq.heappush(h, (max(w, grid[ni][nj]), ni, nj))
                    visited.add((ni, nj))

