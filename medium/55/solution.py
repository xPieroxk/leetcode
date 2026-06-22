class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jumps = 0
        for n in nums:
            if jumps < 0:
                return False
            jumps = max(jumps,n)
            jumps -=1
        return True


# moving forward
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = 0

        for i in range(n):
            if i > reach: return False
            reach = max(reach, i + nums[i])
            if reach >= n - 1: return True # optimization, not needed

        return reach >= n - 1
