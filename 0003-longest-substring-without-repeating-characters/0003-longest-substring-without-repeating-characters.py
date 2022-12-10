class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1
            cSet.add(s[r])
            res = max(res, r - l + 1)
        return res
            
        
        
        
        
        
        
#         c_set = set()
#         res = 0
#         l = 0
        
#         for r in range(len(s)):
#             while s[r] in c_set:
#                 c_set.remove(s[l])
#                 l += 1
#             c_set.add(s[r])
#             res = max(res, r - l + 1)
        
#         return res
            