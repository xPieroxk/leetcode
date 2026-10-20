class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def perm(curr, picked):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not picked[i - 1]:
                    continue
                if not picked[i]:
                    curr.append(nums[i])
                    picked[i] = True
                    perm(curr, picked)

                    curr.pop()
                    picked[i] = False

        nums.sort()
        ans = []
        perm([], [False] * len(nums))

        return ans