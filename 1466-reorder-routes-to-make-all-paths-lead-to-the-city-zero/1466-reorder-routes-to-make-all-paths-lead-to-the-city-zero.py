class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a, b in connections}
        neighbors = {city: [] for city in range(n)}
        
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        change = 0
        visited = set()
        
        def dfs(city):
            nonlocal change
            visited.add(city)
            for nei in neighbors[city]:
                if nei not in visited:
                    if (nei, city) not in edges:
                        change += 1
                    dfs(nei)
        
        dfs(0)
        return change
        
        