class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

# Patience Sorting.
# I do not know the math proof behind but PS guarantees that number of piles will be equal to the LIS.
# If someone ever asks you to derive this solution on a white board, without any help, just leave the room.
# No way someone can derive this in 45mins without having seen this solution before :)
# It took humanity roughly 40 years (from 1935 to 1975) to naturally derive, optimize, and code this specific binary search solution.
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for n in nums:
            i = bisect_left(tails, n)
            if i == len(tails):
                tails.append(n)
            else:
                tails[i] = n

        return len(tails)
