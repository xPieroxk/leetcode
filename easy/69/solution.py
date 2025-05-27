class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # binary search
        ans,left = 0,0
        right = x     #  0 1 2
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                right = mid - 1
            else:
                left = mid + 1
                ans = mid
        return ans
