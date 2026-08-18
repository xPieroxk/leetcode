class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        for _ in range(32):
            ans += int(1 & n)
            n >>= 1

        return ans

# n & (n-1):
# - Subtracting 1 from a number flips the rightmost 1 bit to 0 and turns all bits to its right into 1
# - Performing n & (n - 1) removes the rightmost 1 bit from n
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res