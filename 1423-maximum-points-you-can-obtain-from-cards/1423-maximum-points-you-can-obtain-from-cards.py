class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # dp = {}
        # def dfs(i, j, p):
        #     nonlocal k
        #     if (i, j, p) in dp:
        #         return dp[(i, j, p)]
        #     if k == -1:
        #         return p
        #     k -= 1
        #     dp[(i, j, p)] = max(dfs(i + 1, j, p + cardPoints[i]), dfs(i, j - 1, p + cardPoints[j]))
        #     return dp[(i, j, p)]
        # return dfs(0, len(cardPoints) - 1, 0)
        
        l = 0
        r = len(cardPoints) - k
        total = sum(cardPoints[r:])
        res = total
        while r < len(cardPoints):
            total += cardPoints[l] - cardPoints[r]
            res = max(total, res)
            l += 1
            r += 1
        return res
            