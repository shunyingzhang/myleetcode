class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        i = 0
        r = len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                tmp = nums[l]
                nums[l] = 0
                nums[i] = tmp
                l += 1
                i += 1
                continue
            if nums[i] == 2:
                tmp = nums[r]
                nums[r] = 2
                nums[i] = tmp
                r -= 1
            
            if nums[i] == 1:
                i += 1
            
            
            



        # hmap = defaultdict(int)
        # for n in nums:
        #     hmap[n] += 1
        # for i in range(hmap[0]):
        #     nums[i] = 0
        # for i in range(hmap[0], hmap[0] + hmap[1]):
        #     nums[i] = 1
        # for i in range(hmap[0] + hmap[1], len(nums)):
        #     nums[i] = 2