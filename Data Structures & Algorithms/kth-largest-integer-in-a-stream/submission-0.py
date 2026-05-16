class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.heap = []
        
        heapq.heapify(self.heap)
        for num in nums:
            heapq.heappush(self.heap, num)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.size:
            heapq.heappop(self.heap)
        return self.heap[0]
