class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[l]
        
        while l <= r:
            m = (l + r) // 2
            #Left sorted array
            if nums[m] >= nums[l]:
                res = min(nums[l], res)
                l = m + 1
            else:
                res = min(nums[m], res)
                r = m - 1
        
        return res
            
        
        
        
        
        
#         l = 0
#         r = len(nums) - 1
#         res = nums[l]
        
#         while l <= r:
#             m = (l + r) // 2
#             res = min(res, nums[m])
#             if nums[l] <= nums[m]:
#                 if nums[m] >= nums[r]:
#                     l = m + 1
#                 else:
#                     r = m - 1
#             else:
#                 if nums[m] <= nums[r]:
#                     r = m - 1
#                 else:
#                     l = m + 1
#         return res
                
            