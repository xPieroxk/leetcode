# memo
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i,j):
            if j ==len(t): return 1
            if i == len(s) : return 0
            if (i,j) in memo: return memo[(i,j)]
            ways = 0
            if s[i] == t[j]:
                ways += dfs(i+1,j+1)
            ways += dfs(i+1,j)
            memo[(i,j)] = ways
            return ways

        return dfs(0,0)
# bottom-up
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ROWS, COLS = len(s), len(t)
        dp = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]

        for i in range(ROWS + 1):
            dp[i][0] = 1

        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                c1, c2 = s[i - 1], t[j - 1]
                dp[i][j] = dp[i - 1][j]
                if c1 == c2:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[-1][-1]

# bottom up 1 array
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        p_dp = [0] * (len(t) + 1)
        p_dp[0] = 1

        for i in range(len(s)):
            for j in range(1, len(t) + 1):
                dp[j] = p_dp[j]
                if s[i] == t[j - 1]:
                    dp[j] += p_dp[j - 1]
            dp, p_dp = p_dp, dp

        return p_dp[-1]
