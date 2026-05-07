class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        def bt(i, j, l):
            if l == len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] == '#' or board[i][j] != word[l]:
                return False

            l += 1
            tmp = board[i][j]
            board[i][j] = '#'
            deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for di, dj in deltas:
                if bt(i + di, j + dj, l):
                    return True
            board[i][j] = tmp
            return False

        for i in range(n):
            for j in range(m):
                if bt(i, j, 0):
                    return True
        return False