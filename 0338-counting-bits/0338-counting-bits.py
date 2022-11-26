class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(i, res):
            if i == 0:
                return 0
            res += i % 2
            i = i // 2
            res += helper(i, 0)
            return res
        
        ans = []
        
        for i in range(n + 1):
            ans.append(helper(i, 0))
            
        return ans
        