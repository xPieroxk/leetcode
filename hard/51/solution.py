class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        major = set()
        minor = set()
        board = [["." for _ in range(n)] for _ in range(n)]
        ans = []

        def bt(r):
            if r == n:
                ans.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c not in cols and (r - c) not in major and (r + c) not in minor:
                    cols.add(c)
                    major.add(r - c)
                    minor.add(r + c)
                    board[r][c] = 'Q'
                    bt(r + 1)
                    board[r][c] = '.'
                    cols.remove(c)
                    major.remove(r - c)
                    minor.remove(r + c)

        bt(0)
        return ans
