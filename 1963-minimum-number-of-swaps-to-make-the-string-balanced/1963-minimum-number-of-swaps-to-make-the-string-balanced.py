class Solution:
    def minSwaps(self, s: str) -> int:
        close = 0
        maxClose = 0
        
        for c in s:
            if c == ']':
                close += 1
            else:
                close -= 1
            maxClose = max(close, maxClose)
            
        return maxClose // 2 + maxClose % 2
            
        