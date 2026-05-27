import heapq

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        kLargest = heapq.nlargest(self.k, self.heap)
        return kLargest[-1]



        
