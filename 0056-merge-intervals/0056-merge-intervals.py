class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i, intv in enumerate(intervals):
            if i == 0:
                new = intv
                continue
            if intv[0] <= new[1]:
                new[0] = min(new[0], intv[0])
                new[1] = max(new[1], intv[1])
            else:
                res.append(new)
                new = intv
        res.append(new)    
        return res
        
        
#         intervals.sort()
#         res = []
#         interNew = intervals[0]
        
#         for i in range(len(intervals)):
#             if interNew[1] < intervals[i][0]:
#                 res.append(interNew)
#                 interNew = intervals[i]
#             elif interNew[0] > intervals[i][1]:
#                 res.append(intervals[i])
#             else:
#                 interNew[0] = min(interNew[0], intervals[i][0])
#                 interNew[1] = max(interNew[1], intervals[i][1])
            
#         res.append(interNew)
#         return res
        