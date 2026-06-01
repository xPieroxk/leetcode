from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m + n-2) / (factorial(m-1) * factorial(n-1)))

# dp solution

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
