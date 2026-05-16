class TimeMap:

    def __init__(self):
        self.tm = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.tm[key]
        if len(values) == 0:
            return ""
        
        lo, hi = 0, len(values) - 1
        res = ""
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            ts = values[mid][1]
            if ts <= timestamp:
                lo = mid + 1
                res = values[mid][0]
            else:
                hi = mid - 1
        
        return res
            
