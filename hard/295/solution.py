import heapq


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0:
            heapq.heappush(self.max_heap, -num)
            return

        if num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.min_heap) > len(self.max_heap) + 1:
            item = -heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, item)
        if len(self.max_heap) > len(self.min_heap) + 1:
            item = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, item)

    def findMedian(self) -> float:
        n = len(self.min_heap)
        m = len(self.max_heap)
        if (n + m) % 2 == 0:
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        elif n > m:
            return self.min_heap[0]
        else:
            return -self.max_heap[0]
