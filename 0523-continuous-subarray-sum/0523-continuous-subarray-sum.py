class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap = {0: -1}
        total = 0
        
        for i, n in enumerate(nums):
            total += n
            r = total % k
            
            if r not in hmap:
                hmap[r] = i
            elif i - hmap[r] > 1:
                return True
        
        return False
        