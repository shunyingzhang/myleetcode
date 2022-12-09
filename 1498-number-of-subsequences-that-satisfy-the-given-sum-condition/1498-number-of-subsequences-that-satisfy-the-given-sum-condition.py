class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = 10 ** 9 + 7
        r = len(nums) - 1
        for i, n in enumerate(nums):
            # if n * 2 > target:
            #     return res
            while r >= i and n + nums[r] > target:
                r -= 1
            if i <= r:
                res += (2**(r - i))
                res = res % mod
        
        return res
            
        