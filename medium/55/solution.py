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