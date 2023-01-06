class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxsum = float('-inf')
        for n in nums:
            if cursum < 0:
                cursum = 0
            cursum += n
            maxsum = max(maxsum, cursum)
        return maxsum
        
        
        
        
        
        
        
#         maxSub = nums[0]
#         curSum = 0
        
#         for n in nums:
#             if curSum < 0:
#                 curSum = 0
#             curSum += n
#             maxSub = max(curSum, maxSub)
        
#         return maxSub