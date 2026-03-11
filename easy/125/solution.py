class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s)
        l = -1
        while True:
            r -= 1
            l += 1
            while r >= 0 and not s[r].isalnum():
                r -= 1
            while l < len(s) and not s[l].isalnum():
                l += 1
            if r < 0 or l == len(s):
                break
            if s[l].lower() != s[r].lower():
                return False
        return True
