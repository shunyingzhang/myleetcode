class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heapmax = [[-cnt, key] for key, cnt in count.items()]
        heapq.heapify(heapmax)
        waiting = []
        res = ''
        for i in range(len(s)):
    
            while waiting and waiting[0][0] <= i:
                wait = heapq.heappop(waiting)
                heapq.heappush(heapmax, [wait[1], wait[2]])
                
            if len(heapmax) == 0:
                return ''
    
            count, key = heapq.heappop(heapmax)
  
            res += key
            count += 1
            if count != 0:
                heapq.heappush(waiting, [i + 2, count, key])

        
        return res
        