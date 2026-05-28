class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

        # n = 2
        # 1 + 1 (take one step to first step, take one step to second step)
        # 2 (take two steps from the floor to second step)
        # = 2 ways to climb the stairs
        # dp[0] = 1
        # dp[1] = 2
