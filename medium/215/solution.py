import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heapq.heappush(h, n)
            if len(h) > k:
                heapq.heappop(h)

        return h[0]

# quickselect
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth_idx = len(nums) - k
        l, r = 0, len(nums) - 1
        while True:
            pivot_idx = random.randint(l, r)
            nums[r], nums[pivot_idx] = nums[pivot_idx], nums[r]

            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p < kth_idx:
                l = p + 1
            elif p > kth_idx:
                r = p - 1
            else:
                return nums[p]

#