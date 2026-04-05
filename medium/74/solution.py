class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        bottom = len(matrix)-1
        while up <= bottom:
            m = (bottom+up)//2
            if target > matrix[m][-1]:
                up = m+1
            elif target < matrix[m][0]:
                bottom = m-1
            else:
                break
        else:
            return False

        l = 0
        r = len(matrix[0])-1
        row = (up+bottom) // 2
        while l<=r:
            m = (r+l)//2
            if target == matrix[row][m]:
                return True
            elif target > matrix[row][m]:
                l = m + 1
            else:
                r = m - 1

        return False