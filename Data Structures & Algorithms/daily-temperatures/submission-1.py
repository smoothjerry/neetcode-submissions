class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [[temperatures[0], 0]]
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                _, pastIndex = stack.pop()
                res[pastIndex] = i - pastIndex
            
            stack.append([temperatures[i], i])
        
        return res



        # stack = [(30, 0)]
        # stack[-1] = [(30, 0)] -> is 30 < 38? res[0] = index i - 0
        # monotonically decreasing stack
