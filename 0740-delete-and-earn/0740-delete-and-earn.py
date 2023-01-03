class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        hmap = Counter(nums)
        nums = [0] * (max(hmap.keys()) - min(hmap.keys()) + 1)
        j = 0
        for i in range(min(hmap.keys()), max(hmap.keys()) + 1):
            if hmap[i]:
                nums[j] = i * hmap[i]
            j += 1
        
        zero = 0
        one = 0
        for i in range(len(nums)):
            tmp = one
            one = max(nums[i] + zero, tmp)
            zero = tmp
        
        return one
            