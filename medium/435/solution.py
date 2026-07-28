class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        e = intervals[0][1]

        for i in range(1, len(intervals)):
            ns, ne = intervals[i][0], intervals[i][1]
            if ns >= e:
                e = ne
            else:
                e = min(e, ne)
                ans += 1

        return ans

# sorting by end time
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        s, e = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            ns, ne = intervals[i][0], intervals[i][1]
            if ns >= e:
                s, e = ns, ne
                continue
            ans += 1

        return ans