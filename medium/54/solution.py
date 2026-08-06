class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        ans = []
        top = 0
        bottom = n
        left = 0
        right = m

        while top < bottom and left < right:
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1

            if not (top < bottom and left < right): break

            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1

        return ans
