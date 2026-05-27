class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combo, res = [], []
        def backtrack(i, workingSum):
            if i >= len(nums) or workingSum > target:
                return
            
            if workingSum == target:
                res.append(combo.copy())
                return
            
            # include index i again
            combo.append(nums[i])
            backtrack(i, workingSum + nums[i])

            # move on from i
            combo.pop()
            backtrack(i + 1, workingSum)
        

        backtrack(0, 0)
        return res