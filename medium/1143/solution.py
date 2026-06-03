class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                c1, c2 = text1[i - 1], text2[j - 1]
                if c1 == c2:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

# space optimized using 2 arrays
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [0 for _ in range(m + 1)]
        prev_dp = [0 for _ in range(m + 1)]

        for i in range(n):
            for j in range(1, m + 1):
                if text1[i] == text2[j - 1]:
                    dp[j] = 1 + prev_dp[j - 1]
                else:
                    dp[j] = max(dp[j - 1], prev_dp[j])
            dp, prev_dp = prev_dp, dp

        return prev_dp[-1]