class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        target = sum(piles) // 2
        dp = {}
        def dfs(l, r):
            if (l, r) in dp:
                return dp[(l, r)]
            if l > r:
                return 0
            even = (r - l) % 2
            if even:
                dp[(l, r)] = max(piles[l] + dfs(l + 1, r), piles[r] + dfs(l, r - 1))
            else:
                dp[(l, r)] = max(dfs(l + 1, r), dfs(l, r - 1))
            return dp[(l, r)]
        
        return dfs(0, len(piles) - 1) > target
        