class Solution:
    def rob(self, nums: List[int]) -> int:
        zero = 0
        one = 0
        
        for n in nums:
            tmp = one
            one = max(n + zero, tmp)
            zero = tmp
        return one
        
        
        
        
#         n1 = 0
#         n2 = 0
#         for i in range(len(nums)):
#             tmp = n2
#             n2 = max(nums[i] + n1, n2)
#             n1 = tmp
        
#         return n2
            
            
# #         n = len(nums)
        
# #         for i in range(n - 3, -1, -1):
# #             nums[i] = nums[i] + max(nums[(i + 2):])
        
# #         return max(nums)
