class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = float("inf")
        maxProfit = float("-inf")
        for price in prices:
            if price < minValue:
                minValue = price
            else:
                maxProfit = max(maxProfit, price - minValue)
            
        return 0 if maxProfit == float("-inf") else maxProfit
