class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] += 1
        
        for n, i in count.items():
            freq[i].append(n)
        
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
        
        
        
        
        
        
        
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]
        
#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
        
#         for n, i in count.items():
#             freq[i].append(n)
        
#         res = []
        
#         for i in range(len(freq)-1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res
        