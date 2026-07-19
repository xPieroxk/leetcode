class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurence = {}
        for i, c in enumerate(s):
            lastOccurence[c] = i

        res = []
        size = end = 0

        for i, c in enumerate(s):
            end = max(end, lastOccurence[c])
            size += 1
            if i == end:
                res.append(size)
                size = 0

        return res
