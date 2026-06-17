# top-down
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if (i, j) in memo: return memo[(i, j)]

            if i == len(word1):
                min_op = dfs(i, j + 1) + 1
            elif j == len(word2):
                min_op = dfs(i + 1, j) + 1
            elif word1[i] == word2[j]:
                min_op = dfs(i + 1, j + 1)
            else:
                min_op = 1 + min(dfs(i + 1, j + 1), dfs(i + 1, j), dfs(i, j + 1))

            memo[(i, j)] = min_op
            return min_op

        return dfs(0, 0)

# bottom-up
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1), len(word2)
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for i in range(rows, -1, -1):
            for j in range(cols, -1, -1):
                if i == rows and j == cols: continue
                if i == len(word1):
                    dp[i][j] = dp[i][j + 1] + 1
                elif j == len(word2):
                    dp[i][j] = dp[i + 1][j] + 1
                elif word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]) + 1

        return dp[0][0]

# bottom-up O(min(len(word1),len(word2)))
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [0] * (m+1)
        prev_dp = dp[::]
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n and j == m: continue
                if i == n:
                    dp[j] = dp[j+1] + 1
                elif j == m:
                    dp[j] = prev_dp[j] + 1
                elif word1[i] == word2[j]:
                    dp[j] = prev_dp[j+1]
                else:
                    dp[j] = min(prev_dp[j], dp[j+1],prev_dp[j+1]) + 1
            prev_dp, dp = dp, prev_dp

        return prev_dp[0]
