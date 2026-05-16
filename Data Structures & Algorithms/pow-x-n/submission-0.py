class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(base, exp):
            if exp == 0:
                return 1
            
            if exp % 2 == 0:
                return self.myPow((base * base), exp // 2)
            
            return base * self.myPow(base * base, exp // 2)
        
        res = pow(x, abs(n))
        if n < 0:
            res = 1 / res
        
        return res
