# O(n+m) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        cols, rows = set(), set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            for col in range(m):
                matrix[row][col] = 0

        for col in cols:
            for row in range(n):
                matrix[row][col] = 0


# 0(1) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        zeroCol = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        zeroCol = True
                    else:
                        matrix[0][j] = 0

        # zero columns from 1 to m
        for col in range(1, m):
            if matrix[0][col] == 0:
                for row in range(n):
                    matrix[row][col] = 0
        # zero rows from to n
        for row in range(n):
            if matrix[row][0] == 0:
                for col in range(m):
                    matrix[row][col] = 0
                    # zero the leftover first colum, if needed
        if zeroCol:
            for row in range(n):
                matrix[row][0] = 0
# O(1) space using 2 variables. More readable and intuitive imho.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        first_row = False
        first_col = False

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0: first_row = True
                    if j == 0: first_col = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0
        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0
                    # first row and col
        if first_row:
            for j in range(m):
                matrix[0][j] = 0

        if first_col:
            for i in range(n):
                matrix[i][0] = 0
