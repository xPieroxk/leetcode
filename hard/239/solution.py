import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        window = []
        deleted = {}
        for i in range(k):
            window.append(-nums[i])

        heapq.heapify(window)
        ans.append(-window[0])

        for r in range(k, len(nums)):
            heapq.heappush(window, -nums[r])

            leaving = -nums[r - k]
            deleted[leaving] = deleted.get(leaving, 0) + 1

            while deleted.get(window[0], 0) > 0:
                root = heapq.heappop(window)
                deleted[root] -= 1

            ans.append(-window[0])

        return ans