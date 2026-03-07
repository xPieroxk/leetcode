class Solution(object):
    def sortColors(self, nums):

        counts = [0] * 3

        for n in nums:
            counts[n] += 1

        curr = 0
        for i in range(3):
            while counts[i] > 0:
                nums[curr] = i
                counts[i] -= 1
                curr += 1
