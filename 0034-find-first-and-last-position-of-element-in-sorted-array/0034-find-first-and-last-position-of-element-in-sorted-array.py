class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        lmin = l
        rmax = r
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                rmax = m
                r = m - 1
            elif nums[m] < target:
                lmin = m
                l = m + 1
            else:
                l = lmin
                r = rmax
                break
                  
        if l > r:
            return [-1, -1]
        
        while nums[l] != target:
            l += 1
        while nums[r] != target:
            r -= 1
        
        return [l, r]
            
        