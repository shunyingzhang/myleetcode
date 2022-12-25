class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        
        def dfs(i, summ):
            if i == len(candidates):
                return
            if summ > target:
                return
            if summ == target:
                res.append(sub.copy())
                return
            
            sub.append(candidates[i])
            dfs(i, summ + candidates[i])
            
            sub.pop()
            dfs(i + 1, summ)
            
        dfs(0, 0)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
        
#         def dfs(i, cur, total):
#             if total == target:
#                 res.append(cur.copy())
#                 return
#             if i >= len(candidates) or total > target:
#                 return
            
#             cur.append(candidates[i])
#             dfs(i, cur, total + candidates[i])
#             cur.pop()
#             dfs(i + 1, cur, total)
            
#         curr = []
#         dfs(0, curr, 0)
        
#         return res