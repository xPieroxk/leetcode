import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 0
            freq[task] += 1

        time = 0
        max_heap = [-v for v in freq.values()]
        heapq.heapify(max_heap)
        cooldown_queue = deque()

        while max_heap or cooldown_queue:
            if not max_heap:
                time = cooldown_queue[0][1]

            if cooldown_queue and cooldown_queue[0][1] == time:
                cnt, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, cnt)
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt < 0:
                    cooldown_queue.append((cnt, time + n + 1))
            time += 1
        return time