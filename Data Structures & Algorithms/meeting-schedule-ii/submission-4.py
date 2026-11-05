"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda interval: interval.start)
        heap = []
        for interval in intervals:
            b_start, b_end = interval.start, interval.end
            if heap and b_start >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, b_end)

        return len(heap)
