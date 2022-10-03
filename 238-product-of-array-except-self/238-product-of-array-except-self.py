class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre_ind = 1
        for i in range(len(nums)):
            res[i] *= pre_ind
            pre_ind *= nums[i]
        
        post_ind = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post_ind
            post_ind *= nums[i]
        
        return res
        