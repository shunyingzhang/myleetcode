class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        target = len(nums) - 1
        q = set()
        q.add(0)
        steps = 0
        
        while q:
            steps += 1
            for j in range(len(q)):
                p = q.pop()
                for k in range(nums[p], -1, -1):
                    if k == 0:
                        continue
                    if p + k == target:
                        return steps
                    if p + k < target:
                        q.add(p + k)
        