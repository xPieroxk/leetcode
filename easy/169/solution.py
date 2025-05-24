class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # use moore voting algorithm

        candidate, vote = 0, 0

        for num in nums:
            if vote == 0:
                candidate = num
            vote += 1 if num == candidate else - 1
        return candidate

