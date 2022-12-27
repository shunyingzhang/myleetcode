class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        length =total // 4
        edges= [0] * 4
        matchsticks.sort(reverse = True)
        
        def dfs(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if edges[j] + matchsticks[i] <= length:
                    edges[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    edges[j] -= matchsticks[i]
            return False
    
        return dfs(0)
        
        
        
  
        

            
    
        
        
            
            
        