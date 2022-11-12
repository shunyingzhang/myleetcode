class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crcToPre = {i: [] for i in range(numCourses)}
        visited = set()
        res = []
        
        if prerequisites == []:
            for i in range(numCourses):
                res.append(i)
        
        for crc, pre in prerequisites:
            crcToPre[crc].append(pre)
            
        def dfs(j):
            if j in visited:
                return False
            if crcToPre[j] == []:
                if j not in res:
                    res.append(j)
                return True
            
            visited.add(j)
            for pre in crcToPre[j]:
                if not dfs(pre): return False
                if pre not in res:
                    res.append(pre)
            visited.remove(j)
            crcToPre[j] = []
            if j not in res:
                res.append(j)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        
        return res