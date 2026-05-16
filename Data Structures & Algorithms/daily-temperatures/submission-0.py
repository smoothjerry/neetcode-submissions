class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            k = i + 1
            while k < len(temperatures):
                if temperatures[k] > temperatures[i]:
                    res.append(k - i)
                    break
                k += 1
                
            if k == len(temperatures):
                res.append(0)
        return res
