class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        i = 0
        while l <= r:
            if abs(nums[r]) >= abs(nums[l]):
                res[i] = nums[r] ** 2
                r -= 1
            else:
                res[i] = nums[l] ** 2
                l += 1
            i += 1
        return res[::-1]
            
        
        
        
        return res
        