class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start

                
                
            
        
#         for i in range(len(gas)):
#             g = 0
#             flag = 0
#             if gas[i] == cost[i] and len(gas) == 1:
#                 return i
#             if gas[i] > cost[i]:
#                 g += gas[i] - cost[i]
#                 flag = 1
                
#                 if i == len(gas) - 1:
#                     for j in range(len(gas) - 1):
#                         if g <= 0:
#                             continue
#                         g += gas[j] - cost[j]
#                         flag = i - j
#                 else: 
#                     for j in range((i + 1), len(gas)):
#                         if g <= 0:
#                             continue
#                         g += gas[j] - cost[j]
#                         if i == 0:
#                             flag = i - j + len(gas)
#                         else:
#                             flag = i - j
#                     if g < 0:
#                         continue
#                     if i > 0:
#                         for j in range(i):
#                             if g <= 0:
#                                 continue
#                             g += gas[j] - cost[j]
#                             if i == 0:
#                                 flag = i - j + len(gas)
#                             else:
#                                 flag = i - j
#             if g < 0:
#                 continue
#             # if i == 0 and j == 2:
#             #     return g, flag
#             if g >= 0 and flag == 1:
#                 return i
#         return -1
                    
                
                
                
        