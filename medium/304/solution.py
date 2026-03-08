class NumMatrix(object):

    def __init__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        self.precomputed = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.precomputed[r][c + 1]
                self.precomputed[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1, col1, row2, col2):
        res = 0
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        res += self.precomputed[row2][col2]
        res -= self.precomputed[row1 - 1][col2]
        res -= self.precomputed[row2][col1 - 1]
        res += self.precomputed[row1 - 1][col1 - 1]

        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)