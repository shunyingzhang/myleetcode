class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        CmbPS = [[p, s] for p, s in zip(position, speed)]
        CmbPS = sorted(CmbPS)[::-1]
        fleets = []
        
        for p, s in CmbPS:
            t = (target - p) / s
            if not fleets or t > fleets[-1]:
                fleets.append(t)
        return len(fleets)
        
        
        
        
        
#         combinePandS = [[p, s] for p, s in zip(position, speed)]
#         fleets = []
#         combinePandS = sorted(combinePandS)[::-1]
#         for p, s in combinePandS:
#             time = (target - p) / s
#             if not fleets or time > fleets[-1]:
#                 fleets.append(time)
#         return len(fleets)
        