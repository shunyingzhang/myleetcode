class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heapmin = []
        for n in nums:
            heapq.heappush(heapmin, int(n))
            
        k =  len(nums) - k
        while k > 0:
            heapq.heappop(heapmin)
            k -= 1
            
            
        return str(heapmin[0])