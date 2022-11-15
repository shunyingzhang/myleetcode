class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n - 3, -1, -1):
            nums[i] = nums[i] + max(nums[(i + 2):])
        
        return max(nums)