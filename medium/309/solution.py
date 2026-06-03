class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        # 0 : can buy
        # 1 : can sell
        # 2 : cooldown
        def dfs(i, status):
            if i >= len(prices):
                return 0
            if (i, status) in memo: return memo[(i, status)]

            if status == 0:
                profit = max(dfs(i + 1, 0), dfs(i + 1, 1) - prices[i])
            elif status == 1:
                profit = max(dfs(i + 1, 1), dfs(i + 1, 2) + prices[i])
            else:
                profit = dfs(i + 1, 0)
            memo[(i, status)] = profit
            return profit

        return dfs(0, 0)


# O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        hold = -prices[0]
        sold = float('-inf')
        rest = 0

        for i in range(1, n):
            p_hold = hold
            p_sold = sold
            p_rest = rest

            hold = max(p_rest - prices[i], p_hold)
            sold = p_hold + prices[i]
            rest = max(p_rest, p_sold)

        return max(sold, rest)