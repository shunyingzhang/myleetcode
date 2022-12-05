class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1] * len(nums)
        
        for i, n in enumerate(nums):
            res[i] = prefix
            prefix = res[i] * n
        
        postfix = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= postfix
            postfix = nums[i] * postfix
        
        return res
        
        
        
        
        
#         res = [1] * len(nums)
#         pre_ind = 1
#         for i in range(len(nums)):
#             res[i] *= pre_ind
#             pre_ind *= nums[i]
        
#         post_ind = 1
#         for i in range(len(nums)-1, -1, -1):
#             res[i] *= post_ind
#             post_ind *= nums[i]
        
#         return res
        