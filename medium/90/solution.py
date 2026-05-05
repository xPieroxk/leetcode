class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def bt(i, curr):
            if i == len(nums):
                ans.append(curr[:])
                return
            curr.append(nums[i])
            bt(i + 1, curr)

            curr.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            bt(i + 1, curr)

        bt(0, [])
        return ans