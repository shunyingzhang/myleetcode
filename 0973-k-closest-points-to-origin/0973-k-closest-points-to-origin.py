class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heapmin = []
        for x, y in points:
            heapmin.append([x ** 2 + y ** 2, x, y])
        
        heapq.heapify(heapmin)
        res = []
        while k > 0:
            dis, x, y = heapq.heappop(heapmin)
            res.append([x, y])
            k -= 1
        return res
        
        
        
        
        
        
        
        
        
        
#         minHeap = []
        
#         for x, y in points:
#             minHeap.append([x ** 2 + y ** 2, x, y])
            
#         heapq.heapify(minHeap)
#         res = []
        
#         while k > 0:
#             dis, x, y = heapq.heappop(minHeap)
#             res.append([x, y])
#             k -=1
            
#         return res
        