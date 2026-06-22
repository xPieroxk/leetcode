class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        global_max = float('-inf')

        for n in nums:
            curr_max += n
            if n > curr_max:
                curr_max = n
            global_max = max(global_max, curr_max)

        return global_max