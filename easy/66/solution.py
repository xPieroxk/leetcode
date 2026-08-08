class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while i >= 0:
            digits[i] += 1
            if digits[i] != 10:
                break
            digits[i] = 0
            i -= 1

        if digits[0] == 0:
            digits.insert(0, 1)
        return digits

# more readable
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0

        return [1] + digits
