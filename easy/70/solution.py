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


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        prev = 1
        prev_prev = 2

        for i in range(2, n):
            tmp = prev_prev
            prev_prev = prev + prev_prev
            prev = tmp

        return prev_prev