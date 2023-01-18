class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0
        a = a[::-1]
        b = b[::-1]
        
        for i in range(max(len(a), len(b))):
            if i < len(a):
                va = int(a[i])
            else:
                va = 0    
            if i < len(b):
                vb = int(b[i])
            else:
                vb = 0
            
            vlu = va + vb + carry
            res = str(vlu % 2) + res 
            carry = vlu // 2
            
        if carry:
            res = '1' + res
        return res