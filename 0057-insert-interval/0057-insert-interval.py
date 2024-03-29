class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, intv in enumerate(intervals):
            if intv[1] < newInterval[0]:
                res.append(intv)
            elif intv[0]> newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]      
            else:
                newInterval[0] = min(intv[0], newInterval[0])
                newInterval[1] = max(intv[1], newInterval[1])
        res.append(newInterval)
        return res
        
        
#         n = len(intervals) 
#         res = []
#         for i in range(len(intervals)):
#             if newInterval[1] < intervals[i][0]:
#                 res.append(newInterval)
#                 return res + intervals[i:]
#             elif newInterval[0] > intervals[i][1]:
#                 res.append(intervals[i])
#             else:
#                 newInterval[0] = min(newInterval[0], intervals[i][0])
#                 newInterval[1] = max(newInterval[1], intervals[i][1])
            
#         res.append(newInterval)
#         return res
                
            
                
                    