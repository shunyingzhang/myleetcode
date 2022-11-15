class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one = 0
        two = cost[n - 1]
        
        for i in range(n - 1):
            tmp = two
            two = cost[n - 1 - (i + 1)] + min(two, one)
            one = tmp
        
        return min(one, two)
            
        