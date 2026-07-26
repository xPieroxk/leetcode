class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        ns, ne = newInterval[0], newInterval[1]

        for i, (s, e) in enumerate(intervals):
            if ne < s:
                ans.append([ns, ne])
                ans.extend(intervals[i:])
                return ans
            elif ns > e:
                ans.append([s, e])
            else:
                ns = min(ns, s)
                ne = max(ne, e)

        ans.append([ns, ne])
        return ans