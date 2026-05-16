class Solution:
    def trap(self, height: List[int]) -> int:
        maxRight, maxLeft = [0] * len(height), [0] * len(height)
        l, r = 1, len(height) - 2
        while l < len(height) and r >= 0:
            maxRight[l] = max(maxRight[l - 1], height[l - 1])
            maxLeft[r] = max(maxLeft[r + 1], height[r + 1])
            l += 1
            r -= 1
        
        rainWater = 0
        for i in range(len(height)):
            trapped = min(maxLeft[i], maxRight[i]) - height[i]
            if trapped > 0:
                rainWater += trapped
        
        return rainWater