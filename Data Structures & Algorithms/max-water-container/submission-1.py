class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximumWater = -1
        l, r = 0, len(heights) - 1
        while l < r:
            water = min(heights[l], heights[r]) * (r - l)
            maximumWater = max(maximumWater, water)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maximumWater