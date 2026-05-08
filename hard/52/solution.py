class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        major = set()
        minor = set()
        ans = 0

        def bt(r):
            nonlocal ans
            if r == n:
                ans += 1
                return

            for c in range(n):
                if c not in cols and (r - c) not in major and (r + c) not in minor:
                    cols.add(c)
                    major.add(r - c)
                    minor.add(r + c)
                    bt(r + 1)
                    cols.remove(c)
                    major.remove(r - c)
                    minor.remove(r + c)

        bt(0)
        return ans