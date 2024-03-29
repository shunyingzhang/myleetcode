class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        
        for i in range(1, amount + 1):
            minn = float('inf')
            for c in coins:
                if c > i:
                    continue
                n = 1 + dp[i - c]
                minn = min(minn, n)
            dp[i] = minn
        
        return dp[amount] if dp[amount] != float('inf') else -1
        
        
#         dp = [0] * (amount +  1)
        
#         for i in range(1, amount + 1):
#             dpi = float("inf")
#             for c in coins:
#                 if i < c:
#                     continue
#                 dpi = min(dpi, 1 + dp[i -c])
            
#             dp[i] = dpi
        
#         return dp[amount] if dp[amount] != float('inf') else -1
        