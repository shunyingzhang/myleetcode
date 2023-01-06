class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i, even):
            if (i, even) in dp:
                return dp[(i, even)]
            if i == len(nums):
                return 0
            if even:
                dp[(i, even)] = max(nums[i] + dfs(i + 1, False), dfs(i + 1, even))
            else:
                dp[(i, even)] = max(-nums[i] + dfs(i + 1, True), dfs(i + 1, even))
            return dp[(i, even)]
        return dfs(0, True)