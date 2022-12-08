class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Hmap = {0: 1}
        summ = 0
        res = 0
        for n in nums:
            summ += n
            if summ - k in Hmap:
                res += Hmap[summ - k]
                
            Hmap[summ] = 1 + Hmap.get(summ, 0)
        return res
        
        # res = 0
        # for i in range(len(nums)):
        #     l = i
        #     summ = 0
        #     while l >= 0:
        #         summ += nums[l]
        #         if summ == k:
        #             res += 1
        #             # break
        #         # if summ > k:
        #         #     break
        #         l -= 1
        # return res
        