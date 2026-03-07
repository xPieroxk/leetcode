#merge sort
class Solution(object):
    def sortArray(self, nums):
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(selft, l, r):
        res = []
        i = j = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1

        while i < len(l):
            res.append(l[i])
            i += 1
        while j < len(r):
            res.append(r[j])
            j += 1

        return res
