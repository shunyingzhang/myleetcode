class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [False] * (len(s2) + 1)
        dp[len(s2)] = True
        dpNew = [False] * (len(s2) + 1)
        
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dpNew[j]:
                    dp[j] = True

                if j < len(s2) and s2[j] == s3[i + j] and dp[j + 1]:
                    dp[j] = True
            dpNew = dp
            dp = [False] * (len(s2) + 1)
    
        return dpNew[0]
            
        