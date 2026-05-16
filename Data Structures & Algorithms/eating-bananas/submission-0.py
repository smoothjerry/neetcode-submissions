class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1, 4, 3, 2] -> [1, 2, 3, 4]
        # h = 9
        # k = 2
        # 
        # [25, 10, 23, 4] -> [4, 10, 23, 25]
        # h = 4
        # k = 25
        #
        # want smallest k
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / mid)
            if totalTime <= h:
                # found a valid solution
                # but let's try shrinking the eating rate again
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

