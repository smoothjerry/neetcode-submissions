class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(value, timestamp)]
        else:
            row = self.timeMap[key]
            row.append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        row = self.timeMap[key]
        lo, hi = 0, len(row) - 1
        res = ""
        while lo <= hi:
            mid = (hi + lo) // 2
            val, time = row[mid]
            if time <= timestamp:
                res = val
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res
