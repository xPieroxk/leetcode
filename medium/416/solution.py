class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)
        dp = [False] * (target + 1)
        next_dp = [False] * (target + 1)
        dp[0] = True

        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(1, target + 1):
                if curr > j:
                    next_dp[j] = dp[j]
                else:
                    next_dp[j] = dp[j] or dp[j - curr]
            if next_dp[-1]: return True # optimization, not needed
            dp, next_dp = next_dp, dp

        return dp[-1]

# Solution with just one array. It is equivalent to the 2d or 2-array 1d approaches.
# at the end of each outer loop, the arrays have the exact same values.
#
# Going backwards is just a trick to not reuse numbers. Because we move backward,
# the values we visit have not been updated yet, preventing us from building on sums
# already calculated in this iteration. In the 2d approach, this was handled by
# using a separate array.
#
# Also, the inner loop stops at the current number because going any lower would mean
# an invalid index. In the 2d solution, we had to visit these smaller indexes to
# 'transfer the knowledge' down. In this 1d version, the previous result is already
# sitting in the array, so we don't need to visit them.
#
# While this solution is equivalent, I find it less intuitive to read and visualize.
# Stick with the more natural one you can actually explain and do a favor to yourself.
# Understanding > Memorizing :)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0: return False

        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(len(nums)):
            curr = nums[i]
            for j in range(target, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]
            if dp[-1]: return True# optimization, not needed
        return dp[-1]

