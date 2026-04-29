class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def bt(i, s):
            if i == len(nums):
                ans.append(s.copy())
                return
            s.append(nums[i])
            bt(i + 1, s)
            s.pop()
            bt(i + 1, s)

        bt(0, [])
        return ans
