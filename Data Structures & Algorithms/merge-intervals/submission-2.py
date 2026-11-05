class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # intervals overlap when a starts before b ends and b starts 
        # before a ends
        merged = []
        for b_start, b_end in intervals:
            if not merged or b_start > merged[-1][1]:
                merged.append([b_start, b_end])
            else:
                merged[-1][1] = max(merged[-1][1], b_end)
        
        return merged