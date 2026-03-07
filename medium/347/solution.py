from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, val in freq.items():
            buckets[val].append(key)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
