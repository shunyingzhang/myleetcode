class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1
        while r < len(prices):
            profit_t = prices[r] - prices[l]
            if profit_t > 0:
                profit = max(profit_t, profit)
            else:
                l = r             
            r += 1
            
        return profit