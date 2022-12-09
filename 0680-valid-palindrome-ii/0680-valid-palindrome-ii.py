class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        
        while l < r:
            if s[l] != s[r]:
                skpLeft = s[l + 1: r + 1]
                skpRgt = s[l: r]
                return skpLeft == skpLeft[::-1] or skpRgt == skpRgt[::-1] 
            
            l += 1
            r -= 1
        
        return True
        
        
        