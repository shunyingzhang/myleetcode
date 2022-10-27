class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n = len(nums) - k
        
        while n > 0:
            heapq.heappop(nums)
            n -= 1
            
        return nums[0]
        