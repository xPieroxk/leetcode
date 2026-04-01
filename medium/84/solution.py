class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        bars = []  # index, height

        for i, h in enumerate(heights):
            start = i
            while bars and h <= bars[-1][1]:
                bar_i, bar_h = bars.pop()
                max_area = max(max_area, (i - bar_i) * bar_h)
                start = bar_i
            bars.append((start, h))

        for i, h in bars:
            max_area = max(max_area, (len(heights) - i) * h)

        return max_area
