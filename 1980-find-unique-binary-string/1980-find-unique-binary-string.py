class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        hset = {s for s in nums}
        
        def dfs(i, sub):
            if i == len(nums) and sub not in hset:
                return sub
            if i == len(nums) and sub in hset:
                return None
            res = dfs(i + 1, sub + '0')
            if res:
                return res
            
            res = dfs(i + 1, sub + '1')
            if res:
                return res
        
        return dfs(0, '')
        