class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # [1,2,4,2,3,5,3,4]
        # [4, 4, 5]
        # [[1, 2, 3], [2, 3]]
        buckets = [[] for _ in range(len(hand) // groupSize)]
        heapq.heapify(hand)

        while hand:
            val = heapq.heappop(hand)
            i = 0
            while i < len(buckets):
                if not buckets[i] or val == buckets[i][-1] + 1 and len(buckets[i]) < groupSize:
                    buckets[i].append(val)
                    break
                i += 1
                
            if i == len(buckets):
                return False
        
        for bucket in buckets:
            if len(bucket) != groupSize:
                return False

        return True