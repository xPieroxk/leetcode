class Solution:
    def myPow(self, x: float, n: int) -> float:

        def myPowHelper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = myPowHelper(x * x, n // 2)
            return res * x if n % 2 == 1 else res

        ans = myPowHelper(x, abs(n))
        return ans if n > 0 else 1 / ans