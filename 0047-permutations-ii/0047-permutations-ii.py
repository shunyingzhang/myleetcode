class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        hmap = Counter(nums)
        
        def dfs():
            if len(sub) == len(nums):
                res.append(sub.copy())
                return
            for n in hmap:
                if hmap[n] > 0:
                    sub.append(n)
                    hmap[n] -= 1
                    
                    dfs()
                    
                    sub.pop()
                    hmap[n] += 1
        dfs()
        
        return res
            
        