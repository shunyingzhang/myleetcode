class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        longest = 1
        
        for i in range(len(nums) - 2, -1, -1):
            tmp2 = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    tmp1 = 1 + dp[j]
                    tmp2 = max(tmp1, tmp2)
            dp[i] = tmp2
            longest = max(longest, dp[i])
        
        return longest
            
        