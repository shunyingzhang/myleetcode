class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        minh = []
        for i, ab in enumerate(costs):
            minh.append([ab[1] - ab[0], i])
        minh.sort()
   

        total = 0
        for i in range(len(costs)):
            if i < len(costs) // 2:
                total += costs[minh[i][1]][1]
            else:
                total += costs[minh[i][1]][0] 
        return total