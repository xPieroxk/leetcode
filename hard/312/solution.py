class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        memo = {}
        nums = [1] + nums + [1]

        def solve(i, j):
            if i + 1 == j: return 0
            if (i, j) in memo: return memo[(i, j)]

            coins = 0
            for k in range(i + 1, j):
                gain = nums[i] * nums[k] * nums[j]
                coins = max(coins, solve(i, k) + solve(k, j) + gain)

            memo[(i, j)] = coins
            return coins

        return solve(0, len(nums) - 1)