class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        fastest = 0
        q = deque([0])
        while q:
            i = q.popleft()
            start = max(i + minJump, fastest + 1)
            for j in range(start, min(len(s), i + maxJump + 1)):
                if s[j] == '0':
                    if j == len(s) - 1:
                        return True
                    q.append(j)
            fastest = i + maxJump
            
        return False
         
            
        