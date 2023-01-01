class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):

            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
         
            l = i
            r = i + 1
 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        return res
        
        
        
        
#         res = 0
#         lenP = 0
        
#         for i in range(len(s)):
#             l = i
#             r = i
#             while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
#                 l -= 1
#                 r += 1
#             lenP += int((r - l) / 2)
            
#             l = i
#             r = i + 1
#             while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
#                 l -= 1
#                 r += 1
#             lenP += int((r - l - 1) / 2)
            
#         return lenP