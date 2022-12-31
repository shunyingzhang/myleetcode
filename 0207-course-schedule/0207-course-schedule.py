class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crcToPre = {i: [] for i in range(numCourses)}
        cycle = set()
        
        for crc, pre in prerequisites:
            crcToPre[crc].append(pre)
        
        def dfs(i):
            if i in cycle:
                return False
            if not crcToPre[i]:
                return True
            cycle.add(i)
            for pre in crcToPre[i]:
                if not dfs(pre):
                    return False
            cycle.remove(i)
            crcToPre[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        
        
        
        
        
#         crcToPre ={i: [] for i in range(numCourses)}
#         cycle = set()
        
#         for crc, pre in prerequisites:
#             crcToPre[crc].append(pre)
        
#         def dfs(j):
#             if j in cycle:
#                 return False
#             if crcToPre[j] == []:
#                 return True
            
#             cycle.add(j)
#             for pre in crcToPre[j]:
#                 if not dfs(pre): return False
#             cycle.remove(j)
#             crcToPre[j] = []
#             return True
        
#         for i in range(numCourses):
#             if not dfs(i): return False
        
#         return True
        