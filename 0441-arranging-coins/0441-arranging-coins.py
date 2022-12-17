class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n
        res = 1
        while l <= r:
            m = (l + r) // 2
            if m * (1 + m) // 2 < n:
                l = m + 1
                res = max(res, m)
            elif m * (1 + m) // 2 > n:
                r = m - 1
            else:
                return m
        
        return res
        
        