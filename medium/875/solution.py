class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            speed = 0
            m = (l + r) // 2
            for p in piles:
                speed += (p + m - 1) // m  # math.ceil(p/m)

            if speed > h:
                l = m + 1
            else:
                ans = m
                r = m - 1
        return ans