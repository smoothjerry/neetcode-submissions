class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, num in enumerate(nums):
            if num not in complements:
                complements[num] = i
            
            c = target - num
            if c in complements and complements[c] != i:
                return [complements[c], i]
            
