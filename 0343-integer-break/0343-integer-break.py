class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        dp[n] = 0
        
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        
        return dp[n]