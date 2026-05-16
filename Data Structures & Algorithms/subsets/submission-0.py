class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset)
                return

            # don't include the element 
            backtrack(i + 1, subset.copy())
            
            # don't include the element
            subset.append(nums[i])
            backtrack(i + 1, subset.copy())

        backtrack(0, [])
        return res