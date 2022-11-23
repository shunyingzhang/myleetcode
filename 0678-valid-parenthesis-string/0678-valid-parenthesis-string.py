class Solution:
    def checkValidString(self, s: str) -> bool:
        lMax = 0
        lMin = 0
        
        for c in s:
            if c == '(':
                lMax += 1
                lMin += 1
            elif c == '*':
                lMax += 1
                lMin -= 1
            else:
                lMax -= 1
                lMin -= 1
            if lMax < 0:
                return False
            if lMin < 0:
                lMin = 0
        
        return lMax >= 0 and lMin<= 0
        