class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heapmax = [-cnt for cnt in count.values()]
        heapq.heapify(heapmax)
        queue = []
        t = 0
        while heapmax or queue:
            t += 1
            if heapmax:
                task = heapq.heappop(heapmax)
                task += 1
                if task != 0:
                    queue.append([task, t + n])

            while queue and queue[0][1] <= t:
                heapq.heappush(heapmax, queue.pop()[0])
            
        return t
        
        
        
        
        
        
        
        
        
#         count = Counter(tasks)
#         HeapMax = [-cnt for cnt in count.values()]
#         heapq.heapify(HeapMax)
        
#         queue = deque()
#         t = 0
        
#         while HeapMax or queue:
#             t += 1
#             if HeapMax:
#                 cnt = 1 + heapq.heappop(HeapMax)
#                 if cnt:
#                     queue.append([cnt, t + n])
            
#             if queue and queue[0][1] == t:
#                 heapq.heappush(HeapMax, queue.popleft()[0])
        
#         return t