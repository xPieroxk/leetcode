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
