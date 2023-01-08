class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        for i in range(len(s)):
            count[s[i]] = i
        
        longest = 0
        cur = 0
        res = []
        for i in range(len(s)):
            longest = max(longest, count[s[i]])
            if i == longest:
                res.append(longest + 1 - cur)
                longest = i + 1
                cur = longest
        
        return res
            
        
#         count = {}
#         for i in range(len(s)):
#             count[s[i]] = i
        
#         size = 0
#         end = 0
#         output = []
        
#         for i in range(len(s)):
#             size += 1
#             end = max(end, count[s[i]])
#             if i == end:
#                 output.append(size)
#                 size = 0
#                 continue    
            
#         if size:
#             output.append(size)
        
#         return output
       
            
            
        