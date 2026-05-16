class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounts = collections.defaultdict(int)
        for num in nums:
            numCounts[num] += 1
        
        heap = [(-freq, num) for num, freq in numCounts.items()]
        heapq.heapify(heap)

        res = []
        while k > 0:
            _, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
        
        return res

