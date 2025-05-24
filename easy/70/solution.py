class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0] * (n + 2)
        result[1] = 1
        result[2] = 2
        for i in range(3,n+1):
            result[i] = result[i-1] + result[i-2]
        return result[n]