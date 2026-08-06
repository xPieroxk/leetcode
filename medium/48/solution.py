class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # reverse horizontally
        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]

        # transpose
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
