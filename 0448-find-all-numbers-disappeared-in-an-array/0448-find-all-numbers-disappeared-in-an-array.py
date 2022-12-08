class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # res = [i + 1 for i in range(len(nums))]
        # for n in nums:
        #     if n in res:
        #         res.remove(n)

        # return res

        res = []

        for i, n in enumerate(nums):
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res




