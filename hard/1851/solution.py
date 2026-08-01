import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted(enumerate(queries), key=lambda q: q[1])
        min_heap = []
        ans = [-1] * len(queries)
        i = 0
        for idx, q in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                if intervals[i][1] >= q:
                    heapq.heappush(min_heap, (e - s + 1, e))
                i += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                ans[idx] = min_heap[0][0]
        return ans
