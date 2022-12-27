class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(i, ref):
            if i == len(s):
                return True

            for j in range(i, len(s)):
                c = s[i: j + 1]
                
                if int(c) == ref - 1:
                    if dfs(j + 1, ref - 1):
                        return True
                else:
                    continue
            return False
        
        for i in range(len(s) - 1):
            c = s[: i + 1]
            if dfs(i + 1, int(c)):
                return True
            else:
                continue
        return False
                