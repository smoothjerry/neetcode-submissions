class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        majority = len(nums) / 2
        for num in nums:
            counts[num] = counts[num] + 1
            if counts[num] > majority:
                return num
        
        return