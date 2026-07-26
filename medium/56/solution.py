class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        ns, ne = intervals[0][0], intervals[0][1]

        for s, e in intervals:
            if ne < s:
                ans.append([ns, ne])
                ns, ne = s, e
            else:
                ns, ne = min(s, ns), max(e, ne)

        ans.append([ns, ne])
        return ans