# top-down
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        n, m = len(s), len(p)

        def dfs(i, j):
            if j == m:
                return i == n

            if (i, j) in memo: return memo[(i, j)]

            match = i < n and (s[i] == p[j] or p[j] == '.')

            if j < m - 1 and p[j + 1] == '*' and ((match and dfs(i + 1, j)) or dfs(i, j + 2)):
                return True
            if match and dfs(i + 1, j + 1):
                return True

            memo[(i, j)] = False
            return False

        return dfs(0, 0)

# bottom-up
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(s), len(p)
        dp = [[False for _ in range(m+1)] for _ in range(n+1)]
        dp[-1][-1] = True

        for i in range(n,-1,-1):
            for j in range(m-1,-1,-1):
                match = i<n and (s[i] == p[j] or p[j]=='.')
                if j<m-1 and p[j+1] == '*' and ((match and dp[i+1][j]) or dp[i][j+2]):
                    dp[i][j] = True
                if match and dp[i+1][j+1]:
                    dp[i][j] = True
        return dp[0][0]
