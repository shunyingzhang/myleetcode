class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit_t = prices[r] - prices[l]
                profit = max(profit_t, profit)
            else:
                l = r
                
            r += 1
            
        return profit