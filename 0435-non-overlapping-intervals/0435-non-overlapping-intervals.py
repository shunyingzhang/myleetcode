class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        for i, intv in enumerate(intervals):
            if i == 0:
                new = intv
                continue
            if intv[0] < new[1]:
                res += 1
                if intv[1] < new[1]:
                    new = intv
            else:
                new = intv
        return res
        
#         intervals.sort()
#         overlap = intervals[0]
#         res = 0
        
#         for i in range(1, len(intervals)):
#             if intervals[i][0] < overlap[1]:
#                 res += 1
#                 if overlap[1] > intervals[i][1]:
#                     overlap = intervals[i]
#                 continue
            
#             overlap = intervals[i]
        
#         return res
        