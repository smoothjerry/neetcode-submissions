class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        return max(self.helper(nums[1:]), self.helper(nums[:len(nums) - 1]))
    
    def helper(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            newRob = max(rob2, num + rob1)
            rob1 = rob2
            rob2 = newRob
        return rob2