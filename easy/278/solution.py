class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        # binary search until both left and right coincide
        while left != right:
            mid = ((right - left) // 2) + left
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

