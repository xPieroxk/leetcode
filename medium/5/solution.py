class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Used dynamic programming instead of Manacher's Algorithm because
        # Manacher's is specific to this problem, while DP is more general and
        # can be applied to a wider range of problems. Since I am practicing,
        # I preferred this approach.
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

# 2 pointer
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = length = 0
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > length:
                    start = l
                    length = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > length:
                    start = l
                    length = r - l + 1
                l -= 1
                r += 1

        return s[start:start + length]

# dp refined
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        start = length = -1

        for w_size in range(1, n + 1):
            for i in range(n - w_size + 1):
                j = i + w_size - 1
                if s[i] != s[j]:
                    continue
                if (j - i == 0) or (j - i == 1) or (dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if (j - i + 1) > length:
                        start = i
                        length = j - i + 1
        return s[start:start + length]