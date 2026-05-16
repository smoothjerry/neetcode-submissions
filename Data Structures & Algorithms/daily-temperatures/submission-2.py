class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            
            if not stack:
                res[i] = 0
            else:
                res[i] = stack[-1][1] - i
            
            stack.append([temperatures[i], i])
        
        return res



        # stack = [(30, 0)]
        # stack[-1] = [(30, 0)] -> is 30 < 38? res[0] = index i - 0
        # monotonically decreasing stack
