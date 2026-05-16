class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxContainer = float("-inf")
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            container = width * height
            maxContainer = max(maxContainer, container)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxContainer