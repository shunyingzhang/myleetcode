class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        maxMin = {i : [] for i in range(len(nums))}
        
        maxMin[0].append(nums[0])
        maxMin[0].append(nums[0])
        
        res = nums[0]
        
        for i in range(1, len(nums)):
            maxMin[i].append(max(nums[i], 
                                 nums[i] * maxMin[i - 1][0], 
                                 nums[i] * maxMin[i - 1][1]))
            res = max(res, maxMin[i][0])
            maxMin[i].append(min(nums[i], nums[i] * maxMin[i - 1][0], nums[i] * maxMin[i - 1][1]))
        
        return res
        