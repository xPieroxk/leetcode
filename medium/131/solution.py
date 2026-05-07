class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        partition = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def bt(i):
            if i == len(s):
                ans.append(partition[:])
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    partition.append(s[i:j + 1])
                    bt(j + 1)
                    partition.pop()

        bt(0)
        return ans