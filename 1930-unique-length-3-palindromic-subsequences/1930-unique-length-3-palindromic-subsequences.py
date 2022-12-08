class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = collections.Counter(s)
        
        for c in s:
            right[c] -= 1
            if right[c] == 0:
                right.pop(c)
            
            for i in range(26):
                pc = chr(ord('a') + i)
                if pc in left and pc in right:
                    res.add((c, pc))
            left.add(c)
        
        return len(res)
        