import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-x for x in stones]
        heapq.heapify(s)

        while len(s) > 1:
            x = -heapq.heappop(s)
            y = -heapq.heappop(s)
            z = x - y
            if z > 0:
                heapq.heappush(s, -z)

        return -s[0] if len(s) == 1 else 0
