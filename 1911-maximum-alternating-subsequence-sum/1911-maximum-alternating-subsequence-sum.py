class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        dp[(len(nums), False)] = 0
        dp[(len(nums), True)] = 0
        
        for i in range(len(nums) - 1, -1, -1):
            dp[(i, True)] = max(nums[i] + dp[(i + 1, False)], dp[(i + 1, True)])
            dp[(i, False)] = max(-nums[i] + dp[(i + 1, True)], dp[(i + 1, False)])
        
        return dp[(0, True)]
        
        # dp = {}
        # def dfs(i, even):
        #     if (i, even) in dp:
        #         return dp[(i, even)]
        #     if i == len(nums):
        #         return 0
        #     if even:
        #         dp[(i, even)] = max(nums[i] + dfs(i + 1, False), dfs(i + 1, even))
        #     else:
        #         dp[(i, even)] = max(-nums[i] + dfs(i + 1, True), dfs(i + 1, even))
        #     return dp[(i, even)]
        # return dfs(0, True)