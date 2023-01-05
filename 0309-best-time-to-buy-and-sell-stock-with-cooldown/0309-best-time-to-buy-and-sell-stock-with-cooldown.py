class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        dp[(len(prices), True)] = 0
        dp[(len(prices), False)] = 0
        dp[(len(prices) + 1, True)] = 0
        
        for i in range(len(prices) - 1, -1, -1):
            buy = dp[(i + 1, False)] - prices[i]
            cooling = dp[(i + 1), True]
            dp[(i, True)] = max(buy, cooling)
            
            sell = prices[i] + dp[(i + 2), True]
            cooling = dp[(i + 1), False]
            dp[(i, False)] = max(sell, cooling)
        return dp[(0, True)]
        
#         dp = {}
        
#         def dfs(i, buying):
#             if i >= len(prices):
#                 return 0
#             if (i, buying) in dp:
#                 return dp[(i, buying)]
            
#             if buying:
#                 buy = dfs(i + 1, not buying) - prices[i]
#                 cooldown = dfs(i + 1, buying)
#                 dp[(i, buying)] = max(buy, cooldown)
#             else:
#                 sell = dfs(i + 2, not buying) + prices[i]
#                 cooldown = dfs(i + 1, buying)
#                 dp[(i, buying)] = max(sell, cooldown)
#             return dp[(i, buying)]
        
#         return dfs(0, True)
        
#         dp[(len(prices) + 1, True)]= 0
#         dp[(len(prices), True)] = 0
#         dp[(len(prices) + 1, False)] = 0
#         dp[(len(prices), False)] = 0
        
#         for i in range(len(prices) - 1, -1, -1):
#             dp[(i, True)] = max(dp[(i + 1, True)], dp[(i + 1, False)] - prices[i])
#             dp[(i, False)] = max(dp[(i + 1, False)], dp[(i + 2, True)] + prices[i])
            
#         return dp[(0, True)]
            