class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquare(num):
            output = 0
            while num:
                output += (num % 10) ** 2
                num = num // 10
            return output
        
        loop = set()
        while n not in loop:
            loop.add(n)
            n = sumSquare(n)
        
        return n == 1
        
        
        