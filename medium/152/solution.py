class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curr_min = curr_max = global_max = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            if curr < 0:
                curr_min, curr_max = curr_max, curr_min

            curr_max = max(curr, curr_max * curr)
            curr_min = min(curr, curr_min * curr)

            global_max = max(global_max, curr_max)

        return global_max
