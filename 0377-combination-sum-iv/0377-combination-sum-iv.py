class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if nums[j] <= i:
                    dp[i] += dp[i - nums[j]]
        
        return dp[target]
        
        
        
#         def dfs(tgt):
#             if tgt == 0:
#                 return 1
#             if tgt < 0:
#                 return 0
#             res = 0
#             for i in range(len(nums)):
#                 res += dfs(tgt - nums[i])
            
#             return res
#         return dfs(target)