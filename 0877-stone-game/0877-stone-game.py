class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        target = sum(piles) // 2
        piles = deque(piles)
        
        def dfs(s):
            if not piles and s > target:
                return True
            if not piles and s <= target:
                return False
            pile = piles.popleft()
            if dfs(s + pile):
                return True
            piles.pushleft(pile)
            pile = piles.pop()
            if dfs(s + pile):
                return True
            return False
        return dfs(0)
        