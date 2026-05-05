class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = [False] * len(nums)

        def bt(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for i in range(len(nums)):
                if not visited[i]:
                    curr.append(nums[i])
                    visited[i] = True
                    bt(curr)

                    curr.pop()
                    visited[i] = False

        bt([])
        return ans
