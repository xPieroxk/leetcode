class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_unique = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[last_unique]:
                last_unique += 1
                nums[last_unique] = nums[i]

        return last_unique + 1
