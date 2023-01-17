class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            a = (n >> i) & 1
            res = (a << (31 - i)) | res
        
        return res
        
        
        
        
        
        
        
        
        
#         res = 0
#         for i in range(32):
#             a = (n >> i) & 1
#             res = res | (a << 31 - i)
        
#         return res
        