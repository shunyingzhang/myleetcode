class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crcToPre ={i: [] for i in range(numCourses)}
        visited = set()
        
        for crc, pre in prerequisites:
            crcToPre[crc].append(pre)
        
        def dfs(j):
            if j in visited:
                return False
            if crcToPre[j] == []:
                return True
            
            visited.add(j)
            for pre in crcToPre[j]:
                if not dfs(pre): return False
            visited.remove(j)
            crcToPre[j] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True
        