class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        window = len(needle)

        while i + window <= len(haystack):
            if haystack[i:i + window] == needle:
                return i
            i += 1
        return -1
