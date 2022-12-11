class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        tgt1 = ''
        tgt2 = ''
        
        for i in range(2 * n):
            if i % 2 == 0:
                tgt1 += '0'
                tgt2 += '1'
            else:
                tgt1 += '1'
                tgt2 += '0'

        diff1 = 0
        diff2 = 0
        resMin = 0
                       
        for i in range(n):
            if s[i] != tgt1[i]:
                diff1 += 1
            if s[i] != tgt2[i]:
                diff2 += 1
        resMin = min(diff1, diff2)
        
        l = 1
        for r in range(n, 2 * n):
            if s[l - 1] != tgt1[l - 1]:
                diff1 -= 1
            if s[l - 1] != tgt2[l - 1]:
                diff2 -= 1
            
            if s[r] != tgt1[r]:
                diff1 += 1
            if s[r] != tgt2[r]:
                diff2 += 1
            
            resMin = min(resMin, diff1, diff2)
            l += 1
        
        return resMin
        
        
                
            
        
        