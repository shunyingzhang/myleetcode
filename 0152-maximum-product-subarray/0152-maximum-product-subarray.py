class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxn = 1
        minn = 1
        
        for n in nums:
            if n == 0:
                maxn = 1
                minn = 1
                continue
            tmp = maxn
            maxn = max(tmp * n, minn * n, n)
            minn = min(tmp * n, minn * n, n)
            res = max(res, maxn)
        
        return res
        
#         if len(nums) == 1:
#             return nums[0]
        
#         curMax = 1
#         curMin = 1
        
#         res = nums[0]
        
#         for c in nums:
#             tmp = curMax
#             curMax = max(c, c*curMax, c*curMin)
#             curMin = min(c, c*tmp, c*curMin)
#             res = max(res, curMax)
        
#         return res
        