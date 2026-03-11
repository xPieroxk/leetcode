class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            seen = set()
            for col in range(9):
                curr = board[row][col]
                if curr == ".":
                    continue
                if curr in seen:
                    return False
                seen.add(curr)

        for col in range(9):
            seen = set()
            for row in range(9):
                curr = board[row][col]
                if curr == ".":
                    continue
                if curr in seen:
                    return False
                seen.add(curr)

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    curr = board[row][col]
                    if curr == ".":
                        continue
                    if curr in seen:
                        return False
                    seen.add(curr)

        return True

