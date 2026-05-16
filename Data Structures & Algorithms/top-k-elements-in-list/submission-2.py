class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))
        
        res = []
        while k > 0:
            num = heapq.heappop(heap)[1]
            res.append(num)
            k -= 1
        
        return res