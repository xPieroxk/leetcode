class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        ans = 0
        n, m = len(matrix), len(matrix[0])

        def dfs(i, j):
            if (i, j) in memo: return memo[(i, j)]

            path = 0
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]:
                    path = max(path, dfs(ni, nj))

            memo[(i, j)] = 1 + path
            return 1 + path

        for i in range(n):
            for j in range(m):
                if (i, j) not in memo:
                    ans = max(ans, dfs(i, j))
        return ans
