class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left_height = [0] * n
        max_right_height = [0] * n
        curr_max_left = 0
        curr_max_right = 0
        for i in range(len(height)):
            curr_max_left = max(curr_max_left, height[i])
            max_left_height[i] = curr_max_left

            curr_max_right = max(curr_max_right, height[n - i - 1])
            max_right_height[n - i - 1] = curr_max_right

        ans = 0
        for i, h in enumerate(height):
            ans += min(max_left_height[i], max_right_height[i]) - h
        return ans

