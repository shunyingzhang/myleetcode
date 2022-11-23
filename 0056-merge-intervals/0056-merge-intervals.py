class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        interNew = intervals[0]
        
        for i in range(len(intervals)):
            if interNew[1] < intervals[i][0]:
                res.append(interNew)
                interNew = intervals[i]
            elif interNew[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                interNew[0] = min(interNew[0], intervals[i][0])
                interNew[1] = max(interNew[1], intervals[i][1])
            
        res.append(interNew)
        return res
        