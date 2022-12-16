class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        for n in num:
            if not res:
                res.append(n)
                continue
            while res and n < res[-1] and k > 0:
                res.pop()
                k -= 1
            res.append(n)
        while k > 0 and res:
            res.pop()
            k -= 1
        
        if res:
            return str(int(''.join(res)))
        else:
            return '0'

                
                
        