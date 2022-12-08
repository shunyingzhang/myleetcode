class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0: 0}
        for w in wall:
            length = 0
            for i in range(len(w) - 1):
                length += w[i]
                countGap[length] = 1 + countGap.get(length, 0)
        
        res = len(wall) - max(countGap.values())
    
        
        return res


        # res = len(wall)
        # cross = {i: [0, 0] for i in range(len(wall))}
        # minVal = min(wall[0])
        # for w in wall:
        #     minVal = min(minVal, min(w))
        # for i in range(minVal, sum(wall[0]), minVal):
        #     tmp = 0
        #     for j in range(len(wall)):
        #         if i > cross[j][0]:
        #             cross[j][0] += wall[j][cross[j][1]]
        #             cross[j][1] += 1
        #         if i < cross[j][0]:
        #             tmp += 1
        #     res = min(res, tmp)
        # return res
