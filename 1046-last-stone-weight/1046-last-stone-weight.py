class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -abs(x - y))
        if stones:
            return -stones[0]
        else:
            return 0
        
        
        
        
        
        
        
        
        
        
#         stones = [-s for s in stones]
#         heapq.heapify(stones)
#         while len(stones) > 1:
#             y = heapq.heappop(stones)
#             x = heapq.heappop(stones)
#             if x != y:
#                 heapq.heappush(stones, y - x)
        
#         if len(stones):
#             return abs(stones[0])
#         else:
#             return 0
        