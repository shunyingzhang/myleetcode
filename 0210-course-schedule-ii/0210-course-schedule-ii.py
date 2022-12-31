class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crcToPre = {i: [] for i in range(numCourses)}
        cycle = set()
        visited = set()
        res = []
        
        for crc, pre in prerequisites:
            crcToPre[crc].append(pre)
        
        def dfs(i):
            if i in cycle:
                return False
            if i in visited:
                return True
            
            if not crcToPre[i]:
                visited.add(i)
                res.append(i)
                return True
            
            cycle.add(i)
            for pre in crcToPre[i]:
                if not dfs(pre):
                    return False
            visited.add(i)
            res.append(i)
            cycle.remove(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        
        
        
        
        
        
#         crcToPre = {i: [] for i in range(numCourses)}
#         cycle = set()
#         visited = set()
#         res = []
        
#         if prerequisites == []:
#             for i in range(numCourses):
#                 res.append(i)
#             return res
        
#         for crc, pre in prerequisites:
#             crcToPre[crc].append(pre)
            
#         def dfs(j):
#             if j in visited:
#                 return True
#             if j in cycle:
#                 return False

#             if crcToPre[j] == []:
#                 visited.add(j)
#                 res.append(j)
#                 return True
            
#             cycle.add(j)
#             for pre in crcToPre[j]:
#                 if not dfs(pre): return False
#             cycle.remove(j)
#             # crcToPre[j] = []
#             res.append(j)
#             visited.add(j)
#             return True
        
#         for i in range(numCourses):
#             if not dfs(i): return []
        
#         return res