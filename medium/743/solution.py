from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((t, v))
        distances = {i: float('inf') for i in range(n + 1)}

        h = [(0, k)]
        distances[k] = 0
        count = 0
        while h:
            curr_t, node = heapq.heappop(h)
            if curr_t > distances[node]: continue

            count += 1
            if count == n: return curr_t

            for time, nei in graph[node]:
                if curr_t + time < distances[nei]:
                    distances[nei] = curr_t + time
                    heapq.heappush(h, (curr_t + time, nei))

        return -1