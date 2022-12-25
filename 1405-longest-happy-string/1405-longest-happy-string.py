class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heapmin = []
        if a:
            heapq.heappush(heapmin, [-a, 'a'])
        if b:
            heapq.heappush(heapmin, [-b, 'b'])
        if c:
            heapq.heappush(heapmin, [-c, 'c'])
        
        res = ''
        while heapmin:
            cnt, c = heapq.heappop(heapmin)
            if len(res) >= 2 and res[-1] == res[-2] == c:
                if not heapmin:
                    break
                cnt2, c2 = heapq.heappop(heapmin)
                res += c2
                cnt2 += 1
                
                if cnt2 != 0:
                    heapq.heappush(heapmin, [cnt2, c2])
            else:
                res += c
                cnt += 1
            
            if cnt != 0:
                heapq.heappush(heapmin, [cnt, c])
                
        return res
        