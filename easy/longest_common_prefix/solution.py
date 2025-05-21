class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""

        first = strs[0]
        window_size = 1

        while window_size <= len(first):
            for word in strs[1:]:
                if window_size > len(word) or first[:window_size] != word[:window_size]:
                    return result
            result = first[:window_size]
            window_size += 1
        return result
