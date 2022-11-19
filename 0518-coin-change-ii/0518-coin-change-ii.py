class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [0] * (amount + 1)
        
        for i in range(len(coins) - 1, -1, -1):
            newDp = [0] * (amount + 1)
            newDp[0] = 1
            for j in range(1, amount + 1):
                if coins[i] <= j:
                    newDp[j] = newDp[j - coins[i]] + dp[j]
            dp = newDp
        
        return dp[amount]
        