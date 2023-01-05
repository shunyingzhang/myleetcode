class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        row = [0] * (amount + 1)
        row[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            tmp = row.copy()
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    tmp[j] = row[j] + tmp[j - coins[i]]
            row = tmp
        return row[amount]
        
#         cache = {}

#         def dfs(i, a):
            
    
#             if (i, a) in cache:
#                 return cache[(i, a)]

#             cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
#             return cache[(i, a)]

#         return dfs(0, 0)
            
        
        
#         coins.sort()
#         dp = [0] * (amount + 1)
        
#         for i in range(len(coins) - 1, -1, -1):
#             newDp = [0] * (amount + 1)
#             newDp[0] = 1
#             for j in range(1, amount + 1):
#                 if coins[i] <= j:
#                     newDp[j] = newDp[j - coins[i]] + dp[j]
#             dp = newDp
        
#         return dp[amount]

        