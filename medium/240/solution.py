class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix) - 1, len(matrix[0]) - 1
        r, c = 0, COLS
        while r <= ROWS and c >= 0:
            curr = matrix[r][c]
            if target == curr:
                return True
            elif target > curr:
                r += 1
            else:
                c -= 1

        return False
