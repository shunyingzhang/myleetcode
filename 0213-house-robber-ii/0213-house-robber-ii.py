class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        def help(i1, i2):
            h1 = 0
            h2 = 0
            for i in range(i1, i2):
                tmp = h2
                h2 = max(h2, nums[i] + h1)
                h1 = tmp 
            return h2
        
        
        n1 = help(0, n-1)
        n2 = help(1, n)
        
        return max(n1, n2, nums[0])