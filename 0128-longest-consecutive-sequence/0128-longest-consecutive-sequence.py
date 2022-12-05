class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for n in nums:
            if n - 1 not in num_set:
                length = 0
                while n + length in num_set:
                    length += 1
                longest = max(length, longest)
        return longest
            
        
        
        
        
        
        
        
        
        
        
#         nums_set = set(nums)
#         longest = 0
        
#         for n in nums_set:
#             if (n - 1) not in nums_set:
#                 length = 0
#                 while (n + length) in nums_set:
#                     length += 1
#                 longest = max(longest, length)
        
#         return longest
        