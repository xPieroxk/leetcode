# memo
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        coins.sort(reverse=True) # optimization, not needed

        def dfs(i, remainder):
            if remainder < 0 or i == len(coins): return 0
            if remainder == 0: return 1
            if (i, remainder) in memo: return memo[(i, remainder)]

            keep = dfs(i, remainder - coins[i])
            skip = dfs(i + 1, remainder)

            memo[(i, remainder)] = keep + skip
            return keep + skip

        return dfs(0, amount)
# bottom up
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]

        return dp[-1]

