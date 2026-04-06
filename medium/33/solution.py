class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (r + l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        cut = l
        l, r = (0, cut - 1) if target > nums[-1] else (cut, len(nums) - 1)

        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1

        return -1
