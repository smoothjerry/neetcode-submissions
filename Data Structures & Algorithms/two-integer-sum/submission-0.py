class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, num in enumerate(nums):
            if num not in mapping:
                mapping[num] = i
            
            complement = target - num
            if complement in mapping and mapping[complement] != i:
                return [mapping[complement], i]