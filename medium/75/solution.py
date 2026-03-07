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

'''    class Solution(object):
        def sortColors(self, nums):
            l = m = 0
            r = len(nums) - 1
            while m <= r:
                if nums[m] == 0:
                    nums[l], nums[m] = nums[m], nums[l]
                    m += 1
                    l += 1
                elif nums[m] == 1:
                    m += 1
                else:
                    nums[m], nums[r] = nums[r], nums[m]
                    r -= 1'''
