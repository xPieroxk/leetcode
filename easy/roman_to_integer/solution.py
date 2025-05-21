class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        def toInt(c):
            values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
            return values[c]

        sum = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and toInt(s[i]) < toInt(s[i + 1]):
                sum += toInt(s[i + 1]) - toInt(s[i])
                i += 2  # skip the next character
            else:
                sum += toInt(s[i])
                i += 1
        return sum

