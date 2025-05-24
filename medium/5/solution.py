class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        substrings = [[False for _ in range(len(s))] for _ in range(len(s))]
        longest_palindrome = s[0]

        for i in range(len(s)):
            substrings[i][i] = True
            if i < len(s) - 1 and s[i] == s[i + 1]:
                substrings[i][i + 1] = True
                longest_palindrome = s[i:i + 2]

        for window in range(2, len(s)):
            for i in range(len(s) - window):
                substrings[i][i + window] = substrings[i + 1][i + window - 1] and s[i] == s[i + window]
                if substrings[i][i + window] and window + 1 > len(longest_palindrome):
                    longest_palindrome = s[i:i + window + 1]
        return longest_palindrome
