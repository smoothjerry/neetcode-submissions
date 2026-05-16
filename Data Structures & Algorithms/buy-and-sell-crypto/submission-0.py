class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = float("-inf")
        minSeen = float("inf")

        for price in prices:
            if price < minSeen:
                minSeen = price
            else:
                maxProfit = max(maxProfit, price - minSeen)
        
        return maxProfit if maxProfit != float("-inf") else 0