class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # want to find min speed
        # min speed can be 1 ban/hr all the way up to max(piles).
        # there's no reason to go higher because you can only visit
        # one pile per hour.
        #
        # so we're looking for min(k) for k in range 1..max(piles)
        # such that we at a consumption rate of k bananas/hr, we finish
        # all bananas in at most h hours.

        lo, hi = 1, max(piles)
        res = hi

        while lo <= hi:
            k = (hi + lo) // 2
            hrs = 0
            for p in piles:
                hrs += math.ceil(float(p) / k)
            
            if hrs <= h:
                # we found a valid solution, so 
                # maybe we can shrink k further
                res = k
                hi = k - 1
            else:
                lo = k + 1
        
        return res