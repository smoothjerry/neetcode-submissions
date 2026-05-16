class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # cases
        # multiplying positive to positive - track current max * n 
        # multiplying positive to negative - might be a new minimum, but this might end up being a maximum
        # multiplying negative to negative - might be a new current max
        # multiplying negative to positive - might be a new minimum
        # we also might want to just start over from this number

        global_max = cur_min = cur_max = nums[0]
        
        for i in range(1, len(nums)):
            n = nums[i]
            tmp_max = cur_max * n
            cur_max = max(cur_min * n, cur_max * n, n)
            cur_min = min(cur_min * n, tmp_max, n)
            global_max = max(global_max, cur_max)
            
        return global_max

