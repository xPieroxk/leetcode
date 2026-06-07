# top-down
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) < len(s1) + len(s2): return False
        memo = {}

        def dfs(i, j):
            if i + j == len(s3): return True
            if (i, j) in memo: return memo[(i, j)]

            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True

            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True

            memo[(i, j)] = False
            return False

        return dfs(0, 0)

# top-down
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, k = len(s1), len(s2), len(s3)
        if k != n + m: return False

        # s1 on the columns
        # s2 on the rows
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = True

        for col in range(1, n + 1):
            dp[0][col] = dp[0][col - 1] and s1[col - 1] == s3[col - 1]

        for row in range(1, m + 1):
            dp[row][0] = dp[row - 1][0] and s2[row - 1] == s3[row - 1]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                curr = s3[col + row - 1]
                c1 = s1[col - 1]
                c2 = s2[row - 1]
                if dp[row][col - 1] and c1 == curr:
                    dp[row][col] = True
                if not dp[row][col] and dp[row - 1][col] and c2 == curr:
                    dp[row][col] = True

        return dp[-1][-1]
