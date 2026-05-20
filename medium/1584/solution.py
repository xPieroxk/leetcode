import heapq
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        h = [(0,0)]
        ans = 0
        while h:
            cost, node = heapq.heappop(h)
            if node in visited: continue
            ans += cost
            visited.add(node)

            x1, y1 = points[node]
            for nei in range(n):
                if nei not in visited:
                    x2, y2 = points[nei]
                    distance = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(h, (distance, nei))
        return ans