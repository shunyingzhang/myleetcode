class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float('inf')] * n
        cost[src] = 0
        
        for i in range(k + 1):
            costTmp = cost.copy()
            for s, d, p in flights:
                if cost[s] == float('inf'):
                    continue
                if cost[s] + p < costTmp[d]:
                    costTmp[d] = cost[s] + p
            cost = costTmp.copy()
                
                
        return -1 if cost[dst] == float("inf") else cost[dst]
        