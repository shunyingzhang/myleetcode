class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heapmin = nums
        self.k = k
        heapq.heapify(self.heapmin)
        while len(self.heapmin) > k:
            heapq.heappop(self.heapmin)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heapmin, val)
        if len(self.heapmin) > self.k:
             heapq.heappop(self.heapmin)
        return self.heapmin[0]

        
        
        
        
        
        
#         self.heapmin = nums
#         self.k = k
#         heapq.heapify(self.heapmin)
#         while len(self.heapmin) > k:
#             heapq.heappop(self.heapmin)

#     def add(self, val: int) -> int:
#         heapq.heappush(self.heapmin, val)
#         while len(self.heapmin) > self.k:
#             heapq.heappop(self.heapmin)
        
#         return self.heapmin[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)