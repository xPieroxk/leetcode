class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0
        max_reach = 0
        goal = len(nums) - 1

        while r <goal:
            for i in range(l,r+1):
                max_reach = max(max_reach, i+nums[i])
            l = r+1
            r = max_reach
            jumps+=1
        return jumps