class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search to find the pivot
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
            
        pivot = lo
        lo, hi = 0, len(nums) - 1
        if nums[pivot] <= target <= nums[hi]:
            lo = pivot
        else:
            hi = pivot - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return -1