class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = 0
        total = 0
        frq = 0
        while r < len(nums):
            total += nums[r]
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            
            frq = max(frq, r - l + 1)
            r += 1
            
        return frq
            
            
                
        
        
#         nums.sort()
#         maxFrq = 0
#         for r in range(len(nums) - 2, -1, -1):
#             l = r
#             target = nums[r + 1]
#             frq = 1
#             rsh = k
#             while rsh > 0 and l >= 0:
#                 rsh = rsh - (target - nums[l])
#                 if rsh >= 0:
#                     l -= 1
#                     frq += 1

#             maxFrq = max(maxFrq, frq)
        
#         return maxFrq