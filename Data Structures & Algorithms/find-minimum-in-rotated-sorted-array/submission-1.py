class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min is the place
        # where prev value is greater
        
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (hi + lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        return nums[lo]