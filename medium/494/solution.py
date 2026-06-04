# memo
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, t):
            if i == len(nums):
                if t == 0:
                    return 1
                else:
                    return 0
            if (i, t) in memo: return memo[(i, t)]

            add = dfs(i + 1, t + nums[i])
            less = dfs(i + 1, t - nums[i])
            memo[(i, t)] = add + less
            return add + less

        return dfs(0, target)

# O(1) space bottom up
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for s, count in dp.items():
                next_dp[s - num] += count
                next_dp[s + num] += count
            dp = next_dp

        return dp[target]