class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(i):
            if i == 0:
                return 0
            a = i % 2
            i = i // 2
            res = helper(i) + a
            return res
        
        ans = []
        
        for i in range(n + 1):
            ans.append(helper(i))
            
        return ans
        