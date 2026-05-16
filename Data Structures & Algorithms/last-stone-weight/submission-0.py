class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) >= 2:
            st1 = -1 * heapq.heappop(heap)
            st2 = -1 * heapq.heappop(heap)

            if st1 == st2:
                continue

            elif st1 > st2:
                newSt = st1 - st2
                heapq.heappush(heap, -newSt)
            
            else:
                newSt = st2 - st1
                heapq.heappush(heap, -newSt)
        

        return (-1 * heap[0]) if heap else 0