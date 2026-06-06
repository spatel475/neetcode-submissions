"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) == 0 or len(intervals) == 1:
            return True

        sortedIntervals = sorted(intervals, key=lambda x: (x.start, x.end))

        i = 0
        while i < len(sortedIntervals) - 1:
            curr = sortedIntervals[i]
            next = sortedIntervals[i + 1]

            isValid = curr.start < next.start and curr.end <= next.start and curr.end < next.end
            if not isValid:
                return False
            i += 1
        return True
