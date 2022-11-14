class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        NodeToNode = {i: [] for i in range(n + 1)}
        for a, b, c in times:
            NodeToNode[a].append([b, c])
        
        q = [[0, k]]
        t = 0
        visited = set()
        
        while q:
            w1, n1 = heapq.heappop(q)
            if n1 in visited:
                continue
            
            t = max(t, w1)
            visited.add(n1)
            for n2, w2 in NodeToNode[n1]:
                if n2 not in visited:
                    heapq.heappush(q, [w2 + w1, n2])
                    
        return t if len(visited) == n else -1
            
        
        