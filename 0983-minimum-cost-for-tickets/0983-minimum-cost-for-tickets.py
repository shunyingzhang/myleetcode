class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * (len(days) + 1)
        dp[len(days)] = 0
        
        for i in range(len(days) -1, -1, -1):
            for d, p in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], p + dp[j])
        return dp[0]
        
#         dp = {}
  
#         def dfs(i):
#             if i == len(days):
#                 return 0
#             if i in dp:
#                 return dp[i]
#             dp[i] = float('inf')
#             for d, p in zip([1, 7, 30], costs):
#                 j = i
#                 while j < len(days) and days[j] < days[i] + d:
#                     j += 1
#                 dp[i] = min(dp[i], p + dfs(j))
#             return dp[i]
#         return dfs(0)