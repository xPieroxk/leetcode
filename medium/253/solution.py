"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        points = []
        for i in intervals:
            points.append((i.start,1))
            points.append((i.end,0))
        points.sort()

        max_rooms = curr_rooms = 0

        for p, is_start in points:
            if is_start:
                curr_rooms +=1
                max_rooms = max(curr_rooms, max_rooms)
            else:
                curr_rooms -=1

        return max_rooms