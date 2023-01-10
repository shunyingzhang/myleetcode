class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        for i, intv in enumerate(intervals):
            if i == 0:
                new = intv
                continue
            if intv[1] <= new[1]:
                res += 1
            elif intv[0] == new[0]:
                res += 1
                if intv[1] > new[1]:
                    new = intv
            else:
                new = intv
        return len(intervals) - res