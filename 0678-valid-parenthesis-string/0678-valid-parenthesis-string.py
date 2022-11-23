class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        
        def dfs(i, left):
            if i == len(s):
                return left == 0
            if left < 0:
                return False
            if (i, left) in dp:
                return dp[(i, left)]
            
            if s[i] == '(':
                dp[(i, left)] = dfs(i + 1, left + 1)
            if s[i] == ')':
                dp[(i, left)] = dfs(i + 1, left - 1)
            if s[i] == '*':
                dp[(i, left)] = (dfs(i + 1, left + 1) or dfs(i + 1, left - 1) 
                or dfs(i + 1, left))
            return dp[(i, left)]
                      
                      
        return dfs(0, 0)
        
        
#         lMax = 0
#         lMin = 0
        
#         for c in s:
#             if c == '(':
#                 lMax += 1
#                 lMin += 1
#             elif c == '*':
#                 lMax += 1
#                 lMin -= 1
#             else:
#                 lMax -= 1
#                 lMin -= 1
#             if lMax < 0:
#                 return False
#             if lMin < 0:
#                 lMin = 0
        
#         return lMin == 0
        