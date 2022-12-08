class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 0
        tmp2 = 0
        while r < len(prices):
            tmp1 = prices[r] - prices[l]
            if tmp1 > 0:
                if tmp1 >= tmp2:
                    tmp2 = tmp1
                else:
                    profit += tmp2
                    tmp2 = 0
                    l = r
            else:
                profit += tmp2
                tmp2 = 0
                l = r
            r += 1
            
        if tmp2:
            profit += tmp2
        
        return profit
        