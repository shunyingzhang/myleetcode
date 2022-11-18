class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        dp[(len(prices) + 1, True)]= 0
        dp[(len(prices), True)] = 0
        dp[(len(prices) + 1, False)] = 0
        dp[(len(prices), False)] = 0
        
        for i in range(len(prices) - 1, -1, -1):
            dp[(i, True)] = max(dp[(i + 1, True)], dp[(i + 1, False)] - prices[i])
            dp[(i, False)] = max(dp[(i + 1, False)], dp[(i + 2, True)] + prices[i])
            
        return dp[(0, True)]
            