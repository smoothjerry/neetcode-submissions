class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            if i >= len(nums):
                res.append(subset)
                return
            
            # include i
            subset.append(nums[i])
            backtrack(i + 1, subset.copy())
            subset.pop()

            # don't include i
            backtrack(i + 1, subset)
        

        backtrack(0, [])
        return res