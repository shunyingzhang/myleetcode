class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        k = len(nums) - k
        while k > 0:
            heapq.heappop(nums)
            k -= 1
        
        return nums[0]
        
        
        
        
        
        
        
        
#         heapq.heapify(nums)
#         n = len(nums) - k
        
#         while n > 0:
#             heapq.heappop(nums)
#             n -= 1
            
#         return nums[0]
        