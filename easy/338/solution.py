class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Dynamic programming:
        # - For even i: number of 1s is same as i // 2
        # - For odd i:  number of 1s is 1 more than i // 2
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result
