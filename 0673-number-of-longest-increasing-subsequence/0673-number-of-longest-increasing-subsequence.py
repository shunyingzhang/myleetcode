class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        dp = {i: [1, 1] for i in range(len(nums))}
        lenLIS = 0
        res = 0
        
        for i in range(len(nums) - 1, -1, -1):
            maxsub = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    sub = dp[j][0] + 1
                    if sub > maxsub:
                        dp[i][1] = dp[j][1]
                        maxsub = sub
                    elif sub == maxsub:
                        dp[i][1] += dp[j][1]
                    dp[i][0] = max(dp[i][0], dp[j][0] + 1)
            
            if dp[i][0] == lenLIS:
                res += dp[i][1]
    
            elif dp[i][0] > lenLIS:
                lenLIS = dp[i][0]
                res = dp[i][1]
                
 
        return res
            
                    
                
 