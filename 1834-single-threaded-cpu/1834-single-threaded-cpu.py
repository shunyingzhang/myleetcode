class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda t: t[0])
        tasks = deque(tasks)
        
        t = tasks[0][0]
        # availble = t
        heapmin = []
        heapq.heapify(heapmin)
        res = []
    
        while tasks or heapmin:
            while tasks and tasks[0][0] <= t:
                task = tasks.popleft()
                heapq.heappush(heapmin, [task[1], task[2]])
                
            if heapmin:
                task = heapq.heappop(heapmin)
                res.append(task[1])
                t += task[0]
            else:
                t = tasks[0][0]
            
        return res
        