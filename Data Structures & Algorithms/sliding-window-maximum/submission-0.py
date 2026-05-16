class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        l = 1
        res = [-heap[0][0]]
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))

            curr = None
            while curr == None:
                maxVal, i = heap[0]
                if l <= i <= r:
                    curr = -maxVal
                else:
                    heapq.heappop(heap)

            res.append(curr)

            l += 1
            
        return res