class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        curMax = 1
        curMin = 1
        
        res = nums[0]
        
        for c in nums:
            tmp = curMax
            curMax = max(c, c*curMax, c*curMin)
            curMin = min(c, c*tmp, c*curMin)
            res = max(res, curMax)
            # maxMin[i].append(max(nums[i], 
            #                      nums[i] * maxMin[i - 1][0], 
            #                      nums[i] * maxMin[i - 1][1]))
            # res = max(res, maxMin[i][0])
            # maxMin[i].append(min(nums[i], nums[i] * maxMin[i - 1][0], nums[i] * maxMin[i - 1][1]))
        
        return res
        