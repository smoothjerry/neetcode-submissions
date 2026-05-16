class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            
            else:
                latest = max(merged[-1][1], end)
                merged[-1][1] = latest
        
        return merged

