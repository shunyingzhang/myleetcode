class Solution:
    def myPow(self, x: float, n: int) -> float:
    
        if n == 0:
            return 1
        if x == 0:
            return 0
        
        def helper(a, b):
            if b == 0:
                return 1
            
            res = helper(a * a, b // 2)
            return a * res if b % 2 else res
        
        res = helper(x, abs(n))
        
        return res if n > 0 else 1 / res
        