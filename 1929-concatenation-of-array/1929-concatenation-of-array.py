class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
#         ans = []
        
#         for i in range(2):
#             for n in nums:
#                 ans.append(n)
        
#         return ans
        
        ans = [0] * 2 *len(nums)
        for i, n in enumerate(nums):
            ans[i] = n
            ans[i + len(nums)] = n
        return ans
        