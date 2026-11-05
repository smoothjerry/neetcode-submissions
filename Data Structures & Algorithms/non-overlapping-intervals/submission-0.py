class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for b_start, b_end in intervals[1:]:
            if b_start >= prevEnd:
                prevEnd = b_end
            else:
                res += 1
                prevEnd = min(b_end, prevEnd)
        return res