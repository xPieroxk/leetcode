import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for p in points:
            d = (p[0]**2+p[1]**2)
            heapq.heappush(h,(-d,p))
            if len(h)>k:
                heapq.heappop(h)

        return [t[1] for t in h]