class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, t):
            if (i, t) in dp:
                return dp[(i, t)]
            if i == len(nums) and t == target:
                return 1
            if i == len(nums) and t != target:
                return 0
            dp[(i, t)] = dfs(i + 1, t - nums[i]) + dfs(i + 1, t + nums[i])
            return dp[(i, t)]
        return dfs(0, 0)
        
        
#         cache = {}
        
#         def dfs(i, t):
#             if i == len(nums):
#                 if t == target:
#                     return 1
#                 else:
#                     return 0
#             if (i, t) in cache:
#                 return cache[(i, t)]

#             cache[(i, t)] = dfs(i + 1, t - nums[i]) + dfs(i + 1, t + nums[i])
#             return cache[(i, t)]

        
#         return dfs(0, 0)
        