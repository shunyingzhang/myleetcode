class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        disPoint = {i: [] for i in range(N)}
        
        for i in range(N):
            for j in range(i + 1, N):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                disPoint[i].append([dis, j])
                disPoint[j].append([dis, i])
        
        res = 0
        MinHeap = [[0, 0]]
        visited = set()
        
        while len(visited) < N:
            cost, p = heapq.heappop(MinHeap)
            if p in visited:
                continue
            
            res += cost
            visited.add(p)
            for dis, nei in disPoint[p]:
                if nei not in visited:
                    heapq.heappush(MinHeap, [dis, nei])
            
        return res
        
        