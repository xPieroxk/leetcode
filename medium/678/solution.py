class Solution:
    def checkValidString(self, s: str) -> bool:
        minL = maxL = 0

        for c in s:
            if c == '(':
                minL += 1
                maxL += 1
            elif c == ')':
                minL -= 1
                maxL -= 1
            else:
                minL -= 1
                maxL += 1
            if maxL < 0: return False
            if minL < 0:
                minL = 0

        return minL == 0