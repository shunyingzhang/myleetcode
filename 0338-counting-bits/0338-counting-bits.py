class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1):
            if i == 2 * offset:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp
        
        
#         def helper(i):
#             if i == 0:
#                 return 0
#             count = i % 2
#             i = i // 2
#             res = helper(i) + count
#             return res
        
#         ans = []
        
#         for i in range(n + 1):
#             ans.append(helper(i))
            
#         return ans
        