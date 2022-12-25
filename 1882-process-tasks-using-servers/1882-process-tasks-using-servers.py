class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        heapmin = []
        heapq.heapify(heapmin)
        for i, n in enumerate(servers):
            heapq.heappush(heapmin, [n, i])
            
        t = 0
        process = []
        heapq.heapify(process)
        res = []
        for i, task in enumerate(tasks):
            t = max(t, i)
            if len(heapmin) == 0:
                t = process[0][0]
            while process and process[0][0] <= t:
                time, weight, num= heapq.heappop(process)
                heapq.heappush(heapmin, [weight, num])
                
            weight, num = heapq.heappop(heapmin)   
            res.append(num)
            heapq.heappush(process, [t + task, weight, num])            
        
        return res
        
        