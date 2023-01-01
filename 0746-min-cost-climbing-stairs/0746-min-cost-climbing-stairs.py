class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        zero = 0
        one = cost[n - 1]
        
        for i in range(n - 2, -1, -1):
            tmp = one
            one = cost[i] + min(one, zero)
            zero = tmp
        
        return min(zero, one)
        
        
        
#         n = len(cost)
#         one = 0
#         two = cost[n - 1]
        
#         for i in range(n - 1):
#             tmp = two
#             two = cost[n - 2 - i] + min(two, one)
#             one = tmp
        
#         return min(one, two)
            
        