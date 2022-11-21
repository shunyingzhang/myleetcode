class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= target - i:
                target = i
        
        return not target
        
        
#         dp = [False] * len(nums)
#         dp[len(nums) - 1] = True
        
#         for i in range(len(nums) - 2, -1, -1):
#             if nums[i] == 0:
#                 continue
                
#             for j in range(nums[i], -1, -1):
#                 if j == 0:
#                     continue
#                 if dp[i]:
#                     continue
#                 if (i + j) < len(nums):
#                     dp[i] = dp[i + j]
#                 if dp[i]:
#                     continue
        
#         return dp[0]