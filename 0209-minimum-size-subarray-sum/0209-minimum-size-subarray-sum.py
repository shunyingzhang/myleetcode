class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float(inf)
        l, r = 0, 1
        total = nums[0]
        while l < len(nums):
            if total >= target:
                length = min(length, r - l)
                total -= nums[l]
                l += 1
            elif r < len(nums):
                total += nums[r]
                r += 1
            else:
                return length if  length != float(inf) else 0
        
        return length if  length != float(inf) else 0