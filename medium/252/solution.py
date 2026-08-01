"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals : return True

        intervals.sort(key=lambda o: o.start)
        prev_e = float('-inf')
        for i in intervals:
            s, e= i.start, i.end
            if s<prev_e:
                return False
            prev_e = e

        return True
