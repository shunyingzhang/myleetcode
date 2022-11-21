class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        l = 0
        r = 0
        
        while r < len(nums) - 1:
            fastJump = 0
            for i in range(l, r + 1):
                fastJump = max(fastJump, i + nums[i])
            l = r + 1
            r = fastJump
            step += 1
        
        return step
        