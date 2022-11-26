class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(i):
            if i == 0:
                return 0
            count = i % 2
            i = i // 2
            res = helper(i) + count
            return res
        
        ans = []
        
        for i in range(n + 1):
            ans.append(helper(i))
            
        return ans
        