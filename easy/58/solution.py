class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        spaceFound = False
        ans = 0
        for l in s:
            if l == ' ':
                spaceFound = True
            elif spaceFound:
                ans = 1
                spaceFound = False
            else:
                ans += 1
        return ans
