class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])

        def dfs(i, j):
            if (i < 0 or i == n or j < 0 or j == m or board[i][j] != 'O'):
                return
            board[i][j] = '#'
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(i + di, j + dj)

        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m - 1] == 'O':
                dfs(i, m - 1)

        for j in range(m):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[n - 1][j] == 'O':
                dfs(n - 1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
