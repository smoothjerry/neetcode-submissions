class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 2, -1 , -1):
            maxJumps = nums[i]
            for j in range(i + 1, maxJumps + i + 1):
                if j < len(nums):
                    dp[i] = min(dp[i], 1 + dp[j])

        return dp[0]